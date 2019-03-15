# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/10/11 11:24'
import unittest

import uiautomator2 as u2

from base.baseframe import BaseFrame
from project.yinniqianbaoshanghu.gloablconfig.globalconfig import GlobalConfig

class TestSettings(unittest.TestCase):  # 创建测试类

    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为setUpClass
    def setUpClass(cls):
        cls.baseframe = BaseFrame(GlobalConfig.globaldevice)
        cls.baseframe.findbyresourceId_and_click("com.ahdi.qrindo.merchant:id/iv_cashier_right_top")  # 点击页面右上角的更多图标
        cls.baseframe.findbyresourceId_and_click("com.ahdi.qrindo.merchant:id/tv_my_account")  # 点击设置选项
        pass

    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为tearDownClass
    def tearDownClass(cls):
        cls.baseframe.findbyresourceId_and_click("com.ahdi.qrindo.merchant:id/btn_back")  # 点击设置左上角的返回按钮
        pass

    def setUp(self):  # 每条用例执行测试之前都要执行此方法
        self.baseframe = BaseFrame(GlobalConfig.globaldevice)   #实例化
        #pass


    def tearDown(self):  # 每条用例执行测试之后都要执行此方法
        pass

    def define_setpre(self,outnotificationsswitchid=None,outsoundalertswitchid=None,outnprestatus=None,outsprestatus=None):
        if outnotificationsswitchid ==None:
            notificationsswitchid = 'com.ahdi.qrindo.merchant:id/iv_notice'
        else:
            notificationsswitchid = outnotificationsswitchid

        if outsoundalertswitchid == None:
            soundalertswitchid = 'com.ahdi.qrindo.merchant:id/iv_sound'
        else:
            soundalertswitchid = outsoundalertswitchid
        if outnprestatus==None:
            nprestatus =True
        else:
            nprestatus = outnprestatus

        if outsprestatus ==None:
            sprestatus = True
        else:
            sprestatus = outsprestatus

        getswitchstatus_beforeclick = self.define_getswitchstatus_beforeclick(outnotificationsswitchid=notificationsswitchid,outsoundalertswitchid=soundalertswitchid)
        nstatus = getswitchstatus_beforeclick[0]
        sstatus = getswitchstatus_beforeclick[1]

        if nstatus != nprestatus:
            self.baseframe.findbyresourceId_and_click(notificationsswitchid)  # 点击notificationsswitch
        else:
            pass

        getswitchstatus_beforeclick = self.define_getswitchstatus_beforeclick(
                outnotificationsswitchid=notificationsswitchid, outsoundalertswitchid=soundalertswitchid)
        nstatus = getswitchstatus_beforeclick[0]
        sstatus = getswitchstatus_beforeclick[1]
        if sstatus != sprestatus:
            self.baseframe.findbyresourceId_and_click(soundalertswitchid)  # 点击soundalertswitchid
        else:
            pass

        getswitchstatus_beforeclick = self.define_getswitchstatus_beforeclick(
                outnotificationsswitchid=notificationsswitchid, outsoundalertswitchid=soundalertswitchid)
        nstatus = getswitchstatus_beforeclick[0]
        sstatus = getswitchstatus_beforeclick[1]
        print("前置条件设置为-------------------------")
        print("n:", nstatus)
        print('s:',sstatus)

    def define_aresult(self,outnotificationsswitchid=None,outsoundalertswitchid=None):
        if outnotificationsswitchid ==None:
            notificationsswitchid = 'com.ahdi.qrindo.merchant:id/iv_notice'
        else:
            notificationsswitchid = outnotificationsswitchid

        if outsoundalertswitchid == None:
            soundalertswitchid = 'com.ahdi.qrindo.merchant:id/iv_sound'
        else:
            soundalertswitchid = outsoundalertswitchid

        getswitchstatus_beforeclick = self.define_getswitchstatus_beforeclick(
                outnotificationsswitchid=notificationsswitchid, outsoundalertswitchid=soundalertswitchid)
        nstatus = getswitchstatus_beforeclick[0]
        sstatus = getswitchstatus_beforeclick[1]
        print("实际结果为-------------------------")
        print("n:", nstatus)
        print('s:',sstatus)

    def define_getswitchstatus_beforeclick(self,outnotificationsswitchid=None,outsoundalertswitchid=None):
        if outnotificationsswitchid ==None:
            notificationsswitchid = 'com.ahdi.qrindo.merchant:id/iv_notice'
        else:
            notificationsswitchid = outnotificationsswitchid

        if outsoundalertswitchid == None:
            soundalertswitchid = 'com.ahdi.qrindo.merchant:id/iv_sound'
        else:
            soundalertswitchid = outsoundalertswitchid
        switchstatus = []
        after_notificationsswitch_eleinfo_selected = self.baseframe.findbyresourceId_and_return_selectedstatus(
            notificationsswitchid)
        switchstatus.append(after_notificationsswitch_eleinfo_selected)
        after_soundalertswitch_eleinfo_selected = self.baseframe.findbyresourceId_and_return_selectedstatus(
            soundalertswitchid)
        switchstatus.append(after_soundalertswitch_eleinfo_selected)
        return switchstatus

    def define_getswitchstatus(self,clickselect,outnotificationsswitchid=None,outsoundalertswitchid=None):
        if outnotificationsswitchid ==None:
            notificationsswitchid = 'com.ahdi.qrindo.merchant:id/iv_notice'
        else:
            notificationsswitchid = outnotificationsswitchid

        if outsoundalertswitchid == None:
            soundalertswitchid = 'com.ahdi.qrindo.merchant:id/iv_sound'
        else:
            soundalertswitchid = outsoundalertswitchid
        switchstatus = []
        if clickselect == 'n':
            self.baseframe.findbyresourceId_and_click(notificationsswitchid)  # 点击notificationsswitch
        elif clickselect == 's':
            self.baseframe.findbyresourceId_and_click(soundalertswitchid)  # 点击soundalertswitchid
        else:
            print("clickselect参数错误！clickselect参数只能是n或s，请确保参数正确")
        after_notificationsswitch_eleinfo_selected = self.baseframe.findbyresourceId_and_return_selectedstatus(
            notificationsswitchid)
        switchstatus.append(after_notificationsswitch_eleinfo_selected)
        after_soundalertswitch_eleinfo_selected = self.baseframe.findbyresourceId_and_return_selectedstatus(
            soundalertswitchid)
        switchstatus.append(after_soundalertswitch_eleinfo_selected)
        return switchstatus

    def define_assertluoji(self,outnotificationsswitchid=None,outsoundalertswitchid=None,outclickselect=None):
        if outnotificationsswitchid == None:
            notificationsswitchid = 'com.ahdi.qrindo.merchant:id/iv_notice'
        else:
            notificationsswitchid = outnotificationsswitchid

        if outsoundalertswitchid == None:
            soundalertswitchid = 'com.ahdi.qrindo.merchant:id/iv_sound'
        else:
            soundalertswitchid = outsoundalertswitchid

        if outclickselect ==None:
            clickselect = 'n'
        else:
            clickselect = outclickselect

        print("开始测试-------------------------")
        notificationsswitch_eleinfo_selected = self.baseframe.findbyresourceId_and_return_selectedstatus(notificationsswitchid)
        print('notificationsswitch_eleinfo_selected:',notificationsswitch_eleinfo_selected)
        soundalertswitch_eleinfo_selected = self.baseframe.findbyresourceId_and_return_selectedstatus(soundalertswitchid)
        print('soundalertswitch_eleinfo_selected:', notificationsswitch_eleinfo_selected)

        if notificationsswitch_eleinfo_selected==True and soundalertswitch_eleinfo_selected==True:
            switchstatus = self.define_getswitchstatus(clickselect,notificationsswitchid,soundalertswitchid)
            after_notificationsswitch_eleinfo_selected = switchstatus[0]
            after_soundalertswitch_eleinfo_selected = switchstatus[1]
            if clickselect == 'n':
                self.assertNotEqual(notificationsswitch_eleinfo_selected, after_notificationsswitch_eleinfo_selected)
                self.assertFalse(after_soundalertswitch_eleinfo_selected)
                self.define_aresult(notificationsswitchid,soundalertswitchid)   #打印实际结果
                self.baseframe.findbyresourceId_and_click(notificationsswitchid)  # 点击notificationsswitch
            if clickselect == 's':
                self.assertEqual(notificationsswitch_eleinfo_selected, after_notificationsswitch_eleinfo_selected)
                self.assertNotEqual(soundalertswitch_eleinfo_selected,after_soundalertswitch_eleinfo_selected)
                self.define_aresult(notificationsswitchid, soundalertswitchid)  # 打印实际结果
                self.baseframe.findbyresourceId_and_click(soundalertswitchid)  # 点击soundalertswitchid

        elif notificationsswitch_eleinfo_selected==True and soundalertswitch_eleinfo_selected==False:
            switchstatus = self.define_getswitchstatus(clickselect, notificationsswitchid, soundalertswitchid)
            after_notificationsswitch_eleinfo_selected = switchstatus[0]
            after_soundalertswitch_eleinfo_selected = switchstatus[1]
            if clickselect == 'n':
                self.assertNotEqual(notificationsswitch_eleinfo_selected, after_notificationsswitch_eleinfo_selected)
                self.assertFalse(after_soundalertswitch_eleinfo_selected)
                self.define_aresult(notificationsswitchid, soundalertswitchid)  # 打印实际结果
                self.baseframe.findbyresourceId_and_click(notificationsswitchid)  # 点击notificationsswitch
                self.baseframe.findbyresourceId_and_click(soundalertswitchid)  # 点击soundalertswitchid
            if clickselect == 's':
                self.assertEqual(notificationsswitch_eleinfo_selected, after_notificationsswitch_eleinfo_selected)
                self.assertNotEqual(soundalertswitch_eleinfo_selected,after_soundalertswitch_eleinfo_selected)
                self.define_aresult(notificationsswitchid, soundalertswitchid)  # 打印实际结果
                self.baseframe.findbyresourceId_and_click(soundalertswitchid)  # 点击soundalertswitchid

        elif notificationsswitch_eleinfo_selected == False and soundalertswitch_eleinfo_selected == False:
            switchstatus = self.define_getswitchstatus(clickselect, notificationsswitchid, soundalertswitchid)
            after_notificationsswitch_eleinfo_selected = switchstatus[0]
            after_soundalertswitch_eleinfo_selected = switchstatus[1]
            if clickselect == 'n':
                self.assertNotEqual(notificationsswitch_eleinfo_selected, after_notificationsswitch_eleinfo_selected)
                self.assertNotEqual(soundalertswitch_eleinfo_selected, after_soundalertswitch_eleinfo_selected)
                self.define_aresult(notificationsswitchid, soundalertswitchid)  # 打印实际结果
                self.baseframe.findbyresourceId_and_click(notificationsswitchid)  # 点击notificationsswitch
            if clickselect == 's':
                self.assertEqual(notificationsswitch_eleinfo_selected, after_notificationsswitch_eleinfo_selected)
                self.assertEqual(soundalertswitch_eleinfo_selected,after_soundalertswitch_eleinfo_selected)
                self.define_aresult(notificationsswitchid, soundalertswitchid)  # 打印实际结果


    # @unittest.skip('test_021')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_021(self):
        """
        Notifications与Sound Alert的开关逻辑,Notifications与Sound Alert都是开着的
        """
        outnotificationsswitchid = None
        outsoundalertswitchid = None
        outclickselect = None
        outnprestatus = None
        outsprestatus = None
        self.define_setpre()
        self.define_assertluoji()
        print("当Notifications与Sound Alert开关都处于开启状态，关闭Notifications开关，Notifications与Sound Alert都关闭.---测试通过")
        # self.baseframe.getdeviceinfo()
        # self.baseframe.d.screenshot("home.jpg"

    # @unittest.skip('test_022')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_022(self):
        """
        Notifications与Sound Alert的开关逻辑,Notifications开，Sound Alert关
        """
        outnotificationsswitchid = None
        outsoundalertswitchid = None
        outclickselect = 's'
        outnprestatus = None
        outsprestatus = False
        self.define_setpre(outnotificationsswitchid=outnotificationsswitchid,outsoundalertswitchid=outsoundalertswitchid,
                           outnprestatus=outnprestatus,outsprestatus=outsprestatus)
        self.define_assertluoji(outnotificationsswitchid=outnotificationsswitchid,outsoundalertswitchid=outsoundalertswitchid,outclickselect=outclickselect)
        print("当Notifications开启但Sound Alert关闭时，关闭Notifications开关，Notifications与Sound Alert都关闭.---测试通过")
        # self.baseframe.getdeviceinfo()
        # self.baseframe.d.screenshot("home.jpg"

    # @unittest.skip('test_023')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_023(self):
        """
        Notifications与Sound Alert的开关逻辑,Notifications关，Sound Alert关
        """
        outnotificationsswitchid = None
        outsoundalertswitchid = None
        outclickselect = 's'
        outnprestatus = False
        outsprestatus = False
        self.define_setpre(outnotificationsswitchid=outnotificationsswitchid,outsoundalertswitchid=outsoundalertswitchid,
                           outnprestatus=outnprestatus,outsprestatus=outsprestatus)
        self.define_assertluoji(outnotificationsswitchid=outnotificationsswitchid,outsoundalertswitchid=outsoundalertswitchid,outclickselect=outclickselect)
        print("当Notifications和Sound Alert都关闭时，打开Notifications开关，Notifications与Sound Alert都开启.---测试通过")

    # @unittest.skip('test_031')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_031(self):
        """
        Notifications与Sound Alert的开关逻辑,Notifications与Sound Alert都是开着的
        """
        outnotificationsswitchid = None
        outsoundalertswitchid = None
        outclickselect = None
        outnprestatus = None
        outsprestatus = None
        self.define_setpre(outnotificationsswitchid=outnotificationsswitchid,
                           outsoundalertswitchid=outsoundalertswitchid,
                           outnprestatus=outnprestatus, outsprestatus=outsprestatus)
        self.define_assertluoji(outnotificationsswitchid=outnotificationsswitchid,
                                outsoundalertswitchid=outsoundalertswitchid, outclickselect=outclickselect)
        print("当Notifications与Sound Alert开关都处于开启状态，关闭Sound Alert开关，Notifications开启，Sound Alert关闭.---测试通过")

    # @unittest.skip('test_032')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_032(self):
        """
        Notifications与Sound Alert的开关逻辑,Notifications开，Sound Alert关
        """
        outnotificationsswitchid = None
        outsoundalertswitchid = None
        outclickselect = None
        outnprestatus = None
        outsprestatus = False
        self.define_setpre(outnotificationsswitchid=outnotificationsswitchid,
                           outsoundalertswitchid=outsoundalertswitchid,
                           outnprestatus=outnprestatus, outsprestatus=outsprestatus)
        self.define_assertluoji(outnotificationsswitchid=outnotificationsswitchid,
                                outsoundalertswitchid=outsoundalertswitchid, outclickselect=outclickselect)
        print("当Notifications开启但Sound Alert关闭时，打开Sound Alert开关，Notifications与Sound Alert都开启.---测试通过")
        # self.baseframe.getdeviceinfo()
        # self.baseframe.d.screenshot("home.jpg"

    # @unittest.skip('test_033')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_033(self):
        """
        Notifications与Sound Alert的开关逻辑,Notifications关，Sound Alert关
        """
        outnotificationsswitchid = None
        outsoundalertswitchid = None
        outclickselect = None
        outnprestatus = False
        outsprestatus = False
        self.define_setpre(outnotificationsswitchid=outnotificationsswitchid,outsoundalertswitchid=outsoundalertswitchid,
                           outnprestatus=outnprestatus,outsprestatus=outsprestatus)
        self.define_assertluoji(outnotificationsswitchid=outnotificationsswitchid,outsoundalertswitchid=outsoundalertswitchid,outclickselect=outclickselect)
        print("当Notifications和Sound Alert都关闭时，企图打开Sound Alert开关，Notifications与Sound Alert都关闭.---测试通过")


    def define_versionupdate(self,outversionid=None,outprelastversiontext=None,outtoastmessage=None):
        if outversionid==None:
            versionid = "com.ahdi.qrindo.merchant:id/tv_version_code"
        else:
            versionid = outversionid

        if outprelastversiontext==None:
            prelastversiontext = "V1.0.1"
        else:
            prelastversiontext = outprelastversiontext

        lastversiontext = self.baseframe.findbyresourceId_and_return_text(versionid)
        if lastversiontext==prelastversiontext:
            pretoastmessage = self.baseframe.findbyresourceId_and_click(versionid,outtoastmessage)
            self.assertEqual(outtoastmessage,pretoastmessage)
        else:
            self.assertFalse(True)

    # @unittest.skip('test_051')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_051(self):
        """
        最新版本号，点击版本号，toast提示为'It's the latest version'
        """
        versionid = "com.ahdi.qrindo.merchant:id/tv_version_code"
        prelastversiontext = "V1.0.1"
        toastmessage = "It's the latest version"

        self.define_versionupdate(outversionid=versionid,outprelastversiontext=prelastversiontext,outtoastmessage=toastmessage)
        print("最新版本号，点击版本号，toast提示'It's the latest version'.---测试通过")


















