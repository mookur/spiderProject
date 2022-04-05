'''
urllib库处理网络验证和Cookie时，需要写Opener类和Handler类处理。很麻烦。
为了更方便实现这些操作，可以使用requests库。
'''

import requests

r = requests.get('https://www.baidu.com/')
# 调用get方法，以GET方式请求网页。
# 还有其他请求类型，post、put、delete、patch。

print(type(r))
# 结果：<class 'requests.models.Response'>，返回一个Response对象。

print(r.status_code)
# 打印响应的状态码。
# 结果：200。

print(type(r.text))
# 结果：<class 'str'>，响应体类型是字符串类型。

print(r.text[:100])
# 响应返回的是网页HTML文件。
# <!DOCTYPE html>
# <!--STATUS OK--><html> <head><meta http-equiv=content-type content=text/html;charse

print(r.cookies)
# 结果：<RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
# Cookie类型是RequestsCookieJar。