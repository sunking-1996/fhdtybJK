# coding=utf-8
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


url = "http://www.fhd001.com/loginAccount.do"

body = {"userAccount":"15167168967",
       "userPwd":"123456",
       "isLoginAuto":"false"} #参数存字典

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
          "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
          "Referer":"http://www.fhd001.com/",
          "Cookie":"CNZZDATA1263048142=51987825-1583297402-null%7C1583313201; CNZZDATA1276886889=1211049750-1581389138-%7C1586500912; _pati=dceabddd4793a92e54b1f429d2dddc8b; fhdpdd_user_info_nick=cyccyccyc; fhdpdd_user_info_avatar=https://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTLRrXUnQ7n5vG2bXPMooFQYxyGw4vadia79F5plrgQdkrwBA3d2ObyDcpiaNYII98sBUIVxAqQmmKJA/132; fhd_user_info_nick=sunking; fhd_user_info_avatar=https://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTJiaGdSuKpkrLN4tlrze2OOHwicfS73TJKAScS9toziaicpjWUySrxgickrERnSicVbVtHJSC3Nx2EC5dyA/132; fhdcooperation_id=10086; fhdcooperation_username=%E5%AD%99%E5%BD%AA; fhdcooperation_isAdmin=false; fhdcooperation_isManage=false; fhdcooperation_departmentId=15; fhdcooperation_departmentName=%E7%A0%94%E5%8F%91%E4%B8%AD%E5%BF%83; fhdcooperation_postNo=10; fhdcooperation_postName=%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88; fhdcooperation_token=%7EAwwTIwJBeHVHXVxHclFAJicdcHQZXgJdRFZKUAdfQFMbBQNKEiEOFCNUQFsDQSBRRgB3EAwJRnQDFiQOQ3J3E3IBEyRxQQECTlVVThIhU0EhDRQNdx0mCRJyIBNfBhZzAhF0URIlDBQnU0AjD0FdJkZ9BBB3AEYJDx9XA18HAwYHAw9fG1UJAVpSVVE%3D%7E1%7E; userHeadImgUrl=http%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FQ0j4TwGTfTIdbOjlPgbBtWarETJdX2wSHQNx9icjrG2mpoTuUX6Uobk73BJq6Qh1pB84xC8DBURHfsqQeohlDVA%2F132; yunxu_username=%E5%AD%99%E5%BD%AA; yunxu_token=%7EClPWnK7QjstICAEPA1JSBwFTAE5QAQc%3D%7E1%7E; yunxu_chooseProjectCookieKey=123; JSESSIONID=538A8A21B4CBFD9CCBDF4490F852DE08.fap1-fhdcommon"
}
proxies = {'http': 'http://localhost:8888',
           'https': 'http://localhost:8888'}

session = requests.Session()
session.proxies = proxies
session.verify = False


r1 =session.post(url=url,data=body,headers=header)

print(r1.status_code)
print(r1.cookies)
print(r1.text)
#print(r1.content)

#保存包裹
url1 = "http://www.fhd001.com/package/savePackages.do"

body1 = {"shippingName":"孙彪",
         "shippingMobile":"15167168967",
         "shippingProvince":"浙江省",
         "shippingCity":"杭州市",
         "shippingArea":"江干区",
         "shippingAddress":"九月庭院一单元",
         "newConsignee[consigneeName]":"接口8",
         "newConsignee[consigneeMobile]":"15167169888",
         "newConsignee[consigneeProvince]":"浙江省",
         "newConsignee[consigneeCity]":"杭州市",
         "newConsignee[consigneeArea]":"西湖区",
         "newConsignee[consigneeAddress]":"龙湖天街",
         "consigneeAddressCount":"1",
         "consigneeAddressList":'[{"consigneeName":"接口8","consigneeMobile":"15167169888","consigneePhone":"","consigneeProvince":"浙江省","consigneeCity":"杭州市","consigneeArea":"西湖区","consigneeAddress":"龙湖天街"}]',
         "packageCategory":"服饰"
} #参数存字典

r2 =session.post(url=url1,data=body1)

print(r2.status_code)
print(r2.text)
print(r2.url)


d1   =  r2.json()
print(d1["rcode"])
print(d1["scode"])
print(d1['data'][0])
if d1["rcode"] ==0 and d1["scode"]==0:
    print("新建成功")
else:
    print("保存失败")

#提取packageIds
#正则提取需要的参数值
# import re
# data = re.findall(r"data=(.+?)$",d1)
# print (data)# 这里是list
# #提取为字符串
# print (data[0])

#删除该包裹
url3 = "http://www.fhd001.com/package/deletePackage.do"

body3 = {
    "packageIds":d1['data'][0]
} #参数存字典

r4 =session.post(url=url3,data=body3)
print(r4.status_code)
print(r4.text)


# url2 = "http://common.fhd001.com/fhd/userCustomer/saveUserCustomer.do"
#
# body2 = {"name":"孙彪",
#          "cellphone":"15167168967",
#          "province":"浙江省",
#          "city":"杭州市",
#          "area":"江干区",
#          "address":"九月庭院一单元",
#          "source":"1",
#          "needCount":"true",
#          "referer":"fhdportal",
#          "token":"~ClACBA4EBFFRChhFQgwJX1wBHxEUWF9fW1QUDRoJAF8HVgsCBAYGTVQKAg%3D%3D~1~"
# } #参数存字典
#
# r3 =session.post(url=url2,data=body2)
#
# print(r3.status_code)
# print(r3.text)
# d   =  r3.json()
# print(d["data"]["address"])
# if "九月庭院一单元1" in d["data"]["address"]:
#     print("新建成功")
# else:
#     print("保存失败")
