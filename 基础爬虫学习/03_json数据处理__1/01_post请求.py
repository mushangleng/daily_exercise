# get 请求    获取数据
# post 请求   提交数据

import requests


# get 请求
def get():
    url = 'https://postman-echo.com/get'
    res = requests.get(url)
    print(res.status_code)
    print(res.json())


# 带参数的 get请求
def get_2():
    url = 'https://postman-echo.com/get?name=zhangsan&age=18'
    res = requests.get(url)
    print(res.json())


# 带参数的 get请求
def get_3():
    # 参数部分
    params = {
        "name": "李四",
        "age": 18
    }
    url = 'https://postman-echo.com/get'
    res = requests.get(url, params=params)  # 带参数去发生get请求
    print(res.json())


# post 请求
def post():
    # 需要提交的数据
    data = {
        'account': 'user',
        'pwd': '123456'
    }

    url = 'https://postman-echo.com/post'
    res = requests.post(url,data=data)
    print(res.json())


# get()
# get_2()
# get_3()
post()
