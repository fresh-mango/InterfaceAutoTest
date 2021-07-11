#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import sys
import os
import requests
import json
import operator

base_path = os.getcwd()
sys.path.append(base_path)
from deepdiff import DeepDiff
from Base.runmethod import RunMethod
from Util.operation_excel import HandExcel
from Util.operation_init import HandleInit
from Util.get_data import GetData
from Util.dependent_data import DependentData
from Util.operation_cookie import Operation_Cookie
from Util.operation_header import Operation_Header
from Util.operation_result import Operation_Result
from Util.operation_json import OperationJson
from Util.send_email import SendEmail
from Util.connect_db import OperationMysql

class RunMain():
    def __init__(self):
        self.run = RunMethod()
        self.excel = HandExcel()
        self.hi = HandleInit()
        self.data = GetData()
        self.cookie = Operation_Cookie()
        self.header = Operation_Header()
        self.result = Operation_Result()
        #self.mysql = OperationMysql()
        self.email = SendEmail()



    def run_case(self):
        pass_count = []
        fail_count = []
        leavel = []
        pass_caseid = []
        fail_caseid = []
        rows = self.excel.get_rows()

        for i in range(rows):
            print('当前正在执行第%d次遍历'%(i+1))
            if i==rows:
                print('遍历结束')
            data = self.excel.get_rows_value(i+2)
            is_run = data[2]
            if is_run =='yes':
                case_id = data[0]
                is_depend = data[3]
                depend_data = data[4]
                depend_key = data[5]
                url = data[6]
                method = data[7]
                request_data_key = data[8]
                request_data = self.excel.get_data_for_json(i + 1)
                cookie_method = data[9]
                is_header = data[10]
                expect_method = data[11]
                expect_result = data[12]
                actual_result = data[13]
                daily_data = data[14]



                if is_depend:
                    self.dependt_data = DependentData(is_depend)
                    depend_response_data = self.dependt_data.get_data_for_key(i)
                    depent_key = self.data.get_depend_field(i)
                    request_data[depent_key] = depend_response_data

                elif cookie_method == 'yes':
                    cookie_data = self.cookie.read_cookie_data()
                    response = self.run.run_main(method,url,request_data,cookie_data)

                elif cookie_method == 'write':
                    response = self.run.run_main(method,url,request_data)
                    #cookies = response.cookies
                    #cookie = requests.utils.dict_from_cookiejar(cookies)
                    cookie = self.cookie.get_cookie_for_request(response)
                    self.cookie.write_cookie_data(cookie)

                elif is_header =='yes':
                    header= self.header.get_header_data()
                    self.run.run_main(method,url,request_data,header)

                elif is_header == 'write':
                    response = self.run.run_main(method,url,request_data)
                    headers =self.header.get_header_for_request(response)
                    self.header.write_header_data(headers)

                else:
                    response = self.run.run_main(method,url,request_data)


                res = json.loads(response)
                desc = res['errorDesc']
                code = res['errorCode']



                if expect_method =='message':
                    data = self.excel.split_data_two(expect_result)
                    url_key = data[0]
                    exp_data= data[1]
                    expect_data = self.result.get_result_desc(url_key,exp_data)

                    if expect_data == desc:
                        self.excel.excel_write_data(i + 2, 14, '通过')
                        pass_count.append(i)
                        pass_caseid.append(case_id)
                    else:
                        self.excel.excel_write_data(i + 2, 14, '失败')
                        self.excel.excel_write_data(i + 2, 15, json.dumps(res))
                        fail_count.append(i)
                        fail_caseid.append(case_id)


                if expect_method =='status_code':
                    if int(expect_result) ==code:
                        self.excel.excel_write_data(i + 2, 14, '通过')
                        pass_count.append(i)
                        pass_caseid.append(case_id)
                    else:
                        self.excel.excel_write_data(i + 2, 14, '失败')
                        self.excel.excel_write_data(i + 2, 15, json.dumps(res))
                        fail_count.append(i)
                        fail_caseid.append(case_id)


                if expect_method =='json':

                    except_result_data = self.result.get_key_result(expect_result)
                    result = self.result.operation_result_json(except_result_data,res)
                    if result:
                        self.excel.excel_write_data(i+2,14,'通过')
                        pass_count.append(i)
                        pass_caseid.append(case_id)
                    else:
                        self.excel.excel_write_data(i+2,14,'失败')
                        self.excel.excel_write_data(i+2,15, json.dumps(res))
                        fail_count.append(i)
                        fail_caseid.append(case_id)

        self.email.send_main(pass_count,fail_count,pass_caseid,fail_caseid)


if __name__ == "__main__":
    run=RunMain()
    run.run_case()



