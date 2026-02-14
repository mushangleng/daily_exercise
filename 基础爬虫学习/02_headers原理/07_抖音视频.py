import requests
import os

if not os.path.exists("video"):
    os.mkdir("video")

url = 'https://v26-web.douyinvod.com/c9592727b7056ee83f87813af5472891/6990a527/video/tos/cn/tos-cn-ve-15/oISQP1GTQLAEIwCz8gIaeABqBesTe7WoSQTJAS/?a=6383&ch=224&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=760&bt=760&cs=0&ds=6&ft=4TMWc6Dnppft3dL..sO.C_bAja-CInEiOwZc6Be_fMCCJYpHDDGJYWLems4.pusZ.&mime_type=video_mp4&qs=12&rc=OTk3ZDs4N2Y5Ojs0OmVkPEBpMzxmbHk5cjVwODMzNGkzM0AvM2EuYl4vNl8xYTUxYzNjYSNjZC4xMmRjLmdhLS1kLWFzcw%3D%3D&btag=c0000e00028000&cquery=100H_100K_100o_101s_100B&dy_q=1771076112&feature_id=0ea98fd3bdc3c6c14a3d0804cc272721&l=202602142135125677C4C324C53D59A86D&__vid=7595145719607004459'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0',
    'referer': 'https://www.douyin.com/'
}
res = requests.get(url,headers=headers)
print(res.status_code)

with open('video/动漫解说.mp4','wb') as f:
    f.write(res.content)