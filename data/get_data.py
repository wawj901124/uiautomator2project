# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/7/13 17:48'

from util.operation_excel import OperationExcel   #导入OperationExcel
from data.data_config import *      #导入


class GetData:
    def __init__(self,file_name=None,sheet_id=None):
        self.file_name = file_name
        self.sheet_id = sheet_id
        self.opera_excel = OperationExcel(self.file_name,self.sheet_id)   #实例化

    #去获取excel行数，就是我们的case个数
    def get_case_lines(self):
        return self.opera_excel.get_lines()

    # 获取brandname
    def get_brandname(self,row):
        col = int(get_brandname())  #获取brandname所在的列数
        brandname = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return brandname

    #获取email
    def get_email(self,row):
        col = int(get_email())  #获取email所在的列数
        email = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return email

    #获取contactnumber
    def get_contactnumber(self,row):
        col = int(get_contactnumber())  #获取contactnumber所在的列数
        contactnumber = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return contactnumber

    #获取merchanttype
    def get_merchanttype(self,row):
        col = int(get_merchanttype())  #获取merchanttype所在的列数
        merchanttype = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return merchanttype

    #获取category
    def get_category(self,row):
        col = int(get_category())  #获取category所在的列数
        category = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return category

    #获取criteria
    def get_criteria(self,row):
        col = int(get_criteria())  #获取criteria所在的列数
        criteria = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return criteria

    #获取siup
    def get_siup(self,row):
        col = int(get_siup())  #获取siup所在的列数
        siup = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return siup

    #获取province
    def get_province(self,row):
        col = int(get_province())  #获取province所在的列数
        province = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return province

    #获取city
    def get_city(self,row):
        col = int(get_city())  #获取city所在的列数
        city = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return city

    #获取district
    def get_district(self,row):
        col = int(get_district())  #获取district所在的列数
        district = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return district

    #获取village
    def get_village(self,row):
        col = int(get_village())  #获取village所在的列数
        village = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return village

    #获取postcode
    def get_postcode(self,row):
        col = int(get_postcode())  #获取postcode所在的列数
        postcode = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return postcode

    #获取address
    def get_address(self,row):
        col = int(get_address())  #获取address所在的列数
        address = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return address

    #获取company
    def get_company(self,row):
        col = int(get_company())  #获取company所在的列数
        company = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return company

    #获取npwptaxid
    def get_npwptaxid(self,row):
        col = int(get_npwptaxid())  #获取npwptaxid所在的列数
        npwptaxid = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return npwptaxid

    #获取officialwebsite
    def get_officialwebsite(self,row):
        col = int(get_officialwebsite())  #获取officialwebsite所在的列数
        officialwebsite = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return officialwebsite

    #获取photosiup
    def get_photosiup(self,row):
        col = int(get_photosiup())  #获取photosiup所在的列数
        photosiup = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return photosiup

    #获取photonpwpcompany
    def get_photonpwpcompany(self,row):
        col = int(get_photonpwpcompany())  #获取photonpwpcompany所在的列数
        photonpwpcompany = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return photonpwpcompany

    #获取phototdp
    def get_phototdp(self,row):
        col = int(get_phototdp())  #获取phototdp所在的列数
        phototdp = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return phototdp

    #获取name
    def get_name(self,row):
        col = int(get_name())  #获取name所在的列数
        name = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return name

    #获取typeid
    def get_typeid(self,row):
        col = int(get_typeid())  #获取typeid所在的列数
        typeid = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return typeid

    #获取identitynumber
    def get_identitynumber(self,row):
        col = int(get_identitynumber())  #获取identitynumber所在的列数
        identitynumber = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return identitynumber

    #获取npwp
    def get_npwp(self,row):
        col = int(get_npwp())  #获取npwp所在的列数
        npwp = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return npwp

    #获取addresstwo
    def get_addresstwo(self,row):
        col = int(get_addresstwo())  #获取addresstwo所在的列数
        addresstwo = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return addresstwo

    #获取nationality
    def get_nationality(self,row):
        col = int(get_nationality())  #获取nationality所在的列数
        nationality = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return nationality

    #获取position
    def get_position(self,row):
        col = int(get_position())  #获取position所在的列数
        position = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return position

    #获取phone
    def get_phone(self,row):
        col = int(get_phone())  #获取phone所在的列数
        phone = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return phone

    #获取emailtwo
    def get_emailtwo(self,row):
        col = int(get_emailtwo())  #获取emailtwo所在的列数
        emailtwo = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return emailtwo

    #获取photofullfacebust
    def get_photofullfacebust(self,row):
        col = int(get_photofullfacebust())  #获取photofullfacebust所在的列数
        photofullfacebust = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return photofullfacebust

    #获取locationphoto
    def get_locationphoto(self,row):
        col = int(get_locationphoto())  #获取locationphoto所在的列数
        locationphoto = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return locationphoto

    #获取photoofthecashiersdesk
    def get_photoofthecashiersdesk(self,row):
        col = int(get_photoofthecashiersdesk())  #获取photoofthecashiersdesk所在的列数
        photoofthecashiersdesk = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return photoofthecashiersdesk

    #获取otherphoto
    def get_otherphoto(self,row):
        col = int(get_otherphoto())  #获取otherphoto所在的列数
        otherphoto = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return otherphoto

    #获取bank
    def get_bank(self,row):
        col = int(get_bank())  #获取bank所在的列数
        bank = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return bank

    #获取accountname
    def get_accountname(self,row):
        col = int(get_accountname())  #获取accountname所在的列数
        accountname = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return accountname

    #获取accountnumber
    def get_accountnumber(self,row):
        col = int(get_accountnumber())  #获取accountnumber所在的列数
        accountnumber = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return accountnumber

    #获取qrindoamount
    def get_qrindoamount(self,row):
        col = int(get_qrindoamount())  #获取accountnumber所在的列数
        qrindoamount = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return qrindoamount


if __name__ == '__main__':
    getdata = GetData()   #实例化
    print('---------------------------')
    rows_count = getdata.get_case_lines()
    for i in range(1, rows_count):  # 循环，但去掉第一个
        category = getdata.get_category(i)
        print(category)



