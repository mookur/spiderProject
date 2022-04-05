'''

很多网站要求使用HTTPS协议，有些网站没有设置HTTPS证书 或者 网站证书不被CA机构认可，就会出现SSL证书报错。

如果用requests请求这些网址，会报错。

1.通过在请求中加入verify参数来解决报错。False表示不验证网址的证书，默认是True。
    -没有报错，但是会有警告。
    -1.可以通过设置忽略警告的方式屏蔽这警告。
    -2.通过捕获警告到日志的方式忽略警告。
2.指定一个本地证书 用作客户端证书，可以是单个文件（包含密钥和证书） 或 一个包含两个文件路径的元组

'''

import requests

response = requests.get('https://ssr2.scrape.center/',verify=False)
# 请求一个证书有问题的网址。
print(response.status_code)

# 不会报错，但会出现一个警告。InsecureRequestWarning
# 200


# 1.设置忽略警告 来屏蔽警告
from requests.packages import urllib3

urllib3.disable_warnings()
response = requests.get('https://ssr2.scrape.center/',verify=False)
print(response.status_code)


# 2.设置捕获警告到日志忽略警告
import logging

logging.captureWarnings(True)
response = requests.get('https://ssr2.scrape.center/',verify=False)
print(response.status_code)

# 指定本地证书用作客户证书。
# 我们需要有crt和key文件，并指定路径。另外本地私有证书的key必须是解密状态。
# response = requests.get('https://ssr2.scrape.center/',cert=('/path/server.crt','/path/server.key'))
# print(response.status_code)
