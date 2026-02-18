import requests
import os

if not os.path.exists('王者荣耀'):
    os.mkdir('王者荣耀')

url = 'https://pvp.qq.com/zlkdatasys/heroskinlist.json'
res = requests.get(url)
data_json = res.json()
pflb = data_json['pflb20_3469']
yxlb = data_json['yxlb20_2489']

for i in pflb:
    yx_name = i['yxmclb_9965']
    pf_name = i['pfmclb_7523']
    pf_url = i['fmlb_4536']
    print(yx_name,pf_name,pf_url)

    if not os.path.exists(f'王者荣耀/{yx_name}'):
        os.makedirs(f'王者荣耀/{yx_name}')

    with open(f'王者荣耀/{yx_name}/{pf_name}.jpg','wb') as f:
        f.write(requests.get(pf_url).content)

