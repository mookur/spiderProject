'''
客户端浏览器中保存的Cookie 携带着SessionID信息，服务器检查Cookie找到对应的Session，通过Session辨认用户状态。
传给服务器的Cookie是无效的 或者 Session过期了，客户端就需要重新登陆。


Session的作用：在用get和post 或者 两次get请求 网址时，实际上对应着两个不同的Session。第二次请求是不会有第一次请求的cookie的，
也就不会是登录状态，。Session对象能让 不需要每次设置Cookie，维护一个Session会话。

利用Session可以做到模拟同一个会话而不用担心Cookie问题。通常在模拟登录成功之后，进行下一步操作时用到。
'''

import requests

requests.get('https://www.httpbin.org/cookies/set/number/123456789')
# 第一次请求，设置了一条cookie,number=123456789。

r = requests.get('https://www.httpbin.org/cookies')
# 第二次请求，查看是否存在上次请求设置的cookie。

print(r.text)
# {"cookies": {}}
# 结果并没有，两次请求相当于用 两个浏览器 打开了不同的页面。是完全独立的两个操作，对应两个完全不相关的Session.
# （理解：或者说两个不同的浏览器更好，因为浏览器端没有储存相同的cookie信息）


s = requests.Session()
# 这里创建了一个Session对象。
s.get('https://www.httpbin.org/cookies/set/number/123456789')
# 第一次请求，相当于带着session设置cookie
r = s.get('https://www.httpbin.org/cookies')
# 第二次请求，带着session，里面有cookie了
print(r.text)
#{"cookies": {"number": "123456789"}}
