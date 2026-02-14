# http://www.htqyy.com/

import requests
import os

if not os.path.exists("music"):
    os.mkdir("music")

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0',
    'referer': 'http://www.htqyy.com/'
}

url = 'http://s1.htqyy.com/play9/33/mp3/1'

res = requests.get(url, headers=headers)

print(res.status_code)
# print(res.content)


# with open('music/1.mp3', 'wb') as f:
#     f.write(res.content)

# referer 是HTTP请求头的一个字段，它的作用是告诉服务器：当前的请求是从哪个网页链接过来的。
# 它就是网络浏览的"引荐人"，或者"上一页地址"
