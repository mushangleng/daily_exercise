# https://v8.chaoxing.com/  学习通

import requests

url = 'https://v8.chaoxing.com/'
# res = requests.get(url)
# print(res.status_code)  # 403 拒绝

headers = {
    # UA 用户代理（浏览器的标识）
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0',
}
res = requests.get(url, headers=headers)  # 服务器被你迷惑了，认为你是一个 电脑端的Edg浏览器

print(res.status_code)

# 获取html响应
print(res.text)

# 常见的UA：https://www.cnblogs.com/puwen/p/18721451
