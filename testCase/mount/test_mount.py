#-*- coding:utf-8 -*-
'''
#文件名：
#作者：张利娟
#创建日期：2018/1/17
#模块描述：调用审计存储扩展模块
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys,time
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("/testIsomp/testData/")
from _testDataPath import dataFileName
sys.path.append("/testIsomp/common")
from _icommon import commonFun,frameElement
from _log import log
sys.path.append("/testIsomp/webElement/mount/")
from test_mount_ment import MountPage

class testMount(object):
    def __init__(self, driver):
        self.driver = driver
        self.log = log()
        self.mountpage = MountPage(driver)
        self.cmf = commonFun(driver)
        self.frameElem = frameElement(driver)

    u'''
    获取测试数据
        Parameters:
            - sheetname:sheet名称
        return：表格数据
    '''
    def get_table_date(self, sheetname):
        dateFile = dataFileName()
        mountPath = dateFile.audit_mount_test_date_url()
        mountDate = dateFile.get_data(mountPath, sheetname)
        return mountDate

    u'''弹出框'''
    def pupop(self):
        mountMsg = "/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"
        return mountMsg

    u'''校验审计存储扩展'''
    def check_mount_002(self):
        #日志开始记录
        self.log.log_start("check audit mount")
        #获取添加审计存储扩展测试数据
        mountDate = self.get_table_date("check_audit_mount")
        #保存成功的弹出框
        mountMsg = self.pupop()
        #无检查点的测试项标识，如果为True说明通过
        flag = False

        for dataRow in range(len(mountDate)):
            data = mountDate[dataRow]
            try:
                #如果不是第一行标题，则读取数据
                if dataRow == 1:
                    self.mountpage.select_type(data[2])
                elif dataRow == 2:
                    self.mountpage.distal_ip(data[3])
                elif dataRow == 3:
                    self.mountpage.distal_path(data[4])
                elif dataRow == 4:
                    self.mountpage.local_path(data[5])
                elif dataRow == 5:
                    self.mountpage.distal_account(data[6])
                elif dataRow == 6:
                    self.mountpage.distal_ip(data[3])
                    self.mountpage.distal_passwd(data[7])
                if dataRow != 0:
                    time.sleep(3)
                    self.mountpage.add()
                    self.frameElem.switch_to_content()
                    self.cmf.test_win_check_point("xpath", mountMsg, data, flag)
            except Exception as e:
                print("check audit mount:" + str(e))

        self.log.log_end("check audit mount")

    u'''添加windows类型的审计存储扩展'''
    def add_mount_windows_001(self):

        #日志开始记录
        self.log.log_start("addsysmount")
        #获取添加审计存储扩展测试数据
        mountDate = self.get_table_date("add_audit_mount")
        #保存成功的弹出框
        mountMsg = self.pupop()

        #无检查点的测试项标识，如果为True说明通过
        flag = False
        for dataRow in range(len(mountDate)):
            data = mountDate[dataRow]
            try:
                #如果不是第一行标题，则读取数据
                if dataRow != 0:
                    self.mountpage.select_type(data[2])
                    self.mountpage.distal_ip(data[3])
                    self.mountpage.distal_path(data[4])
                    self.mountpage.local_path(data[5])
                    if dataRow == 1:
                        self.mountpage.distal_account(data[6])
                        self.mountpage.distal_passwd(data[7])
                    time.sleep(10)
                    self.mountpage.add()
                    time.sleep(10)
                    self.frameElem.switch_to_content()
                    self.cmf.test_win_check_point("xpath", mountMsg, data, flag)
                    if dataRow == 2:
                        self.mountpage.subcheckbox()
                    self.mountpage.subcheckbox()
                    self.mountpage.delete()
                    self.cmf.click_msg_button(1)
            except Exception as e:
                print ("add sysmount fail:" + str(e))
        self.mountpage.click_right_button('1')
        self.log.log_end("add seccussful")