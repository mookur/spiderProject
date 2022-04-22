'''
1.文本获取
  用XPath中的text方法可以获取节点中的文本，接下来尝试获取前面的li节点的文本。

  输出的结果是['\r\n     ']，没有获取任何文本，这是为什么？
  因为xpath中text方法前面是/，含义是直接子节点。li里面的是a标签，这是不文本，而文本在a节点里面是子孙节点。
  而第二个li中是有修正后的换行文本的，所以获取到的就是换行符。
  <li class="item-0"><a href="link1.html">first item</a></li>
  <li class="item-0"><a href="link5.html">fifth item</a>
  </li>

  \r和\n的区别：
  \r : 回车符（return），回到一行的开头
  \n : 换行符（newline），另起一行

  '\r'是回车，'\n'是换行，前者使光标到行首，后者使光标下移一格。通常用的Enter是两个加起来。
   有的编辑器只认\r\n，有的编辑器则两个都认。所以要想通用的话，最好用\r\n换行。
   Windows系统里面，每行结尾是 回车+换行(CR+LF)，即“\r\n”；
'''
from lxml import etree

html = etree.parse('./test.html',etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]/text()')
print(result)
print('11\r12')

# 想要获取文本，有两种方法，第一种是先选取a节点在获取文本
# 第一种获取到的信息更准确。
result = html.xpath('//li[@class="item-0"]/a/text()')
print(result)

# 第二种是直接使用//。
# 第二种能获取更全面的信息，但也会夹杂特殊字符。
result = html.xpath('//li[@class="item-0"]//text()')
print(result)

'''
2.属性获取
  这里的属性获取和前面的 属性匹配是不同的，属性匹配是用中括号加属性名和值来定位某个标签如：[@class="xxx"]
  而属性获取是获取属性的文本信息。
'''
from lxml import etree

html = etree.parse('./test.html',etree.HTMLParser())
result = html.xpath('//li/a/@href')
print(result)
