# https://www.qqtn.com/tx/nvshengtx_1.html

import requests
from lxml import etree
import os

if not os.path.exists("头像"):
    os.mkdir("头像")

for page in range(1, 11):
    print(f"-----------------------------------开始爬第{page}页-----------------------------------")
    url = f'https://www.qqtn.com/tx/nvshengtx_{page}.html'
    res = requests.get(url)

    # 解决乱码
    # res.encoding = 'gb2312'
    res.encoding = res.apparent_encoding

    # 1、把获取的响应数据 变成 html数据
    html = etree.HTML(res.text)

    # 2、用xpath解析html数据
    src_list = html.xpath('//ul[@class="g-gxlist-imgbox"]/li/a/img/@src')
    name_list = html.xpath('//ul[@class="g-gxlist-imgbox"]/li/a/img/@alt')

    for src, name in zip(src_list, name_list):
        with open(f"头像/{name}.jpg", 'wb') as f:
            f.write(requests.get(src).content)

        print(f'{name}.jpg下载完成')
