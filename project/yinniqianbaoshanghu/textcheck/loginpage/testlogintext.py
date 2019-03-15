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

    #页面元素检查
    def defineloginpage(self,outtestcasediscription=None,outprepagetext=None):
        if outprepagetext==None:
            prepagetext = 'Log in'
        else:
            prepagetext = outprepagetext

        if outtestcasediscription==None:
            testcasediscription = '测试用例'
        else:
            testcasediscription = outtestcasediscription

        preele = self.baseframe.findbytext(prepagetext)  # 确认有显示文字“QRindo-Merchant”
        self.assertTrue(preele)
        print("%s_%s.---测试通过" %(testcasediscription,prepagetext))


    @staticmethod    #根据不同的参数生成测试用例
    def getTestFunc(outtestcasediscription,outprepagetext):
        def func(self):
            self.defineloginpage(outtestcasediscription,outprepagetext)
        return func

def __generateTestCases_loginpage():
    file_name = "D:/Users/Administrator/PycharmProjects/uiautomator2project/dataconfig/autologin.xls"
    sheet_id = 0
    datasheet = GetData(file_name,sheet_id)   #实例化
    rows_count = datasheet.get_case_lines()   #获取表的行数
    for i in range(37, rows_count):  # 循环，但去掉第一
        args = []
        args.append(datasheet.get_case_title_content(i))
        args.append(datasheet.get_pre_text_content(i))
        setattr(TestLogin, 'test_func_%s_%s_%s' % (datasheet.get_case_id_content(i),args[0],args[1]),
                TestLogin.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头

__generateTestCases_loginpage()

if __name__ == '__main__':
    print("hello world")
    unittest.main()










