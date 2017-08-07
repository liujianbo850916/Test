# -*- coding: utf_8 -*-
from HttpLibrary import HttpApi
import HTMLTestRunner
import requests
import time
import sys
import unittest
reload(sys)
sys.setdefaultencoding("utf-8")



class TestApi(unittest.TestCase):
    def setUp(self):
        self.api = HttpApi()


    def test_login(self):
        url = "http://www.4snow.cn/Home/Index/go/op/login"
        data = {"login":"wangyang","pwd":"qwer1234"}
        result = self.api.http_request("POST",url,data,True)
        self.assertEqual(result["status"],0)
        self.assertEqual(result["data"]["loginname"],u"tiandao_admin")

def Suite():
    testunit=unittest.TestSuite()
    testunit.addTest(TestApi("test_login"))
    return testunit


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    HtmlFile = "D:\\python\python_scripts\\" + now + "HTMLtemplate.html"
    print HtmlFile
    fp = file(HtmlFile, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"云杉接口测试报告", description=u"用例测试执行情况")
    runner.run(Suite())
