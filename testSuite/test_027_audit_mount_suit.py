# -*- coding:utf-8 -*-
'''
#文件名：
#作者：张利娟
#创建日期：2018/1/17
#模块描述：
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 导入驱动
sys.path.append("/testIsomp/common/")
from _initDriver import initDriver
sys.path.append("/testIsomp/testCase/mount/")
from test_mount import testMount
sys.path.append("/testIsomp/testSuite/common_suite_file/")
from common_suite_file import setDriver, CommonSuiteData
import unittest

class testMountSuit(unittest.TestCase):
	def setUp(self):
		self.browser = setDriver().set_driver()
		self.comsuit = CommonSuiteData(self.browser)
		self.testmount = testMount(self.browser)

		#前置条件
		self.comsuit.audit_mount_module_prefix_condition()

	def test_audit_mount(self):
		#添加审计存储扩展
		self.testmount.add_mount_windows_001()
		#审计存储扩展校验
		self.testmount.check_mount_002()

	#后置条件
	def tearDown(self):
		self.comsuit.audit_mount_module_post_condition()
		initDriver().close_driver(self.browser)

if __name__ == "__main__":
	unittest.main()

