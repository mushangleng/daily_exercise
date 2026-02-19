'''
网页
JSON 字典数据   键值对取值
HTML 标签数据   xpath解析

xpath
1、定位标签
2、取值
    文本  /text()
    属性  @属性名

'''

# 字符串是没有层级关系的，先变成HTML
# pip install lxml -i https://pypi.tuna.tsinghua.edu.cn/simple

from lxml import etree

response = '''
    <div>
        <p>注意你的言语，变成你的行为</p>
        <p>注意你的行为，变成你的习惯</p>
        <p id='p3'>注意你的习惯，塑造你的性格</p>
        <p>注意你的性格，决定你的人生</p>
    </div>
'''

# 1、把字符串变成HTML数据
html = etree.HTML(response)

# 2、从html中解析数据，获取你要的内容
p_s = html.xpath('//div/p[1]/text()')  # // 在整篇文档中，满足后面的条件
print(p_s)

# xpath 如果路径错了，不会报错，因为根据指定的路径 去查找的
