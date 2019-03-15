# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/10/10 10:35'
import unittest
import uiautomator2 as u2

from base.baseframe import BaseFrame
from base.watcherframe import WatcherFrame
from project.yinniqianbaoshanghu.gloablconfig.globalconfig import GlobalConfig

class TestLogin(unittest.TestCase):  # 创建测试类

    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为setUpClass
    def setUpClass(cls):

        # cls.d = u2.connect('192.168.199.168')
        # cls.d = u2.connect_usb('127.0.0.1:62025')
        cls.watcherframe = WatcherFrame(GlobalConfig.globaldevice) #实例化
        cls.watcherframe.new_create_watcher()
        cls.watcherframe.new_create_watcher(outwatchername='OK',outconditiontextname='OK',outclicktextname='OK')
        cls.watcherframe.start_watcher()
        print('\n')
        pass

    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为tearDownClass
    def tearDownClass(cls):
        print('\n')
        cls.watcherframe.close_all_watchers()
        pass

    def setUp(self):  # 每条用例执行测试之前都要执行此方法
        self.baseframe = BaseFrame(GlobalConfig.globaldevice)   #实例化
        print('\n')
        #pass


    def tearDown(self):  # 每条用例执行测试之后都要执行此方法
        print('\n')
        pass

    def definelogin(self,outadborder=None,outphonenumberid=None,outphonenumberinput=None,outpwdid=None,outpwdinput=None,outloginbuttonid=None,outprepagetext=None,outpretoastmessage=None):
        if outadborder==None:
            adborder = "com.ahdi.qrindo.merchant"
        else:
            adborder=outadborder

        if outphonenumberid ==None:
            phonenumberid = "com.ahdi.qrindo.merchant:id/et_phonenumber"
        else:
            phonenumberid = outphonenumberid

        if outphonenumberinput ==None:
            phonenumberinput = '81122336666'
        else:
            phonenumberinput = outphonenumberinput

        if outpwdid == None:
            pwdid = "com.ahdi.qrindo.merchant:id/et_pwd"
        else:
            pwdid = outpwdid

        if outpwdinput ==None:
            pwdinput = "abc123456"
        else:
            pwdinput = outpwdinput

        if outloginbuttonid == None:
            loginbuttonid = "com.ahdi.qrindo.merchant:id/btn_login"
        else:
            loginbuttonid = outloginbuttonid

        # self.baseframe.adbshell(adborder)
        # self.baseframe.findbytext_and_click(adborder)
        self.baseframe.startapp(adborder)
        self.baseframe.findbyresourceId_and_input(phonenumberid, phonenumberinput)  # 输入账号
        self.baseframe.findbyresourceId_and_input(pwdid, pwdinput)  # 输入密码
        pretoastmessage = self.baseframe.findbyresourceId_and_click(loginbuttonid,
                                                                    outpretoastmessage=outpretoastmessage)  # 点击登录按钮
        if pretoastmessage == None:
            if outprepagetext == None:
                prepagetext = None
            else:
                prepagetext = outprepagetext

            if prepagetext == None:
                self.assertTrue(False, '断言错误，请填写预期显示控件的text内容，即确保outprepagetext字段内容不为None，然后再运行测试用例')
            else:
                preele = self.baseframe.findbytext(prepagetext)  # 确认有显示文字“QRindo-Merchant”
                self.assertTrue(preele)
        else:
            toastmessage = self.baseframe.getToast()
            self.assertEqual(pretoastmessage, toastmessage)




    # @unittest.skip('test_020')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_020(self):
        """
        正确的账号和密码，登录成功
        """
        outadborder = None
        outphonenumberid = None
        outphonenumberinput = None
        outpwdid = None
        outpwdinput = None
        outloginbuttonid = None
        outprepagetext = 'QRindo-Merchant'
        outpretoastmessage = None

        self.definelogin(outprepagetext=outprepagetext)
        print("已经注册商户的正确的钱包账号和密码，登录成功.---测试通过")

    # @unittest.skip('test_001')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_001(self):
        """
        非8或08开头的手机
        """
        outadborder = None
        outphonenumberid = None
        outphonenumberinput = '1122336666'
        outpwdid = None
        outpwdinput ='123456'
        outloginbuttonid = None
        outprepagetext = None
        outpretoastmessage = 'You have entered an invalid Indonesia number'
        self.definelogin(outphonenumberinput=outphonenumberinput,outpwdinput=outpwdinput,outpretoastmessage=outpretoastmessage)
        print("非8或08开头的手机号登录，toast提示 'You have entered an invalid Indonesia number'.---测试通过")

    # @unittest.skip('test_002')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_002(self):
        """
        正确的钱包账号和密码，非商户
        """
        outadborder = None
        outphonenumberid = None
        outphonenumberinput = '81122337788'
        outpwdid = None
        outpwdinput ='a123456'
        outloginbuttonid = None
        outprepagetext = 'Login account is not bound to the merchant(MC320)'
        outpretoastmessage = None
        self.definelogin(outphonenumberinput=outphonenumberinput,outpwdinput=outpwdinput,outprepagetext=outprepagetext)
        self.baseframe.findbytext_and_click('OK')
        print("没有注册商户的正确的钱包账号和密码，登录提示'Login account is not bound to the merchant(MC320)'.---测试通过")

    # @unittest.skip('test_003')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_003(self):
        """
        未注册的印尼手机号码
        """
        outadborder = None
        outphonenumberid = None
        outphonenumberinput = '86754893987'
        outpwdid = None
        outpwdinput ='a123456'
        outloginbuttonid = None
        outprepagetext = 'Incorrect account number or login password. Please try again(PP001)'
        outpretoastmessage = None
        self.definelogin(outphonenumberinput=outphonenumberinput,outpwdinput=outpwdinput,outprepagetext=outprepagetext)
        self.baseframe.findbytext_and_click('OK')
        print("没有注册商户的钱包账号登录，提示'Incorrect account number or login password. Please try again(PP001)'.---测试通过")


    # @unittest.skip('test_004')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_004(self):
        """
        已注册的账号，错误的密码及锁定
        """
        for i in range(0,5):
            outadborder = None
            outphonenumberid = None
            outphonenumberinput = '833669911'
            outpwdid = None
            outpwdinput ='123456'
            outloginbuttonid = None
            outprepagetext = 'Incorrect account number or login password. Please try again(PP001)'
            outpretoastmessage = None
            self.definelogin(outphonenumberinput=outphonenumberinput,outpwdinput=outpwdinput,outprepagetext=outprepagetext)
            self.baseframe.findbytext_and_click('OK')
            print('密码错误%s此---'%str(i+1))
        outadborder = None
        outphonenumberid = None
        outphonenumberinput = '833669911'
        outpwdid = None
        outpwdinput = '123456'
        outloginbuttonid = None
        outprepagetext = 'Login password entered incorrectly too many times. Please wait 5hours 60mins before trying again or reset password(PP013)'
        outpretoastmessage = None
        self.definelogin(outphonenumberinput=outphonenumberinput, outpwdinput=outpwdinput,
                         outprepagetext=outprepagetext)
        self.baseframe.findbytext_and_click('OK')
        print("正确的钱包账号，错误的密码，提示'Incorrect account number or login password. Please try again(PP001)'，错误第五次后提示 'Login password entered incorrectly too many times. Please wait 5hours 60mins before trying again or reset password(PP013)'.---测试通过")


    # @unittest.skip('test_005')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_005(self):
        """
        账号长度输入小于8位，密码位数等于6位，登录按钮置灰不可用
        """
        outadborder = None
        outphonenumberid = None
        outphonenumberinput = '1234567'
        outpwdid = None
        outpwdinput ='123456'
        outloginbuttonid = None
        outprepagetext = 'Log in'
        outpretoastmessage = None
        self.definelogin(outphonenumberinput=outphonenumberinput,outpwdinput=outpwdinput,outprepagetext=outprepagetext)
        eleenable = self.baseframe.findbytext_and_return_enabledstatus('Log in')
        self.assertFalse(eleenable)
        print("账号长度输入小于8位，密码位数等于6位，登录按钮置灰不可用.---测试通过")

    # @unittest.skip('test_006')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_006(self):
        """
        账号长度输入等于8位，密码位数小于6位，登录按钮置灰不可用
        """
        outadborder = None
        outphonenumberid = None
        outphonenumberinput = '12345678'
        outpwdid = None
        outpwdinput ='12345'
        outloginbuttonid = None
        outprepagetext = 'Log in'
        outpretoastmessage = None
        self.definelogin(outphonenumberinput=outphonenumberinput,outpwdinput=outpwdinput,outprepagetext=outprepagetext)
        eleenable = self.baseframe.findbytext_and_return_enabledstatus('Log in')
        self.assertFalse(eleenable)
        print("账号长度输入等于8位，密码位数小于6位，登录按钮置灰不可用.---测试通过")

    # @unittest.skip('test_007')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_007(self):
        """
        账号长度输入大于13位时，密码位数等于6位，登录按钮置灰不可用
        """
        outadborder = None
        outphonenumberid = None
        outphonenumberinput = '12345678901234'
        outpwdid = None
        outpwdinput ='123456'
        outloginbuttonid = None
        outprepagetext = 'Log in'
        outpretoastmessage = None
        self.definelogin(outphonenumberinput=outphonenumberinput,outpwdinput=outpwdinput,outprepagetext=outprepagetext)
        eleenable = self.baseframe.findbytext_and_return_enabledstatus('Log in')
        self.assertFalse(eleenable)
        print("账号长度输入大于13位时，密码位数等于6位，登录按钮置灰不可用.---测试通过")
        # eleinfo_text = self.baseframe.findbyresourceId_and_return_text("com.ahdi.qrindo.merchant:id/et_phonenumber")
        # textlong = len(eleinfo_text)
        # print("textlong:",textlong )
        # self.assertEqual(textlong,14)

    # @unittest.skip('test_008')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_008(self):
        """
        账号长度输入等于13位时，密码位数大于24位，登录按钮置灰不可用
        """
        outadborder = None
        outphonenumberid = None
        outphonenumberinput = '1234567890123'
        outpwdid = None
        outpwdinput ='1234567890123456789012345'
        outloginbuttonid = None
        outprepagetext = 'Log in'
        outpretoastmessage = None
        self.definelogin(outphonenumberinput=outphonenumberinput,outpwdinput=outpwdinput,outprepagetext=outprepagetext)
        eleenable = self.baseframe.findbytext_and_return_enabledstatus('Log in')
        self.assertFalse(eleenable)
        print("账号长度输入等于13位时，密码位数大于24位，登录按钮置灰不可用.---测试通过")

    # #### @unittest.skip('test_0191')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    # def test_0191(self):
    #     """
    #     账号长度输入等于13位时，密码位数大于24位，登录按钮置灰不可用
    #     """
    #     outadborder = 'am start -n com.ahdi.qrindo.mbmwallet/com.altopay.wallet.ui.activities.LoginActivity'
    #     outphonenumberid = 'com.ahdi.qrindo.mbmwallet:id/et_login_phone_number'
    #     outphonenumberinput = '1234567890123'
    #     outpwdid = 'com.ahdi.qrindo.mbmwallet:id/et_login_pwd'
    #     outpwdinput ='1234567890123456789012345'
    #     outloginbuttonid = 'com.ahdi.qrindo.mbmwallet:id/btn_login'
    #     outprepagetext = 'Log in'
    #     outpretoastmessage = None
    #     self.definelogin(outphonenumberinput=outphonenumberinput,outpwdinput=outpwdinput,outprepagetext=outprepagetext,
    #                      outadborder=outadborder,outphonenumberid=outphonenumberid,outpwdid =outpwdid ,outloginbuttonid=outloginbuttonid)
    #     eleenable = self.baseframe.findbytext_and_return_enabledstatus('Log in')
    #     self.assertFalse(eleenable)

if __name__ == '__main__':
    print("hello world")
    unittest.main()










