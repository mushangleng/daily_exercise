# Fetch/XHR 都是浏览器中js用来与服务器进行网络通信（发生和接收数据）的API，它们是实现'前后端交互'的核心技术。
# 它们是浏览器提供js代码的‘收发器’，让你能在不刷新页面的情况下，从服务器获取数据（如加载的新内容）或者提取数据（如提交表单）。
import os
import requests
import time

if not os.path.exists('斗鱼'):
    os.mkdir('斗鱼')


# 保存图片数据
def get_pic(name, url):
    # 给图片的链接发送get请求
    data = requests.get(url).content

    with open(f'斗鱼/{name}.jpg', 'wb') as f:
        f.write(data)

    print(f'{name}.png下载成功')


def run():
    for page in range(1, 9):
        print(f'----------开始下载第{page}页----------')

        url = f'https://www.douyu.com/wgapi/ordnc/live/web/room/mixList/2/1008/0/{page}'
        res = requests.get(url)
        data_json = res.json()

        # 获取列表
        rl = data_json['data']['rl']

        # 遍历列表，获取主播的名字和图片
        for i in rl:
            nn = i['nn']
            rs1 = i['rs1']
            # 保存
            get_pic(nn, rs1)

        time.sleep(1)


# 如果在当前文件中运行，就执行后面的代码
if __name__ == '__main__':
    run()
