import unittest
import uiautomator2 as u2
import datetime

from base.baseframe import BaseFrame
from base.watcherframe import WatcherFrame
from project.yinniqianbaoshanghu.gloablconfig.globalconfig import GlobalConfig
from data.get_data_login import GetData

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

    #登录的测试方法
    def definelogin(self,outtestcasediscription=None,outphonenumberinput=None,
                    outpwdinput=None,outprepagetext=None,
                    outpretoastmessage=None,outexceptiontext=None):

        packagename = "com.ahdi.qrindo.merchant"
        phonenumberid = "com.ahdi.qrindo.merchant:id/et_phonenumber"

        if outphonenumberinput ==None:
            phonenumberinput = '81122336666'
        else:
            phonenumberinput = outphonenumberinput

        pwdid = "com.ahdi.qrindo.merchant:id/et_pwd"

        if outpwdinput ==None:
            pwdinput = "abc123456"
        else:
            pwdinput = outpwdinput

        loginbuttonid = "com.ahdi.qrindo.merchant:id/btn_login"

        if outtestcasediscription==None:
            testcasediscription = '测试用例'
        else:
            testcasediscription = outtestcasediscription

        self.baseframe.startapp(packagename)
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

        if outexceptiontext == 'OK':
            print("")
        elif outexceptiontext == 'Log in':
            eleenable = self.baseframe.findbytext_and_return_enabledstatus('Log in')
            self.assertFalse(eleenable)
        print("%s.---测试通过" %testcasediscription)


    @staticmethod    #根据不同的参数生成测试用例
    def getTestFunc(outtestcasediscription,outphonenumberinput,
                    outpwdinput,outprepagetext,
                    outpretoastmessage,outexceptiontext):
        def func(self):
            self.definelogin(outtestcasediscription,outphonenumberinput,
                    outpwdinput,outprepagetext,
                    outpretoastmessage,outexceptiontext)
        return func


    @unittest.skip('test_020')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
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

# def generateTestCases():
#     arglists = [("非8或08开头的手机号登录，toast提示 'You have entered an invalid Indonesia number'",
#                  '1122336666','123456',None,
#                  'You have entered an invalid Indonesia number',None),
#                 ("没有注册商户的正确的钱包账号和密码，登录提示'Login account is not bound to the merchant(MC320)'",
#                  '81122337788','a123456','Login account is not bound to the merchant(MC320)',
#                  None,'OK'),
#                 ('没有注册的钱包账号登录，提示“Incorrect account number or login password Please try again(PP001)”',
#                  '86754893987','a123456','Incorrect account number or login password. Please try again(PP001)',
#                  None,'OK'),
#                 ('正确的钱包账号，错误的密码，提示“Incorrect account number or login password Please try again(PP001)”',
#                  '833669911','123456','Incorrect account number or login password. Please try again(PP001)',
#                  None,'OK'),
#                 ("账号长度输入小于8位，密码位数等于6位，登录按钮置灰不可用",
#                  '1234567','123456','Log in',
#                  None,'Log in'),
#                 ("账号长度输入等于8位，密码位数小于6位，登录按钮置灰不可用",
#                  '12345678','12345','Log in',
#                  None,'Log in'),
#                 ("账号长度输入大于13位时，密码位数等于6位，登录按钮置灰不可用",
#                  '12345678901234','123456','Log in',
#                  None,'Log in'),
#                 ("账号长度输入等于13位时，密码位数大于24位，登录按钮置灰不可用",
#                  '1234567890123','1234567890123456789012345','Log in',
#                  None,'Log in'),
#                 ("已经注册商户的正确的钱包账号和密码，登录成功",
#                  None,None,'QRindo-Merchant',
#                  None,None),
#
#     ]
#     for i in range(0,len(arglists)):
#         args = arglists[i]
#         setattr(TestLogin, 'test_func_%s_%s' % (i,args[0]),
#                 TestLogin.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头

def __generateTestCases():
    file_name = "D:/Users/Administrator/PycharmProjects/uiautomator2project/dataconfig/autologin.xls"
    sheet_id = 0
    datasheet = GetData(file_name,sheet_id)   #实例化
    rows_count = datasheet.get_case_lines()   #获取表的行数
    for i in range(1, rows_count):  # 循环，但去掉第一
        args = []
        args.append(datasheet.get_case_title_content(i))
        args.append(datasheet.get_account_input_content(i))
        args.append(datasheet.get_password_input_content(i))
        args.append(datasheet.get_pre_text_content(i))
        args.append(datasheet.get_pre_toast_content(i))
        args.append(datasheet.get_pre_back_text_content(i))
        setattr(TestLogin, 'test_func_%s_%s' % (datasheet.get_case_id_content(i),args[0]),
                TestLogin.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头


__generateTestCases()

if __name__ == '__main__':
    print("hello world")
    unittest.main()










