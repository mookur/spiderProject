'''
除了用text和content获取了响应的内容。
还有其他的属性和方法获取其他信息。

'''

import requests

r = requests.get('https://ssr1.scrape.center/')
print(type(r.status_code),r.status_code)
# <class 'int'> 200

print(type(r.headers),r.headers)
# <class 'requests.structures.CaseInsensitiveDict'>

print(type(r.cookies),r.cookies)
# <class 'requests.cookies.RequestsCookieJar'> <RequestsCookieJar[]>
# 得到cookie

print(type(r.url),r.url)
# <class 'str'>   https://ssr1.scrape.center/
# 得到url

print(type(r.history),r.history)
# <class 'list'>   []
# 得到请求历史

