#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import requests
import json
from Util.operation_json import OperationJson

file_path4= 'D:/uatotest/Config/cookie.json'
file_path5 = 'D:/Uatotest/Config/save.json'

class Operation_Cookie():
    def __init__(self,file_path=None):
        #self.response = json.loads(response)
        self.op_json = OperationJson(file_path4)


    #通过登录获取cookie
    def get_cookie_for_login(self):
        url = 'http://www.baidu.com'
        headers = {"Accept": "application/json, text/javascript, */*; q=0.01"}
        body = { "username": "liuzz05@****.com","password": "123456"}
        try:
            #res = requests.post(url=url, headers=headers, data=body)
            res = requests.get(url)
            cookies = res.headers
            cookie = requests.utils.dict_from_cookiejar(cookies)
            return cookie
        except Exception as err:
            print('获取cookie失败：\n{0}'.format(err))

    #执行请求时获取cookie
    def get_cookie_for_request(self,response):
        cookies = response.cookies
        cookie = requests.utils.dict_from_cookiejar(cookies)
        return cookie


    #通过配置文件获取cookie数据
    def read_cookie_data(self):
        data = self.op_json.read_data()
        return data



    #根据关键字key获取配置文件里的cookie数据
    def get_cookie_value(self,key=None):
        return self.op_json.get_data(key)



     #写cookie数据到配置文件json里
    def write_cookie_data(self, data):
        with open(file_path5, 'a') as fp:
            fp.write(json.dumps(data) + '\n')



    # 将登录时获取到的cookie数据写入配置文件里
    def write_cookie_data_login(self):
        self.write_cookie_data(self.get_cookie_for_login())



if __name__ == "__main__":
    opjson = Operation_Cookie()
    data =opjson.get_cookie_for_login()
    print(type(data))
    print(data)


