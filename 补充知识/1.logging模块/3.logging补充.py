# 为什么有时候日志会输出两次？

import logging

# 初始化日志，并设置日志级别
logging.basicConfig(level=logging.DEBUG)

# 定义root记录器，
# 这行不用写也一样，只是为了下面能打印这个。
root = logging.getLogger()

# 定义child记录器
child = logging.getLogger("child")
console_handler = logging.StreamHandler()
child.addHandler(console_handler)

# 记录一条info记录
child.info("child info")

print(root.handlers)
# [<StreamHandler <stderr> (NOTSET)>]

'''
代码中明明只记录了一次日志，却输出了两次，而且两次的日志格式不一样。
这是因为child这个记录器添加了一个叫console_handler的处理器，而root根记录器默认也带有自己的处理器。

根据python中日志模块的处理机制，子记录器记录的消息会自动传播给父级记录器的关联的处理器
所以，child记录的消息除了发给自己的handler外，还是传播给root记录器的handler，因此最终输出了两次
'''

# 如果不希望子记录器的消息传播给父级记录器，可以设置记录器的属性propagate为False，关闭传播。
child.propagate = False
child.info("child info")

'''
配置处理器的最佳实践是给顶级记录器配置处理器，再根据需要创建子记录器，因为记录最终都会传播给父记录器
(子记录器没有配置会拿上一级记录器的配置）
'''
import logging

parent = logging.getLogger('parent')
parent.setLevel(logging.DEBUG)
parent.addHandler(logging.StreamHandler())

# 不需要给子记录器单独配置Handler
child = logging.getLogger()
child.info('info')

'''
为什么输出的日志是红色？
可以查看StreamHandler的源码
初始化这个handler时，会接受一个stream的参数，如果不传，默认就使用系统标准错误流（sys.stderr)输出，
pycharm对错误输出的字体样式做了红色渲染，如果换成sys.stdout输出的就不是红色了。
'''
import logging
import sys

handler = logging.StreamHandler(stream=sys.stdout)
logging.basicConfig(level=logging.DEBUG,handlers=[handler])

# 或者指定stream参数
# logging.basicConfig(level=logging.DEBUG,stream=sys.stdout)

logging.info('info')

'''
怎么生成以日期时间命名的日志？
实际应用中方，我们会对日志进行归档存储，每天生成一份日志，如果哪天出了问题，也方便定位，
直接找到当天的日志文件。我们需要给logger添加一个TimedRotatingFileHandler处理器就行。

'''

'''
为什么我日志配置后不生效？
实际场景中，代码没这么简单，通常是在a模块中的某个函数中初始化日志框架配置， 
在b模块在外层创建了名字叫b的记录器 logger_b，
然后在a中导入b模块时，这时候日志配置还没初始化，
最后导致logger_b的配置就成了默认配置。所以有可能出现日志不生效的情况。
'''