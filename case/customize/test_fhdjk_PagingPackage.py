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
    u'''分页查询包裹信息'''
    resp = None

    @classmethod
    def setUpClass(cls):      # 前置
        print('--- setUpClass ---')
        print('--- 分页查询包裹信息 ---')
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

    def test_create_packageNote_001_stayCount(self):        #待打数量统计
        '''正例:待打数量统计'''
        print("正例:待打数量统计")
        self.url = "http://www.fhd001.com/package/queryPackage.do"
        self.body = {"page":"1",
                     "pageSize":"0",
                     "status":"0"

        } #参数存字典
        request = self.s.post(url=self.url,data=self.body)
        # con = request.content
        # print (request.content)
        global resp
        resp = request.json()
        print ("待打数量%d"%(resp['data']['total']))
        if resp["rcode"] ==0 and resp["scode"]==0:
            print("pass")
        else:
            print("false")

    def test_create_packageNote_002_hasCount(self):        #已打数量统计
        '''正例:已打数量统计'''
        print("正例:已打数量统计")
        self.url = "http://www.fhd001.com/package/queryPackage.do"
        self.body = {"page":"1",
                     "pageSize":"0",
                     "status":"4"

        } #参数存字典
        request = self.s.post(url=self.url,data=self.body)
        # con = request.content
        # print (request.content)
        global resp
        resp = request.json()
        print ("已打数量%d"%(resp['data']['total']))
        if resp["rcode"] ==0 and resp["scode"]==0:
            print("pass")
        else:
            print("false")

    def test_create_packageNote_003_tenLines(self):        #每页显示10行
        '''正例:每页显示10行'''
        print("正例:每页显示10行")
        self.url = "http://www.fhd001.com/package/queryPackage.do"
        self.body = {"sort":"createTime",
                     "desc":"true",
                     "page":"1",
                     "pageSize":"10",
                     "status":"0"

        } #参数存字典
        request = self.s.post(url=self.url,data=self.body)
        global resp
        if resp["rcode"] ==0 and resp["scode"]==0:
            print("pass")
        else:
            print("false")

    def test_create_packageNote_004_twentyLines(self):        #每页显示20行
        '''正例:每页显示20行'''
        print("正例:每页显示20行")
        self.url = "http://www.fhd001.com/package/queryPackage.do"
        self.body = {"sort":"createTime",
                     "desc":"true",
                     "page":"1",
                     "pageSize":"20",
                     "status":"0"

        } #参数存字典
        request = self.s.post(url=self.url,data=self.body)
        global resp
        if resp["rcode"] ==0 and resp["scode"]==0:
            print("pass")
        else:
            print("false")

    def test_create_packageNote_005_fiftyLines(self):        #每页显示50行
        '''正例:每页显示50行'''
        print("正例:每页显示50行")
        self.url = "http://www.fhd001.com/package/queryPackage.do"
        self.body = {"sort":"createTime",
                     "desc":"true",
                     "page":"1",
                     "pageSize":"50",
                     "status":"0"

        } #参数存字典
        request = self.s.post(url=self.url,data=self.body)
        global resp
        if resp["rcode"] ==0 and resp["scode"]==0:
            print("pass")
        else:
            print("false")

    def test_create_packageNote_006_oneHundredLines(self):        #每页显示100行
        '''正例:每页显示100行'''
        print("正例:每页显示100行")
        self.url = "http://www.fhd001.com/package/queryPackage.do"
        self.body = {"sort":"createTime",
                     "desc":"true",
                     "page":"1",
                     "pageSize":"100",
                     "status":"0"

        } #参数存字典
        request = self.s.post(url=self.url,data=self.body)
        global resp
        if resp["rcode"] ==0 and resp["scode"]==0:
            print("pass")
        else:
            print("false")


if __name__ == "__main__":
    unittest.main()
