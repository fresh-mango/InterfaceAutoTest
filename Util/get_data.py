#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from Util.operation_init  import HandleInit
from Util.operation_json import OperationJson
from Util.operation_excel import HandExcel

class GetData():
    def __init__(self):
        self.ope_excel = HandExcel()
        self.hand_init = HandleInit()


    #获取excel行数，暨case个数
    def get_case_lines(self):
        return self.ope_excel.get_rows()


    #判断是否执行
    def get_is_run(self,row):
        flag = None
        col = self.hand_init.get_run()
        run_model = self.ope_excel.get_cell_value(row,col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag


    #判断前置条件是否有case依赖
    def is_depend(self,row):
        col = self.hand_init.get_pre_condition()
        depend_case_id = self.ope_excel.get_cell_value(row,col)
        if depend_case_id == "":
            return None
        else:
            return depend_case_id


    #获取依赖数据的key
    def get_depend_key(self,row):
        col = self.hand_init.get_data_depend()
        depend_key = self.ope_excel.get_cell_value(row,col)
        if depend_key == "":
            return None
        else:
            return depend_key


    #获取数据依赖字段
    def get_depend_field(self,row):
        col = self.hand_init.get_field_depend()
        field_data = self.ope_excel.get_cell_value(row,col)
        if field_data == "":
            return None
        else:
            return field_data


    #获取url
    def get_request_url(self,row):
        col = self.hand_init.get_url()
        url = self.ope_excel.get_cell_value(row,col)
        return url


    #获取请求方式
    def get_request_method(self,row):
        col = self.hand_init.get_request_way()
        request_method = self.ope_excel.get_cell_value(row,col)
        return request_method


    #获取请求数据的关键字key
    def get_request_data(self,row):
        col = self.hand_init.get_reque_data()
        request_key = self.ope_excel.get_cell_value(row,col)
        if request_key == "":
            return None
        else:
            return  request_key


    #通过获取关键字key拿到请求数据
    def get_data_for_json(self,row):
        operate_josn = OperationJson()
        request_data = operate_josn.get_data(self.get_request_data(row))
        return request_data


    #是否写入cookie
    def get_operate_cookie(self,row):
        col = self.hand_init.get_ope_cookie()
        operate_cookie = self.ope_excel.get_cell_value(row,col)
        if operate_cookie != "":
            return operate_cookie
        else:
            return None


    #是否携带header
    def get_operate_header(self,row):
        col = self.hand_init.get_ope_header()
        operate_header = self.ope_excel.get_cell_value(row,col)
        if operate_header != "":
            return operate_header
        else:
            return None


    #获取预期结果
    def get_expect_result(self,row):
        col = self.hand_init.get_expe_result()
        expect_result = self.ope_excel.get_cell_value(row,col)
        if expect_result == "":
            return None
        else:
            return expect_result



    #写日志数据
    def write_result(self,row,value):
        col = self.hand_init.get_daily_data()
        self.ope_excel.excel_write_data(row,col,value)










if __name__ == "__main__":
    get_data = GetData()
    print(get_data.get_request_url(6))