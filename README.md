# InterfaceAutoTest
基于python开发的接口自动化测试框架，使用Excel来管理测试用例，共5个大模块，详情信息如下说明。
/Run:		Run_main.py,主程序运行文件
/Base:		runmethod.py,接口请求方式基类封装
/Case: 		存放、管理测试用例
/Config: 	server.ini,服务器节点信息配置、公共参数配置。其它json文件，为测试数据，可根据自己的项目需要自行修改、删除、添加。	
/Util: 		connect_db.py,数据库配置、执行sql语句模块。
			dependent_data.py，处理依赖接口关系模块。
			get_data.py，获取数据、处理数据模块。
			operation_cookie.py，管理cookie数据模块
			operation_excel.py，读取操作excel文件模块。
			operation_header.py，管理请求头信息模块。
			operation_init.py，管理数据初始化模块。
			operation_json.py，读取操作json文件模块。
			operation_result.py，断言文件模块。
			send_email.py，邮件管理、测试统计结果模块
