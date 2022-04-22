'''
8.属性匹配
  在选取节点的时候，还可以使用@符号实现属性过滤。例如，要选取class属性为item-0：

  这里通过加入[@class='item-0']，限制了节点的class属性为item-0。
  符合这个条件的有两个li节点，所以返回结果是有两个。
'''
from lxml import etree

html = etree.parse('./test.html',etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]')
print(result)

'''
9.属性多值匹配
  有时候，某些节点的某个属性可能有多个值，例如：
  下面的HTML中li节点的class属性就有两个值：li 和 li-first。
  此时如果还用之前的单个属性匹配获取节点，就无法获取了。返回结果是空列表。
  
'''
from lxml import etree

text = '''
<li class="li li-first"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[@class="li"]/a/text()')
print(result)

# 这种情况需要用到contains方法：
# 这样就能得到返回结果：['first item']
# contains方法经常在某个节点的 某个属性有多个值时 用到。
result = html.xpath('//li[contains(@class,"li")]/a/text()')
print(result)

'''
10.多属性匹配
   我们还可能遇到一种情况，就是根据多个属性确定一个节点，这时需要同时匹配多个属性。
   运算符and用于连接多个属性：
   
   这里的and时XPath中的运算符，还有其他运算符：
   or	或	            age=19 or age=20	如果age是19则返回True。如果age是21则返回false 两个条件满足一个即可
   and	与	            age>19 and age<20	如果age是20则返回True。如果age是18则返回false 两个条件同时满足即可
   mod	计算除法的余数	    5 mod 2	1
   |	计算两个节点集	    //book|//cd	返回所有拥有book和cd元素的节点集
   其他的还有加减乘除，大于小于不等于，很简单不写了。注意除是 div 就行。
'''
from lxml import etree

text = '''
<li class="li li-first" name="item"><a href="link.html">first</a>
'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class,"li") and @name="item"]/a/text()')
print(result)
