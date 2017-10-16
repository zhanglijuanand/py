#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：2017/6/14
#模块描述：调用角色定义模块
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("/testIsomp/testData/")
from _testDataPath import dataFileName
sys.path.append("/testIsomp/common")
from _icommon import commonFun,frameElement,tableElement
from _log import log
sys.path.append("/testIsomp/webElement/role/")
from test_roledf import Role

class testRole(object):

	def __init__(self,driver):
		self.driver = driver
		self.log = log()
		self.role = Role(driver)
		self.cmf = commonFun(driver)
		self.tableElem = tableElement(driver)
		self.frameElem = frameElement(driver)

	u'''获取测试数据
	   Parameters:
	      - sheetname:sheet名称
	   return：表格数据
	'''
	def get_table_data(self, sheetname):
		dataFile = dataFileName()
		roledfPath = dataFile.get_role_test_data_url()
		roledfData = dataFile.get_data(roledfPath, sheetname)
		return roledfData

	u'''弹出框'''
	def popup(self):
		roleMsg="/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"
		return  roleMsg

	u'''添加系统级角色'''
	def add_sysrole_001(self):

		#日志开始记录
		self.log.log_start("addsysrole")
		#获取添加系统管理员测试数据
		roledfData = self.get_table_data("add_sys_role")
		#保存成功的弹出框
		roleMsg = self.popup()

		#无检查点的测试项标识，如果为True说明通过
		flag = False

		for dataRow in range(len(roledfData)):
			data = roledfData[dataRow]

			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.role.add()
					self.role.edit_rolename(data[2])
					self.role.edit_shortname(data[3])
					self.role.select_sysrole()
					self.role.save_button()
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", roleMsg, data, flag)
					self.cmf.back()
			except Exception as e:
				print ("add sysrole fail:" + str(e))

		self.log.log_end("addsysrole")

	u'''添加部门管理员'''
	def add_dptrole_002(self):

		self.log.log_start("addroledpt")
		#获取添加部门管理员测试数据
		roledfData = self.get_table_data("add_dpt_role")
		#保存成功的弹出框
		roleMsg = self.popup()
		#无检查点的测试项标识，如果为True说明通过
		flag = False

		for dataRow in range(len(roledfData)):
			data = roledfData[dataRow]

			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.role.add()
					self.role.edit_rolename(data[2])
					self.role.edit_shortname(data[3])
					self.role.level()
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.role.select_dptrole()
					self.role.save_button()
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", roleMsg, data, flag)
					self.cmf.back()
			except Exception as e:
				print ("add sysrole fail:" + str(e))

		self.log.log_end("addroledpt")

	u'''编辑系统管理员'''
	def edit_role_003(self):

		self.log.log_start("editrole")
		#获取编辑系统管理员测试数据
		roledfData = self.get_table_data("edit_role")
		#保存成功的弹出框
		roleMsg = self.popup()

		#无检查点的测试项标识，如果为True说明通过
		flag = False

		for dataRow in range(len(roledfData)):
			data = roledfData[dataRow]
			try:

				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.role.edit(data[2])
					self.role.edit_rolename(data[3])
					self.role.edit_shortname(data[4])
					self.role.save_button()
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", roleMsg, data, flag)
					self.cmf.back()
			except Exception as e:
				print ("Edit role fail:" + str(e))

		self.log.log_end("editrole")

	u'''编辑可管理角色'''
	def edit_managerole_004(self):

		self.log.log_start("editmanagerole")
		#获取编辑系统管理员测试数据
		roledfData = self.get_table_data("edit_mange_role")
		#右侧已选可管理角色框
		roleMsg = "roles"

		for dataRow in range(len(roledfData)):
			data = roledfData[dataRow]
			#无检查点的测试项标识，如果为True说明通过
			flag = False

			try:

				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.role.edit(data[2])
					self.role.select_manage_role(int(data[3]))
					self.role.manage_role_add(int(data[3]))
					self.cmf.select_check_point("id", roleMsg, data, flag)
					self.role.save_button()
					self.frameElem.switch_to_content()
					self.role.click_ok_button()
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.cmf.back()
			except Exception as e:
				print ("Edit managed roles fail:" + str(e))

		self.log.log_end("editmanagerole")

	u'''编辑其他权限'''
	def edit_otherrole_005(self):

		self.log.log_start("editotherrole")
		#获取编辑系统管理员测试数据
		roledfData = self.get_table_data("edit_other_role")
		#右侧已选其他权限框
		roleMsg = "otherPrivileges"

		for dataRow in range(len(roledfData)):
			data = roledfData[dataRow]
			#无检查点的测试项标识，如果为True说明通过
			flag = False
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.role.edit(data[2])
					self.role.other_role_add(int(data[3]))
					self.cmf.select_check_point("id", roleMsg, data, flag)
					self.role.save_button()
					self.frameElem.switch_to_content()
					self.role.click_ok_button()
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.cmf.back()
			except Exception as e:
				print("Edit other permissions fail:" + str(e))

		self.log.log_end("editotherrole")

	u'''删除角色'''
	def del_role_006(self):
		self.log.log_start("delrole")

		#获取删除超级管理员测试数据
		roledfData = self.get_table_data("del_role")
		#删除的弹出框
		roleMsg = self.popup()
		#无检查点的测试项标识，如果为True说明通过
		flag = False

		for dataRow in range(len(roledfData)):
			data = roledfData[dataRow]

			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.role.delete(data[2])
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", roleMsg, data, flag)
					#校验删除后的角色是否存在
					if self.cmf.is_namevalue_exsit(data[2], "fortRoleName"):
						print("The super administrator has been deleted")
			except Exception as e:
				print ("Deleting the super administrator failed:" + str(e))

		self.log.log_end("delrole")

	u'''全选删除角色'''
	def bulkdel_role_007(self):

		self.log.log_start("bulkdelrole")

		#获取删除超级管理员测试数据
		roledfData = self.get_table_data("bulk_delrole")

		#删除的弹出框
		roleMsg = self.popup()

		#无检查点的测试项标识，如果为True说明通过
		flag = False

		for dataRow in range(len(roledfData)):
			data = roledfData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.cmf.check_all()
					self.cmf.bulkdel("delete_role")
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", roleMsg, data, flag)
			except Exception as e:
				print ("Select Delete roles failure:" + str(e))

		self.log.log_end("bulkdelrole")

	u'''校验角色名称和没有选择菜单项'''
	def check_rolename(self):

		self.log.log_start("checkrolename")
		#获取校验角色名称的数据
		roledfData = self.get_table_data("check_rolename")
		#弹出框
		roleMsg = self.popup()
		#无检查点的测试项标识，如果为True说明通过
		flag = False

		self.role.add()

		for dataRow in range(len(roledfData)):
			#把单行的数据赋值给列表data
			data = roledfData[dataRow]

			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.role.edit_rolename(data[2])
					self.role.edit_shortname(data[3])
					self.role.save_button()
					self.frameElem.switch_to_content()
					#设定没有检查点的测试项通过
					self.cmf.test_win_check_point("xpath", roleMsg, data, flag)
					self.frameElem.from_frame_to_otherFrame("mainFrame")
			except Exception as e:
				print ("Failed to verify the role name" + str(e))

		self.cmf.back()
		self.log.log_end("checkrolename")

	u'''检验名称简写'''
	def check_shortname(self):

		self.log.log_start("checkshortname")
		#获取校验角色名称的数据
		roledfData = self.get_table_data("check_shortname")
		#弹出框
		roleMsg = self.popup()
		#无检查点的测试项标识，如果为True说明通过
		flag = False

		for dataRow in range(len(roledfData)):
			#把单行的数据赋值给列表data
			data = roledfData[dataRow]

			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.role.add()
					self.role.edit_rolename(data[2])
					self.role.edit_shortname(data[3])
					self.role.select_sysrole()
					self.role.save_button()
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", roleMsg, data, flag)
					self.cmf.back()
			except Exception as e:
				print ("Failed to verify the name abbreviation:" + str(e))

		self.log.log_end("checkshortname")

	u'''校验其他权限选择'''
	def check_other_role(self):

		self.log.log_start("checkother")
		#获取其他权限选择的数据
		roledfData = self.get_table_data("ckeck_other")
		#弹出框
		roleMsg = self.popup()
		#无检查点的测试项标识，如果为True说明通过
		flag = False

		for dataRow in range(len(roledfData)):
			#把单行的数据赋值给列表data
			data = roledfData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.role.edit(data[2])
					self.role.other_role_add(int(data[3]))
					self.role.other_role_add(int(data[4]))
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", roleMsg, data, flag)
					self.cmf.back()
			except Exception as e:
				print ("Check other rights options failed:" + str(e))

		self.log.log_end("checkother")

	u'''校验批量删除'''
	def check_bulkdel(self):

		self.log.log_start("checkbulkdel")
		#获取校验角色名称的数据
		roledfData = self.get_table_data("check_bulk")
		#弹出框
		roleMsg = self.popup()
		#无检查点的测试项标识，如果为True说明通过
		flag = False

		for dataRow in range(len(roledfData)):
			#把单行的数据赋值给列表data
			data = roledfData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.cmf.bulkdel("delete_role")
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", roleMsg, data, flag)
			except Exception as e:
				print ("Check batch deletion failed" + str(e))

		self.log.log_end("checkbulkdel")

	u'''角色查询'''
	def role_query_008(self):

		self.log.log_start("rolequery")
		#获取角色查询的数据
		roledfData = self.get_table_data("role_query")

		for dataRow in range(len(roledfData)):
			#把单行的数据赋值给列表data
			data = roledfData[dataRow]
			table_xpath = "/html/body/form/div/div[6]/div[2]/div/table"

			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					if dataRow < 3:
						if dataRow == 1:
							self.role.shortname_query(data[2])

						elif dataRow == 2:
							self.role.rolename_query(data[1])

						self.frameElem.from_frame_to_otherFrame("mainFrame")
						#获取表格行数
						get_table_rows = self.tableElem.get_table_rows_count(table_xpath)
						if get_table_rows < 1:
							self.log.log_detail(data[0], True)
					else:
						if dataRow == 3:
							self.role.click_query()

						elif dataRow == 4:
							self.role.rolename_query(data[1])

						elif dataRow == 5:
							self.role.shortname_query(data[2])

						self.frameElem.from_frame_to_otherFrame("mainFrame")
						#获取表格行数
						get_table_rows = self.tableElem.get_table_rows_count(table_xpath)
						if get_table_rows > 0:
							self.log.log_detail(data[0], True)
			except Exception as e:
				print ("Query role failed" + str(e))

		self.log.log_end("rolequery")
