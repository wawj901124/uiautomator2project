# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/10/11 11:24'
import unittest
import uiautomator2 as u2

from base.baseframe import BaseFrame
from project.yinniqianbaoshanghu.gloablconfig.globalconfig import GlobalConfig

class TestLogout(unittest.TestCase):  # 创建测试类

    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为setUpClass
    def setUpClass(cls):
        cls.baseframe = BaseFrame(GlobalConfig.globaldevice)
        cls.baseframe.findbyresourceId_and_click("com.ahdi.qrindo.merchant:id/iv_cashier_right_top")  # 点击页面右上角的更多图标
        cls.baseframe.findbyresourceId_and_click("com.ahdi.qrindo.merchant:id/tv_my_account")  # 点击设置选项
        pass

    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为tearDownClass
    def tearDownClass(cls):
        pass

    def setUp(self):  # 每条用例执行测试之前都要执行此方法
        self.baseframe = BaseFrame(GlobalConfig.globaldevice)   #实例化
        #pass


    def tearDown(self):  # 每条用例执行测试之后都要执行此方法
        pass

    def define_loggout(self,outlogouttext=None,outlogoutconfirmtext=None,outpretext=None):
        if outlogouttext==None:
            logouttext = "Log Out"
        else:
            logouttext = outlogouttext

        if outlogoutconfirmtext==None:
            logoutconfirmtext = "Log Out"
        else:
            logoutconfirmtext = outlogoutconfirmtext

        if outpretext==None:
            pretext = "Log in"
        else:
            pretext = outpretext

        self.baseframe.findbytext_and_click(logouttext)  # 点击登出
        self.baseframe.findbytext_and_click(logoutconfirmtext)  # 点击登出
        preele = self.baseframe.findbytext(pretext)  # 确认有显示文字“Log in”
        self.assertTrue(preele)



    # @unittest.skip('test_001')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_001(self):
        """
        点击登出，退出到登录页
        """
        logouttext = "Log Out"
        logoutconfirmtext = "Cancel"
        pretext = "Log Out"

        self.define_loggout(outlogouttext=logouttext,outlogoutconfirmtext=logoutconfirmtext,outpretext=pretext)

    # @unittest.skip('test_002')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_002(self):
        """
        点击登出，退出到登录页
        """
        logouttext = "Log Out"
        logoutconfirmtext = "Log Out"
        pretext = "Log in"

        self.define_loggout(outlogouttext=logouttext,outlogoutconfirmtext=logoutconfirmtext,outpretext=pretext)

















