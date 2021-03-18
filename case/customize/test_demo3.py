# coding:utf-8
import xlrd
import requests
import unittest
import importlib
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
def setUpModule():    # 当前模块执行前只执行一次
    print('=== setUpModule ===')

def tearDownModule(): # 当前模块执行后只执行一次
    print('=== tearDownModule ===')

class Test_login(unittest.TestCase):
    '''登录接口'''
    url = "http://www.fhd001.com/loginAccount.do"
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
                      "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
                      "Referer":"http://www.fhd001.com/",
                      "Cookie":"CNZZDATA1263048142=51987825-1583297402-null%7C1583313201; CNZZDATA1276886889=1211049750-1581389138-%7C1586500912; _pati=dceabddd4793a92e54b1f429d2dddc8b; fhdpdd_user_info_nick=cyccyccyc; fhdpdd_user_info_avatar=https://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTLRrXUnQ7n5vG2bXPMooFQYxyGw4vadia79F5plrgQdkrwBA3d2ObyDcpiaNYII98sBUIVxAqQmmKJA/132; fhd_user_info_nick=sunking; fhd_user_info_avatar=https://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTJiaGdSuKpkrLN4tlrze2OOHwicfS73TJKAScS9toziaicpjWUySrxgickrERnSicVbVtHJSC3Nx2EC5dyA/132; fhdcooperation_id=10086; fhdcooperation_username=%E5%AD%99%E5%BD%AA; fhdcooperation_isAdmin=false; fhdcooperation_isManage=false; fhdcooperation_departmentId=15; fhdcooperation_departmentName=%E7%A0%94%E5%8F%91%E4%B8%AD%E5%BF%83; fhdcooperation_postNo=10; fhdcooperation_postName=%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88; fhdcooperation_token=%7EAwwTIwJBeHVHXVxHclFAJicdcHQZXgJdRFZKUAdfQFMbBQNKEiEOFCNUQFsDQSBRRgB3EAwJRnQDFiQOQ3J3E3IBEyRxQQECTlVVThIhU0EhDRQNdx0mCRJyIBNfBhZzAhF0URIlDBQnU0AjD0FdJkZ9BBB3AEYJDx9XA18HAwYHAw9fG1UJAVpSVVE%3D%7E1%7E; userHeadImgUrl=http%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FQ0j4TwGTfTIdbOjlPgbBtWarETJdX2wSHQNx9icjrG2mpoTuUX6Uobk73BJq6Qh1pB84xC8DBURHfsqQeohlDVA%2F132; yunxu_username=%E5%AD%99%E5%BD%AA; yunxu_token=%7EClPWnK7QjstICAEPA1JSBwFTAE5QAQc%3D%7E1%7E; yunxu_chooseProjectCookieKey=123; JSESSIONID=538A8A21B4CBFD9CCBDF4490F852DE08.fap1-fhdcommon"
        }   # get方法其它加个ser-Agent就可以了
    # self.proxies = {'http': 'http://localhost:8888',
    #                'https': 'http://localhost:8888'}
    # self.s.proxies = .proxies

    @classmethod          # 声明为类方法（必须）

    def setUpClass(cls):  # 类方法，注意后面是，整个类只执行一次
        print('--- setUpClass ---')
        print('--- 登录接口 ---')

    @classmethod
    def tearDownClass(cls):
        print('--- tearDownClass ---')

    def setUp(self):  # 该类中每个测试用例执行一次
        print('... setUp ...')

    def tearDown(self):
        print('... tearDown ...')

    def test_login_001_normal(self):  # 测试用例
        '''正例:正确入参'''
        print("正例:正确入参")
        self.body = {"userAccount":"15167168967",
                    "userPwd":"123456"} #参数存字典
        self.s = requests.session()
        self.s.verify = False
        request = self.s.post(url=self.url,data=self.body,headers=self.header)
        d   =  request.json()  #解析json
        if d["rcode"] ==0 and d["scode"]==0:
            print("pass")
        else:
            print("false")

if __name__ == '__main__':
    unittest.main(verbosity=2) # 运行本测试类所有用例,verbosity为结果显示级别
