#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import operator
from Util.operation_json import OperationJson
from deepdiff import DeepDiff


file_path6 = 'D:/uatotest/Config/code_message.json'


class Operation_Result():

    def __init__(self):
        self.op_result = OperationJson(file_path6)
        self.data = self.read_result()



    #读取result文件
    def read_result(self):
        data = self.op_result.read_data()
        return data


    #根据关键字获取预期结果json数据
    def get_key_result(self,key=None):
        data = self.op_result.get_data(key)
        new_data = {k: v for i in data for (k, v) in i.items()}
        return new_data

    #获取预期结果--文本信息
    def get_result_desc(self,url_key,desc):
        data = self.op_result.get_data(url_key)
        if data != None:
            for i in data:
                message = i.get(desc)
                if message:
                    return message
        return None


    #获取预期结果--json数据
    def get_result_json(self,url_key,status):
        data = self.op_result.get_data(url_key)
        if data != None:
            for i in data:
                message = i.get(status)
                if message:
                    return message
        return None



    #判断两个字典是否相等
    def operation_result_json(self,dict1, dict2):
        if isinstance(dict1, dict) and isinstance(dict2, dict):
            cmp_dict = DeepDiff(dict1, dict2, ignore_order=True).to_dict()
            if cmp_dict.get("dictionary_item_added"):
                return False
            else:
                return True
        return False




    #判断一个字符串是否包含在另外一个字符串
    def is_contain(self,str_one,str_two):
        flag = None
        if operator.contains(str_one,str_two):
            flag = True
        else:
            flag = False
        return flag




if __name__ == "__main__":

    dict1 = [{"aaa": "AAA", "ccc": "BBBB", "bbb": "A1A", "CC": [{"11": "22"}, {"11": "44"}]}]
    dict2 = [{"aaa": "AAA", "ccc": "BBBB", "bbb": "A1A", "CC": [{"11": "22"}, {"11": "44"}]}]

    op_result = Operation_Result()
    data = op_result.read_result()
    print(data)
    print(type(data))



