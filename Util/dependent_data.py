#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import json

from jsonpath_rw import jsonpath,parse
from Base.runmethod import RunMethod
from Util.get_data import GetData
from Util.operation_excel import HandExcel


class DependentData():
    def __init__(self,case_id):
        self.case_id = case_id
        self.ope_excel = HandExcel()
        self.data = GetData()

    # 通过case_id去获取该case_id的整行数据
    def get_case_line_data(self):
        row_data = self.ope_excel.get_rows_value(self.case_id)
        return row_data

    #执行前置条件所依赖的case,获取结果集
    def run_dependent(self):
        run_method = RunMethod()
        row_num = self.ope_excel.get_rows_number(self.case_id)
        request_data = self.data.get_data_for_json(row_num)
        method = self.data.get_request_method(row_num)
        url = self.data.get_request_url(row_num)
        res = run_method.run_main(method,url,request_data)
        return json.loads(res)


    #根据依赖数据key，在前置条件所依赖的case结果集里匹配响应值，并返回响应值
    def get_data_for_key(self,row):
        depend_data = self.data.get_depend_key(row)
        response_data = self.run_dependent()
        json_exe = parse(depend_data)
        madle = json_exe.find(response_data)
        return [math.value for math in madle][0]






if __name__ == "__mian__":
    dep_data = DependentData()
    a = dep_data.run_dependent()
    print(a)

