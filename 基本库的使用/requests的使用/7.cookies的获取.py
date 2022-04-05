'''
为什么要Cookie？很多页面是需要登录之后才能查看，输入账号和密码拿到了类型登录的凭证才能登录。Cookies在客户端或浏览器端，session在服务器。
Cookie保存着登录的凭证，客户端或浏览器携带Cookie，发送给服务器。服务器识别后就可以返回登录后的页面。

'''
import requests

r = requests.get('https://www.baidu.com')
print(r.cookies)
# 结果：<RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>

print(type(r.cookies))
# 返回的是一个cookieJar对象。
# 结果：<class 'requests.cookies.RequestsCookieJar'>

print(r.cookies.items())
# <class 'list'>
# items方法将Cookie转化为 由元组组成的 列表。
# 结果：[('BDORZ', '27315')]

for key, value in r.cookies.items():
    # 遍历列表，元组元素赋值取出。
    print(key,value)
