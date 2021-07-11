#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests
import json

class RunMethod():
    def post_main(self,url,data,header=None):
        res=None
        if header != None:
            res = requests.post(url=url,data=data,headers=header,verify=False).json()
        else:
            res = requests.post(url=url,data=data,,verify=False)).json()
        return res


    def get_main(self,url,data=None,header=None):
        res = None
        if header != None:
            res = requests.get(url=url, data=data, headers=header,verify=False)).json()
        else:
            res = requests.get(url=url, data=data,verify=False)).json()
        return res


    def run_main(self,method,url,data=None,header=None):
        res = None
        if method == 'post':
            res = self.post_main(url,data,header))
        else:
            res = self.get_main(url,data,header))
        return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)

if __name__ == "__main__":
    method='get'
    url='http://class.imooc.com/api/scinfo'
    data= {"app":{"htts_data":"1507790990186"},"web":{"timestamp":"1507989375749","uid":"5249191"}}
    data = json.dumps(data)

    rm = RunMethod()
    data= rm.run_main(method=method,url=url,data=data)
    print(data)

