'''
5.所有节点
  我们一般会以//开头的XPath规则，来选取所有符合要求的节点。
  这里使用*代表匹配所有的节点，也就是获取整个HTML文本中的所有节点。
  运行结果返回的是一个列表，其中每个元素是Element类型，类型后面跟着节点的名称，如html、body等。

  （这里会有个疑问，就是为什么结果是Element类型的对象，而不是html实际的文本或html的一段内容？
  其实可能由于先学的是beautifulsoup导致，这里其实xpath还没用到属性匹配，内容获取相关的方法，
  只是先进行定位，所以输出的不是内容文本。）
'''
from lxml import etree

html = etree.parse('./test.html',etree.HTMLParser())
result = html.xpath('//*')
print(result)

# 当然也可以匹配指定节点的名称。
result = html.xpath('//li')
print(result)
print(result[0])

'''
6.子节点
  通过/或//即可查找元素的子节点或子孙节点。假如想选择li节点的所有直接子节点a，则可以这样实现：
  这里通过追加/a的方式，选择了所有li节点的所有直接子节点a。其中//li用于选中所有li节点，/a用于选中li节点的所有直接子节点a。
'''
from lxml import etree

html = etree.parse('./test.html',etree.HTMLParser())
result = html.xpath('//li/a')
print(result)

# 上面的/用于选取节点的直接子节点，如果要获取节点的所有子孙节点，可以使用//。
# 运行结果是相同的，同理也可以使用//a。
# 但如果这里使用//ul//a，就只能获取一个空列表，因为/用于获取直接子节点，而ul的直接子节点是li节点。
result = html.xpath('//ul//a')
print(result)

'''
7.父节点
  通过连续的/和//可以查找子节点或子孙节点，那么假如知道了子节点，怎么查找父节点呢？这里可以通过..实现。
  例如，首先选中href属性为link4.html的a节点，然后获取其父节点，在获取父节点的class属性。
  
  输出结果得到了li节点的属性，也就是['item-1']。
  这里也可以说明上面那个疑问，这里如果不加@class得到的只会是li节点的对象。
'''
from lxml import etree

html = etree.parse('./test.html',etree.HTMLParser())
result = html.xpath('//a[@href="link4.html"]/../@class')
print(result)

# 也可以通过parent::获取父节点，代码如下：
# 后面的*表示所有的，因为只有一个，这里也可以把*换成li。
# 这后面必须加点东西例如*，不然会报错，不知道你要获取什么。
result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(result)
