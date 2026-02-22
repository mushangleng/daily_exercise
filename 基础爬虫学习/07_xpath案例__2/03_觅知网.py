import requests, os
from lxml import etree

if not os.path.exists("觅知网"):
    os.mkdir("觅知网")


def get_one(id):
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "max-age=0",
        "priority": "u=0, i",
        "referer": "https://www.51miz.com/so-chahua/84962.html",
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
        "couponSign": "1",
        "ustk": "202512231644_3704283163_761510570",
        "seoChannel": "1",
        "_uab_collina": "176647948865711007292242",
        "is_beijing": "0",
        "Qs_lvt_158497": "1766479489",
        "ufrom": "41",
        "semplan": "1",
        "semunit": "1",
        "semkeywordid": "1",
        "semsource": "1",
        "QuDao": "51",
        "PixelRatio": "0.8999999761581421",
        "www.echatsoft.com_12020_encryptVID": "4ZlbLmxHNG3n5IAxXvw%2FCg%3D%3D",
        "www.echatsoft.com_12020_chatVisitorId": "4707523505",
        "echat_firsturl": "--1",
        "echat_firsttitle": "--1",
        "Hm_lvt_bc4ea2e575079e12dc5f2c93526232a8": "1766479489,1766492983",
        "HMACCOUNT": "34F1CD1E408C916F",
        "Hm_lvt_d8453059bf561226f5e970ffb07bd9d2": "1766479489,1766492983",
        "backurl": "https%3A%2F%2Fwww.51miz.com%2Fsucai%2F1264512.html%3Fkeyword_id%3D84962",
        "Qs_pv_158497": "819742345405620600%2C3375658615205429000%2C1572791983403476000%2C998830084142326400%2C377072287742475650",
        "Hm_lpvt_d8453059bf561226f5e970ffb07bd9d2": "1766495543",
        "Hm_lpvt_bc4ea2e575079e12dc5f2c93526232a8": "1766495543"
    }
    url = f"https://www.51miz.com/sucai/{id}.html"
    params = {
        "keyword_id": "84962"
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)

    html = etree.HTML(response.text)
    # div class="img-box pr"
    name = html.xpath('//div[@class="img-box pr"]/img/@alt')[0]
    src = "https:" + html.xpath('//div[@class="img-box pa"]/img/@src')[0]
    src = src.split("?")[0]

    with open(f'觅知网/{name}.jpg', 'wb') as f:
        f.write(requests.get(src).content)
    print(f'{name}.jpg下载完成')


# https://www.51miz.com/sucai/1264512.html?keyword_id=84962
# https://www.51miz.com/sucai/1265157.html?keyword_id=84962

# 获取所有的id
def get_all():
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "max-age=0",
        "priority": "u=0, i",
        "sec-ch-ua": "\"Chromium\";v=\"142\", \"Google Chrome\";v=\"142\", \"Not_A Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
    }
    cookies = {
        "couponSign": "1",
        "ustk": "202512231644_3704283163_761510570",
        "seoChannel": "1",
        "_uab_collina": "176647948865711007292242",
        "is_beijing": "0",
        "Qs_lvt_158497": "1766479489",
        "ufrom": "41",
        "semplan": "1",
        "semunit": "1",
        "semkeywordid": "1",
        "semsource": "1",
        "QuDao": "51",
        "PixelRatio": "0.8999999761581421",
        "www.echatsoft.com_12020_encryptVID": "4ZlbLmxHNG3n5IAxXvw%2FCg%3D%3D",
        "www.echatsoft.com_12020_chatVisitorId": "4707523505",
        "echat_firsturl": "--1",
        "echat_firsttitle": "--1",
        "Hm_lvt_bc4ea2e575079e12dc5f2c93526232a8": "1766479489,1766492983",
        "HMACCOUNT": "34F1CD1E408C916F",
        "Hm_lvt_d8453059bf561226f5e970ffb07bd9d2": "1766479489,1766492983",
        "backurl": "https%3A%2F%2Fwww.51miz.com%2Fsucai%2F1209117.html%3Fkeyword_id%3D84962",
        "Qs_pv_158497": "1572791983403476000%2C998830084142326400%2C377072287742475650%2C191258782694704700%2C1299889113002654500",
        "Hm_lpvt_d8453059bf561226f5e970ffb07bd9d2": "1766495991",
        "Hm_lpvt_bc4ea2e575079e12dc5f2c93526232a8": "1766495991"
    }
    url = "https://www.51miz.com/so-chahua/84962.html"
    response = requests.get(url, headers=headers, cookies=cookies)

    # <a class="image-box"
    html = etree.HTML(response.text)
    a_s = html.xpath('//a[@class="image-box"]/@href')
    for a in a_s:
        get_one(a.split("sucai/")[-1].split(".")[0])


get_all()

# 作业  把上面这个代码加上分页 爬取
