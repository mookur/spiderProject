'''
对于https://www.httpbin.org/get网址，当我们想附加额外信息。
可以写成https://www.httpbin.org/get?name=jim&age=18，然后拿去请求。
但有时参数太长。就可以把参数写成字典，然后给get方法传递参数。
'''

import requests

data = {'name':'jim',
        'age':'18'
        }
r = requests.get('https://www.httpbin.org/get',params=data)
print(r.text)
print(type(r.text))
# <class 'str'>
# 这个网页返回的类型是字符串类型，但很特殊，是JSON格式的。
# 所以可以调用json方法解析，得到一个JSON格式数据。

print(r.json())
# {
# 'args': {'age': '18', 'name': 'jim'},
# 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'www.httpbin.org',
# 'User-Agent': 'python-requests/2.25.0', 'X-Amzn-Trace-Id': 'Root=1-61e21be1-168fa5f62548608527107da1'},
# 'origin': '223.73.61.26',
# 'url': 'https://www.httpbin.org/get?name=jim&age=18'
# }
# json方法可以将JSON格式的字符串，转化为字典。
# 如果返回的结果不是JSON格式，就会出现解析错误，抛出json.decoder.JSONDecodeError异常。


print(type(r.json()))
# <class 'dict'>

print(r.json()["args"])
# {'age': '18', 'name': 'jim'}

