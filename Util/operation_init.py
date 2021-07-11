#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import sys
import os
import configparser
base_path = os.getcwd()
sys.path.append(base_path)
file_path1 = "D:/Uatotest/Config/server.ini"

class HandleInit():

    def load_ini(self):
        file_path = file_path1
        cf = configparser.ConfigParser()
        cf.read(file_path, encoding="utf-8-sig")
        return cf


    #获取ini里面的value
    def get_value(self, key, node=None):
        if node == None:
            node = 'server'
        cf = self.load_ini()
        try:
            data = cf.get(node, key)
        except Exception:
            print("没有获取到值")
            data = None
        return data

    #获取case_id
    def get_case_id(self):
        return int(self.get_value('case_id'))

    #获取是否执行
    def get_run(self):
        return int(self.get_value('is_run'))

    #获取前置条件
    def get_pre_condition(self):
        return int(self.get_value('pre_condition'))

    #获取依赖数据
    def get_data_depend(self):
        return int(self.get_value('data_depend'))

    #获取数据依赖字段
    def get_field_depend(self):
        return int(self.get_value('field_depend'))

    #获取url
    def get_url(self):
        return int(self.get_value('url'))

    #获取请求方式
    def get_request_way(self):
        return int(self.get_value('request_way'))

    #获取请求数据
    def get_reque_data(self):
        return int(self.get_value('request_data'))

    #获取cookie操作
    def get_ope_cookie(self):
        return int(self.get_value('operate_cookie'))

    #获取header操作
    def get_ope_header(self):
        return int(self.get_value('operate_header'))

    #获取预期结果方式
    def get_expect_method(self):
        return int(self.get_value('expect_method'))

    #获取预期结果
    def get_expect_result(self):
        return int(self.get_value('expect_result'))

    #获取实际结果
    def get_actual_result(self):
        return int(self.get_value('actual_result'))

    #获取日志数据
    def get_daily_data(self):
        return int(self.get_value('daily_data'))



if __name__ == "__main__":
    hi = HandleInit()
    data = hi.get_actual_result()

    print(type(data))
    print(data)


