import requests

jar = requests.cookies.RequestsCookieJar()
# 创建CookieJar对象。
# 不知道这里cookies为什么显黄色。

cookies = '_octo=GH1.1.988146769.1646178917; _device_id=1b787c6161561ee70983e03f6098a796; user_session=ValTqWdvmdEWwD4X7PwA5LBjzfARlx9CvpD4xv_ohnfAn__P; __Host-user_session_same_site=ValTqWdvmdEWwD4X7PwA5LBjzfARlx9CvpD4xv_ohnfAn__P; logged_in=yes; dotcom_user=mookur; has_recent_activity=1; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; tz=Asia%2FShanghai; _gh_sess=nWWcyPfyLNgVH8ASF0HiEyY4DjK0WhTwUQuhx3l73FIi1HWkJtoAL5aB%2BrcPjzSfHpwlzDGPTEBJfvpqLSlPjo0xvlPB5Dy%2F7DiYgiS9ntxZeOTG7Ed5dWUJuFH0OSVUGvJOR2iv1wBCR9ReFyH2k1bp40uhBIA4psbh%2FTGabbIDUK3nhmxn%2Bbx%2BWgYuZ0r4--jwc9G6pEk95lx7Qx--cN5vT5Lb0G29MWsJ3sPmjg%3D%3D'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}

for cookie in cookies.split(';'):
    key, value = cookie.split('=',1)
    # 1还是一样，代表分成两份。split方法里的参数。

    jar.set(key,value)
    # cookiejar的set方法。能够设置好每个Cookie条目的键名和键值。

r = requests.get('https://github.com/',cookies=jar,headers=header)
print(r.text)
# 打印出来可以发现HTML文档存在github用户名的信息。
# 通过Cookie获取了登录后的页面。
# 这是比较专业的方法，也可以直接把cookies放在自己创建的请求头字典里面，进行传递。