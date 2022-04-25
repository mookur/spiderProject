'''
1.group方法
  实现了匹配，但如果想从字符串中提取一部分内容，就需要使用括号（）将想要提取的内容的 表达式括起来。
  ()实际标记了一个子表达式的开始和结束位置，被标记的每个子表达式一次对应每个分组，调用group方法传入分组的索引即可获取结果

  可以看到，我们成功得到了124567.这里用的是group（1），他与group（）有所不同，后者会输出完整的匹配结果。
  前者会输出第一个被（）包围的匹配结果。假如正则表达式后面还有用（）包围的内容，那么可以依次使用group（2）、group（3）。。。
'''
import re

content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^Hello\s(\d+)\sWorld',content)
print(result)
print(result.group())
print(result.group(1))
print(result.span())

'''
2.sub方法
  除了使用正则表达式提取信息，有时候还需要借助它来修改文本。
  例如想把一串文本中的所有数字都去掉，如果只用replace方法，就太繁琐了，这时可以借助sub方法
'''
import re

content = '3234das1eqd34d35ad'
content = re.sub('\d+','',content)
print(content)

'''
3.compile方法
  compile方法可以将正则字符串编译成正则表达式对象，以便在后面的匹配中复用。
  
  这个实例有3个日期，想分别将时间去掉，利用compile方法将正则表达式编译成一个正则表达式对象，就可以没必要重复写三个一样表达式
  
  另外，compile还可以传入修饰符，这样在search，findall方法中就不需要额外传了。
  可以说compile方法是给表达式做了一层封装，以便我们更好地复用。
'''
import re

content1 = '2019-12-15 12:00'
content2 = '2019-11-15 12:00'
content3 = '2019-03-15 12:00'
pattern = re.compile('\d{2}:\d{2}')
result1 = re.sub(pattern,'',content1)
result2 = re.sub(pattern,'',content2)
result3 = re.sub(pattern,'',content3)
print(result1,result2,result3)

