import requests
import os

if not os.path.exists("video"):
    os.mkdir("video")

# 酷狗音乐
url = 'https://webfs.kugou.com/202512112044/85ac185bd91deaba7bcc089e36cb6a7d/v3/89a13bba382b4cf1b911b5c9571e4c92/yp/full/ap1014_us2101794080_mii0w1iw8z2ai2iphcu80ooo2ki81120_pi406_mx822658289_s3573803764.mp3'
url = 'https://webfs.kugou.com/202512112050/7ee3c02acf807e54920731239308ba0d/v3/cef68c55140296503b5b91be6d1a8d94/yp/p_0_960141/ap1014_us2101794080_mii0w1iw8z2ai2iphcu80ooo2ki81120_pi406_mx805550981_s1141743429.mp3'

# 网易云
url = 'https://m804.music.126.net/20251211213730/7332f79c1ba06743f0d33286d52aaf66/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/76257311845/6c93/f9fc/abec/32ded10b6cc11f278114086317bab603.m4a?vuutv=vyopGSe6fbflyhHcm2quyA1uek7t+tfttBbF4irLkho2vkUpKrEOl0UTUplW6FcEFSauFPiPMAsheUA9C7pvGNcBUBZ053XSZQSIPNFOo5s=&authSecret=0000019b0d8aacc01b540a3b1d7325c0&cdntag=bWFyaz1vc193ZWIscXVhbGl0eV9leGhpZ2g'

# 抖音视频
url = 'https://v3-web.douyinvod.com/51a7a9a7aac7d456d848fda9b26c9f21/693aee52/video/tos/cn/tos-cn-ve-15/oYFHgeUeGBFPL9XBzyIxrcQPcCaILCtASz7fDA/?a=6383&ch=10010&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=2408&bt=2408&cs=2&ds=10&ft=_7BhlHPIAARXPsb68uCd.FGcvk3.-IhE-h8lH6gOqmRYgSAWPPlFFPg3P3-PRfqs&mime_type=video_mp4&qs=15&rc=OzUzPDg0aTs4OGg0ZDplaEBpamRpaW45cnhveDMzNGkzM0AuNDQyYi1fNTUxYjIzMjUwYSMtYW1lMmRjZHBgLS1kLWFzcw%3D%3D&btag=c0000e00008000&cquery=101r_100B_100x_100z_100o&dy_q=1765458968&feature_id=8129a1729e50e93a9e951d2e5fa96ae4&l=20251211211608EAE06C1D5191D22E9811&__vid=7474103216330804489'
url = 'https://v3-web.douyinvod.com/112530fec11ca3c58a79e1c2fe3bb637/693aee61/video/tos/cn/tos-cn-ve-15c000-ce/oMhAEaOeWEAnQHko4T9oUfQWhwi5kCBj0IleVi/?a=6383&ch=10010&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=2363&bt=2363&cs=2&ds=10&ft=_7BhlHPIAARXPsb68uCd.FGcvk3.-IhE-h8lH6gOqmRYgSAWPPlFFPg3P3-PRfqs&mime_type=video_mp4&qs=15&rc=ZGdoNTszaDRnOTxoZjU1N0BpampxZHM5cjppNjMzbGkzNEAxYS4tNWE1XjYxXmAzYjUuYSNkZDFmMmRjNV5hLS1kLWJzcw%3D%3D&btag=c0000e00010000&cquery=100x_100z_100o_101r_100B&dy_q=1765458968&feature_id=10cf95ef75b4f3e7eac623e4ea0ea691&l=20251211211608EAE06C1D5191D22E9811&__vid=7553930981939367225'

# with open('music/昨天今天-王心凌.mp3', 'wb') as f:
#     f.write(requests.get(url).content)


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
    'referer': 'https://www.douyin.com/'
}

res = requests.get(url, headers=headers)

# print(res.content)

# 保存到文件中
with open('video/井川里予2.mp4', 'wb') as f:
    f.write(res.content)
