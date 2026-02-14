import requests

# 快速构建请求头参数 在抓到的包上右键，点复制，点以CURL(bash)格式复制，粘贴到 https://spidertools.cn/#/curl2Request

headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "origin": "https://m.bilibili.com",
    "priority": "i",
    "range": "bytes=0-",
    "referer": "https://m.bilibili.com/",
    "sec-fetch-dest": "video",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Mobile/15E148 Safari/604.1"
}
url = "https://cn-nmghhht-cu-01-08.bilivideo.com/upgcxcode/06/57/26087195706/26087195706-1-16.mp4"
params = {
    "e": "ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=",
    "mid": "0",
    "deadline": "1765466920",
    "gen": "playurlv3",
    "og": "ali",
    "nbs": "1",
    "oi": "0x240883520448e9d0043ae9430c7c7eb8",
    "trid": "0000a7df2d93545246299abf70c548baec5h",
    "os": "bcache",
    "platform": "html5",
    "uipk": "5",
    "upsig": "30f8296a585df4a9a5cdd745c7539b91",
    "uparams": "e,mid,deadline,gen,og,nbs,oi,trid,os,platform,uipk",
    "cdnid": "5248",
    "bvc": "vod",
    "nettype": "0",
    "bw": "174396",
    "lrs": "37",
    "build": "0",
    "dl": "0",
    "f": "h_0_0",
    "agrr": "0",
    "buvid": "",
    "orderid": "0,1"
}
response = requests.get(url, headers=headers, params=params)

print(response.text)
print(response.content)

with open('video/高数.mp4', 'wb') as f:
    f.write(response.content)

print('ok')

# 作业
# 1 抓    2个抖音视频
# 2 抓    2个 B站的教学视频
