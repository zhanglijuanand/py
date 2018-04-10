#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：2017/6/12
#模块描述：角色定义
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("/testIsomp/common/")
from _icommon import getElement,selectElement,frameElement,commonFun

class Role(object):

	#角色名称
	FORTROLE_NAME = "fortRoleName"
	#名称简写
	FORTROLE_SHORTNAME = "fortRoleShortName"
	#添加按钮
	ADD_ROLE = "add_role"
	#部门级
	DEPARTMENT = "department"
	#保存按钮
	SAVE_ROLE = "save_role"

	def __init__(self, driver):
		self.driver = driver
		self.getElem = getElement(driver)
		self.selectElem = selectElement(driver)
		self.frameElem = frameElement(driver)
		self.cmf = commonFun(driver)

	u'''点击添加按钮'''
	def add(self):
		try:
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			self.getElem.find_element_wait_and_click("id", self.ADD_ROLE)
		except Exception:
			print("Click the Add button to fail")

	u'''选择级别为部门级'''
	def level(self):
		try:
			self.getElem.find_element_wait_and_click_EC("id", self.DEPARTMENT)
		except Exception:
			print("The selection level is departmental failure")

	u'''全选部门级角色'''
	def select_dptrole(self):
		try:
			self.getElem.find_element_wait_and_click_EC("xpath", "/html/body/form/div/div[2]/div[2]/table[1]/tbody/tr[4]/td[2]/ul/li[1]/span[2]")
			self.getElem.find_element_wait_and_click_EC("xpath", "/html/body/form/div/div[2]/div[2]/table[1]/tbody/tr[4]/td[2]/ul/li[2]/span[2]")
			self.getElem.find_element_wait_and_click_EC("xpath", "/html/body/form/div/div[2]/div[2]/table[1]/tbody/tr[4]/td[2]/ul/li[3]/span[2]")
			self.getElem.find_element_wait_and_click_EC("xpath", "/html/body/form/div/div[2]/div[2]/table[1]/tbody/tr[4]/td[2]/ul/li[4]/span[2]")
			self.getElem.find_element_wait_and_click_EC("xpath", "/html/body/form/div/div[2]/div[2]/table[1]/tbody/tr[4]/td[2]/ul/li[5]/span[2]")
		except Exception:
			print("Select the role of department level failure")

	u'''全选系统级角色'''
	def select_sysrole(self):
		try:
			self.getElem.find_element_wait_and_click_EC("xpath", "/html/body/form/div/div[2]/div[2]/table[1]/tbody/tr[4]/td[2]/ul/li[1]/span[2]")
			self.getElem.find_element_wait_and_click_EC("xpath", "/html/body/form/div/div[2]/div[2]/table[1]/tbody/tr[4]/td[2]/ul/li[2]/span[2]")
			self.getElem.find_element_wait_and_click_EC("xpath", "/html/body/form/div/div[2]/div[2]/table[1]/tbody/tr[4]/td[2]/ul/li[3]/span[2]")
			self.getElem.find_element_wait_and_click_EC("xpath", "/html/body/form/div/div[2]/div[2]/table[1]/tbody/tr[4]/td[2]/ul/li[4]/span[2]")
			self.getElem.find_element_wait_and_click_EC("xpath", "/html/body/form/div/div[2]/div[2]/table[1]/tbody/tr[4]/td[2]/ul/li[5]/span[2]")
			self.getElem.find_element_wait_and_click_EC("xpath", "/html/body/form/div/div[2]/div[2]/table[1]/tbody/tr[4]/td[2]/ul/li[6]/span[2]")
			self.getElem.find_element_wait_and_click_EC("xpath", "/html/body/form/div/div[2]/div[2]/table[1]/tbody/tr[4]/td[2]/ul/li[7]/span[2]")
			self.getElem.find_element_wait_and_click_EC("xpath", "/html/body/form/div/div[2]/div[2]/table[1]/tbody/tr[4]/td[2]/ul/li[8]/span[2]")
		except Exception:
			print("Select the role of system level failure")

	u'''点击编辑角色界面的保存按钮'''
	def save_button(self):
		try:
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			self.getElem.find_element_wait_and_click_EC("id", self.SAVE_ROLE, 5)
		except Exception:
			print("Click the Save button to fail")

	u'''选择可管理角色
	   Parameters:
	      -index：select的索引，例0,1,2,从0开始计数
	'''
	def select_manage_role(self, index):
		#option位于是第几个
		manage_index = index + 1
		option_xpath = "//select[@id='allRoles']/option[" + str(manage_index) + "]"
		selem = self.getElem.find_element_with_wait("id", "allRoles")

		#查看元素是否被选中
		option_selected = self.selectElem.select_element_check("xpath", option_xpath)

		if option_selected is False:
			self.selectElem.select_element_by_index(selem, index)

	u'''点击可管理角色添加'''
	def manage_role_add(self, index):
		try:
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			self.getElem.find_element_wait_and_click("id", "add_roles")
			selem = self.getElem.find_element_with_wait("id", "allRoles")
			self.selectElem.deselect_element_by_index(selem, index)
		except Exception:
			print("Click the manageAdd button to fail")

	u'''添加其他权限
	   Parameters:
	      -index：select的索引，例0,1,2,从0开始计数
	'''
	def other_role_add(self, index):
		#option位于是第几个
		opt_index = index + 1
		option_xpath = "//select[@id='allOtherPrivileges']/option[" + str(opt_index) + "]"
		selem = self.getElem.find_element_with_wait("id", "allOtherPrivileges")

		#查看元素是否被选中
		option_selected = self.selectElem.select_element_check("xpath", option_xpath)

		if option_selected is False:
			self.selectElem.select_element_by_index(selem, index)

		self.getElem.find_element_wait_and_click("id", "add_privileges")
		#对已选择的角色取消选择
		self.selectElem.deselect_element_by_index(selem, index)

	u'''点击编辑按钮
	   Parameters:
	      - rolename:角色名称
	'''
	def edit(self, rolename):
		try:
			row = self.cmf.find_row_by_name(rolename, "fortRoleName")
			update_xpath = "/html/body/form/div/div[6]/div[2]/div/table/tbody/tr[" + str(row) + "]/td[6]/input[1]"
			self.getElem.find_element_wait_and_click("xpath", update_xpath)
		except Exception:
			print("Click the Edit button to fail")

	u'''点击删除按钮
	   Parameters:
	      - rolename:角色名称
	'''
	def delete(self, rolename):
		try:
			row = self.cmf.find_row_by_name(rolename, "fortRoleName")
			update_xpath = "/html/body/form/div/div[6]/div[2]/div/table/tbody/tr[" + str(row) + "]/td[6]/input[2]"
			self.getElem.find_element_wait_and_click("xpath", update_xpath)
		except Exception:
			print("Click the delete button to fail")

	u'''编辑角色名称
	   Parameters:
	      - rolename:角色名称
	'''
	def edit_rolename(self, rolename):
		try:
			self.getElem.find_element_wait_and_clear("id", self.FORTROLE_NAME)
			self.getElem.find_element_wait_and_sendkeys("id", self.FORTROLE_NAME, rolename)
		except Exception:
			print("Role name fill in error")

	u'''编辑名称简写
	    Parameters：
	       -shortname 名称简写
	'''
	def edit_shortname(self, shortname):
		try:
			self.getElem.find_element_wait_and_clear("id", self.FORTROLE_SHORTNAME)
			self.getElem.find_element_wait_and_sendkeys("id", self.FORTROLE_SHORTNAME, shortname)
		except Exception:
			print("Name abbreviation fill in error")

	u'''点击确定按钮'''
	def click_ok_button(self):
		self.driver.switch_to_default_content()
		self.getElem.find_element_wait_and_click_EC("xpath", "/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button",5)

	u'''角色名称查询
	    Parameters：
	       -rolename  角色名称
	'''
	def rolename_query(self, rolename):
		try:
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			self.getElem.find_element_wait_and_sendkeys("id", "fortRoleName",rolename)
			self.click_query()
			self.click_reset()
		except Exception:
			print("Query rolename failed")

	u'''名称简写查询
	    Parameters：
	       -shortname 名称简写
	'''
	def shortname_query(self, shortname):
		try:
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			self.getElem.find_element_wait_and_sendkeys("id", "fortRoleShortName", shortname)
			self.click_query()
			self.click_reset()
		except Exception:
			print("Query shortname failed")

	u'''点击查询按钮'''
	def click_query(self):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		self.getElem.find_element_wait_and_click_EC("id", "query_role")

	u'''点击重置按钮'''
	def click_reset(self):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		self.getElem.find_element_wait_and_click_EC("id", "resetting")
