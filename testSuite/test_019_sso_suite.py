#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("/testIsomp/common/")
from _initDriver import initDriver

sys.path.append("/testIsomp/testCase/sso")
from test_sso import testSso

sys.path.append("/testIsomp/testSuite")
from common_suite_file import CommonSuiteData,setDriver

import unittest

class testSsoSuite(unittest.TestCase):
    def setUp(self):
        #定义驱动
        self.browser = setDriver().set_driver()
        self.commonSuite = CommonSuiteData(self.browser)     
        self.ssoMethod = testSso(self.browser)
        #self.commonSuite.login_and_switch_to_common()
        #单点登录前置条件
        self.commonSuite.sso_prefix_condition()
    
    def test_cmd_sso_method(self):
        #命令单点登录
        self.ssoMethod.cisco_sso_login_001()
        self.ssoMethod.cisco_niming_sso_login_002()
        self.ssoMethod.huawei_sso_login_003()
        self.ssoMethod.debian_sso_login_004()
        
    def tearDown(self):
        pass
        #单点登录后置条件
        self.commonSuite.sso_post_condition()
        initDriver().close_driver(self.browser)

if __name__ == "__main__":
    unittest.main()
