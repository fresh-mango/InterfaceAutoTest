#!/usr/bin/env python
# -*- encoding: utf-8 -*-

file_path2 = 'D:/uatotest/Config/request.json'
file_path3 = 'D:/Uatotest/Config/save.json'

import json
class OperationJson():
    def __init__(self,file_path=None):
        if file_path==None:
            self.file_path = file_path2
        else:
            self.file_path = file_path
        self.data = self.read_data()

    #读取json文件
    def read_data(self):
        with open(self.file_path,encoding='utf-8-sig',errors='ignore') as fp:
            data= json.load(fp,strict=False)
            #data = fp.readline()
            return data


    #根据关键字获取数据
    def get_data(self,key=None):
        if key:
            return self.data[key]
        else:
            return self.data



    #写json数据
    def write_data(self,data):
        with open(file_path3,'a') as fp:
            fp.write(json.dumps(data)+'\n')





if __name__ == "__main__":
    opjson = OperationJson()
    data = opjson.get_data('order_list')
    print(type(data))
    print(data)

