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

    def test_create_package_normal(self):        #新建自定义包裹
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

        print (resp['data'])
        # print (resp)


    def test_delete_package_normal(self):        #删除自定义包裹
        u'''删除自定义包裹'''
        global resp

        self.url = "http://www.fhd001.com/package/deletePackage.do"
        self.body = {"packageIds":resp['data'][0]
        } #参数存字典
        request = self.s.post(url=self.url,data=self.body)

        # print(request.status_code)
        # print(request.text)
        # print(type(request.url))

        resp  =  request.json()
        if resp["rcode"] ==0 and resp["scode"]==0:
            print("删除成功")
        else:
            print("删除失败")

if __name__ == "__main__":
    unittest.main()
