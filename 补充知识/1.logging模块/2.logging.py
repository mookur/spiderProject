import logging

'''
前面介绍的日志记录，其实都是通过一个叫做日志记录器（logger）的实例对象创建的，每个记录器都有一个名称，
直接使用logging来记录日志是，系统会默认创建名为root的记录器，这个记录器是根记录器。
记录器支持层级结构，子记录器通常不需要单独设置日志级别以及Handle（后面会介绍），如果子记录器没有单独设置，则依从父级的设置。

'''
# 记录器名称可以是任意名称，不过最佳实践是直接用模块的名称当作记录器的名字。
logger =  logging.getLogger(__name__)
'''
默认情况下，记录器采用层级结构，上句点作为分隔符排列在命名空间的层次结构中。层次结构列表中位于下方的记录器
是列表中较高位置的记录器的子级。例如，有个名叫foo的记录器，而名字是foo.bar,foo.bar.baz和foo.bam的记录器都是foo的子级

'''
'''
处理器Handler，记录器负责日志的记录，但是日志最终记录在哪里记录器并不关心，而是交给了另一个家伙--处理器去处理了。

例如一个Flask项目，你可能会将INFO级别的日志记录到文件，将ERROE级别的日志记录到标准输出，将某些关键日志（例如有订单或者严重错误）
发送到某个邮件地址通知老板。这时候你的记录器添加多个不同的处理器来处理不同的消息日志，依次根据消息的重要性发送到特定的位置

python内置了很多实用的处理器：
1.StreamHandle标准流处理器，将消息发送到标准输出流、错误流。
2.FileHandler 文件处理器，将消息发送到文件
3.RotatingHandler文件处理器，文件达到指定大小后，启用新文件存储日志
4.TimedRotatingFileHandler文件处理器，日志以特定的时间间隔轮换日志文件

Handler处理器操作：
setLevel
setFormatter
addFilter()
removeFilter()
'''

import logging
from logging import StreamHandler
from logging import FileHandler

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)
# 设置为DEBUG等级

stream_handler = StreamHandler()
stream_handler.setLevel(logging.WARNING)
logger.addHandler(stream_handler)
# 标准流处理器，设置的级别为WARNING

file_handler= FileHandler(filename='test.log')
file_handler.setLevel(logging.INFO)
logger.addHandler(file_handler)
# 文件处理器，设置的级别为INFO

logger.debug('this is debug')
logger.info('this is info')
logger.error('this is error')
logger.warning('this is waring')

# 可以看到在命令行窗口输出的日志内容是error和warning
# 文件夹里的是info error waring
# 尽管我们将logger的级别设置为了DEBUG，但是debug记录的消息并没有输出，因为我们给两个Handler设置的级别都要比DEBUG高，
# 所以这条被过滤了。但如果设置的级别高于处理器Handler，处理器不会执行。

'''
格式器（formatter），格式器在前面已经介绍了，不过那是通过logging.basicConfig来指定的，其实格式器还可以
以对象的形式来设置在Handler上。格式器可以指定日志的输出格式，时间、级别、名字等等。
'''
import logging
from logging import StreamHandler

logger = logging.getLogger(__name__)

stream_handler = StreamHandler()
stream_handler.setLevel(logging.WARNING)
# 标准流处理器

formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
# 创建一个格式器

stream_handler.setFormatter(formatter)
# 作用到handler上

logger.addHandler(stream_handler)
# 添加处理器

logger.info('this is info')
logger.error('this is error')
logger.warning('this is warning')

'''
注意，格式器只能作用在处理器上，通过处理器的setFormatter方法设置格式器。
而且一个Handler只能设置一个格式器。是一对一的关系。
而logger与handler是一对多的关系，一个logger可以添加多个handler。
handler和logger都可以设置日志的等级
'''

'''
回到最开始的地方，logging.basicConfig()方法为我们干了啥？
1.创建一个root记录器
2.设置root的日志级别为warning
3.为root记录器添加StreamHandler处理器
4.为处理器设置一个简单格式器
'''
logging.basicConfig()

# 就等价与：
import sys
import logging
from logging import StreamHandler
from logging import Formatter

logger = logging.getLogger("root")
# 1.创建一个名为root的记录器
logger.setLevel(logging.WARNING)
# 2.设置root记录器的日志级别-WARNING
handler = StreamHandler(sys.stderr)
# 3.设置一个处理器
formatter = Formatter('%(asctime)s  %(levelname)s  %(name)s  %(message)s')
# 4.设置一个格式器
handler.setFormatter(formatter)
# 5.处理器添加格式器
logger.addHandler(handler)
# 6.记录器添加处理器

logger.warning("warning!!!")
'''
logging.basicConfig方法做的事情是相当于给日志系统做一个最基本的配置，方便开发者快速接入使用。
它必须在开始记录日志前调用。不过如果root记录器已经指定有其他处理器，这时候在调用basicConfig，则方法将失效，它什么都不会做。

'''

'''
日志配置
日志的配置除了前面介绍的将配置直接写在代码中，还可以将配置信息单独放在配置文件中，实现配置与代码分离。
'''
import logging
import logging.config

logging.config.fileConfig('logging.conf')
# 加载配置

logger = logging.getLogger()
#创建logger

logger.debug('debug!!!!')
# 应用代码