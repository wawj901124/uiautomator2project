# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/7/13 17:26'

class GlobalVar:
    def __init__(self):
        #用例数据
        self.case_id = '0'
        self.case_title = '1'
        self.account_input = '2'
        self.password_input = '3'
        self.pre_text = '4'
        self.pre_toast = '5'
        self.pre_back_text = '6'
        self.test_result = '7'
        self.test_description = '8'


    #获取case_id列数
    def get_case_id(self):
        return self.case_id

    #获取case_title列数
    def get_case_title(self):
        return self.case_title

    #获取account_input列数
    def get_account_input(self):
        return self.account_input

    #获取password_input列数
    def get_password_input(self):
        return self.password_input

    #获取pre_text列数
    def get_pre_text(self):
        return self.pre_text

    #获取pre_toast列数
    def get_pre_toast(self):
        return self.pre_toast

    #获取pre_back_text列数
    def get_pre_back_text(self):
        return self.pre_back_text

    #获取test_result列数
    def get_test_result(self):
        return self.test_result

    #获取test_description列数
    def get_test_description(self):
        return self.test_description
