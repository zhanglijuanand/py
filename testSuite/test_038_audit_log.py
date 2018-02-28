#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("/testIsomp/common/")
from _initDriver import initDriver

sys.path.append("/testIsomp/testCase/audit_management")
from test_audit_log import *

sys.path.append("/testIsomp/testSuite")
from common_suite_file import CommonSuiteData,setDriver

import unittest

class testAuditLogSuite(unittest.TestCase):
    def setUp(self):
        #定义驱动
        self.browser = setDriver().set_driver()
        self.commonSuite = CommonSuiteData(self.browser)        
        self.auditLog = testAuditLog(self.browser)
        #运维审计检索前置条件
        self.commonSuite.audit_log_prefix_condition()
    
    def test_audit_log_query(self):
        #运维审计检索
        self.auditLog.Audit_log_query_001()

    def tearDown(self):
        #运维审计后置条件
        self.commonSuite.audit_log_post_condition()
        initDriver().close_driver(self.browser)

if __name__ == "__main__":
    unittest.main()
