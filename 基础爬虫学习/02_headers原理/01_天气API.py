import requests


# 查询国内城市的天气
def func1():
    city = input("请输入国内的某个城市：")

    res = requests.get(
        f'http://gfeljm.tianqiapi.com/api?unescape=1&version=v9&appid=81758555&appsecret=22fvyh1d&city={city}')
    # print(res.status_code)
    data = res.json()

    # print(data)

    city = data['city']
    date = data['data'][0]['date']
    wea_day = data['data'][0]['wea_day']
    print(city)
    print(date)
    print(wea_day)


# 查询国外的城市天气
def func2():
    city = input("请输入国外的某个城市：")

    res = requests.get(f'http://v5.tianqiapi.com/api?version=v5&appid=81758555&appsecret=22fvyh1d&city={city}')
    # print(res.status_code)
    data = res.json()
    print(data)

func1()
func2()
