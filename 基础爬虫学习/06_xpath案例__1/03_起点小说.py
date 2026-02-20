# https://www.qidian.com/book/1041637443/ 捞尸人

# 右键 -> 检查 -> 点右上角的停用断点 -> 刷新网页
# 如果右键没得用  就 按F12

import requests
from lxml import etree
import os

if not os.path.exists("捞尸人"):
    os.mkdir("捞尸人")

url = 'https://www.qidian.com/book/1041637443/'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
    'cookie': 'e1=%7B%22l6%22%3A%221%22%2C%22l7%22%3A%22%22%2C%22pid%22%3A%22qd_P_xiangqing%22%2C%22eid%22%3A%22%22%2C%22l1%22%3A3%7D; e2=%7B%22l6%22%3A%221%22%2C%22l7%22%3A%22%22%2C%22pid%22%3A%22qd_P_xiangqing%22%2C%22eid%22%3A%22%22%2C%22l1%22%3A3%7D; newstatisticUUID=1766211490_788952455; _csrfToken=UCZoQBq80sUHHg5w9WV4RlsXolzuT2iINqWt8ikH; fu=2134100898; traffic_utm_referer=; supportwebp=true; e1=%7B%22l6%22%3A%22%22%2C%22l7%22%3A%22%22%2C%22l1%22%3A3%2C%22l3%22%3A%22%22%2C%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_A1001%22%7D; e2=%7B%22l6%22%3A%22%22%2C%22l7%22%3A%22%22%2C%22l1%22%3A3%2C%22l3%22%3A%22%22%2C%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_A16%22%7D; supportWebp=true; abPolicies=%7B%22g17%22%3A1%2C%22g16%22%3A0%2C%22g18%22%3A1%2C%22g19%22%3A0%2C%22g12%22%3A0%2C%22g14%22%3A0%7D; traffic_search_engine=; x-waf-captcha-referer=; Hm_lvt_f00f67093ce2f38f215010b699629083=1766212482,1766214795,1766235638,1766237130; Hm_lpvt_f00f67093ce2f38f215010b699629083=1766237130; HMACCOUNT=34F1CD1E408C916F; w_tsfp=ltvuV0MF2utBvS0Q76zrl0yvFTovcz44h0wpEaR0f5thQLErU5mD14R5ucr0NXfY5sxnvd7DsZoyJTLYCJI3dwNFQ8yZdooW2FjDmtcjjYgTVBhiFcjaWQMfKu8kvmFBf3hCNxS00jA8eIUd379yilkMsyN1zap3TO14fstJ019E6KDQmI5uDW3HlFWQRzaLbjcMcuqPr6g18L5a5WuOt1z9K1olUbxFgxPDgypMCnwht0O8IOxVNhupIpinSqA='
}
res = requests.get(url, headers=headers)

html = etree.HTML(res.text)

# <ul class="volume-chapters">
ul = html.xpath('//ul[@class="volume-chapters"]')[0]

index = 1
for li in ul:
    href = li.xpath('.//a/@href')
    alt = li.xpath('.//a/@alt')
    href = "".join(href)
    href = f'https:{href}'
    alt = "".join(alt).replace("在线阅读", "")

    # 请求章节地址
    response = requests.get(href, headers=headers)

    # 获取章节内容
    html2 = etree.HTML(response.text)
    main = html2.xpath('//main/p/text()')
    main = "\n".join(main)

    # 把每一章写入到文件中
    with open(f"捞尸人/{index}_{alt}.docx", 'w', encoding='utf-8') as f:
        f.write(alt + '\n')
        f.write(main)
    index += 1
    print(f"{alt}.txt下载成功")


# 作业
# 1、爬取网易云音乐你喜欢的榜单
# 2、爬取起点小说你喜欢的小说
