# https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js?ts=2952076

import requests
import os

if not os.path.exists('英雄联盟'):
    os.mkdir('英雄联盟')
class LOL():
    def __init__(self):
        self.url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js?ts=2952076'
        self.url_detail = 'https://game.gtimg.cn/images/lol/act/img/js/hero/{}.js?ts=2952077'

    def get_data(self):
        hero = requests.get(self.url).json()['hero']
        for i in hero:
            heroId = i['heroId']
            yx_name = i['name']
            # print(heroId, yx_name)
            self.get_skin(heroId, yx_name)
            break

    def get_skin(self, heroId, yx_name):
        if not os.path.exists(f'英雄联盟/{yx_name}'):
            os.makedirs(f'英雄联盟/{yx_name}')    #创建多层路径


        skins = requests.get(self.url_detail.format(heroId)).json()['skins']
        for i in skins:
            pf_name = i['name']
            mainImg = i['mainImg']
            if mainImg != '':
                print(pf_name, mainImg)

                res = requests.get(mainImg).content
                with open(f'英雄联盟/{yx_name}/{pf_name}.jpg', 'wb') as f:
                    f.write(res)


if __name__ == '__main__':
    lol = LOL()
    lol.get_data()
