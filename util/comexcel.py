#-*- coding: utf-8 -*-

#比对两个Excel文件内容的差异
#---------------------假设条件----------------
#1、源表和目标表格式一致
#2、不存在合并单元格
#3、第2行开始比对
#---------------------------------------------

import xlrd
import xlwt
import os
import time  # 引入time模块

#往日志文件中追加内容函数
def writeappend_logfile(filename,content):
    file=open(filename,'a',encoding="utf-8") #以追加方式打开日志文件
    time_now= time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  #系统时间格式化
    file.writelines(time_now+':'+content+'\n')      #写入内容
    file.close() #关闭文件

def read_excel(ori_path,tar_path,sub_name):#
    success=0        #匹配一致数量
    fail=0           #匹配不一致数量
    origin_xls={} #存储源xls文件
    target_xls={} #比对的xls文件
    wb_ori=xlrd.open_workbook(ori_path) #打开原始文件
    wb_tar=xlrd.open_workbook(tar_path) #打开目标文件
    sheet_num = len(wb_ori.sheets()) #源表子表数量
##    for sheet_i in range(sheet_num):  #excel中子页面数量
##        sheet_ori=wb_ori.sheet_by_index(sheet_i) #通过索引值获取源表名
##        sheet_tar=wb_tar.sheet_by_index(sheet_i) #通过索引值获取源表名

    startime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())    #获取系统当前时间并格式化为格式
    print (startime,' 开始比对...')
    logname='log_'+startime[0:10]+'.log'               #截取日期年月日构成日志文件名

    logfile=open(logname,'w',encoding="utf-8")    #创建日志文件,如果文件存在则清空内容，不存在则创建，如果需要同时批量比对多张表，可以考虑将日志文件名作为参数传入
    logfile.writelines(startime+':【开始比对】...'+'\n')       #写入开始时间
    logfile.close()            #关闭日志文件

    try:
        sheet_ori=wb_ori.sheet_by_name(sub_name)
        sheet_tar=wb_tar.sheet_by_name(sub_name)
        if sheet_ori.name==sheet_tar.name:
            #sheet表名
            if sheet_ori.name==sub_name:
            #先将数存入dictionary中dictionary(rows:list)
            #第一行存储表头
            #源表取一行数据与目标表全表进行比对如果表中存在主键可以用主键进行索引
            #数据从excel第3行开始
                for rows in range(1,sheet_ori.nrows):
                    orign_list=sheet_ori.row_values(rows) #源表i行数据
                    target_list=sheet_tar.row_values(rows) #目标表i行数据
                    origin_xls[rows]=orign_list     #源表写入字典
                    target_xls[rows]=target_list    #目标表写入字典

                if origin_xls[1]  == target_xls[1]:
                    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+' 表头一致')
                for ori_num in origin_xls:
                    flag='false'          #判断是否一致标志
                    for tar_num in target_xls:
                        if origin_xls[ori_num]==target_xls[tar_num]:
                            flag='true'
                            break              #如果匹配到结果退出循环
                    if flag=='true':           #匹配上结果输出后台日志
                        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+' row:%d is ok'%ori_num)
                        success+=1
                    else:                      #匹配不上将源表中行记录写入txt
                        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+' row:%d is different'%ori_num)
                        fail+=1
                        data=origin_xls[ori_num]
                        logstr='【不一致】row<'+str(ori_num)+'>:'+str(data)
                        writeappend_logfile(logname,logstr)
               # logstr='【比对完成】总记录数:'+str(ori_num)+'条,一致:'+str(success)+'条,不一致:'+str(fail)+'条'
                logstr='【比对完成】总记录数:{:d}条,一致:{:d}条,不一致:{:d}条'.format(ori_num,success,fail)
                print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+' 【%s】比对结束'%sheet_ori.name)
                print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+' 总记录数:%d条,一致:%d条,不一致:%d条'%(ori_num,success,fail))
                writeappend_logfile(logname,logstr)

        else:
            errmsg='【'+sub_name+'】子表名不一致'
            writeappend_logfile(logname,errmsg)
    except Exception as err:
       writeappend_logfile(logname,str(err)) #输出异常

def main():
    pass

if __name__ == '__main__':
    # read_excel(r'D:\\Users\\Administrator\\PycharmProjects\\uiautomator2project\\dataconfig\\merchantcontent.xls','D:\\Users\\Administrator\\PycharmProjects\\uiautomator2project\\dataconfig\\autologin.xls','Sheet1')
    read_excel(r'D:\\Users\\Administrator\\PycharmProjects\\uiautomator2project\\dataconfig\\autologin.xls', r'D:\\Users\\Administrator\\PycharmProjects\\uiautomator2project\\dataconfig\\merchantcontent.xls','Sheet1')