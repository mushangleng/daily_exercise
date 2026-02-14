# API接口
# 应用程序编程接口（英语：Application Programming Interface，简称：API）
#
# 是一些预先定义的函数，目的是提供应用程序与开发人员基于某软件或硬件得以访问
#
# 一组例程的能力，而又无需访问源码，或理解内部工作机制的细节
import requests

# 天气api网站  点进右上角的 用户中心 先注册登录   (作业，打印天气)
# http://tianqiapi.com/


# 青云客网络
# http://api.qingyunke.com/


while True:
    my_say = input("我说：")

    url = f"http://api.qingyunke.com/api.php?key=free&appid=0&msg={my_say}"

    # 请求这个API接口，得到json数据，获取回复内容
    res = requests.get(url).json()['content']

    print("豆包说：", res)

    if my_say == '拜拜':
        break
