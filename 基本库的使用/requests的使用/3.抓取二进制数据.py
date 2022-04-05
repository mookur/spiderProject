'''
抓取的网页返回的是可能是一个HTML文档，也可能是一个JSON格式字符串。

而图片、音频、视频这些文件的本质都是由二进制组成。他们有特定的保存格式和特定的解析方式（才会有这么形形色色的多媒体）

所以想要抓取他们，就要拿到他们的二进制数据。

'''

import requests

r = requests.get('https://scrape.center/favicon.ico')

with open('favicon.ico','wb') as f:
    f.write(r.content)

# print(r.text)
# 因为是二进制数据，打印时会转化为str类型，写就是图片直接转化为字符串，所以会出现乱码。

# print(r.content)
# 返回结果前面带有一个b，代表这是bytes类型的数据。