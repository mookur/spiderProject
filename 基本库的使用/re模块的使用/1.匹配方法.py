'''
1.正则表达式测试工具 http://tool.oschina.net/regex/.在上面输入文本，右侧有一些写好的规则，也可以自己写。

  python有re库，提供了正则表达式的实现。

'''
'''
常用匹配规则：
^	匹配字符串的开头
$	匹配字符串的末尾
.	匹配任意字符，除了(\n，就是除了换行)

[...]	用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
[^...]	不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。

*	匹配0个或多个的表达式。
+	匹配1个或多个的表达式。
?	匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式

{ n}	精确匹配 n 个前面表达式。例如， o{2} 不能匹配 "Bob" 中的 "o"，但是能匹配 "food" 中的两个 o。
{ n,}	匹配 n 个前面表达式。例如， o{2,} 不能匹配"Bob"中的"o"，但能匹配 "foooood"中的所有 o。"o{1,}" 等价于 "o+"。"o{0,}" 则等价于 "o*"。
{ n, m}	匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式

a| b	匹配a或b

(re)	捕获一个组
(?p<name>re) 给组取名
(?p=name)  使用已取名的组
(?imx)	正则表达式包含三种可选标志：i, m, 或 x 。只影响括号中的区域。
(?-imx)	正则表达式关闭 i, m, 或 x 可选标志。只影响括号中的区域。
(?: re)	类似 (...), 但是不表示一个组
(?imx: re)	在括号中使用i, m, 或 x 可选标志
(?-imx: re)	在括号中不使用i, m, 或 x 可选标志
(?#...)	注释.
(?= re)	前向肯定界定符。如果所含正则表达式，以 ... 表示，在当前位置成功匹配时成功，否则失败。但一旦所含表达式已经尝试，匹配引擎根本没有提高；模式的剩余部分还要尝试界定符的右边。
(?! re)	前向否定界定符。与肯定界定符相反；当所含表达式不能在字符串当前位置匹配时成功
(?> re)	匹配的独立模式，省去回溯。
\w	匹配字母数字及下划线（匹配字符）（中文可以匹配）
\s	空格
\b	匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
\d	匹配任意数字，等价于 [0-9].

\W	匹配非字母数字及下划线
\S	匹配任意非空字符
\B	匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。
\D	匹配任意非数字
\A	匹配字符串开始
\Z	匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串。
\z	匹配字符串结束
\G	匹配最后匹配完成的位置。
\n, \t, 等.	匹配一个换行符。匹配一个制表符。等
\1...\9	匹配第n个分组的内容。
\10	匹配第n个分组的内容，如果它经匹配。否则指的是八进制字符码的表达式。

# [^\\\/\^] 表示除了(\)(/)(^)之外的所有字符
'''

'''
2.match匹配
  match方法只从字符串的起始位置开始匹配正则表达式，如果匹配，就返回要匹配成功的结果；如果不匹配，就返回None。
  
  首先声明一个字符串，接着写了一个表达式，^表示匹配字符串的开头。
  \s表示空格，\d表示匹配数字，写好几个太麻烦，可以在后面跟{4}的形式代表次数。
  将输出结果打印出来，可以看到结果是SRE_Match对象，证明匹配成功。
  该对象有两个方法，一个是group方法，可以输出匹配到的内容。还有一个是span方法，可以输出匹配的范围。
'''
import re

content = 'Hello 123 4567 World_This is a Regex Demo'
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}',content)
print(len(content))
print(result)
print(result.group())
print(result.span())

'''
3.search匹配
  match方法是从字符串的开头开始匹配的，意味着一旦开头不匹配，整个匹配就失败了。
  match匹配更适合检测某个字符串是否符合某个正则表达式的规则
  
  而search匹配会扫描整个字符串，然后返回第一个匹配成功的结果，
  在匹配时，会依次以每个字符作为开头扫描字符串，直到找到第一个符合规则的字符串。没有返回None。
  
'''
import re

content = 'Extra stings Hello 1234567 World_This a Regex Demo Extra    stings'
result = re.search('Hello.*?(\d+).*?Demo',content)
print(result)
# 如果把search改为match就匹配不到了。

'''
4.findall匹配
  search只能返回匹配成功的第一个字符串，如果想要匹配所有与表达式相符的字符串，就要用到findall
  
  可以看到，返回的是列表，每个元素都是元组类型，我们用索引依次取出每个条目即可。
'''
html = '''<div id="songs-list">
<h2 class="title">经典老歌</h2>
<p class="introduction">
经典老歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2">一路上有你</li>
<li data-view="7">
<a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
</li>
<li data-view="4" class="active">
<a href="/3.mp3" singer="齐秦">往事随风</a>
</li>
<li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
<li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
<li data-view="5">
<a href="/6.mp3" singer="邓丽君">但愿人长久</a>
</li>
</ul>
</div>'''
results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>',html,re.S)
print(results)
print(type(results))
for result in results:
    print(result)
    print(result[0],result[1],result[2])

