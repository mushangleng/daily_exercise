# 网易云的外链
# 指将网易云音乐嵌入到其他的网站或平台上的链接
# http://music.163.com/song/media/outer/url?id=3314414289.mp3

import requests
from lxml import etree
import os
import re

chars = r'[<>:/\\|?*]'

if not os.path.exists("网易云音乐"):
    os.mkdir("网易云音乐")

url = 'https://music.163.com/discover/toplist?id=19723756'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
}
res = requests.get(url, headers=headers)

html = etree.HTML(res.text)

ul = html.xpath('//ul[@class="f-hide"]')[0]

for li in ul:
    href = li.xpath('.//a/@href')
    name = li.xpath('.//a/text()')
    href = "".join(href)
    id = href.split("=")[-1]
    href = f'http://music.163.com/song/media/outer/url?id={id}.mp3'

    name = "".join(name)
    # 如果name中出现了chars中的任意字符，那么就替换为空
    name = re.sub(chars, '', name)

    with open(f'网易云音乐/{name}.mp3', 'wb') as f:
        f.write(requests.get(href).content)

    print(f"{name}.mp3下载完成")
