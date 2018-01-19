#coding=utf-8
u'''
#文件名：
#被测软件版本号：V2.8.1
#作成人：张利娟
#生成日期：2018/1/15
#模块描述：添加审计存储扩展
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys,time
reload(sys)
sys.setdefaultencoding('utf-8')
#导入通用模块
sys.path.append("/testIsomp/common/")
from _initDriver import *
from _icommon import getElement,selectElement,commonFun,frameElement
from _cnEncode import cnEncode

class MountPage(object):
   #保存按钮
    SAVE = "save"
   #删除按钮
    DELETE = "delete"
   #全选按钮
    SUB_CHECK_BOX = "subCheckbox"
   #windows类型
    WINDOWS = "windows"
   #linux类型
    LINUX = "linux"
   #ISCSI类型
    ISCSI = "iscsi"
   #远端IP
    DISTAL_IP ="distalIp"
   #远端路径
    DISTAL_PATH = "distalPath"
   #本地路径
    LOCAL_PATH = "localPath"
   #远端账号
    DISTAL_ACCOUNT = "distalAccount"
   #远端密码
    DISTAL_PASSWD = "distalPassword"
   #ISCSI名称
    ISCSI_NAME = "iscsiName"
   #新增盘符
    NEW_DISK_NAME = "newDiskName"

    def __init__(self, driver):
       self.driver = driver
       self.getElem = getElement(driver)
       self.selectElem = selectElement(driver)
       self.frameElem = frameElement(driver)
       self.cmf = commonFun(driver)
       self.cnEn = cnEncode()

    u'''点击添加按钮'''
    def add(self):
        try:
            self.frameElem.from_frame_to_otherFrame("rigthFrame")
            self.getElem.find_element_wait_and_click_EC("id", "save")
        except Exception:
            print("Click the Save button to fail")

    u'''点击删除按钮'''
    def delete(self):
        try:
            self.frameElem.from_frame_to_otherFrame("rigthFrame")
            self.getElem.find_element_wait_and_click_EC("id", self.DELETE)
        except Exception:
            print("Click the Delete button to fail")

    u'''点击复选框'''
    def subcheckbox(self):
        try:
            self.frameElem.from_frame_to_otherFrame("rigthFrame")
            self.getElem.find_element_wait_and_click_EC("id", self.SUB_CHECK_BOX)
        except Exception:
            print("Click the subcheckbox checkbox to fail")

    u'''定义类型
        Parameters：
	       -stauts:类型的value值
    '''
    def select_type(self, stauts):
       self.frameElem.from_frame_to_otherFrame("rigthFrame")
       selem = self.getElem.find_element_with_wait_EC("id", "auditStorageExtendType")
       self.selectElem.select_element_by_value(selem, stauts)

    u'''输入远端IP
	    Parameters：
	       -disip 远端IP
	'''
    def distal_ip(self, disip):
        disip = self.cnEn.is_float(disip)
        self.frameElem.from_frame_to_otherFrame("rigthFrame")
        self.getElem.find_element_wait_and_clear_EC("id", "distalIp")
        self.getElem.find_element_wait_and_sendkeys("id", "distalIp", disip)
        self.getElem.find_element_wait_and_click_EC("id", "distalPath")
        time.sleep(5)
        self.getElem.find_element_with_wait_EC("classname", "ip_succ")

    u'''输入远端路径
	    Parameters：
	       -dispath 远端路径
    '''
    def distal_path(self, dispath):
        try:
            self.frameElem.from_frame_to_otherFrame("rigthFrame")
            self.getElem.find_element_wait_and_clear_EC("id", self.DISTAL_PATH)
            self.getElem.find_element_wait_and_sendkeys("id", self.DISTAL_PATH, dispath)
        except Exception:
            print("distal path is error")

    u'''输入本地路径
	    Parameters：
	       -localpath 本地路径
    '''
    def local_path(self, localpath):
        try:
            self.frameElem.from_frame_to_otherFrame("rigthFrame")
            self.getElem.find_element_wait_and_clear_EC("id", self.LOCAL_PATH)
            self.getElem.find_element_wait_and_sendkeys("id", self.LOCAL_PATH,localpath )
        except Exception:
            print("local path is error")

    u'''输入远端账号
	    Parameters：
	       -disaccount 远端账号
    '''
    def distal_account(self, disaccount):
        try:
            self.frameElem.from_frame_to_otherFrame("rigthFrame")
            self.getElem.find_element_wait_and_clear_EC("id", self.DISTAL_ACCOUNT)
            self.getElem.find_element_wait_and_sendkeys("id", self.DISTAL_ACCOUNT, disaccount)
        except Exception:
            print("distal account is error")

    u'''输入远端密码
	    Parameters：
	       -dispasswd 远端密码
    '''
    def distal_passwd(self, dispasswd):
       try:
           self.frameElem.from_frame_to_otherFrame("rigthFrame")
           self.getElem.find_element_wait_and_clear_EC("id", self.DISTAL_PASSWD)
           self.getElem.find_element_wait_and_sendkeys("id", self.DISTAL_PASSWD, dispasswd)
       except Exception:
           print("distal passwd is error")

    u'''点击左侧框
	    Parameters：
	       -value： 0代表选择审计留存，1代表选择审计存储扩展
    '''
    def click_right_button(self, value):
        self.frameElem.from_frame_to_otherFrame("leftFrame")
        val = self.cnEn.is_float(value)
        if val == '0':
            self.getElem.find_element_wait_and_click_EC("id", "url0")
        else:
            self.getElem.find_element_wait_and_click_EC("id", "url1")

