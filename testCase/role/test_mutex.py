#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：2017/7/3
#模块描述：
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
sys.path.append("/testIsomp/testCase/role/")
from test_role import  testRole
sys.path.append("/testIsomp/log/")
from _log import log
sys.path.append("/testIsomp/webElement/role/")
from test_role_mutex import roleMutex

class testMutex(object):

	def __init__(self, driver):
		self.driver = driver
		self.log = log()
		self.rolemutex = roleMutex(driver)
		self.role = testRole(driver)
		self.cmf = commonFun(driver)
		self.frameElem = frameElement(driver)

	u'''添加互斥角色'''
	def add_mutex_role_001(self):

		#日志开始记录
		self.log.log_start("addmutexrole")
		#获取添加互斥角色测试数据
		rolemutexData = self.role.get_table_data("role_mutex_add")
		#保存成功的弹出框
		roleMsg = self.role.popup()
		#无检查点的测试项标识，如果为True说明通过
		flag = False

		for dataRow in range(len(rolemutexData)):
			data = rolemutexData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.rolemutex.click_add_mutex()
					self.rolemutex.select_role(int(data[2]), dataRow)
					self.rolemutex.select_mutex_role(int(data[3]), dataRow)
					self.rolemutex.save_mutex_button(dataRow)
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", roleMsg, data, flag)
			except Exception as e:
				print ("add mutexrole fail:" + str(e))

		self.log.log_end("addmutexrole")

	u'''校验添加互斥角色后用户添加角色'''
	def check_addmutex_user_addrole_002(self):

		#日志开始记录
		self.log.log_start("check_addmutex_user_addrole")
		#获取添加互斥角色测试数据
		rolemutexData = self.role.get_table_data("check_add_mutex")
		#保存成功的弹出框
		roleMsg = self.role.popup()
		#无检查点的测试项标识，如果为True说明通过
		flag = False

		for dataRow in range(len(rolemutexData)):
			data = rolemutexData[dataRow]

			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.rolemutex.click_user_role(data[2])
					self.rolemutex.select_all_role(int(data[3]))
					self.rolemutex.click_add_role(int(data[3]))
					self.rolemutex.select_all_role(int(data[4]))
					self.rolemutex.click_add_role(int(data[4]))
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", roleMsg, data, flag)
					self.cmf.back()
			except Exception as e:
				print ("add checkuseraddrole fail:" + str(e))

		self.log.log_end("check_addmutex_user_addrole")

	u'''校验添加互斥角色后用户编辑中的添加角色'''
	def check_addmutex_user_editrole_003(self):

		#日志开始记录
		self.log.log_start("check_addmutex_user_editrole")
		#获取添加互斥角色测试数据
		rolemutexData = self.role.get_table_data("check_add_mutex")
		#保存成功的弹出框
		roleMsg = self.role.popup()
		#无检查点的测试项标识，如果为True说明通过
		flag = False

		for dataRow in range(len(rolemutexData)):
			data = rolemutexData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.rolemutex.click_user_edit(data[2])
					self.rolemutex.click_role_message()
					self.rolemutex.select_all_role(int(data[3]))
					self.rolemutex.click_add_role(int(data[3]))
					self.rolemutex.select_all_role(int(data[4]))
					self.rolemutex.click_add_role(int(data[4]))
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", roleMsg, data, flag)
					self.cmf.back()
			except Exception as e:
				print ("add checkusereditrole fail:" + str(e))

		self.cmf.select_menu(u"角色管理", u"角色互斥定义")
		self.log.log_end("check_addmutex_user_editrole")

	u'''编辑互斥角色'''
	def edit_mutex_role_004(self):

		self.log.log_start("editmutexrole")
		#获取编辑互斥角色测试数据
		rolemutexData = self.role.get_table_data("role_mutex_mod")
		#保存成功的弹出框
		roleMsg = self.role.popup()

		#无检查点的测试项标识，如果为True说明通过
		flag = False

		for dataRow in range(len(rolemutexData)):
			data = rolemutexData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.rolemutex.edit_mutex(data[2])
					self.rolemutex.select_role(int(data[4]), dataRow)
					self.rolemutex.deselect_edit_mutex(data[2], data[3])
					self.rolemutex.select_mutex_role(int(data[5]), dataRow)
					self.rolemutex.save_mutex_button(dataRow)
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", roleMsg, data, flag)
			except Exception as e:
				print ("Edit mutex role fail:" + str(e))

		self.log.log_end("editmutexrole")

	u'''校验编辑互斥角色后用户添加角色'''
	def check_editmutex_user_addrole_005(self):

		#日志开始记录
		self.log.log_start("check_editmutex_user_addrole")
		#获取添加互斥角色测试数据
		rolemutexData = self.role.get_table_data("check_edit_mutex")
		#保存成功的弹出框
		roleMsg = self.role.popup()
		#无检查点的测试项标识，如果为True说明通过
		flag = False

		for dataRow in range(len(rolemutexData)):
			data = rolemutexData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.rolemutex.click_user_role(data[2])
					self.rolemutex.select_all_role(int(data[3]))
					self.rolemutex.click_add_role(int(data[3]))
					self.rolemutex.select_all_role(int(data[4]))
					self.rolemutex.click_add_role(int(data[4]))
					self.rolemutex.select_all_role(int(data[5]))
					self.rolemutex.click_add_role(int(data[5]))
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", roleMsg, data, flag)
					self.cmf.back()
			except Exception as e:
				print ("add checkeditmutex fail:" + str(e))

		self.log.log_end("check_editmutex_user_addrole")

	u'''校验编辑互斥角色后用户编辑中的添加角色'''
	def check_editmutex_user_editrole_006(self):

		#日志开始记录
		self.log.log_start("check_editmutex_user_editrole")
		#获取添加互斥角色测试数据
		rolemutexData = self.role.get_table_data("check_edit_mutex")
		#保存成功的弹出框
		roleMsg = self.role.popup()
		#无检查点的测试项标识，如果为True说明通过
		flag = False

		for dataRow in range(len(rolemutexData)):
			data = rolemutexData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.rolemutex.click_user_edit(data[2])
					self.rolemutex.click_role_message()
					self.rolemutex.select_all_role(int(data[3]))
					self.rolemutex.click_add_role(int(data[3]))
					self.rolemutex.select_all_role(int(data[4]))
					self.rolemutex.click_add_role(int(data[4]))
					self.rolemutex.select_all_role(int(data[5]))
					self.rolemutex.click_add_role(int(data[5]))
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", roleMsg, data, flag)
					self.cmf.back()
			except Exception as e:
				print ("add checkeditmutex fail:" + str(e))

		self.cmf.select_menu(u"角色管理", u"角色互斥定义")
		self.log.log_end("check_editmutex_user_editrole")

	u'''删除角色互斥'''
	def del_mutex_role_007(self):

		self.log.log_start("delmutexrole")
		#获取删除角色互斥测试数据
		rolemutexData = self.role.get_table_data("role_mutex_del")
		#保存成功的弹出框
		roleMsg = self.role.popup()

		#无检查点的测试项标识，如果为True说明通过
		flag = False

		for dataRow in range(len(rolemutexData)):
			data = rolemutexData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.rolemutex.delete_mutex(data[2])
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", roleMsg, data, flag)
			except Exception as e:
				print ("Del mutex role fail:" + str(e))

		self.log.log_end("delmutexrole")

	u'''校验角色互斥'''
	def check_mutex_role_008(self):

		self.log.log_start("checkmutexrole")
		#获取编辑互斥角色测试数据
		rolemutexData = self.role.get_table_data("role_mutex_check")
		#保存成功的弹出框
		roleMsg = self.role.popup()

		#无检查点的测试项标识，如果为True说明通过
		flag = False

		self.rolemutex.click_add_mutex()

		for dataRow in range(len(rolemutexData)):
			data = rolemutexData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					if dataRow == 3:
						self.rolemutex.click_add_mutex()
					else:
						if dataRow != 1:
							self.rolemutex.check_select_role(int(data[2]))
							if dataRow != 2:
								self.rolemutex.check_select_mutex_role(int(data[3]))
						self.rolemutex.check_save_mutex()
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", roleMsg, data, flag)
			except Exception as e:
				print ("Check mutex role fail:" + str(e))

		self.cmf.select_menu(u"角色管理", u"角色定义")
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		self.log.log_end("checkmutexrole")