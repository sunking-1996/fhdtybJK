# coding:utf-8
import requests
import unittest
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from common.phone import create_phone
phone = create_phone()
from common.loginon import Test_login
def setUpModule():    # 当前模块执行前只执行一次
    print('=== setUpModule ===')

def tearDownModule(): # 当前模块执行后只执行一次
    print('=== tearDownModule ===')
class Test_create_package(unittest.TestCase):
    u'''保存自定义包裹'''
    resp = None

    @classmethod
    def setUpClass(cls):      # 前置
        print('--- setUpClass ---')
        print('--- 保存自定义包裹 ---')
        cls.s=Test_login.login_on()
        # # cls.proxies = {'http': 'http://localhost:8888',
        # #                'https': 'http://localhost:8888'}
        # # cls.s.proxies = cls.proxies
        cls.s.verify = False

    @classmethod
    def tearDownClass(cls):
        print('--- tearDownClass ---')

    def setUp(self):  # 该类中每个测试用例执行一次
        print('... setUp ...')

    def tearDown(self):
        print('... tearDown ...')

    def test_create_package_001_normal(self):        #新建自定义包裹
        '''正例:正确入参'''
        print("正例:正确入参")
        self.url = "http://www.fhd001.com/package/savePackages.do"
        self.body = {"shippingName":"接口测试寄件人",
                     "shippingMobile":create_phone(),
                     "shippingPhone":"",
                     "shippingProvince":"浙江省",
                     "shippingCity":"杭州市",
                     "shippingArea":"西湖区",
                     "shippingAddress":"紫荆天街",
                     "newConsignee[consigneeName]":"接口测试收件人",
                     "newConsignee[consigneeMobile]":phone,
                     "newConsignee[consigneePhone]":"",
                     "newConsignee[consigneeProvince]":"江西省",
                     "newConsignee[consigneeCity]":"上饶市",
                     "newConsignee[consigneeArea]":"广丰区",
                     "newConsignee[consigneeAddress]":"月兔广场",
                     "consigneeAddressCount":"1",
                     "consigneeAddressList":'[{"consigneeName":"接口测试收件人","consigneeMobile":'+phone+',"consigneePhone":"","consigneeProvince":"江西省","consigneeCity":"上饶市","consigneeArea":"广丰区","consigneeAddress":"月兔广场"}]',
                     "packageAmts":"",
                     "packageCategory":"服饰",
                     "packageNote":""
        } #参数存字典
        request = self.s.post(url=self.url,data=self.body)

        global resp
        resp = request.json()
        if resp["rcode"] ==0 and resp["scode"]==0:
            print("pass")
        else:
            print("false")

    def test_create_package_002_shippingName_null(self):        #新建自定义包裹
        '''反例:寄件人姓名空参'''
        print("反例:寄件人姓名空参")
        self.url = "http://www.fhd001.com/package/savePackages.do"
        self.body = {"shippingName":"",
                     "shippingMobile":create_phone(),
                     "shippingPhone":"",
                     "shippingProvince":"浙江省",
                     "shippingCity":"杭州市",
                     "shippingArea":"西湖区",
                     "shippingAddress":"紫荆天街",
                     "newConsignee[consigneeName]":"接口测试收件人",
                     "newConsignee[consigneeMobile]":phone,
                     "newConsignee[consigneePhone]":"",
                     "newConsignee[consigneeProvince]":"江西省",
                     "newConsignee[consigneeCity]":"上饶市",
                     "newConsignee[consigneeArea]":"广丰区",
                     "newConsignee[consigneeAddress]":"月兔广场",
                     "consigneeAddressCount":"1",
                     "consigneeAddressList":'[{"consigneeName":"接口测试收件人","consigneeMobile":'+phone+',"consigneePhone":"","consigneeProvince":"江西省","consigneeCity":"上饶市","consigneeArea":"广丰区","consigneeAddress":"月兔广场"}]',
                     "packageAmts":"",
                     "packageCategory":"服饰",
                     "packageNote":""
        } #参数存字典
        request = self.s.post(url=self.url,data=self.body)

        global resp
        resp = request.json()
        if resp["rcode"] ==0 and resp["scode"]==0:
            print("pass")
        else:
            print("false")

    def test_create_package_003_shippingPhone_null(self):        #新建自定义包裹
        '''反例:寄件人号码空参'''
        print("反例:寄件人号码空参")
        self.url = "http://www.fhd001.com/package/savePackages.do"
        self.body = {"shippingName":"接口测试寄件人",
                     "shippingMobile":"",
                     "shippingPhone":"",
                     "shippingProvince":"浙江省",
                     "shippingCity":"杭州市",
                     "shippingArea":"西湖区",
                     "shippingAddress":"紫荆天街",
                     "newConsignee[consigneeName]":"接口测试收件人",
                     "newConsignee[consigneeMobile]":phone,
                     "newConsignee[consigneePhone]":"",
                     "newConsignee[consigneeProvince]":"江西省",
                     "newConsignee[consigneeCity]":"上饶市",
                     "newConsignee[consigneeArea]":"广丰区",
                     "newConsignee[consigneeAddress]":"月兔广场",
                     "consigneeAddressCount":"1",
                     "consigneeAddressList":'[{"consigneeName":"接口测试收件人","consigneeMobile":'+phone+',"consigneePhone":"","consigneeProvince":"江西省","consigneeCity":"上饶市","consigneeArea":"广丰区","consigneeAddress":"月兔广场"}]',
                     "packageAmts":"",
                     "packageCategory":"服饰",
                     "packageNote":""
        } #参数存字典
        request = self.s.post(url=self.url,data=self.body)

        global resp
        resp = request.json()
        if resp["rcode"] ==0 and resp["scode"]==0:
            print("pass")
        else:
            print("false")

    def test_create_package_004_shippingAddress_null(self):        #新建自定义包裹
        '''反例:寄件人地址空参'''
        print("反例:寄件人地址空参")
        self.url = "http://www.fhd001.com/package/savePackages.do"
        self.body = {"shippingName":"接口测试寄件人",
                     "shippingMobile":create_phone(),
                     "shippingPhone":"",
                     "shippingProvince":"",
                     "shippingCity":"",
                     "shippingArea":"",
                     "shippingAddress":"",
                     "newConsignee[consigneeName]":"接口测试收件人",
                     "newConsignee[consigneeMobile]":phone,
                     "newConsignee[consigneePhone]":"",
                     "newConsignee[consigneeProvince]":"江西省",
                     "newConsignee[consigneeCity]":"上饶市",
                     "newConsignee[consigneeArea]":"广丰区",
                     "newConsignee[consigneeAddress]":"月兔广场",
                     "consigneeAddressCount":"1",
                     "consigneeAddressList":'[{"consigneeName":"接口测试收件人","consigneeMobile":'+phone+',"consigneePhone":"","consigneeProvince":"江西省","consigneeCity":"上饶市","consigneeArea":"广丰区","consigneeAddress":"月兔广场"}]',
                     "packageAmts":"",
                     "packageCategory":"服饰",
                     "packageNote":""
        } #参数存字典
        request = self.s.post(url=self.url,data=self.body)

        global resp
        resp = request.json()
        if resp["rcode"] ==0 and resp["scode"]==0:
            print("pass")
        else:
            print("false")

    def test_create_package_005_shippingPhone_wrong(self):        #新建自定义包裹
        '''反例:寄件人号码错参'''
        print("反例:寄件人号码错参")
        self.url = "http://www.fhd001.com/package/savePackages.do"
        self.body = {"shippingName":"接口测试寄件人",
                     "shippingMobile":"10086",
                     "shippingPhone":"",
                     "shippingProvince":"浙江省",
                     "shippingCity":"杭州市",
                     "shippingArea":"西湖区",
                     "shippingAddress":"紫荆天街",
                     "newConsignee[consigneeName]":"接口测试收件人",
                     "newConsignee[consigneeMobile]":phone,
                     "newConsignee[consigneePhone]":"",
                     "newConsignee[consigneeProvince]":"江西省",
                     "newConsignee[consigneeCity]":"上饶市",
                     "newConsignee[consigneeArea]":"广丰区",
                     "newConsignee[consigneeAddress]":"月兔广场",
                     "consigneeAddressCount":"1",
                     "consigneeAddressList":'[{"consigneeName":"接口测试收件人","consigneeMobile":'+phone+',"consigneePhone":"","consigneeProvince":"江西省","consigneeCity":"上饶市","consigneeArea":"广丰区","consigneeAddress":"月兔广场"}]',
                     "packageAmts":"",
                     "packageCategory":"服饰",
                     "packageNote":""
        } #参数存字典
        request = self.s.post(url=self.url,data=self.body)

        global resp
        resp = request.json()
        if resp["rcode"] ==0 and resp["scode"]==0:
            print("pass")
        else:
            print("false")

    def test_create_package_006_shippingAddress_wrong(self):        #新建自定义包裹
        '''反例:寄件人地址错参'''
        print("反例:寄件人地址错参")
        self.url = "http://www.fhd001.com/package/savePackages.do"
        self.body = {"shippingName":"接口测试寄件人",
                     "shippingMobile":create_phone(),
                     "shippingPhone":"",
                     "shippingProvince":"XX省",
                     "shippingCity":"XX市",
                     "shippingArea":"XX区",
                     "shippingAddress":"XXXX",
                     "newConsignee[consigneeName]":"接口测试收件人",
                     "newConsignee[consigneeMobile]":phone,
                     "newConsignee[consigneePhone]":"",
                     "newConsignee[consigneeProvince]":"江西省",
                     "newConsignee[consigneeCity]":"上饶市",
                     "newConsignee[consigneeArea]":"广丰区",
                     "newConsignee[consigneeAddress]":"月兔广场",
                     "consigneeAddressCount":"1",
                     "consigneeAddressList":'[{"consigneeName":"接口测试收件人","consigneeMobile":'+phone+',"consigneePhone":"","consigneeProvince":"江西省","consigneeCity":"上饶市","consigneeArea":"广丰区","consigneeAddress":"月兔广场"}]',
                     "packageAmts":"",
                     "packageCategory":"服饰",
                     "packageNote":""
        } #参数存字典
        request = self.s.post(url=self.url,data=self.body)

        global resp
        resp = request.json()
        if resp["rcode"] ==0 and resp["scode"]==0:
            print("pass")
        else:
            print("false")

    def test_create_package_007_consigneeName_null(self):        #新建自定义包裹
        '''反例:收件人姓名空参'''
        print("反例:收件人姓名空参")
        self.url = "http://www.fhd001.com/package/savePackages.do"
        self.body = {"shippingName":"接口测试寄件人",
                     "shippingMobile":create_phone(),
                     "shippingPhone":"",
                     "shippingProvince":"浙江省",
                     "shippingCity":"杭州市",
                     "shippingArea":"西湖区",
                     "shippingAddress":"紫荆天街",
                     "newConsignee[consigneeName]":"",
                     "newConsignee[consigneeMobile]":phone,
                     "newConsignee[consigneePhone]":"",
                     "newConsignee[consigneeProvince]":"江西省",
                     "newConsignee[consigneeCity]":"上饶市",
                     "newConsignee[consigneeArea]":"广丰区",
                     "newConsignee[consigneeAddress]":"月兔广场",
                     "consigneeAddressCount":"1",
                     "consigneeAddressList":'[{"consigneeName":"","consigneeMobile":'+phone+',"consigneePhone":"","consigneeProvince":"江西省","consigneeCity":"上饶市","consigneeArea":"广丰区","consigneeAddress":"月兔广场"}]',
                     "packageAmts":"",
                     "packageCategory":"服饰",
                     "packageNote":""
        } #参数存字典
        request = self.s.post(url=self.url,data=self.body)

        global resp
        resp = request.json()
        if resp["rcode"] ==0 and resp["scode"]==0:
            print("pass")
        else:
            print("false")

    def test_create_package_008_consigneePhone_null(self):        #新建自定义包裹
        '''反例:收件人号码空参'''
        print("反例:收件人号码空参")
        self.url = "http://www.fhd001.com/package/savePackages.do"
        self.body = {"shippingName":"接口测试寄件人",
                     "shippingMobile":create_phone(),
                     "shippingPhone":"",
                     "shippingProvince":"浙江省",
                     "shippingCity":"杭州市",
                     "shippingArea":"西湖区",
                     "shippingAddress":"紫荆天街",
                     "newConsignee[consigneeName]":"接口测试收件人",
                     "newConsignee[consigneeMobile]":"",
                     "newConsignee[consigneePhone]":"",
                     "newConsignee[consigneeProvince]":"江西省",
                     "newConsignee[consigneeCity]":"上饶市",
                     "newConsignee[consigneeArea]":"广丰区",
                     "newConsignee[consigneeAddress]":"月兔广场",
                     "consigneeAddressCount":"1",
                     "consigneeAddressList":'[{"consigneeName":"接口测试收件人","consigneeMobile":"","consigneePhone":"","consigneeProvince":"江西省","consigneeCity":"上饶市","consigneeArea":"广丰区","consigneeAddress":"月兔广场"}]',
                     "packageAmts":"",
                     "packageCategory":"服饰",
                     "packageNote":""
        } #参数存字典
        request = self.s.post(url=self.url,data=self.body)

        global resp
        resp = request.json()
        if resp["rcode"] ==0 and resp["scode"]==0:
            print("pass")
        else:
            print("false")

    def test_create_package_009_consigneeAddress_null(self):        #新建自定义包裹
        '''反例:收件人地址空参'''
        print("反例:收件人地址空参")
        self.url = "http://www.fhd001.com/package/savePackages.do"
        self.body = {"shippingName":"接口测试寄件人",
                     "shippingMobile":create_phone(),
                     "shippingPhone":"",
                     "shippingProvince":"浙江省",
                     "shippingCity":"杭州市",
                     "shippingArea":"西湖区",
                     "shippingAddress":"紫荆天街",
                     "newConsignee[consigneeName]":"接口测试收件人",
                     "newConsignee[consigneeMobile]":phone,
                     "newConsignee[consigneePhone]":"",
                     "newConsignee[consigneeProvince]":"",
                     "newConsignee[consigneeCity]":"",
                     "newConsignee[consigneeArea]":"",
                     "newConsignee[consigneeAddress]":"",
                     "consigneeAddressCount":"1",
                     "consigneeAddressList":'[{"consigneeName":"接口测试收件人","consigneeMobile":'+phone+',"consigneePhone":"","consigneeProvince":"","consigneeCity":"","consigneeArea":"","consigneeAddress":""}]',
                     "packageAmts":"",
                     "packageCategory":"服饰",
                     "packageNote":""
        } #参数存字典
        request = self.s.post(url=self.url,data=self.body)

        global resp
        resp = request.json()
        if resp["rcode"] ==0 and resp["scode"]==0:
            print("pass")
        else:
            print("false")

    def test_create_package_010_consigneePhone_wrong(self):        #新建自定义包裹
        '''反例:收件人号码错参'''
        print("反例:收件人号码错参")
        self.url = "http://www.fhd001.com/package/savePackages.do"
        self.body = {"shippingName":"接口测试寄件人",
                     "shippingMobile":create_phone(),
                     "shippingPhone":"",
                     "shippingProvince":"浙江省",
                     "shippingCity":"杭州市",
                     "shippingArea":"西湖区",
                     "shippingAddress":"紫荆天街",
                     "newConsignee[consigneeName]":"接口测试收件人",
                     "newConsignee[consigneeMobile]":"10086",
                     "newConsignee[consigneePhone]":"",
                     "newConsignee[consigneeProvince]":"江西省",
                     "newConsignee[consigneeCity]":"上饶市",
                     "newConsignee[consigneeArea]":"广丰区",
                     "newConsignee[consigneeAddress]":"月兔广场",
                     "consigneeAddressCount":"1",
                     "consigneeAddressList":'[{"consigneeName":"接口测试收件人","consigneeMobile":"10086","consigneePhone":"","consigneeProvince":"江西省","consigneeCity":"上饶市","consigneeArea":"广丰区","consigneeAddress":"月兔广场"}]',
                     "packageAmts":"",
                     "packageCategory":"服饰",
                     "packageNote":""
        } #参数存字典
        request = self.s.post(url=self.url,data=self.body)

        global resp
        resp = request.json()
        if resp["rcode"] ==0 and resp["scode"]==0:
            print("pass")
        else:
            print("false")

    def test_create_package_011_consigneeAddress_wrong(self):        #新建自定义包裹
        '''反例:收件人地址错参'''
        print("反例:收件人地址错参")
        self.url = "http://www.fhd001.com/package/savePackages.do"
        self.body = {"shippingName":"接口测试寄件人",
                     "shippingMobile":create_phone(),
                     "shippingPhone":"",
                     "shippingProvince":"浙江省",
                     "shippingCity":"杭州市",
                     "shippingArea":"西湖区",
                     "shippingAddress":"紫荆天街",
                     "newConsignee[consigneeName]":"接口测试收件人",
                     "newConsignee[consigneeMobile]":phone,
                     "newConsignee[consigneePhone]":"",
                     "newConsignee[consigneeProvince]":"XX省",
                     "newConsignee[consigneeCity]":"XX市",
                     "newConsignee[consigneeArea]":"XX区",
                     "newConsignee[consigneeAddress]":"XXXX",
                     "consigneeAddressCount":"1",
                     "consigneeAddressList":'[{"consigneeName":"接口测试收件人","consigneeMobile":'+phone+',"consigneePhone":"","consigneeProvince":"XX省","consigneeCity":"XX市","consigneeArea":"XX区","consigneeAddress":"XXXX"}]',
                     "packageAmts":"",
                     "packageCategory":"服饰",
                     "packageNote":""
        } #参数存字典
        request = self.s.post(url=self.url,data=self.body)

        global resp
        resp = request.json()
        if resp["rcode"] ==0 and resp["scode"]==0:
            print("pass")
        else:
            print("false")

    def test_create_package_012_all_none(self):        #新建自定义包裹
        '''反例:参数全为None'''
        print("反例:参数全为None")
        self.url = "http://www.fhd001.com/package/savePackages.do"
        self.body = {"shippingName":None,
                     "shippingMobile":None,
                     "shippingPhone":None,
                     "shippingProvince":None,
                     "shippingCity":None,
                     "shippingArea":None,
                     "shippingAddress":None,
                     "newConsignee[consigneeName]":None,
                     "newConsignee[consigneeMobile]":None,
                     "newConsignee[consigneePhone]":None,
                     "newConsignee[consigneeProvince]":None,
                     "newConsignee[consigneeCity]":None,
                     "newConsignee[consigneeArea]":None,
                     "newConsignee[consigneeAddress]":None,
                     "consigneeAddressCount":"1",
                     "consigneeAddressList":'[{"consigneeName":None,"consigneeMobile":None,"consigneePhone":"","consigneeProvince":None,"consigneeCity":None,"consigneeArea":None,"consigneeAddress":None}]',
                     "packageAmts":"",
                     "packageCategory":"服饰",
                     "packageNote":""
        } #参数存字典
        request = self.s.post(url=self.url,data=self.body)

        global resp
        resp = request.json()
        if resp["rcode"] ==0 and resp["scode"]==0:
            print("pass")
        else:
            print("false")

    def test_create_package_013_all_null(self):        #新建自定义包裹
        '''反例:参数全为空'''
        print("反例:参数全为空")
        self.url = "http://www.fhd001.com/package/savePackages.do"
        self.body = {"shippingName":"",
                     "shippingMobile":"",
                     "shippingPhone":"",
                     "shippingProvince":"",
                     "shippingCity":"",
                     "shippingArea":"",
                     "shippingAddress":"",
                     "newConsignee[consigneeName]":"",
                     "newConsignee[consigneeMobile]":"",
                     "newConsignee[consigneePhone]":"",
                     "newConsignee[consigneeProvince]":"",
                     "newConsignee[consigneeCity]":"",
                     "newConsignee[consigneeArea]":"",
                     "newConsignee[consigneeAddress]":"",
                     "consigneeAddressCount":"1",
                     "consigneeAddressList":'[{"consigneeName":"","consigneeMobile":"","consigneePhone":"","consigneeProvince":"","consigneeCity":"","consigneeArea":"","consigneeAddress":""}]',
                     "packageAmts":"",
                     "packageCategory":"服饰",
                     "packageNote":""
        } #参数存字典
        request = self.s.post(url=self.url,data=self.body)

        global resp
        resp = request.json()
        if resp["rcode"] ==0 and resp["scode"]==0:
            print("pass")
        else:
            print("false")


    # def test_002(self):        #删除自定义包裹
    #     u'''删除自定义包裹'''
    #     global resp
    #
    #     self.url = "http://www.fhd001.com/package/deletePackage.do"
    #     self.body = {"packageIds":resp['data'][0]
    #     } #参数存字典
    #     request = self.s.post(url=self.url,data=self.body)
    #
    #     print(request.status_code)
    #     print(request.text)
    #     print(type(request.url))
    #
    #     resp  =  request.json()
    #     if resp["rcode"] ==0 and resp["scode"]==0:
    #         print("删除成功")
    #     else:
    #         print("删除失败")

if __name__ == "__main__":
    unittest.main()
