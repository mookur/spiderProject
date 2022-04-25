'''
1.通用匹配
  出现空白字符就需要写\s匹配，出现数字就需要写\d匹配，这样的工作量其实非常大。
  其实完全没必要这么做，因为有一个万能匹配可以用，就是.*。其中.可以匹配任意字符（除换行符）,*代表匹配前面的字符无限次，
  所以他们组合在一起就可以匹配任意字符。
'''
import re

content = 'Hello 123 4567 World_This is a Regex Demo'
result = re.match('^Hello.*Demo$',content)
print(result.group())

'''
2.贪婪与非贪婪
  使用通用匹配.*匹配到的内容有时候并不是我们想要的结果。
  这里我们依然想获取目标字符串中间的数字，所以正则表达式中间写的依然是（\d+).奇怪的事，我们只得到的数字7.

  其实这里涉及到贪婪匹配和非贪婪匹配的问题。在贪婪匹配下，.*会匹配尽可能多的字符。正则表达式中，.*后面是\d+，也就是至少一个数字，
  而且没有指定具体几个数字，因此，.*会匹配尽可能多的字符，这里就把123456都匹配了，
  只给\d+留下一个可满足条件的数字7，因此最后得到的内容就只有数字7.

  这很明显会给我们带来很大的不便。有时候，匹配结果会莫名其妙少一部分内容。其实，这里只需要使用非贪婪匹配就好了。
  非贪婪匹配的写法是.*?，多了一个?。
  
  此时就可以成功获取1234567了。原因可想而知，贪婪匹配是匹配尽可能多的字符，非贪婪匹配就是匹配尽可能少的字符，我愿称为摸鱼匹配。
  当.*?匹配到Hello后面的空白字符时，在往后的字符就是数字的，而\d+恰好可以匹配，于是它就不匹配了，而是交给\d+去匹配（开始摸鱼的）
  .*?匹配了尽可能少的字符，\d+的结果就是1234567.

  所以说，在做匹配的时候，字符串中间尽量使用非贪婪匹配。但这里需要注意，如果匹配到的结果在字符串末尾，.*?有可能匹配不到任何内容了。因为他会匹配尽可能少的内容。
'''
import re

content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*(\d+).*Demo$',content)
print(result)
print(result.group(1))

# 使用非贪婪就可以解决
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*?(\d+).*Demo$',content)
print(result)
print(result.group(1))

# 字符串末尾，.*?有可能匹配不到任何内容了。
content = 'http://weibo.com/comment/kEraCn'
result1 = re.match('.*?comment/(.*?)',content)
result2 = re.match('.*?comment/(.*)',content)
print(result1.group(1))
print(result2.group(1))

'''
3.修饰符
  在正则表达式中，可以用一些可选标志修饰符来控制匹配的模式。修饰符被指定为一个可选的标志。
'''
import re

content = '''Hello 1234567 World_This
is a Regex Demo
'''
# result = re.match('^He.*?(\d).*?Demo$',content)
# print(result.group(1))
# 可以发现会报错，因为.是不匹配换行符的。

# 这里只需加一个修饰符re.S,即可修正这个错误。
# 这个修饰符的作用是是匹配内容包括换行符在内的所有的字符（这里发现在'''后面就换行也不行，内部任何地方换行都行）
# 这里的re.S是特指在.中加上换行。
result = re.match('^He.*?(\d+).*?Demo$',content,re.S)
print(result.group(1))

'''
其他修饰符：
re.I   使匹配对大小写不敏感
re.L   实现本地化识别（locale-aware）匹配
re.M   多行匹配，影响^和$
re.S   使匹配内容包括换行符在内的所有字符
re.U   根据Unicode字符集解析字符。这个标志会影响\w\W\b\B
re.X   该标志能够给予你更灵活的格式，以便将正则表达式书写更易于理解

'''

'''
4.转义匹配
  正则表达式定义了许多匹配模式，但如果目标字符串就包含了这个字符，那就需要转移匹配了。
  
  当在目标字符串中遇到特殊冲突字符时，在此前面加上反斜杠\即可。
'''
import re

content = '(百度)www.baidu.com'
result = re.match('\(百度\)www\.baidu\.com',content)
print(result)
