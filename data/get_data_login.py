# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/7/13 17:48'

from util.operation_excel import OperationExcel   #导入OperationExcel
from data.data_config_login import *      #导入


class GetData:
    def __init__(self,file_name=None,sheet_id=None):
        self.file_name = file_name
        self.sheet_id = sheet_id
        self.opera_excel = OperationExcel(self.file_name,self.sheet_id)   #实例化
        self.global_var = GlobalVar()   #实例化

    #去获取excel行数，就是我们的case个数
    def get_case_lines(self):
        return self.opera_excel.get_lines()

    # 获取case_id单元格内的内容
    def get_case_id_content(self,row):
        col = int(self.global_var.case_id)  #获取case_id所在的列数
        case_id_content = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        if case_id_content == '':
            return None
        else:
            return case_id_content

    #获取case_title单元格内的内容
    def get_case_title_content(self,row):
        col = int(self.global_var.case_title)  #获取case_title所在的列数
        case_title_content = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        if case_title_content == '':
            return None
        else:
            return case_title_content

    #获取account_input单元格内的内容
    def get_account_input_content(self,row):
        col = int(self.global_var.account_input)  #获取account_input所在的列数
        account_input_content = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        if account_input_content == '':
            return None
        else:
            return account_input_content

    #获取password_input单元格内的内容
    def get_password_input_content(self,row):
        col = int(self.global_var.password_input)  #获取password_input所在的列数
        password_input_content = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        if password_input_content == '':
            return None
        else:
            return password_input_content

    #获取pre_text单元格内的内容
    def get_pre_text_content(self,row):
        col = int(self.global_var.pre_text)  #获取pre_text所在的列数
        pre_text_content = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        if pre_text_content == '':
            return None
        else:
            return pre_text_content

    #获取pre_toast单元格内的内容
    def get_pre_toast_content(self,row):
        col = int(self.global_var.pre_toast)  #获取pre_toast所在的列数
        pre_toast_content = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        if pre_toast_content == '':
            return None
        else:
            return pre_toast_content

    #获取pre_back_text单元格内的内容
    def get_pre_back_text_content(self,row):
        col = int(self.global_var.pre_back_text)  #获取pre_back_text所在的列数
        pre_back_text_content = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        if pre_back_text_content == '':
            return None
        else:
            return pre_back_text_content


    #写入test_result
    def write_test_result(self,row,value):
        col = int(self.global_var.test_result)  #获取test_result所在的列数
        self.opera_excel.write_value(row,col,value)   #向指定的单元格写入内容

    #写入test_description
    def write_test_description(self,row,value):
        col = int(self.global_var.test_description)  #获取test_description所在的列数
        self.opera_excel.write_value(row,col,value)   #向指定的单元格写入内容


if __name__ == '__main__':

    getdata = GetData()   #实例化
    print('---------------------------')
    rows_count = getdata.get_case_lines()
    for i in range(1, rows_count):  # 循环，但去掉第一个
        url = getdata.get_case_id_content(i)
        print(url)