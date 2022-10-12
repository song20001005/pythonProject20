import requests
import execjs

headers = {
    "user-agent": "yuanrenxue.project",
}
cookies = {'sessionid': '5l3kxrp7ajbvsuginrpdbpm4a6v0yiqa'}
session = requests.session()
session.headers = headers
session.cookies.update(cookies)

with open('02.js', 'r', encoding='utf-8') as f:
    js_code = f.read()
func = execjs.compile(js_code)

url = "https://match.yuanrenxue.com/api/match/2"

all_sum = 0
for page in range(1, 6):
    co = {'m': func.call('get_m')}

    session.cookies.update(co)
    params = {
        "page": str(page),
    }
    res = session.get(url, params=params)
    print(res.text)

    for data in res.json()['data']:
        all_sum += data['value']

print(all_sum)