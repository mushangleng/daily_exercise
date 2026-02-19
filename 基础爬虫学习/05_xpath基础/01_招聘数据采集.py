# https://yiqifu.baidu.com/g/aqc/joblist?q=python
import requests

import pandas  # 保存到excel

# pip install pandas -i https://pypi.tuna.tsinghua.edu.cn/simple
# pip install openpyxl -i https://pypi.tuna.tsinghua.edu.cn/simple

# 创建一个列表，用来存每个岗位
li_data = []

url = 'https://yiqifu.baidu.com/g/aqc/joblist/getDataAjax'

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
    "referer": 'https://yiqifu.baidu.com/g/aqc/joblist?q=python'
}

for page in range(1, 8):
    print(f'----------开始爬取第{page}页----------')
    params = {
        "q": "python",  # 关键词
        "page": str(page),  # 页码
        "pagesize": "20"  # 一页的数量
    }

    res = requests.get(url, params=params, headers=headers)
    li = res.json()['data']['list']

    for i in li:
        # 创建一个字典，用来存岗位的信息
        message = {}
        message['岗位'] = i['jobName'].replace("<em>", '').replace("</em>", '')
        message['薪资'] = i['salary']
        message['公司'] = i['company']
        message['城市'] = i['city']
        message['学历'] = i['edu']
        message['经验'] = i['exp']

        bid = i['bid']
        jobId = i['jobId']

        # 岗位职责
        url_detail = f"https://yiqifu.baidu.com/g/aqc/jobDetailAjax?jobId={jobId}&bid={bid}"
        res = requests.get(url_detail,
            headers=headers, params=params)

        message['职责'] = res.json()['data']['desc']
        # 把这个字典添加到列表中
        li_data.append(message)

# 1、把列表转出数据框类型 表示表格
df = pandas.DataFrame(li_data)

# 2、把表格存到Excel中                           不要行索引
df.to_excel("python招聘数据采集.xlsx", index=False)

# PermissionError: [Errno 13] Permission denied: 'python招聘数据采集.xlsx'   必须关掉这个Excel文件
