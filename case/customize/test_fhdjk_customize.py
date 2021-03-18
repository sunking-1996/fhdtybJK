# # coding:utf-8
# import requests
# import unittest
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# from common.phone import create_phone
# phone = create_phone()
# class Test_customize(unittest.TestCase):
#     u'''自定义打印'''
#     resp = None
#
#     @classmethod
#     def setUpClass(cls):      # 前置
#         cls.url = "http://www.fhd001.com/loginAccount.do"
#         cls.header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
#                       "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
#                       "Referer":"http://www.fhd001.com/",
#                       "Cookie":"CNZZDATA1263048142=51987825-1583297402-null%7C1583313201; CNZZDATA1276886889=1211049750-1581389138-%7C1586500912; _pati=dceabddd4793a92e54b1f429d2dddc8b; fhdpdd_user_info_nick=cyccyccyc; fhdpdd_user_info_avatar=https://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTLRrXUnQ7n5vG2bXPMooFQYxyGw4vadia79F5plrgQdkrwBA3d2ObyDcpiaNYII98sBUIVxAqQmmKJA/132; fhd_user_info_nick=sunking; fhd_user_info_avatar=https://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTJiaGdSuKpkrLN4tlrze2OOHwicfS73TJKAScS9toziaicpjWUySrxgickrERnSicVbVtHJSC3Nx2EC5dyA/132; fhdcooperation_id=10086; fhdcooperation_username=%E5%AD%99%E5%BD%AA; fhdcooperation_isAdmin=false; fhdcooperation_isManage=false; fhdcooperation_departmentId=15; fhdcooperation_departmentName=%E7%A0%94%E5%8F%91%E4%B8%AD%E5%BF%83; fhdcooperation_postNo=10; fhdcooperation_postName=%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88; fhdcooperation_token=%7EAwwTIwJBeHVHXVxHclFAJicdcHQZXgJdRFZKUAdfQFMbBQNKEiEOFCNUQFsDQSBRRgB3EAwJRnQDFiQOQ3J3E3IBEyRxQQECTlVVThIhU0EhDRQNdx0mCRJyIBNfBhZzAhF0URIlDBQnU0AjD0FdJkZ9BBB3AEYJDx9XA18HAwYHAw9fG1UJAVpSVVE%3D%7E1%7E; userHeadImgUrl=http%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FQ0j4TwGTfTIdbOjlPgbBtWarETJdX2wSHQNx9icjrG2mpoTuUX6Uobk73BJq6Qh1pB84xC8DBURHfsqQeohlDVA%2F132; yunxu_username=%E5%AD%99%E5%BD%AA; yunxu_token=%7EClPWnK7QjstICAEPA1JSBwFTAE5QAQc%3D%7E1%7E; yunxu_chooseProjectCookieKey=123; JSESSIONID=538A8A21B4CBFD9CCBDF4490F852DE08.fap1-fhdcommon"
#         }   # get方法其它加个ser-Agent就可以了
#         cls.body = {"userAccount":"15167168967",
#                     "userPwd":"123456",
#                     "isLoginAuto":"false"} #参数存字典
#         # cls.proxies = {'http': 'http://localhost:8888',
#         #                'https': 'http://localhost:8888'}
#         # cls.s.proxies = cls.proxies
#         cls.s = requests.session()
#         cls.s.verify = False
#
#         request = cls.s.post(url=cls.url,data=cls.body,headers=cls.header)
#
#         print(request.status_code)
#         print(request.text)
#         print(type(request.url))
#
#         d   =  request.json()  #解析json
#         if d["rcode"] ==0 and d["scode"]==0:
#             print("登录成功")
#         else:
#             print("登录失败")
#
#     def test_001(self):        #新建自定义包裹
#         u'''新建自定义包裹'''
#         self.url = "http://www.fhd001.com/package/savePackages.do"
#         self.body = {"shippingName":"蓝川科技",
#                      "shippingMobile":create_phone(),
#                      "shippingProvince":"浙江省",
#                      "shippingCity":"杭州市",
#                      "shippingArea":"西湖区",
#                      "shippingAddress":"剑桥公社F座",
#                      "newConsignee[consigneeName]":"接口测试",
#                      "newConsignee[consigneeMobile]":phone,
#                      "newConsignee[consigneeProvince]":"浙江省",
#                      "newConsignee[consigneeCity]":"杭州市",
#                      "newConsignee[consigneeArea]":"西湖区",
#                      "newConsignee[consigneeAddress]":"剑桥公社",
#                      "consigneeAddressCount":"1",
#                      "consigneeAddressList":'[{"consigneeName":"接口测试","consigneeMobile":'+phone+',"consigneePhone":"","consigneeProvince":"浙江省","consigneeCity":"杭州市","consigneeArea":"西湖区","consigneeAddress":"剑桥公社"}]',
#                      "packageCategory":"服饰"
#         } #参数存字典
#         request = self.s.post(url=self.url,data=self.body)
#
#         print(request.status_code)
#         print(request.text)
#         print(type(request.url))
#
#         global resp
#         resp = request.json()
#         if resp["rcode"] ==0 and resp["scode"]==0:
#             print("保存成功")
#         else:
#             print("保存失败")
#
#
#     # def test_002(self):        #删除自定义包裹
#     #     u'''删除自定义包裹'''
#     #     global resp
#     #
#     #     self.url = "http://www.fhd001.com/package/deletePackage.do"
#     #     self.body = {"packageIds":resp['data'][0]
#     #     } #参数存字典
#     #     request = self.s.post(url=self.url,data=self.body)
#     #
#     #     print(request.status_code)
#     #     print(request.text)
#     #     print(type(request.url))
#     #
#     #     resp  =  request.json()
#     #     if resp["rcode"] ==0 and resp["scode"]==0:
#     #         print("删除成功")
#     #     else:
#     #         print("删除失败")
#
# if __name__ == "__main__":
#     unittest.main()
