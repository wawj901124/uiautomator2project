# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/10/10 16:21'
import unittest

from base.baseframe import BaseFrame
from base.watcherframe import WatcherFrame
from project.yinniqianbaoshanghu.gloablconfig.globalconfig import GlobalConfig
from util.gettimestr import GetTimeStr

class TestTips(unittest.TestCase):  # 创建测试类

    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为setUpClass
    def setUpClass(cls):
        cls.watcherframe = WatcherFrame(GlobalConfig.globaldevice) #实例化
        cls.watcherframe.start_all_watchers()
        pass

    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为tearDownClass
    def tearDownClass(cls):
        cls.watcherframe.close_all_watchers()
        pass

    def setUp(self):  # 每条用例执行测试之前都要执行此方法
        self.watcherframe = WatcherFrame(GlobalConfig.globaldevice) #实例化
        self.baseframe = BaseFrame(GlobalConfig.globaldevice)   #实例化
        print("测试用例开跑-----------------------------------------------")
        #pass


    def tearDown(self):  # 每条用例执行测试之后都要执行此方法
        print("测试用例跑完-----------------------------------------------")
        pass

    def define_tips(self,outtipooptionsid=None,outoptiontext=None,
                    outfixedfeeinputid=None,outfixedfeeinputtext=None,outfixedfeeconfirmid=None,
                    outpercentagefeeinputid=None,outpercentagefeeinputtext=None,outpercentagefeeconfirmid=None,
                    outpretext=None, outbeisaoid=None, outzhusaoid=None,
                    outmoneyinputid=None,outmoneyinputtext=None,outpretoastmessage=None):
        if outtipooptionsid==None:
            tipooptionsid = 'com.ahdi.qrindo.merchant:id/tv_tips_show'
        else:
            tipooptionsid =outtipooptionsid

        if outoptiontext== None:
            optiontext = 'No Tips'
        else:
            optiontext = outoptiontext



        if outfixedfeeinputid == None:
            fixedfeeinputid = 'com.ahdi.qrindo.merchant:id/edt_pwd'
        else:
            fixedfeeinputid = outfixedfeeinputid

        if outfixedfeeinputtext == None:
            fixedfeeinputtext = '1000'
        else:
            fixedfeeinputtext = outfixedfeeinputtext

        if outfixedfeeconfirmid ==None:
            fixedfeeconfirmid = 'com.ahdi.qrindo.merchant:id/btn_confirm'
        else:
            fixedfeeconfirmid = outfixedfeeconfirmid

        if outpercentagefeeinputid==None:
            percentagefeeinputid = 'com.ahdi.qrindo.merchant:id/edt_pwd'
        else:
            percentagefeeinputid = outpercentagefeeinputid

        if outpercentagefeeinputtext==None:
            percentagefeeinputtext = '100'
        else:
            percentagefeeinputtext =outpercentagefeeinputtext

        if outpercentagefeeconfirmid ==None:
            percentagefeeconfirmid = 'com.ahdi.qrindo.merchant:id/btn_confirm'
        else:
            percentagefeeconfirmid = outpercentagefeeconfirmid

        if outpretext==None:
            pretext = 'No Tips'
        else:
            pretext= outpretext

        if outbeisaoid ==None:
            beisaoid = 'com.ahdi.qrindo.merchant:id/iv_cashier_show_qr'
        else:
            beisaoid = outbeisaoid

        if outzhusaoid ==None:
            zhusaoid = 'com.ahdi.qrindo.merchant:id/iv_cashier_scan_qr'
        else:
            zhusaoid = outzhusaoid

        if outmoneyinputid == None:
            moneyinputid = 'com.ahdi.qrindo.merchant:id/edt_pay_num'
        else:
            moneyinputid = outmoneyinputid

        if outmoneyinputtext ==None:
            moneyinputtext = None
        else:
            moneyinputtext = outmoneyinputtext

        if optiontext == 'com.ahdi.qrindo.merchant:id/btn_back':
            cancelid = optiontext
            cancelpretext = self.baseframe.findbyresourceId_and_return_text(tipooptionsid)  # 查看小费选项显示内容
            self.baseframe.findbyresourceId_and_click(tipooptionsid)  # 点击小费选项
            self.baseframe.findbyresourceId_and_click(cancelid)  # # 选择小费选项_No Tips、Consumer Input、Fixed Fee、Percentage Fee、Cancel
            resulttext = self.baseframe.findbyresourceId_and_return_text(tipooptionsid)  # 查看小费选项显示内容
            self.assertEqual(cancelpretext, resulttext)
        else:
            self.baseframe.findbyresourceId_and_click(tipooptionsid)   #点击小费选项
            self.baseframe.findbytext_and_click(optiontext)  # # 选择小费选项_No Tips、Consumer Input、Fixed Fee、Percentage Fee、Cancel

            if optiontext == 'Fixed Fee':
                self.baseframe.findbyresourceId_and_input(fixedfeeinputid, fixedfeeinputtext)  # 输入固定金额费用
                self.baseframe.findbyresourceId_and_click(fixedfeeconfirmid)  # 点击确认按钮
            if optiontext == 'Percentage Fee':
                self.baseframe.findbyresourceId_and_input(percentagefeeinputid, percentagefeeinputtext)  # 输入百分比金额费用
                self.baseframe.findbyresourceId_and_click(percentagefeeconfirmid)  # 点击确认按钮

            resulttext = self.baseframe.findbyresourceId_and_return_text(tipooptionsid)  # 查看小费选项显示内容
            self.assertEqual(pretext, resulttext)
            zhusaoenablestatus = self.baseframe.findbyresourceId_and_return_enabledstatus(beisaoid)  # 查看被扫可用状态
            self.assertTrue(zhusaoenablestatus)
            beisaoenablestatus = self.baseframe.findbyresourceId_and_return_enabledstatus(zhusaoid)  # 查看主扫可用状态
            if optiontext == 'No Tips':
                self.assertTrue(beisaoenablestatus)
            else:
                self.assertFalse(beisaoenablestatus)

        self.baseframe.findbyresourceId_and_input(moneyinputid,moneyinputtext)   #输入金额
        toastmessage = self.baseframe.findbyresourceId_and_click(beisaoid,outpretoastmessage)   #不输入金额，点击被扫，查看toast提示
        if toastmessage != None:
            self.assertEqual(outpretoastmessage,toastmessage)
        else:
            self.baseframe.delaytime(5)
            self.baseframe.findbytext("Scan to pay me")
            gett = GetTimeStr()   #实例化

            totalamount = self.baseframe.findbyresourceId_and_return_text('com.ahdi.qrindo.merchant:id/tv_fee_total')
            totalamountstr = gett.getsplitstr(totalamount)
            print("totalamountstr:",totalamountstr)

            payamount = self.baseframe.findbyresourceId_and_return_text('com.ahdi.qrindo.merchant:id/tv_Amount')
            payamountstr = gett.getsplitstr(payamount)
            print("payamountstr:",payamountstr)

            tipsamount = self.baseframe.findbyresourceId_and_return_text('com.ahdi.qrindo.merchant:id/tv_tips_fee')
            tipsamountstr = gett.getsplitstr(tipsamount)
            print("tipsamountstr:",tipsamountstr)

            totalamountint = int(totalamountstr)
            pretotalamountint = int(payamountstr)+int(tipsamountstr)
            print("totalamountint:",totalamountint)
            print("pretotalamountint:",pretotalamountint)

            self.assertEqual(pretotalamountint,totalamountint)
            self.baseframe.findbyresourceId_and_click("com.ahdi.qrindo.merchant:id/btn_back")






   

    @unittest.skip('test_011')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_011(self):
        """
        无小费时，主扫和被扫都可用，不输入金额，Toast提示
        """
        outtipooptionsid = None
        outoptiontext = None
        outpretext = None
        outbeisaoid = None
        outzhusaoid = None
        outfixedfeeinputid = None
        outfixedfeeinputtext = None
        outfixedfeeconfirmid = None
        outpercentagefeeinputid = None
        outpercentagefeeinputtext = None
        outpercentagefeeconfirmid = None
        outmoneyinputid = None
        outmoneyinputtext = None
        outpretoastmessage = 'The amount cannot be empty'

        self.define_tips(outpretoastmessage=outpretoastmessage)
        print("小费选项为‘No Tips’时，主扫和被扫都可用.不输入金额，点击被扫，Toast提示‘The amount cannot be empty’.---测试通过")

    @unittest.skip('test_012')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_012(self):
        """
        小费类型为Consumer Input，主扫不可用，被扫可用，不输入金额，Toast提示
        """
        outtipooptionsid = None
        outoptiontext = 'Consumer Input'
        outpretext = 'Consumer Input'
        outbeisaoid = None
        outzhusaoid = None
        outfixedfeeinputid = None
        outfixedfeeinputtext = None
        outfixedfeeconfirmid = None
        outpercentagefeeinputid = None
        outpercentagefeeinputtext = None
        outpercentagefeeconfirmid = None
        outmoneyinputid = None
        outmoneyinputtext = None
        outpretoastmessage = 'The amount cannot be empty'

        self.define_tips(outoptiontext=outoptiontext,outpretext=outpretext,outpretoastmessage=outpretoastmessage)
        print("小费选项为‘Consumer Input’时，主扫不可用，被扫可用.不输入金额，点击被扫，Toast提示‘The amount cannot be empty’.---测试通过")

    @unittest.skip('test_013')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_013(self):
        """
        小费类型为Fixed Fee，主扫不可用，被扫可用，不输入金额，Toast提示
        """
        outtipooptionsid = None
        outoptiontext = 'Fixed Fee'
        outfixedfeeinputid = None
        outfixedfeeinputtext = '10000'
        outfixedfeeconfirmid = None
        outpercentagefeeinputid = None
        outpercentagefeeinputtext = None
        outpercentagefeeconfirmid = None
        outpretext = 'Rp.%s'%outfixedfeeinputtext
        outbeisaoid = None
        outzhusaoid = None
        outmoneyinputid = None
        outmoneyinputtext = None
        outpretoastmessage = 'The amount cannot be empty'

        self.define_tips(outoptiontext=outoptiontext,outfixedfeeinputtext=outfixedfeeinputtext,outpretext=outpretext,outpretoastmessage=outpretoastmessage)
        print("小费选项为‘Fixed Fee’时，主扫不可用，被扫可用.不输入金额，点击被扫，Toast提示‘The amount cannot be empty’.---测试通过")

    @unittest.skip('test_014')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_014(self):
        """
        小费类型为Percentage Fee，主扫不可用，被扫可用，不输入金额，Toast提示
        """
        outtipooptionsid = None
        outoptiontext = 'Percentage Fee'
        outfixedfeeinputid = None
        outfixedfeeinputtext = None
        outfixedfeeconfirmid = None
        outpercentagefeeinputid = None
        outpercentagefeeinputtext = '10'
        outpercentagefeeconfirmid = None
        outpretext = '%s%%'%outpercentagefeeinputtext
        outbeisaoid = None
        outzhusaoid = None
        outmoneyinputid = None
        outmoneyinputtext = None
        outpretoastmessage = 'The amount cannot be empty'

        self.define_tips(outoptiontext=outoptiontext,outpercentagefeeinputtext=outpercentagefeeinputtext,outpretext=outpretext,outpretoastmessage=outpretoastmessage)
        print("小费选项为‘Percentage Fee’时，主扫不可用，被扫可用.不输入金额，点击被扫，Toast提示‘The amount cannot be empty’.---测试通过")

    @unittest.skip('test_015')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_015(self):
        """
        小费类型为Cancel，主扫和被扫状态不变，不输入金额，Toast提示
        """
        outtipooptionsid = None
        outoptiontext = 'com.ahdi.qrindo.merchant:id/btn_back'
        outfixedfeeinputid = None
        outfixedfeeinputtext = None
        outfixedfeeconfirmid = None
        outpercentagefeeinputid = None
        outpercentagefeeinputtext = None
        outpercentagefeeconfirmid = None
        outpretext = None
        outbeisaoid = None
        outzhusaoid = None
        outmoneyinputid = None
        outmoneyinputtext = None
        outpretoastmessage = 'The amount cannot be empty'

        self.define_tips(outoptiontext=outoptiontext,outpretoastmessage=outpretoastmessage)
        print("小费选项为‘Cancel’时，主扫与被扫保持原有状态不变.不输入金额，点击被扫，Toast提示‘The amount cannot be empty’.---测试通过")



    @unittest.skip('test_021')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_021(self):
        """
        无小费时，主扫和被扫都可用，输入金额，跳转到二维码页面
        """
        outtipooptionsid = None
        outoptiontext = None
        outpretext = None
        outbeisaoid = None
        outzhusaoid = None
        outfixedfeeinputid = None
        outfixedfeeinputtext = None
        outfixedfeeconfirmid = None
        outpercentagefeeinputid = None
        outpercentagefeeinputtext = None
        outpercentagefeeconfirmid = None
        outmoneyinputid = None
        outmoneyinputtext = '1001000'
        outpretoastmessage = None

        self.define_tips(outmoneyinputtext = outmoneyinputtext)
        print("小费选项为‘No Tips’时，主扫和被扫都可用.输入金额，点击被扫，跳转到二维码页面.---测试通过")

    @unittest.skip('test_022')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_022(self):
        """
        小费类型为Consumer Input，主扫不可用，被扫可用，输入金额，跳转到二维码页面
        """
        outtipooptionsid = None
        outoptiontext = 'Consumer Input'
        outpretext = 'Consumer Input'
        outbeisaoid = None
        outzhusaoid = None
        outfixedfeeinputid = None
        outfixedfeeinputtext = None
        outfixedfeeconfirmid = None
        outpercentagefeeinputid = None
        outpercentagefeeinputtext = None
        outpercentagefeeconfirmid = None
        outmoneyinputid = None
        outmoneyinputtext =  '1000'
        outpretoastmessage = None

        self.define_tips(outoptiontext=outoptiontext,outpretext=outpretext,outmoneyinputtext = outmoneyinputtext)
        print("小费选项为‘Consumer Input’时，主扫不可用，被扫可用.输入金额，点击被扫，跳转到二维码页面.---测试通过")

    @unittest.skip('test_023')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_023(self):
        """
        小费类型为Fixed Fee，主扫不可用，被扫可用，输入金额，跳转到二维码页面
        """
        outtipooptionsid = None
        outoptiontext = 'Fixed Fee'
        outfixedfeeinputid = None
        outfixedfeeinputtext = '100'
        outfixedfeeconfirmid = None
        outpercentagefeeinputid = None
        outpercentagefeeinputtext = None
        outpercentagefeeconfirmid = None
        outpretext = 'Rp.%s'%outfixedfeeinputtext
        outbeisaoid = None
        outzhusaoid = None
        outmoneyinputid = None
        outmoneyinputtext = '1000'
        outpretoastmessage = None

        self.define_tips(outoptiontext=outoptiontext,outfixedfeeinputtext=outfixedfeeinputtext,outpretext=outpretext,outmoneyinputtext=outmoneyinputtext)
        print("小费选项为‘Fixed Fee’时，主扫不可用，被扫可用.输入金额，点击被扫，跳转到二维码页面.---测试通过")

    @unittest.skip('test_024')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_024(self):
        """
        小费类型为Percentage Fee，主扫不可用，被扫可用，输入金额，跳转到二维码页面
        """
        outtipooptionsid = None
        outoptiontext = 'Percentage Fee'
        outfixedfeeinputid = None
        outfixedfeeinputtext = None
        outfixedfeeconfirmid = None
        outpercentagefeeinputid = None
        outpercentagefeeinputtext = '10'
        outpercentagefeeconfirmid = None
        outpretext = '%s%%'%outpercentagefeeinputtext
        outbeisaoid = None
        outzhusaoid = None
        outmoneyinputid = None
        outmoneyinputtext = '1000'
        outpretoastmessage = None

        self.define_tips(outoptiontext=outoptiontext,outpercentagefeeinputtext=outpercentagefeeinputtext,outpretext=outpretext,outmoneyinputtext=outmoneyinputtext)
        print("小费选项为‘Percentage Fee’时，主扫不可用，被扫可用.输入金额，点击被扫，跳转到二维码页面.---测试通过")

    @unittest.skip('test_025')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_025(self):
        """
        小费类型为Cancel，主扫和被扫状态不变，输入金额，跳转到二维码页面
        """
        outtipooptionsid = None
        outoptiontext = 'com.ahdi.qrindo.merchant:id/btn_back'
        outfixedfeeinputid = None
        outfixedfeeinputtext = None
        outfixedfeeconfirmid = None
        outpercentagefeeinputid = None
        outpercentagefeeinputtext = None
        outpercentagefeeconfirmid = None
        outpretext = None
        outbeisaoid = None
        outzhusaoid = None
        outmoneyinputid = None
        outmoneyinputtext = '1000'
        outpretoastmessage = None

        self.define_tips(outoptiontext=outoptiontext,outmoneyinputtext=outmoneyinputtext)
        print("小费选项为‘Cancel’时，主扫与被扫保持原有状态不变.输入金额，点击被扫，跳转到二维码页面.---测试通过")


