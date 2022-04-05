'''
记录日志最简单的方法就是在你想要的地方加上一句print，但在一些大一点的项目，需要查看历史日志定位问题，用print就不合时宜了。
print打印出来的日志没有时间，不知道日志记录的位置，也没有可读的日志格式，还不能把日志输出到指定文件。。。除非全部自己重复造一遍轮子。

而内置的logging模块给开发者提供了非常丰富的功能。能使日志更具可读性。

'''

import logging

logging.debug('this is debug')
logging.info('this is info')
logging.warning('this is warn')
logging.error('this is error')
logging.critical('this is critical')

# WARNING:root:this is warn
# ERROR:root:this is error
# CRITICAL:root:this is critical
'''
直接使用logging提供日志消息记录的方法。可以把它与print相类比，毕竟本质就是要记录信息。
那为甚么有两个日志没打印出来。其实在logging模块，日志（也就是信息）分为5个级别，依次从小到大。

DEBUG  debug级别用来记录详细的信息，方便定位问题进行调试，在生产环境我们一般不开启DEBUG
INFO   用来记录关键代码点的信息，以便代码是否按照我们预期的执行，生产环境通常会设置INFO级别
WARNING 记录某些不预期发生的情况，如磁盘不足
ERROR  由于一个更严重的问题导致某些功能不能正常运行时记录的信息
CRITICAL 当发生严重错误，导致应用程序不能继续运行时记录的信息

而默认情况下的日志级别是WARGING，低于WARING的日志信息都不会输出。所以上面debug和info记录的日志不会打印。
还可以看到日志内容都打印在标准输出流，也就是命令行窗口。后面还会介绍把日志放在文件里、发给邮件等等。


'''

# 如何让debug级别的信息也输出？当然是修改默认的日志级别。
# 在开始记录日志前可以使用logging.basicConfig方法可以设定日志级别
logging.basicConfig(level=logging.DEBUG)
logging.debug("this is debug")
logging.info("this is info")
logging.error("this is error")
'''
可以看到，这也没有打印debug和info的消息，这是为什么？
其实上面说了要在首行使用basicConfig才有用，而在顶部已经运行过一段代码了，所以级别还是默认的warning。
只要再开个py文件就行行了。这里为了使笔记在一起，就没有另开一个了。
'''

# 上面说过，logging会默认把日志输出到标准输出流，就是只在命令行窗口输出，程序重启后历史日志没地方找，
# 所以把日志内容永久记录是一个很常见的需求。同样通过配置函数logging.basicConfig可以指定日志输出到什么地方。

logging.basicConfig(filename='test.log',level=logging.INFO)
logging.debug('this is debug')
logging.info('this is info')
logging.error('this is error')
'''
最后出现test.log文件，文件记录的内容如下：
INFO:root:this is info
ERROR:root:this is error

每次重新运行时，日志会以追加的方式在后面，如果每次运行前要覆盖之前的日志，则需指定
filemode='w'，这个和open函数写数据到文件用的参数是一样的。
'''

# 指定日志记录格式
# 默认的输出格式包含3部分，日志级别，日志记录器的名字，以及日志的内容，中间用':'连接。
# 如果我们想改变日志格式，例如想加入日期时间、显示日志器名字，我们是可以指定format参数来设置日志的格式
logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s %(message)s')
logging.error('this is error')

'''
当然，日志格式化输出还提供了非常多的参数。
asctime   %(asctime)s   日志何时被创建。默认形式为'2003-07-08 13:34:23,123'(逗号后面的数字为时间的毫秒部分）
levelname %(levelname)s  日志的级别（'DEBUG','INFO','WARNING','ERROR','CRITICAL')
message   %(message)s    记入日志的消息记录）
name      %（name）s    用于记录日志的记录器名称
process   %（process）d  进程ID（如果可用）
thread    %（thread）d   线程ID（如果可用）
'''