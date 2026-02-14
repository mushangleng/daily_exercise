# requests库的安装
# pip install requests -i https://mirrors.aliyun.com/pypi/simple/
# =============镜像源==============
# 阿里云 https://mirrors.aliyun.com/pypi/simple/
# 中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
# 豆瓣(douban) https://pypi.douban.com/simple/
# 清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
# 中国科学技术大学 https://pypi.mirrors.ustc.edu.cn/simple/

import requests

# 测试的网址
# https://postman-echo.com/get

# get 请求是用于从服务器获取数据的
'''
常用的状态码                打电话      
200         成功          你打过去，对方接听了
302         重定向         你打过去，您拨打的电话已被呼叫转移
404         不存在         你打过去，您拨打的电话是空号，请核对后在拨
503         内部错误       你打过去，您拨打的电话已停机
'''

response = requests.get('https://postman-echo.com/get')
print(response)  # <Response [200]>
print(response.status_code)  # 200 状态码
print(response.headers)  # 响应头
print(response.text)  # 响应体  <class 'str'>
print(response.content)  # 二进制  图片 视频
print(response.json())  #  <class 'dict'>
print(response.cookies)  # 缓存
print(response.encoding)  # utf-8
'''
Response常用属性
status_code     获取HTTP响应的状态码
headers         HTTP响应的头信息，返回的是一个字典
text            HTTP响应的主体内容，此属性会自动对结果进行解码
content         HTTP响应的二进制内容
json()          如果HTTP响应的内容是json，我们可以用此方法解析json，返回一个字典
cookies         一个CookieJar对象，包含服务器设置的所有cookies
encoding        获取响应的编码方式
'''

'''
HTTP状态码
1xx（信息响应）：这类状态码代表请求已被接受，需要进一步处理。这类响应是临时响应，只包含状态行和某些可选的响应头信息，并以空行结束。
100 Continue：服务器已收到请求的一部分，客户端应该继续发送其余的请求。

2xx （成功） ：这类状态码表明服务器成功地接受了由客户端发出的请求
200 OK： 请求成功。请求所希望的回应头或数据体将随此响应返回。
201 Created： 请求已被实现，并且有一个新的资源已经依据请求的需要而创建。

3xx （重定向）：完成请求所需额外的步骤。
302 Found：请求的资源现在临时从不同的URI响应请求。
304 Not Modified：资源未改变，直接使用浏览器缓存即可。

4xx（请求错误）：这类的状态码代表了客户端看起来可能发生了错误，妨碍了服务器的处理
400 Bad Request：请求无法被服务器理解
401 Unauthorized：当前请求需要用户验证
403 Forbidden：服务器了解客户端的请求，但是拒绝执行它
404 Not Found：请求失败，请求所希望得到的资源未被在服务器上发现

5xx（服务器错误）：这类状态码代表服务器在处理请求的过程中发生了错误
500 Internal Server Error：服务器遇到了一个未曾预料的状况，导致了它无法完成对请求的处理
502 Bad Gateway：服务器是一个网关或者代理服务器，它收到了来自上游服务器的无效响应
503 Service Unavailable：由于临时的服务器维护或者过载，服务器当前无法处理请求
'''
