#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：
#模块描述：
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#导入驱动
sys.path.append("/testIsomp/common/")
from _initDriver import initDriver
from _icommon import commonFun
sys.path.append("/testIsomp/testCase/role/")
from test_role import testRole
from test_mutex import testMutex
sys.path.append("/testIsomp/testSuite/common_suite_file/")
from common_suite_file import setDriver,CommonSuiteData
import unittest

class testRoleSuite(unittest.TestCase):

	def setUp(self):

		#调用驱动
		self.browser = setDriver().set_driver()

		self.comsuit = CommonSuiteData(self.browser)
		self.cmf = commonFun(self.browser)
		self.testrole = testRole(self.browser)
		self.testmutex = testMutex(self.browser)

		#角色前置条件
		self.comsuit.role_module_prefix_condition()

	def test_role(self):

		u'''添加系统级角色'''
		self.testrole.add_sysrole_001()
		u'''添加部门管理员'''
		self.testrole.add_dptrole_002()
		u'''编辑系统管理员'''
		self.testrole.edit_role_003()
		u'''角色查询'''
		self.testrole.role_query_008()
		u'''切换到角色互斥定义页面'''
		self.cmf.select_menu(u"角色管理", u"角色互斥定义")
		u'''添加互斥角色'''
		self.testmutex.add_mutex_role_001()
		u'''校验添加互斥角色后用户添加角色'''
		self.testmutex.check_addmutex_user_addrole_002()
		u'''校验添加互斥角色后用户编辑中的添加角色'''
		self.testmutex.check_addmutex_user_editrole_003()
		u'''编辑互斥角色'''
		self.testmutex.edit_mutex_role_004()
		u'''校验编辑互斥角色后用户添加角色'''
		self.testmutex.check_editmutex_user_addrole_005()
		u'''校验编辑互斥角色后用户编辑中的添加角色'''
		self.testmutex.check_editmutex_user_editrole_006()
		u'''删除角色互斥'''
		self.testmutex.del_mutex_role_007()
		u'''校验角色互斥'''
		self.testmutex.check_mutex_role_008()
		u'''编辑可管理角色'''
		self.testrole.edit_managerole_004()
		u'''校验其他权限选择'''
		self.testrole.check_other_role()
		u'''编辑其他权限'''
		self.testrole.edit_otherrole_005()
		u'''校验角色名称和没有选择菜单项'''
		self.testrole.check_rolename()
		u'''检验名称简写'''
		self.testrole.check_shortname()
		u'''校验批量删除'''
		self.testrole.check_bulkdel()
		u'''删除角色'''
		self.testrole.del_role_006()
		u'''全选删除角色'''
		self.testrole.bulkdel_role_007()

	def tearDown(self):
		#角色后置条件
		self.comsuit.role_module_post_condition()

		initDriver().close_driver(self.browser)

if __name__ == "__main__":
	unittest.main()
