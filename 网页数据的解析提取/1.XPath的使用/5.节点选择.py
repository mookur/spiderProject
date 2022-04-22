'''
1.按序选择
  在选择节点时，某些属性可能同时匹配了多个节点，但是我们只要其中国的某一个。
  第一次选择时，选取了第一个li节点，但这里要注意的是，这里和写代码不同序号以1开头，不是0.
  第四次选择时，调用了last方法在减二得到的就是倒数第三个。
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
result = html.xpath("//li[1]/a/text()")
print(result)
result = html.xpath("//li[last()]/a/text()")
print(result)
result = html.xpath("//li[position()<3]/a/text()")
print(result)
result = html.xpath("//li[last()-2]/a/text()")
print(result)

'''
2.节点轴的选择
  包括获取子元素、兄弟元素、父元素、祖先元素等。
  
  第一次选择时，调用了ancestor轴，可以获取所有祖先节点。其后需要跟两个冒号，然后是节点的选择器，这里我们直接使用*，表示获取所有节点。
  第三次，调用attribute轴，可以获取所有属性值，其后跟的选择器还是*，返回值就是li节点的所有属性值。
  第四次，调用child轴，可以获取所有直接子节点。改为*其实也是相同结果，因为span节点是子孙节点了。
  第五次，调用descendant轴，准确来说是获取所有后代节点。因为改为*，a节点也能获取。
  第六次，调用following轴，可以获取当前节点后面的所有节点，不包括本节点和本节点的所有子节点，会包括后面节点的子节点。
  最后一次，调用可以获取后续同级节点，和第六次比就少了所有的a节点，只有li节点。
'''
from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html"><span>first item</span></a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
</div>
'''
html = etree.HTML(text)
result = html.xpath('//li[1]/ancestor::*')
print(result)
result = html.xpath('//li[1]/ancestor::div')
print(result)
result = html.xpath('//li[1]/attribute::*')
print(result)
result = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(result)
result = html.xpath('//li[1]/descendant::span')
print(result)
result = html.xpath('//li[1]/following::*')
print(result)
result = html.xpath('//li[1]/following-sibling::*')
print(result)
