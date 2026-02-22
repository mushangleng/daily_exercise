# https://www.huya.com/video/g/all?set_id=49  首页

# 从首页去获取所有的视频详情页
# https://www.huya.com/video/play/1086664984.html
# https://www.huya.com/video/play/1086543900.html


import requests, os, re
from lxml import etree

chars = r'[<>:/\\|?*]'

if not os.path.exists("虎牙视频"):
    os.mkdir("虎牙视频")


# 获取一个视频
def get_one(id):
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9",
        "referer": "https://www.huya.com/",
        "sec-ch-ua": "\"Chromium\";v=\"142\", \"Google Chrome\";v=\"142\", \"Not_A Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "script",
        "sec-fetch-mode": "no-cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
    }
    cookies = {
        "__yamid_new": "CB77A3B5C8200001C35F10201D004200",
        "game_did": "aUidfA12EoppFOrrB8mcVeh0bLhJI1kYm1G",
        "SoundValue": "0.50",
        "udb_guiddata": "0e9f19a0b56e4aa3a5376c1374d08d17",
        "guid": "0a7d76e5d3c83b693e017bc17cc13ae6",
        "_qimei_uuid42": "19c0c0f302410042a9ac84934e5eaae6aaebcf971c",
        "udb_deviceid": "w_1051888309056806912",
        "__yamid_tt1": "0.9397823512473191",
        "hdid": "fda619d69510a615b56041968572656014f3d884",
        "_qimei_fingerprint": "c1bf65fdcc9cdd0d077469b04dff41d7",
        "_qimei_h38": "fdedcb29a9ac84934e5eaae602000009719c0c",
        "alphaValue": "0.80",
        "_qimei_q32": "79b18b55fbe6c372550e488ebb161a19",
        "_qimei_q36": "cc53a43526f8d09a7629fdd4300010e19912",
        "udb_appid": "5002",
        "hiido_ui": "0.7850524024241377",
        "isInLiveRoom": "",
        "__yasmid": "0.9397823512473191",
        "_yasids": "__rootsid%3DCB7B3ADBF9000001A1D51CE0E860F700",
        "Hm_lvt_51700b6c722f5bb4cf39906a596ea41f": "1765525717,1765631064,1766469808,1766489514",
        "HMACCOUNT": "34F1CD1E408C916F",
        "sdid": "0UnHUgv0_qmfD4KAKlwzhqZtMNefr0qH1hqPMHSNKzbKrGMk0Uol6FQb_tD48ok0rhznS5XNRrNPnEnQ8qE-awAxSa5Y-IcIBG3y47TT2PI3WVkn9LtfFJw_Qo4kgKr8OZHDqNnuwg612sGyflFn1dh98ihEEVJLJ9-yBVcvRfBQLg_e41GpWqcjjYXZ3dvyQ",
        "udb_passdata": "3",
        "huya_flash_rep_cnt": "4",
        "huya_web_rep_cnt": "180",
        "rep_cnt": "206",
        "Hm_lpvt_51700b6c722f5bb4cf39906a596ea41f": "1766490001"
    }
    url = "https://liveapi.huya.com/moment/getMomentContent"
    params = {
        # "callback": "jQuery112405038800743079105_1766490000946",  # 注释才能拿到json数据
        "videoId": id,
        "uid": "",
        "_": "1766490000948"
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)

    # 获取视频的链接 和 视频的名称
    video_link = response.json()['data']['moment']['videoInfo']['definitions'][0]['url']
    video_name = response.json()['data']['moment']['title']
    video_name = re.sub(chars, "", video_name)

    with open(f'虎牙视频/{video_name}.mp4', 'wb') as f:
        f.write(requests.get(video_link).content)

    print(f'{video_name}.mp4下载完成')


# 获取所有的视频id
def get_all(page):
    import requests

    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-CN,zh;q=0.9",
        "priority": "u=0, i",
        "referer": "https://www.huya.com/video/g/all?set_id=49&order=hot&page=4",
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
        "huya_ua": "webh5&1.0.0&huya",
        "__yamid_new": "CB77A3B5C8200001C35F10201D004200",
        "game_did": "aUidfA12EoppFOrrB8mcVeh0bLhJI1kYm1G",
        "SoundValue": "0.50",
        "udb_guiddata": "0e9f19a0b56e4aa3a5376c1374d08d17",
        "guid": "0a7d76e5d3c83b693e017bc17cc13ae6",
        "_qimei_uuid42": "19c0c0f302410042a9ac84934e5eaae6aaebcf971c",
        "udb_deviceid": "w_1051888309056806912",
        "__yamid_tt1": "0.9397823512473191",
        "hdid": "fda619d69510a615b56041968572656014f3d884",
        "_qimei_fingerprint": "c1bf65fdcc9cdd0d077469b04dff41d7",
        "_qimei_h38": "fdedcb29a9ac84934e5eaae602000009719c0c",
        "alphaValue": "0.80",
        "_qimei_q32": "79b18b55fbe6c372550e488ebb161a19",
        "_qimei_q36": "cc53a43526f8d09a7629fdd4300010e19912",
        "udb_appid": "5002",
        "hiido_ui": "0.7850524024241377",
        "amkit3-v-player-machine-id": "0.743451343509916",
        "isInLiveRoom": "",
        "amkit3-player-danmu-pop": "1",
        "__yasmid": "0.9397823512473191",
        "_yasids": "__rootsid%3DCB7B3ADBF9000001A1D51CE0E860F700",
        "Hm_lvt_51700b6c722f5bb4cf39906a596ea41f": "1765525717,1765631064,1766469808,1766489514",
        "HMACCOUNT": "34F1CD1E408C916F",
        "sdid": "0UnHUgv0_qmfD4KAKlwzhqZtMNefr0qH1hqPMHSNKzbKrGMk0Uol6FQb_tD48ok0rhznS5XNRrNPnEnQ8qE-awAxSa5Y-IcIBG3y47TT2PI3WVkn9LtfFJw_Qo4kgKr8OZHDqNnuwg612sGyflFn1dh98ihEEVJLJ9-yBVcvRfBQLg_e41GpWqcjjYXZ3dvyQ",
        "udb_passdata": "3",
        "huya_flash_rep_cnt": "4",
        "amkit3-v-player-session-id": "0.5985681313448474",
        "huya_web_rep_cnt": "180",
        "Hm_lpvt_51700b6c722f5bb4cf39906a596ea41f": "1766491411",
        "rep_cnt": "290"
    }
    url = "https://www.huya.com/video/g/all"
    params = {
        "set_id": "49",
        "order": "hot",
        "page": page
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)

    # 用xpath解析出id
    html = etree.HTML(response.text)
    # <ul class='vhy-video-list clearfix '   <li data-vid="1086664984"
    id_s = html.xpath("//ul[@class='vhy-video-list clearfix ']/li/@data-vid")

    # 循环去下载每一个视频
    for id in id_s:
        get_one(id)


if __name__ == "__main__":
    for page in range(1, 3):
        print(f"--------------------开始下载第{page}页--------------------")
        get_all(page)
