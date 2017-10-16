#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#导入登录
sys.path.append("/testIsomp/testCase/login")
from test_login import *

sys.path.append("/testIsomp/webElement/user/")
from userElement import UserPage

sys.path.append("/testIsomp/testSuite")
from common_suite_file import CommonSuiteData,setDriver

import unittest

class testLoginSuite(unittest.TestCase):
    def setUp(self):
        
        #定义驱动
        self.browser = setDriver().set_driver()
        self.commonSuite = CommonSuiteData(self.browser)
        self.userElem = UserPage(self.browser)
        
        self.commonSuite.login_module_prefix_condition()

    def test_login(self):
        test_login = testLogin(self.browser)
        #登录
        test_login.login()
    
    def tearDown(self):
        self.commonSuite.login_module_post_condition()      
        initDriver().close_driver(self.browser)

if __name__ == "__main__":
    unittest.main()
