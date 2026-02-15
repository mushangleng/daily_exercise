import requests


headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://music.163.com",
    "priority": "u=1, i",
    "referer": "https://music.163.com/",
    "sec-ch-ua": "\"Chromium\";v=\"142\", \"Google Chrome\";v=\"142\", \"Not_A Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
}

# 用户的身份证  VIP
cookies = {
    "_ntes_nnid": "fc66d4c6f00806bb48da4ffd4127b43c,1765457831215",
    "_ntes_nuid": "fc66d4c6f00806bb48da4ffd4127b43c",
    "NMTID": "00OI8QB277rgJkdxEJUkK4_3vy-Xy8AAAGbDXylTw",
    "WEVNSM": "1.0.0",
    "WNMCID": "qcordt.1765457831737.01.0",
    "WM_TID": "jqM3FBaa67pBERUVVEeD3xHiOvTIPKk%2F",
    "__snaker__id": "1edddfLX19WN63AR",
    "gdxidpyhxdE": "CfRfYQuV8ZSZCRbp39eAZl%2Fx%2F%2Bfn4eb7Mfv7woPeMcK%2BK5NPQti2lm5XUUy1A%5CxGxHZBRiUbIJxBiDsi%2FmX7U7VIwVObbRUKVq0D4DrebQ0hCdq9Co%2B04gbLYXTZOpkl%5ColnHN6pJZwX0Rdie7eKqe3J7mi6o83ZbAIYdbuDASng7z3x%3A1765458733392",
    "sDeviceId": "YD-ZSfcslCQSIVFVwUEBRPHz0DiarTMr1gE",
    "P_INFO": "15674995298|1765457890|1|music|00&99|null&null&null#hun&null#10#0|&0||15674995298",
    "MUSIC_U": "000522168BCC5E21882F096BE2706A70540A1816154ED4A5F3E6FC4443042D8B8ED4F385D220F075733087DFD756D974EA3A4943A8595255F5BBE9AC4B1405689928F336FC6C0EC94B88AD12579593E722C5C79DBE4184C4F40BEDF0A8EB7FB1B292C83F327609540ACBEFB68AD56E151E4E75FF5C1C033D90F35298FC90F4A883D1F1ACA7B74CDBBFC5844AC11DD6C93B658258D98938CAD8502D3C975AEC17C64FAC8B5A75E56454D1D54A5F9BAB10DA2E9E6A4C208153AABEBC5B3661CBDC4C49E8ABDE267CC88BC70E729088E9F945EDB186E08032D3FD0F52F5ABE5C8AA65BD7D1706F9536DE1CC1A2A5F922B7D342DBBFDF42E7ABED75B1423AD53B929C14F7058C03B62D8E5390B11CBEC2CC7352B51C13B28BF201249AA0EC3DD8A252D6BEEE520C3DB8DCC9AA1516B7FA0526D2E1A9D2D1F529FA60CC5A4AB2C99AD4C2EA39DD88E9CDB6AEDF66A76C782B4C3CF2AF1E4C60BE0B931B6D8FC62ADB65AB564CA92B77839666E13A54EC5DC6870624025C9D8FBF741ED47ECB53844C8103C417E20F107D64791080F22241087CC",
    "__csrf": "18a625cc314e022929f308fdeff6a74d",
    "__remember_me": "true",
    "ntes_kaola_ad": "1",
    "_iuqxldmzr_": "32",
    "JSESSIONID-WYYY": "SBwaSo4YFd4HDECI%2Bha6pezMixQ0fRwOCiIAC7BENa5tTM%5CsGYbbDqV7B%5C412YN5CyAMcbsDHYTTQPpAeIA85wKetrI9hplZ3S9yPPktnpUf6FpKg0oue0XIEIi1l%2BdVbFRpF4rykC2S32ilyIwxDsimf3PmCxzB%5CBs%2F%5CHdFIap16uHk%3A1765628336846",
    "WM_NI": "JFMKVDXCSEHmGCEfErc%2FZUi7gd3oCWXUcMePQGQi5C1od7EociE4MpTcgMYFy6SzgsdMs%2BF%2Fp%2FLpWQve8gW2jKLBWYmDww4XeoRNtPGkLOKuJkL2kKPw6Bh5XtkGSg%2FENWI%3D",
    "WM_NIKE": "9ca17ae2e6ffcda170e2e6eed8b2619388a982c180f58e8fa6c54a868e8b87d667f497bed2d967fbed00a2f32af0fea7c3b92a8a9a83acd5509c9d9da6cb67859d8b87c87aa1f196b6ec3da5bcfd90c25d9c8badaee85c93999f8ab849f3b1acd8c865a1b78bd5d07c98bda9aedc4ebbea9d9be679a893bdccc525b4f18491d65bb6bbf888d63aaa9584a3d653af9cb998b754a7b19eaff75c85b584b0ca7f8ab584d3ea4194a9faa3eb3f9caca5a8d26ded9b82b8cc37e2a3",
    "ntes_utid": "tid._.m8N%252BxmwOoH1AUkBUEAfSnlXneuHJ7Z4D._.0",
    "playerid": "14732688"
}
url = "https://music.163.com/weapi/song/enhance/player/url/v1"
params = {
    "csrf_token": "18a625cc314e022929f308fdeff6a74d"
}
data = {
    "params": "ULQPotb7qmsNO4df0dug2EQQt9BwO20USp7kQ8Xbi+s7yeoBrLK2SFGCxM4bupKVkMaAB649NLAk8L74g8RJ34rVWQd/mbQajc9NxuWus3LvjWprDJiugn5enl8UlFD5bAyhB2TNcENh+whc7HVOBbRyJDFYvGeVSaq/IOQMF/khx+cMAU1XmeLR0V+8hgTpcXsjf/nSqY2W0hRtJ588wA==",
    "encSecKey": "891b9c2f826f6dd446801b584f571654ba4c3f47c41c9dc6f13c04a9f4551f13474f459d9ae31032a46cce5a7fc2a939f3af88bf6d9a93900400488621c844249263cac8f46ac911cdc5be76215a6ffc37fb6a08a9a59a872339bf76684f0e83746617b45e4200a8c77785013f4c3ec6a024adf8fee5efb7d07ed45cc48dd85e"
}
response = requests.post(url, headers=headers, params=params, data=data,cookies=cookies)


url = response.json()['data'][0]['url']
print(url)

import os
if not os.path.exists('music'):
    os.mkdir('music')


with open('music/vip.mp3','wb') as f:
    f.write(requests.get(url).content)

print('vip歌曲下载完成')