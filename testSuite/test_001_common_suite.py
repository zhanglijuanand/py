#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：
#模块描述：公共
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import unittest
sys.path.append("/testIsomp/common/")
from _initDriver import initDriver
sys.path.append("/testIsomp/testSuite/common_suite_file/")
from common_suite_file import setDriver,CommonSuiteData

class testCommonSuite(unittest.TestCase):

	def setUp(self):
		#调用驱动
		self.browser = setDriver().set_driver()
		self.comsuit = CommonSuiteData(self.browser)

	def test_common(self):
		self.comsuit.module_common_prefix_condition()
		self.comsuit.add_user_with_role()
		self.comsuit.user_quit()

	def tearDown(self):
		initDriver().close_driver(self.browser)

if __name__ == "__main__":
	unittest.main()