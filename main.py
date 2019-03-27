import json
import os.path
from requests import post

import config
from api import query
from code import kd100_codes

data_path = os.path.split(os.path.realpath(__file__))[0] + '/' + 'data.json'

def sc_noti(company, postid, context, full):
    company = kd100_codes[company]  # 换成中文
    text = '{company}快递{postid}状态变化：{status}'.format(company=company, postid=postid, status=context)

    desp = ''
    for i in full:
        desp = desp + '{time} **{stat}**\n\n'.format(time=i.get('time'), stat=i.get('context'))

    print(text)

    post(config.sc_url, data={'text': text,'desp': desp})


with open(data_path) as a:
    data = json.loads(a.read())

data_n = {}

for i in config.post_list:
    postid = i.get('postid')
    company = i.get('company')

    if not postid or not company:
        print('config.py文件错误！')
        exit(0)

    # 如果是一个新的数据
    if not data.get(postid):
        data[postid] = {}
        data[postid]['last_time'] = '0'

    # 状态已经是已签收
    if data.get(postid).get('state', '0') == '3':
        data_n[postid] = data[postid]
        continue

    result = query(company, postid)

    if not result:
        print('获取api数据出错！')
        continue

    last_time = result.get('data')[0].get('time')
    context = result.get('data')[0].get('context')
    full = result.get('data')

    if last_time != data.get(postid).get('last_time'):
        data[postid]['last_time'] = last_time
        data[postid]['state'] = result.get('state')
        sc_noti(company, postid, context, full)

    # 写入数据，舍弃旧数据
    data_n[postid] = data[postid]

with open(data_path, 'w') as a:
    a.write(json.dumps(data_n))
