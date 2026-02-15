import os
import requests

if not os.path.exists('虎牙'):
    os.mkdir('虎牙')
    os.mkdir('虎牙/1')
    os.mkdir('虎牙/2')
    os.mkdir('虎牙/3')
    os.mkdir('虎牙/4')
    os.mkdir('虎牙/5')
    os.mkdir('虎牙/6')


class Huya():
    def __init__(self):
        self.path = 1
        self.url = 'https://live.huya.com/liveHttpUI/getLiveList?iGid=1663&iPageNo=1&iPageSize=120'

    def get_data(self):
        vList = requests.get(self.url).json()['vList']
        self.get_img_url(vList)

    def get_img_url(self, vList):
        for i in vList:
            sNick = i['sNick']
            sScreenshot = i['sScreenshot']
            self.get_pci(sNick, sScreenshot)

    def get_pci(self, name, url):
        res = requests.get(url).content
        with open(f'虎牙/{self.path}/{name}.jpg', 'wb') as f:
            f.write(res)
        print(f'{name}.jpg下载成功')


if __name__ == "__main__":
    huya = Huya()

    for page in range(1, 7):
        print(f'----------开始下载第{page}页----------')
        huya.path = page
        huya.url = f'https://live.huya.com/liveHttpUI/getLiveList?iGid=1663&iPageNo={page}&iPageSize=120'
        huya.get_data()
