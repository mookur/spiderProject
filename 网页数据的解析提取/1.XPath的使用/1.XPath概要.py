'''
1.XPath概览：XPath的的全称是XML Path Language，即XML路径语言，用来在XML文档中查找信息的。
  XPath的选择功能十分强大，它提供了非常简单明了的路径选择表达式。它还提供了100多个内建函数，用于字符串、数值、时间的匹配以及节点、序列的处理。

2.XPath 常用规则：
  nodename      选取此节点的所有子节点
  /             从当前节点选取直接子节点
  //            从当前节点选取子孙节点
  .             选取当前节点
  ..            选取当前节点的父节点
  @             选取属性

3.准备工作：
  pip3 install xlml
'''



'''
4.实例引入
  首先导入lxml库的etree模块，然后声明一段HTML文本，接着对HTML类进行初始化，这样就成功构造一个XPath解析对象。
  此处需要注意一点，原text中的最后li标签是没有闭合的，而etree模块可以自动修正HTML文本。打印结果发现自动补全。
  之后调用tostring方法，即可输出修正后的HTML代码。但结果是byte类型。利用decode方法将其转化成str类型
'''
from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
</div>
'''
html = etree.HTML(text)
result = etree.tostring(html)
print(result.decode('utf-8'))
# 查看结果可以发现，经过处理之后的li节点标签得以补全，并且自动添加了body、html标签

# 另外也可以不声明html文本也就是text，直接读取文本文件进行解析。
from lxml import etree

html = etree.parse('./test.html',etree.HTMLParser())
result = etree.tostring(html)
print(result.decode('utf-8'))
# 这次的输出结果略有不同，多了一个DOCTYPE声明（我的还多了&#13，不知道是什么），不过对解析结果无任何影响。




