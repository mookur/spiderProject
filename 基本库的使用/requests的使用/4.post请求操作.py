# post请求时另一种常见的请求方式。

import requests

data = {'name':'mook','age':14}
r = requests.post('https://www.httpbin.org/post',data=data)
# 这个网站能判断请求是不是post方式，如果是，就会返回相关的请求信息。

print(r.text)

'''
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "age": "14", 
    "name": "mook"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Content-Length": "16", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "www.httpbin.org", 
    "User-Agent": "python-requests/2.25.0", 
    "X-Amzn-Trace-Id": "Root=1-61e3d22c-7f68dd8179b2b8f6568b7843"
  }, 
  "json": null, 
  "origin": "223.73.61.26", 
  "url": "https://www.httpbin.org/post"
}

'''

