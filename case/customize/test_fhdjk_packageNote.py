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
    u'''保存包裹常用备注'''
    resp = None

    @classmethod
    def setUpClass(cls):      # 前置
        print('--- setUpClass ---')
        print('--- 保存包裹常用备注 ---')
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

    def test_create_packageNote_001_normal(self):        #保存包裹常用备注
        '''正例:正确入参'''
        print("正例:正确入参")
        self.url = "http://www.fhd001.com/package/savePackageCommonNote.do"
        self.body = {"packageNote":"接口自动化包裹备注"
        } #参数存字典
        request = self.s.post(url=self.url,data=self.body)

        global resp
        resp = request.json()
        if resp["rcode"] ==0 and resp["scode"]==0:
            print("pass")
        else:
            print("false")

    def test_create_packageNote_002_note_null(self):        #保存包裹常用备注
        '''反例:包裹备注为空'''
        print("反例:包裹备注为空")
        self.url = "http://www.fhd001.com/package/savePackageCommonNote.do"
        self.body = {"packageNote":""
        } #参数存字典
        request = self.s.post(url=self.url,data=self.body)

        global resp
        resp = request.json()
        if resp["rcode"] ==0 and resp["scode"]==0:
            print("pass")
        else:
            print("false")

    def test_create_packageNote_003_note_none(self):        #保存包裹常用备注
        '''反例:包裹备注为None'''
        print("反例:包裹备注为None")
        self.url = "http://www.fhd001.com/package/savePackageCommonNote.do"
        self.body = {"packageNote":None
        } #参数存字典
        request = self.s.post(url=self.url,data=self.body)

        global resp
        resp = request.json()
        if resp["rcode"] ==0 and resp["scode"]==0:
            print("pass")
        else:
            print("false")



if __name__ == "__main__":
    unittest.main()
