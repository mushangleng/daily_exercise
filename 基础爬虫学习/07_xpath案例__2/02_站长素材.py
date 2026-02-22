# https://sc.chinaz.com/tupian/qinglvtupian.html  第一页
# https://sc.chinaz.com/tupian/qinglvtupian_2.html 第二页
# https://sc.chinaz.com/tupian/qinglvtupian_3.html 第三页
# https://sc.chinaz.com/tupian/qinglvtupian_4.html 第四页



import requests,os
from lxml import etree

if not os.path.exists("站长素材"):
    os.mkdir("站长素材")

def get_one(href):
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "max-age=0",
        "priority": "u=0, i",
        "referer": "https://sc.chinaz.com/tupian/qinglvtupian_3.html",
        "sec-ch-ua": "\"Chromium\";v=\"142\", \"Google Chrome\";v=\"142\", \"Not_A Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
    }
    cookies = {
        "cz_statistics_visitor": "0282f04e-5146-8853-efca-8f9b9d35d762",
        "_clck": "1lu8hif%5E2%5Eg23%5E0%5E2183",
        "Hm_lvt_398913ed58c9e7dfe9695953fb7b6799": "1766473942,1766492980",
        "HMACCOUNT": "34F1CD1E408C916F",
        "_clsk": "jzxhnl%5E1766493127402%5E1%5E1%5Eh.clarity.ms%2Fcollect",
        "Hm_lpvt_398913ed58c9e7dfe9695953fb7b6799": "1766493263"
    }
    url = f"https://sc.chinaz.com{href}"
    response = requests.get(url, headers=headers, cookies=cookies)
    # 解决乱码
    response.encoding = response.apparent_encoding

    html = etree.HTML(response.text)
    # xpath div class='img-box'
    src = html.xpath("//div[@class='img-box']/img/@src")[0]

    # 如果src里面没有"https:" 我们才去拼接
    if "https:" not in src:
        src = "https:" + src
    # 欧美街头时尚街拍手牵手逛街情侣图片.png下载完成
    # https:https://scpic.chinaz.net/files/default/imgs/2024-09-03/c4bc612b96406438.jpg

    alt = html.xpath("//div[@class='img-box']/img/@alt")[0]

    with open(f"站长素材/{alt}.png",'wb') as f:
        f.write(requests.get(src).content)

    print(f'{alt}.png下载完成')


# 获取所有的图片id
def get_all(page):

    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-CN,zh;q=0.9",
        "priority": "u=0, i",
        "referer": "https://sc.chinaz.com/tupian/qinglvtupian_2.html",
        "sec-ch-ua": "\"Chromium\";v=\"142\", \"Google Chrome\";v=\"142\", \"Not_A Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
    }
    cookies = {
        "cz_statistics_visitor": "0282f04e-5146-8853-efca-8f9b9d35d762",
        "_clck": "1lu8hif%5E2%5Eg23%5E0%5E2183",
        "_clsk": "1v32lg3%5E1766478579330%5E2%5E1%5Eh.clarity.ms%2Fcollect",
        "Hm_lvt_398913ed58c9e7dfe9695953fb7b6799": "1766473942,1766492980",
        "HMACCOUNT": "34F1CD1E408C916F",
        "Hm_lpvt_398913ed58c9e7dfe9695953fb7b6799": "1766493051"
    }
    url = f"https://sc.chinaz.com/tupian/qinglvtupian{page}.html"


    response = requests.get(url, headers=headers, cookies=cookies)

    html = etree.HTML(response.text)

    #  <a class="name"
    href_s = html.xpath("//a[@class='name']/@href")
    for href in href_s:
        get_one(href)


url = f"https://sc.chinaz.com/tupian/qinglvtupian_2.html"

if __name__ == "__main__":

    for page in range(1,4):
        print(f"--------------------开始下载第{page}页--------------------")

        if page == 1:
            page = ""
        else:
            page = f'_{page}'   # 第二次循环page=_2

        get_all(page)
