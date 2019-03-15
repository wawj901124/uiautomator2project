import unittest

# 在jenkins运行时经常提示找不到包，所以就需要手动添加PYTHONPATH，通过追加sys.path列表来实现
import os
import sys

rootpath = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
syspath = sys.path
sys.path = []
sys.path.append(rootpath)  # 将工程根目录加入到python搜索路径中
sys.path.extend([rootpath + i for i in os.listdir(rootpath) if i[0] != "."])  # 将工程目录下的一级目录添加到python搜索路径中
sys.path.extend(syspath)
# 追加完成


import HTMLTestRunner #引入 HTMLTestRunner 包
from test import *
from test.alltest_list import caselist  #调用数组文件
from util.gettimestr import GetTimeStr
from util.send_attach_email import SendEmail


#将用例组件成数组
alltestnames = caselist()

suite=unittest.TestSuite()


for testpy in alltestnames:
    try:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName(testpy))    #默认加载所有用例
    except Exception:
        print('ERROR: Skipping tests from "%s".' % testpy)
        try:
            __import__(test)
        except ImportError:
            print('Could not import the "%s" test module.'% testpy)
        else:
            print('Could not load the "%s" test suite.' % testpy)
        from traceback import print_exc
        print_exc()
print('---------------------------')
stdout_backup = sys.stdout
gettime = GetTimeStr()
timestr = gettime.getTimeStr()
logpath = "../log/%s_message.txt" % timestr
print("Now all print info will be written to log文件：", logpath)
# define the log file that receives your log info
log_file = open(logpath, "w", encoding="utf-8")
# redirect print output to log file
sys.stdout = log_file
print('----------开始打印日志-----------------\n')
print('Running the tests...')
gettime = GetTimeStr()
filename ='../report/%s_report.html' % gettime.getTimeStr()
fp = open(filename, 'wb')

# 定义测试报告
runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'uiautomation2 python 自动化测试_测试报告',
    description=u'用例执行情况：')
runner.run(suite)
fp.close()

#发送report至邮箱
send_e = SendEmail()
send_e.send_main([1],[2],filename)

print('\n----------日志打印结束-----------------')
log_file.close()
# restore the output to initial pattern
sys.stdout = stdout_backup
print("Now this will be presented on screen")

# 发送log至邮箱
send_e = SendEmail()
send_e.send_main([1], [2], logpath)

