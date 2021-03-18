# coding=utf-8
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# r = requests.get('http://www.fhd001.com/')
#
# print(r.status_code)
# print(r.headers)
a="周杰伦"
url = "https://www.baidu.com/"
par = {"wd":"%s"%a} #参数存字典
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"}
proxies = {'http': 'http://localhost:8888', 'https': 'http://localhost:8888'}

session = requests.Session()
session.proxies = proxies
session.verify = False
session.headers = header

r1 =session.get(url=url,params=par)

print(r1.status_code)
print(r1.cookies)
print(r1.encoding)
print(r1.text)
#print(r1.content)
