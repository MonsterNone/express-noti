import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Referer': 'http://www.kuaidi100.com/'
}

kd100_url = 'http://www.kuaidi100.com/query'
kd100_params = {
    'type': '',
    'postid': '',
}


def query(company, postid):
    kd100_params['type'] = company
    kd100_params['postid'] = postid
    r = requests.get(kd100_url, params=kd100_params, headers=headers)
    r = r.json()
    if r.get('message') != 'ok':
        print(r)
        return False
    else:
        return r
