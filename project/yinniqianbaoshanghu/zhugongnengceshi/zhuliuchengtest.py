# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/7/27 12:24'
import unittest
import HTMLTestRunner

import uiautomator2 as u2
import time

from base.baseframe import BaseFrame
from base.watcherframe import WatcherFrame


class TestZhuGongNeng(unittest.TestCase):  # 创建测试类

    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为setUpClass
    def setUpClass(cls):
        cls.d = u2.connect_usb('127.0.0.1:62025')
        cls.watcherframe = WatcherFrame(cls.d) #实例化
        cls.watcherframe.new_create_watcher()
        cls.watcherframe.start_watcher()
        pass

    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为tearDownClass
    def tearDownClass(cls):
        cls.watcherframe.close_all_watchers()
        pass

    def setUp(self):  # 每条用例执行测试之前都要执行此方法
        # self.d = u2.connect('172.20.157.7')
        self.d = u2.connect_usb('127.0.0.1:62025')
        self.baseframe = BaseFrame(self.d)
        #pass


    def tearDown(self):  # 每条用例执行测试之后都要执行此方法
        pass

    @unittest.skip('test_01')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_01(self):
        """
        登录页登录
        """
        d = self.d
        d.adb_shell('am start -n com.ahdi.qrindo.merchant/com.altopay.app.main.ui.activities.LoginActivity')
        d(resourceId="com.ahdi.qrindo.merchant:id/et_phonenumber").send_keys('81122336666')   #输入账号
        d(resourceId="com.ahdi.qrindo.merchant:id/et_pwd").send_keys('abc123456')   #输入密码
        d(resourceId="com.ahdi.qrindo.merchant:id/btn_login").click() #点击登录按钮
        time.sleep(3)




    @unittest.skip('test_02')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_02(self):
        """
        金额页输入金额生成二维码
        """
        d = self.d
        d(resourceId="com.ahdi.qrindo.merchant:id/edt_pay_num").send_keys('1000')   #输入金额
        d(resourceId="com.ahdi.qrindo.merchant:id/rl_canclick_tips").click()   #点击小费下拉框
        time.sleep(3)
        d(resourceId="com.ahdi.qrindo.merchant:id/tv_tips_item", text=u"Fixed Fee").click()   #点击固定费率
        time.sleep(3)
        d(resourceId="com.ahdi.qrindo.merchant:id/edt_pwd").send_keys('1000')   #输入金额
        d(resourceId="com.ahdi.qrindo.merchant:id/btn_confirm").click()   #点击确认按钮
        time.sleep(3)
        d(text=u"Show QR").click()   #点击生成二维码文字
        time.sleep(3)
        d(text=u"Scan to pay me")   #确认有显示文字“Scan to pay me”
        d(resourceId="com.ahdi.qrindo.merchant:id/btn_back").click()   #点击页面左上角的返回按钮
        time.sleep(3)

    @unittest.skip('test_03')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_03(self):
        """
        输入金额页到历史记录页
        """
        d = self.d
        d(resourceId="com.ahdi.qrindo.merchant:id/iv_cashier_right_top").click()   #点击页面右上角的更多图标
        time.sleep(3)
        d(resourceId="com.ahdi.qrindo.merchant:id/tv_transactions").click()   #点击历史记录选项
        time.sleep(3)
        d(text=u"History Transactions")   #确认有显示文字“History Transactions”
        d(resourceId="com.ahdi.qrindo.merchant:id/btn_back").click()   #点击页面左上角的返回按钮
        time.sleep(3)

    @unittest.skip('test_04')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_04(self):
        """
        输入金额页到设置页，登出到登录页
        """
        d = self.d
        d(resourceId="com.ahdi.qrindo.merchant:id/iv_cashier_right_top").click()   #点击页面右上角的更多图标
        time.sleep(3)
        d(resourceId="com.ahdi.qrindo.merchant:id/tv_my_account").click()   #点击设置选项
        time.sleep(3)
        d(text=u"Log Out").click()   #点击登出
        time.sleep(3)
        d(resourceId="com.ahdi.qrindo.merchant:id/tv_dialog_cancel").click()   #点击登出
        time.sleep(3)
        d(text=u"Log in")   #确认有显示文字“Log in”

    # @unittest.skip('test_011')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_011(self):
        """
        登录页登录
        """
        self.baseframe.adbshell('am start -n com.ahdi.qrindo.merchant/com.altopay.app.main.ui.activities.LoginActivity')
        self.baseframe.findbyresourceId_and_input("com.ahdi.qrindo.merchant:id/et_phonenumber",'81122336666')   #输入账号
        self.baseframe.findbyresourceId_and_input("com.ahdi.qrindo.merchant:id/et_pwd", 'abc123456')  #输入密码
        self.baseframe.findbyresourceId_and_click("com.ahdi.qrindo.merchant:id/btn_login") #点击登录按钮
        self.baseframe.findbytext("QRindo-Merchant")  # 确认有显示文字“QRindo-Merchant”

    # @unittest.skip('test_012')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_012(self):
        """
        金额页输入金额生成二维码
        """
        self.baseframe.findbyresourceId_and_input("com.ahdi.qrindo.merchant:id/edt_pay_num", '1000')  #输入金额
        self.baseframe.findbyresourceId_and_click("com.ahdi.qrindo.merchant:id/rl_canclick_tips")  # 点击小费下拉框
        self.baseframe.findbytext_and_click("Fixed Fee")  # 点击固定费率
        self.baseframe.findbyresourceId_and_input("com.ahdi.qrindo.merchant:id/edt_pwd", '1000')  # 输入小费金额
        self.baseframe.findbyresourceId_and_click("com.ahdi.qrindo.merchant:id/btn_confirm")  # 点击确认按钮
        self.baseframe.findbytext_and_click("Show QR")  # 点击生成二维码文字
        self.baseframe.findbytext("Scan to pay me")   #确认有显示文字“Scan to pay me”
        self.baseframe.findbyresourceId_and_click("com.ahdi.qrindo.merchant:id/btn_back")  # 点击页面左上角的返回按钮
        self.baseframe.findbytext("QRindo-Merchant")  # 确认有显示文字“QRindo-Merchant”

    # @unittest.skip('test_013')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_013(self):
        """
        输入金额页到历史记录页
        """
        self.baseframe.findbyresourceId_and_click("com.ahdi.qrindo.merchant:id/iv_cashier_right_top")  # 点击页面右上角的更多图标
        self.baseframe.findbyresourceId_and_click("com.ahdi.qrindo.merchant:id/tv_transactions")  # 点击历史记录选项
        self.baseframe.findbytext("History Transactions")  # 确认有显示文字“Scan to pay me”
        self.baseframe.findbyresourceId_and_click("com.ahdi.qrindo.merchant:id/btn_back")  # 点击页面左上角的返回按钮
        self.baseframe.findbytext("QRindo-Merchant")  # 确认有显示文字“QRindo-Merchant”

    # @unittest.skip('test_014')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_014(self):
        """
        输入金额页到设置页，登出到登录页
        """
        self.baseframe.findbyresourceId_and_click("com.ahdi.qrindo.merchant:id/iv_cashier_right_top")  # 点击页面右上角的更多图标
        self.baseframe.findbyresourceId_and_click("com.ahdi.qrindo.merchant:id/tv_my_account")  # 点击设置选项
        self.baseframe.findbytext_and_click("Log Out")  # 点击登出
        self.baseframe.findbyresourceId_and_click("com.ahdi.qrindo.merchant:id/tv_dialog_cancel")  # 点击登出
        self.baseframe.findbytext("Log in")  # 确认有显示文字“QRindo-Merchant”

# if __name__ == '__main__':
#     # # unittest.main()
#     # #使用HTMLTestRunner跑
#     # filepath = "./report/htmlreport.html"   #放置报告的路径
#     # fp = open(filepath,'wb')   #资源流,以读写的方式打开 file用open替代即可
#     # suite = unittest.TestSuite()  #创建一个用例容器
#     # suite.addTest(TestLoginPage('test_05'))
#     # runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='this is a report',description='report description')   #设置报告的标题和描述
#     # runner.run(suite)  #执行用例集suite



