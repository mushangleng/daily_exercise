#https://image.baidu.com/search/acjson?tn=resultjson_com&word=%E8%B5%B5%E4%B8%BD%E9%A2%96&ie=utf-8&fp=result&fr=&ala=0&applid=10233202889017618015&pn=30&rn=30&nojc=0&gsm=1e&newReq=1

import requests
import uuid
import os

word = input("你要爬谁的图片？")
page = int(input("你要爬几页？"))

if not os.path.exists(word):
    os.mkdir(word)

for i in range(0, page):
    print(f'开始爬取第{i+1}页')
    params = {
        "tn": "resultjson_com",
        "word": word,
        "ie": "utf-8",
        "fp": "result",
        "fr": "",
        "ala": "0",
        "applid": "10233202889017618015",
        "pn": str(i*30),  # 第一页0 第二页30 第三页6 !转成字符串
        "rn": "30", # 每一页有30张图片，一页最多60张
        "nojc": "0",
        "gsm": "1e",
        "newReq": "1"
    }
    url = 'https://image.baidu.com/search/acjson'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Referer": "https://image.baidu.com/search/index?tn=baiduimage&fm=result&ie=utf-8&word=%E8%B5%B5%E4%B8%BD%E9%A2%96",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Google Chrome\";v=\"144\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }

    cookies = {
        "BAIDUID": "9A664BC64769547B39B89A62E1BF7384:FG=1",
        "H_WISE_SIDS": "67224_67319_67317_67314_67323_67321_67442_67548_67546_67600_67616_67594_67634_67651_67695_67719_67757_67749_67731_67816_67836",
        "BAIDUID_BFESS": "9A664BC64769547B39B89A62E1BF7384:FG=1",
        "ab_sr": "1.0.1_MTk2Mjc4NzgyMDA5NzUwNjM3MmUwMzQ3NGUwNGM4MTBkM2VmMzhmOGUwZTM2MjRmODJjNTY1OWZkNjlkNmZjMTViY2MzNTc4NTZlZjI2ODE0Y2UzNzM5YmM3MzkyMjEzNjgwOTI0YzE5ZTIwYzdkNTg4N2UxMjc1ZWVlOGE3NzIxZDQ5NmIxZTBlODgyNWJjYjBhMjhmNjg3ODdhMzZhNQ=="
    }



    res = requests.get(url,headers=headers,params=params)

    # print(res.status_code)
    img_list = res.json()['data']['images']
    # print(len(img_list))

    for i in img_list:
        url = i['thumburl']
        # print(url)

        unique_id = uuid.uuid4()             # 给每张图片起一个唯一名字
        # print(unique_id, type(unique_id))    # 看一下类型，需要转成字符串
        id_str = str(unique_id)
        # print(id_str,type(id_str))

        res = requests.get(url).content
        with open(f'{word}/{id_str}.png', 'wb') as f:
            f.write(res)

