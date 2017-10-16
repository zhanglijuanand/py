#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：2017/7/18
#模块描述：资源账号管理
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("/testIsomp/common")
from _icommon import commonFun,frameElement
from _log import log
sys.path.append("/testIsomp/testCase/role/")
from test_role import testRole
sys.path.append("/testIsomp/webElement/role/")
from test_roledf import Role
sys.path.append("/testIsomp/webElement/resource/")
from test_resource_accountmgr_ment import Accountmgr
from test_linux_ment import LinuxResource
sys.path.append("/testIsomp/testData/")
from _testDataPath import dataFileName

class testResourceAccount(object):

	def __init__(self, driver):
		self.driver = driver
		self.log = log()
		self.cmf = commonFun(driver)
		self.frameElem = frameElement(driver)
		self.testrole = testRole(driver)
		self.linux = LinuxResource(driver)
		self.account = Accountmgr(driver)
		self.role = Role(driver)
		self.data = dataFileName()

	u'''添加和编辑资源账号'''
	def add_edit_resource_account_001(self, dataPath, sheetName):

		#日志开始记录
		self.log.log_start("add_edit_resource_account")
		#获取添加资源账号测试数据
		accountData = self.data.get_data(dataPath, sheetName)
		#保存成功的弹出框
		accountMsg = self.testrole.popup()

		#无检查点的测试项标识，如果为True说明通过
		flag = False

		for dataRow in range(len(accountData)):
			data = accountData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					#点击账号管理
					if dataRow == 1:
						self.account.click_account_manage_button(data[2])
					self.linux.add_edit_resource_account(data[3], data[4], data[5], data[6], data[7])
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", accountMsg, data, flag)
					self.cmf.back()
			except Exception as e:
				print ("add_edit_resource_account fail:" + str(e))
		self.cmf.back()

		self.log.log_end("add_edit_resource_account")

	u'''查询资源账号'''
	def query_resource_account_002(self, dataPath, sheetName):

		#日志开始记录
		self.log.log_start("query_resource_account")
		#获取查询资源账号测试数据
		accountData = self.data.get_data(dataPath, sheetName)

		for dataRow in range(len(accountData)):
			data = accountData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					if dataRow == 1:
						self.account.click_account_manage_button(data[1])
						self.account.query_name(data[2])
					if dataRow == 2 or dataRow == 3:
						self.account.is_authorize(data[3])
					if dataRow == 4:
						self.account.query_name(data[2])
						self.account.is_authorize(data[3])
					self.account.click_account_query()
					self.role.click_reset()
					self.log.log_detail(data[0], True)
			except Exception as e:
				print ("query_resource_account fail:" + str(e))
		self.cmf.back()

		self.log.log_end("query_resource_account")

	u'''检验资源账号'''
	def check_resource_account_003(self, dataPath, sheetName):

		#日志开始记录
		self.log.log_start("check_resource_account")
		#获取检验资源测试数据
		resourceData = self.data.get_data(dataPath, sheetName)
		#保存成功的弹出框
		resourceMsg = self.testrole.popup()

		#无检查点的测试项标识，如果为True说明通过
		flag = False

		for dataRow in range(len(resourceData)):
			data = resourceData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					if dataRow == 1:
						self.account.click_account_manage_button(data[2])
						self.account.click_account_add_edit_button()
					self.linux.check_resource_account(data[3], data[4], data[5], data[6])
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", resourceMsg, data, flag)
			except Exception as e:
				print ("check_resource_account fail:" + str(e))

		self.cmf.back()

		self.cmf.back()

		self.log.log_end("check_resource_account")

	u'''删除资源账号'''
	def del_resource_account_004(self, dataPath, sheetName):

		#日志开始记录
		self.log.log_start("del_resource_account")
		#获取删除资源账号测试数据
		accountData = self.data.get_data(dataPath, sheetName)
		#保存成功的弹出框
		accountMsg = self.testrole.popup()

		#无检查点的测试项标识，如果为True说明通过
		flag = False

		for dataRow in range(len(accountData)):
			data = accountData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.account.click_account_manage_button(data[2])
					self.account.click_account_del(data[3])
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", accountMsg, data, flag)
					self.cmf.click_msg_button(1)
			except Exception as e:
				print ("del_resource_account fail:" + str(e))
		self.cmf.back()
		self.log.log_end("del_resource_account")

	u'''全选删除资源账号'''
	def bulkdel_resource_account_005(self, dataPath, sheetName):

		#日志开始记录
		self.log.log_start("bulkdel_resource_account")
		#获取全选删除资源账号测试数据
		accountData = self.data.get_data(dataPath, sheetName)
		#保存成功的弹出框
		accountMsg = self.testrole.popup()

		#无检查点的测试项标识，如果为True说明通过
		flag = False

		for dataRow in range(len(accountData)):
			data = accountData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.account.click_account_manage_button(data[2])
					self.cmf.check_all()
					self.cmf.bulkdel("delete_account")
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", accountMsg, data, flag)
					self.cmf.click_msg_button(1)
			except Exception as e:
				print ("bulkdel_resource_account failure:" + str(e))
		self.cmf.back()

		self.log.log_end("bulkdel_resource_account")

