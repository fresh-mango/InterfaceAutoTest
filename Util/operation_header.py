#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import json
from Util.operation_json import OperationJson

file_path6 = 'D:/uatotest/Config/header.json'
file_path7 = 'D:/uatotest/Config/save.json'

headers ="""
Accept: text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Connection: keep-alive
Cookie: imooc_uuid=030f25b5-6c74-4f5a-93c1-dc371eb2f782; imooc_isnew_ct=1622561151; loginstate=1; apsid=NkNzgwZjc5YjE1NTRmODhiZGIxNTE0NzIyZWFjODcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANzQxMzc0MQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABtYW5nb2xvZ29AMTYzLmNvbQAAAAAAAAAAAAAAAAAAAGE4ZjY4OTUyZjg1ZTk3ZmFlNTE5OTQ3NGQ4NjdlM2Y3mlG2YAaY%2FV4%3DZG; last_login_username=mangologo%40163.com; imooc_isnew=2; IMCDNS=0; Hm_lvt_f0cfcccd7b1393990c78efdeebff3968=1622911505; couponHide=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%227413741%22%2C%22first_id%22%3A%22179c82e5e2b905-098a5736d3eb7d-f7f1939-921600-179c82e5e2c643%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_utm_source%22%3A%22bdpinpai%22%2C%22%24latest_utm_campaign%22%3A%22SEM%22%2C%22%24latest_utm_term%22%3A%22%E6%85%95%E8%AF%BE%E7%BD%91%22%7D%2C%22%24device_id%22%3A%22179c82e5e2b905-098a5736d3eb7d-f7f1939-921600-179c82e5e2c643%22%7D; Hm_lpvt_f0cfcccd7b1393990c78efdeebff3968=1622911602; cvde=60bbaa0f7d492-7
Host: www.imooc.com
Referer: https://www.imooc.com/
sec-ch-ua: " Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"
sec-ch-ua-mobile: ?0
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36
X-Requested-With: XMLHttpRequest"""


class Operation_Header():
    def __init__(self):
        self.header = OperationJson(file_path6)

    #通过配置文件获取header数据
    def get_header_data(self):
        data = self.header.read_data()
        return data

    #写header数据到配置文件json里
    def write_header_data(self,data):
        with open(file_path7, 'a') as fp:
            fp.write(json.dumps(data) + '\n')

    #执行请求时获取header
    def get_header_for_request(self,response):
        headers = response.header
        return headers


    #生成header
    def gen_headers(self, s):
        ls = s.split('\n')
        lsl = []
        ls = ls[1:-1]
        headers = {}
        for l in ls:
            l = l.split(': ')
            lsl.append(l)
        for x in lsl:
            headers[str(x[0]).strip('    ')] = x[1]
        return headers



if __name__ == "__main__":
    op_header = Operation_Header()
    data = op_header.get_header_data()
    print(data)
    print(type(data))


