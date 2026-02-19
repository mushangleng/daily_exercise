url = 'https://v8.chaoxing.com/'
head = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
}

import requests

res = requests.get(url, headers=head)
print(res.text)

from lxml import etree

html = etree.HTML(res.text)

h3 = html.xpath('//div[@class="left"]/h3/text()')
print(h3)
