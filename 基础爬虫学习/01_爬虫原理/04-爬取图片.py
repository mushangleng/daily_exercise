# https://www.qqtn.com/tx/nvshengtx_1.html

# 图片的网址 https://pic.qqans.com/up/2024-6/17174597153652891.jpg

import requests

url = 'https://pic.qqans.com/up/2024-6/17174597153652891.jpg'
res = requests.get(url)
print(res.status_code)  # 200

data = res.content # 获取图片的二进制
print(data)

# for i in res.content:
#     # print(i) # 十进制
#     # print(bin(i)) # 二进制 0b开头
#     # print(oct(i)) # 八进制  0o开头
#     print(hex(i)) # 十六进制 0x开头


# 把数据写入到文件中
with open('mv.png','wb') as f:
    f.write(data)