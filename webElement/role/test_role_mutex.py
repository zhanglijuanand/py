#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：2017/7/3
#模块描述：角色互斥定义
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

class roleMutex(object):

	#添加互斥角色按钮
	ADD_LEVEL = "add_level"

	def __init__(self, driver):
		self.driver = driver
		self.getElem = getElement(driver)
		self.selectElem = selectElement(driver)
		self.frameElem = frameElement(driver)
		self.cmf = commonFun(driver)

	u'''点击角色互斥的添加按钮'''
	def click_add_mutex(self):
		try:
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			self.getElem.find_element_wait_and_click_EC("id", self.ADD_LEVEL,5)
		except Exception:
			print("Click Add mutex button failed")

	u'''选择角色
	   Parameters:
	      -index：select的索引，例0,1,2,从0开始计数
	      -number：表示第几次添加
	'''
	def select_role(self, index, number):
		#option位于第几个
		manage_index = index + 1
		option_xpath = "/html/body/div/div[3]/div["+str(number)+"]/table/tbody/tr/td[1]/select/option[" + str(manage_index) + "]"
		select_xpath = "/html/body/div/div[3]/div["+str(number)+"]/table/tbody/tr/td[1]/select"
		selem = self.getElem.find_element_with_wait("xpath", select_xpath)

		#查看元素是否被选
		option_selected = self.selectElem.select_element_check("xpath", option_xpath)

		if option_selected is False:
			self.selectElem.select_element_by_index(selem, index)

	u'''选择互斥角色
	   Parameters:
	      -index：select的索引，例0,1,2,从0开始计数
	      -number：表示第几次添加
	'''
	def select_mutex_role(self, index, number):
		#option位于第几个
		manage_index = index + 1
		option_xpath = "/html/body/div/div[3]/div["+str(number)+"]/table/tbody/tr/td[3]/select/option[" + str(manage_index) + "]"
		select_xpath = "/html/body/div/div[3]/div["+str(number)+"]/table/tbody/tr/td[3]/select"
		selem = self.getElem.find_element_with_wait("xpath", select_xpath)

		#查看元素是否被选
		option_selected = self.selectElem.select_element_check("xpath", option_xpath)

		if option_selected is False:
			self.selectElem.select_element_by_index(selem, index)

	u'''点击添加互斥角色界面的保存按钮
	   Parameters:
	      -number：表示第几次添加
	'''
	def save_mutex_button(self, number):
		try:
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			xpath = "/html/body/div/div[3]/div["+str(number)+"]/table/tbody/tr/td[4]/input[3]"
			self.getElem.find_element_wait_and_click_EC("xpath", xpath, 5)
		except Exception:
			print("Click the Save button to fail")

	u'''点击编辑按钮
	   Parameters:
	      - name:被编辑的角色列角色名称
	'''
	def edit_mutex(self, name):
		self.operation_object(name, "edit_role_mutex")

	u'''点击删除按钮
	   Parameters:
	      - name:角色列所选择的角色名称
	'''
	def delete_mutex(self, name):
		self.operation_object(name, "delete_role_mutex")

	u'''取消编辑的角色互斥select框中选中的项
	   Parameters:
	      - rolename:角色列所选择的角色名称
	      - mutexname:角色互斥列所选择的角色名称
	'''
	def deselect_edit_mutex(self, rolename, mutexname):

		self.frameElem.from_frame_to_otherFrame("mainFrame")
		#获取页面有多少个(角色select)
		sltargets = self.driver.find_elements_by_name("select_role")
		for sle in sltargets:
			self.get_option_object(rolename, mutexname, sle)

	u'''校验选择角色
	   Parameters:
	      -index：select的索引，例0,1,2,从0开始计数
	'''
	def check_select_role(self, index):

		self.frameElem.from_frame_to_otherFrame("mainFrame")
		selem = self.getElem.find_element_with_wait("name", "select_role")
		self.selectElem.select_element_by_index(selem, index)

	u'''校验选择互斥角色
	   Parameters:
	      -index：select的索引，例0,1,2,从0开始计数
	'''
	def check_select_mutex_role(self, index):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		selem = self.getElem.find_element_with_wait("name", "select_mutex_role")
		self.selectElem.select_element_by_index(selem, index)

	u'''校验点击保存按钮'''
	def check_save_mutex(self):
		self.getElem.find_element_wait_and_click_EC("name", "save")

	u'''点击用户的角色按钮
	   Parameters:
	      -username：用户账号
	'''
	def click_user_role(self, username):

		self.cmf.select_menu(u"运维管理", u"用户")
		self.frameElem.from_frame_to_otherFrame("mainFrame")

		#获取用户位于第几行
		userrow = self.cmf.find_row_by_name(username, "fortUserAccount")
		role_xpath = "/html/body/form/div/div[7]/div[2]/div/table/tbody/tr[" + str(userrow) + "]/td[9]/input[2]"
		self.getElem.find_element_wait_and_click("xpath", role_xpath)

	u'''点击用户的编辑按钮
	   Parameters:
	      -username：用户账号
	'''
	def click_user_edit(self, username):

		self.cmf.select_menu(u"运维管理", u"用户")
		self.frameElem.from_frame_to_otherFrame("mainFrame")

		#获取用户位于第几行
		userrow = self.cmf.find_row_by_name(username, "fortUserAccount")
		role_xpath = "/html/body/form/div/div[7]/div[2]/div/table/tbody/tr[" + str(userrow) + "]/td[9]/input[1]"
		self.getElem.find_element_wait_and_click("xpath", role_xpath)

	u'''选择所有角色
	   Parameters:
	      -index：select的索引，例0,1,2,从0开始计数
	'''
	def select_all_role(self, index):

		#option位于第几个
		manage_index = index + 1
		option_xpath = "//select[@id='Roles']/option[" + str(manage_index) + "]"
		selem = self.getElem.find_element_with_wait("id", "Roles")

		#查看元素是否被选中
		option_selected = self.selectElem.select_element_check("xpath", option_xpath)
		if option_selected is False:
			self.selectElem.select_element_by_index(selem, index)

	u'''点击用户添加角色的添加按钮'''
	def click_add_role(self, index):
		try:
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			self.getElem.find_element_wait_and_click_EC("id", "add_roles")
			selem = self.getElem.find_element_with_wait("id", "Roles")
			self.selectElem.deselect_element_by_index(selem, index)
		except Exception:
			print("Click add role button to fail")

	u'''点击用户的角色信息按钮'''
	def click_role_message(self):
		try:
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			self.getElem.find_element_wait_and_click_EC("xpath", "//form[@id='user_form']/div/div[2]/div/a[2]")
		except Exception:
			print("Click role message button to fail")

	u'''操作对象
	   Parameters:
	      - name:被操作的角色列角色名称
	      - idstr:被操作的按钮id字符
	'''
	def operation_object(self, name, idstr):
		try:
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			#获取页面有多少个(角色select)
			sltargets = self.driver.find_elements_by_name("select_role")

			for sle in sltargets:
				self.loop_object(name, sle, idstr)
				break
		except Exception:
			print("Click  button to fail")

	u'''循环对象
	   Parameters:
	      - name:被操作的角色列角色名称
	      - sle:select对象
	      - idstr:被操作的按钮id字符
	'''
	def loop_object(self, name, sle, idstr):

		#获取option对象
		optargets = sle.find_elements_by_tag_name("option")

		for opt in optargets:
			if opt.text == name and opt.get_attribute("disabled") != "true":
				#获取当前角色select的id
				role_select_id = sle.get_attribute("id")
				#获取当前按钮id
				buttonid = idstr + str(role_select_id[-1])
				self.getElem.find_element_wait_and_click_EC("id", buttonid, 5)
				break

	u'''取消select框中选中的项
	   Parameters:
	      - select_mutex_id:当前角色互斥select的id
	      - mutexname:角色互斥列所选择的角色名称
	'''
	def uncheck(self, select_mutex_id, mutexname):

		#获取当前角色互斥select
		selem = self.getElem.find_element_with_wait("id", select_mutex_id)
		mutextarges = selem.find_elements_by_tag_name("option")

		#循环option对象
		for mutexopt in mutextarges:
			if mutexopt.get_attribute("class") == "opti":
				self.selectElem.deselect_element_by_text(selem, mutexname)

	u'''获取option对象进行取消选中
	   Parameters:
	      - rolename:角色列所选择的角色名称
	      - mutexname:角色互斥列所选择的角色名称
	      - sle:select对象
	'''
	def get_option_object(self, rolename, mutexname, sle):

		#获取option对象
		optargets = sle.find_elements_by_tag_name("option")

		#循环option对象
		for opt in optargets:
			if opt.text == rolename and opt.get_attribute("disabled") != "true":
				#获取当前角色select的id
				role_select_id = sle.get_attribute("id")
				#获取当前角色互斥select的id
				select_mutex_id = "select_mutex_role"+str(role_select_id[-1])
				#取消select框中选中的项
				self.uncheck(select_mutex_id, mutexname)