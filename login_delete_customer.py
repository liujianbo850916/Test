# -*- coding: utf_8 -*-
import HTMLTestRunner
from unittest import TestCase
import sys
from HttpLibrary import HttpApi
import unittest
import requests
import time
reload(sys)
sys.setdefaultencoding("utf-8")


# class类
class TestApi(unittest.TestCase):
    # class下初始化方法
    def setUp(self):
        self.api = HttpApi()

    def Test_login(self):
        '''测试登录接口'''
        # 接口url
        url = "http://www.4snow.cn/Home/Index/go/op/login"
        # 接口参数
        data = {"login":"xiaogu","pwd":"123456"}
        # 结果中包含方法post、url、data，当结果为真时返回下面
        result = self.api.http_request("POST",url,data,True)
        # 验证是否返回"status":0
        self.assertEqual(result["status"],0)
        # 验证返回结果中是否返回data下loginname为xiaogu
        self.assertEqual(result["data"]["loginname"],u"xiaogu")

    def test_delete(self):
        '''批量删除客户信息'''
        # 查询url
        url = "http://www.4snow.cn/Business/Cust/go/op/query"
        data = {"page":"1","size":"5","range":"personal"}
        result = self.api.http_request("POST",url,data,True)
        self.assertEqual(result["status"],0)

        # 删除url
        delete_url = "http://www.4snow.cn/Business/Cust/go/op/delete"
        # for循环
        for i in range(len(result["data"]["list"])):
            # 定义变量id等于，循环结果中包含循环list的id
            id = result["data"]["list"][i]["id"]
            # 定义变量delete_data等于id
            delete_data = {"id":id}
            # 定义变量test中包含的方法、变量名delete_url、变量名delete_data
            test = self.api.http_request("POST",delete_url,delete_data,True)
            # 验证是否返回"status":0
            self.assertEqual(test["status"],0)



# 定义Suite方法
def Suite():
    testunit = unittest.TestSuite()
    # 调用Test_login方法
    testunit.addTest(TestApi("Test_login"))
    # 调用test_delete方法
    testunit.addTest(TestApi("test_delete"))
    return testunit







if __name__ == '__main__':
    # 获取当前时间
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    HtmlFile = "D:\\python\python_scripts\\" + now + "HTMLtemplate.html"
    print HtmlFile
    fp = file(HtmlFile, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"云杉接口测试报告", description=u"用例测试执行情况")
    # 执行Suite方法的测试用例
    runner.run(Suite())