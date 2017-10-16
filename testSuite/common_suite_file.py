#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import time
#导入驱动
sys.path.append("/testIsomp/common/")
from _icommon import getElement,selectElement,frameElement,commonFun
from _initDriver import initDriver
from _globalVal import globalValue
from _fileRead import fileRead

sys.path.append("/testIsomp/webElement/auth_method/")
from authMethodElement import AuthMethodPage

sys.path.append("/testIsomp/webElement/role/")
from test_roledf import Role

#导入登录
sys.path.append("/testIsomp/webElement/login/")
from loginElement import loginPage

sys.path.append("/testIsomp/testData/")
from _testDataPath import dataFileName

sys.path.append("/testIsomp/webElement/user/")
from userElement import UserPage

sys.path.append("/testIsomp/webElement/department/")
from test_dptm_ment import Department

sys.path.append("/testIsomp/webElement/resource/")
from test_resource_common import Resource
from test_windows_ment import WindowsResource
from databaseElement import DatabaseResource
from test_resource_accountmgr_ment import Accountmgr
sys.path.append("/testIsomp/webElement/group/")
from test_regroup_ment import Regroup
from test_usergroup_ment import Usergroup
sys.path.append("/testIsomp/webElement/client_conf")
from clientConfElement import ClientPage
sys.path.append("/testIsomp/webElement/rule")
from test_command_rule_ment import CommandRule

#导入应用发布
sys.path.append("/testIsomp/webElement/application")
from appConfElement import AppPage
sys.path.append("/testIsomp/webElement/authorization")
from authrizationElement import AuthorizationPage
sys.path.append("/testIsomp/testCase/authorization/")
from test_authorization import testAuthorization

class setDriver():
   
    u'''本地驱动'''
    def set_local_driver(self):
        driver = initDriver().open_driver()
        return driver

    u'''远程驱动'''
    def set_remote_driver(self):
        driver_lists = globalValue().get_value()
        driver = initDriver().remote_open_driver(driver_lists[0],driver_lists[1])
        
#        driver = initDriver().remote_open_driver("http://172.16.10.21:5555/wd/hub","firefox")
        return driver

    #获取驱动
    def set_driver(self):
         #读取test.conf文件内容
        fileList = fileRead().get_ip_address()
        #读取开关字符，0代表本地登录，1代表远程登录
        ipAdd = fileList[3].strip('\n')
        if ipAdd == '0':
            return self.set_local_driver()
        elif ipAdd == '1':
            return self.set_remote_driver()

class CommonSuiteData():
    
    def __init__(self,driver):
        self.driver = driver
        self.dataFile = dataFileName()
        self.cmf = commonFun(self.driver)
        self.initDriver = initDriver()
        self.loginElem = loginPage(self.driver)
        self.roleElem = Role(self.driver)
        self.userElem = UserPage(self.driver)
        self.frameElem = frameElement(self.driver)
        self.authElem = AuthMethodPage(self.driver)
        self.dptment = Department(self.driver)
        self.resource = Resource(self.driver)
        self.account = Accountmgr(self.driver)
        self.windowsElem = WindowsResource(self.driver)
        self.databaseElem = DatabaseResource(self.driver)
        self.usergroup = Usergroup(self.driver)
        self.regroup = Regroup(self.driver)
        self.appElem = AppPage(self.driver)
        self.authorizationElem = AuthorizationPage(self.driver)
        self.testAutho = testAuthorization(self.driver)
        self.clientElem = ClientPage(self.driver)
        self.command = CommandRule(self.driver)

    u'''切换模块
            parameter:
                levelText1 : 一级模块名称
                levelText2 : 二级模块名称
    '''     
    def switch_to_moudle(self,levelText1,levelText2):
        time.sleep(1)
        self.frameElem.from_frame_to_otherFrame("topFrame")
        
        self.cmf.select_menu(levelText1)
        self.cmf.select_menu(levelText1,levelText2)
    

#-----------------------------------角色相关----------------------------------        
    u'''填写角色基本信息'''
    def set_role_basic_info(self,list):
#        self.cmf.select_menu(u'角色管理',u'角色定义')
        self.switch_to_moudle(u'角色管理',u'角色定义')
        self.roleElem.add()
        self.roleElem.edit_rolename(list[0])
        self.roleElem.edit_shortname(list[1])
        
    u'''系统级角色模板
            parameter : 
                list : 角色数据列表
    '''
    def set_sys_role(self,list):
        self.set_role_basic_info(list)
        self.roleElem.select_sysrole()
        self.roleElem.save_button()
        self.roleElem.click_ok_button()
    
    u'''部门级角色模板
            parameter : 
                list : 角色列表数据
    '''    
    def set_dep_role(self,list):
        self.set_role_basic_info(list)
        self.roleElem.level()
        time.sleep(1)
#        self.driver.implicitly_wait(10)
        self.roleElem.select_dptrole()
        self.roleElem.save_button()
        self.roleElem.click_ok_button()
    
    u'''删除角色'''
    def del_role(self):
        self.switch_to_moudle(u'角色管理',u'角色定义')
        self.cmf.check_all()
        self.cmf.bulkdel("delete_role")
        self.roleElem.click_ok_button()

#----------------------------------------用户相关------------------------------  
    
    u'''填写用户信息
            parameters:
                data[1] : 用户名称
                data[3] : 用户账号
                data[4] : 用户密码
                data[5] : 确认密码
                data[6] : 开始时间
                data[7] : 访问方式
                data[8] : AD域账号
                roleText : 用户角色
    '''
    def set_user_basic_info(self,data,roleText):
        
#        self.cmf.select_menu(u"运维管理",u"用户")
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        self.userElem.add_button()
        self.userElem.set_user_account(data[3])
        self.userElem.set_user_name(data[1])
        self.userElem.set_user_pwd(data[4])
        self.userElem.set_user_enquire_pwd(data[5])
        self.userElem.set_start_time(data[6])
        if data[10] != "":
            self.userElem.set_dep(data[10])
        if data[7] !="":
            #设置访问方式
            self.userElem.click_advanced_option()
            self.userElem.set_auth_method_rule(data[7])
            
            #访问方式不是默认方式
            if int(data[7]) != 2:
                self.userElem.set_ad_name(data[8])
        if data[9] != "":
            self.userElem.set_user_role(roleText)
            self.userElem.click_role_add_button()
        self.userElem.save_button()
        self.cmf.click_login_msg_button()
        

    u'''删除用户'''
    def del_user(self):
        self.switch_to_moudle(u"运维管理",u"用户")
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        self.userElem.select_all_button()
        self.userElem.del_button()
        self.frameElem.switch_to_content()
        self.cmf.click_login_msg_button()
        self.cmf.click_login_msg_button()
    
    u'''用户退出'''
    def user_quit(self):
        self.loginElem.quit()
    
#-----------------------------部门--------------------------------------------
    u'''填写部门名称
            parameters :
                data[0] : 部门名称
                data[1] : 操作类型(添加：0)
                data[2] : 添加的部门名称
    '''
    def set_dep(self,data):
        self.switch_to_moudle(u"运维管理",u"组织定义")
        self.dptment.click_left_department()
        #点击展开按钮
        self.dptment.click_dept_switch()
        self.dptment.click_basic_operation(data[0], int(data[1]))
        self.dptment.popup_sendkey(data[2])
        self.dptment.click_ok_button()
        self.cmf.click_login_msg_button()
    
    def set_del_dep(self,data):
        self.switch_to_moudle(u"运维管理",u"组织定义")
        self.dptment.click_left_department()
        self.dptment.click_dept_switch()
        self.dptment.click_basic_operation(data[0],int(data[1]))
        self.cmf.click_login_msg_button()
        self.cmf.click_login_msg_button()
        
#-----------------------------用户组------------------------------------------    
    u'''添加用户到用户组'''
    def set_user_to_group(self,data):
#        self.usergroup.click_left_usergroup()
#        self.usergroup.click_usergroup_switch()
        self.usergroup.click_usergroup_add_user(data[3], data[4])
        self.regroup.check_depart(data[5])
        self.usergroup.click_usergroup_add_user_query()
        self.regroup.check_all_resource()
        self.regroup.click_resource_okbutton()
        self.cmf.click_login_msg_button()
    
    u'''填写用户组信息
            parameters:
                data[0] : 操作类型(添加：0)
                data[1] : 部门名称
                data[2] : 编辑的用户组名称
                data[3] : 添加的用户组名称
    '''
    def set_add_user_group(self,data):
        self.switch_to_moudle(u"运维管理",u"组织定义")
        self.usergroup.click_left_usergroup()
        self.usergroup.click_usergroup_switch()
        self.usergroup.usergroup_click_basic_operation(int(data[0]), data[1], data[2])
        self.dptment.popup_sendkey(data[3])
        self.dptment.click_ok_button()
        self.cmf.click_login_msg_button()
        if data[4] != "":
            self.set_user_to_group(data)
    
    u'''删除用户组
            parameters :
                data[0] : 操作类型(删除:4)
                data[1] : 部门名称
                data[2] : 删除的用户组名称
    '''
    def set_del_user_group(self,data):
        self.switch_to_moudle(u"运维管理",u"组织定义")
        self.usergroup.click_left_usergroup()
        self.usergroup.click_usergroup_switch()
        self.usergroup.usergroup_click_basic_operation(int(data[0]), data[1], data[2])
        self.cmf.click_login_msg_button()
        self.cmf.click_login_msg_button()
        
#-----------------------------资源组------------------------------------------    
    u'''添加资源到资源组'''
    def set_res_to_group(self,data):
#        self.regroup.click_left_regroup()
#        self.regroup.click_regroup_switch()
        self.regroup.click_regroup_add_resouce(data[3], data[4])
        self.regroup.check_depart(data[5])
        self.regroup.click_regroup_add_resouce_query()
        self.regroup.check_all_resource()
        self.regroup.click_resource_okbutton()
        self.cmf.click_login_msg_button()
    
    u'''填写资源组信息
            parameters:
                data[0] : 操作类型(添加：0)
                data[1] : 部门名称
                data[2] : 编辑的资源组名称
                data[3] : 添加的资源组名称
    '''    
    def set_add_res_group(self,data):
        self.switch_to_moudle(u"运维管理",u"组织定义")
        self.regroup.click_left_regroup()
        self.regroup.click_regroup_switch()
        self.regroup.regroup_click_basic_operation(int(data[0]), data[1], data[2])
        self.dptment.popup_sendkey(data[3])
        self.dptment.click_ok_button()
        self.cmf.click_login_msg_button()
        if data[4] != "":
            self.set_res_to_group(data)
    
    u'''删除资源组
            parameters :
                data[0] : 操作类型(删除:4)
                data[1] : 部门名称
                data[2] : 删除的资源组名称
    '''
    def set_del_res_group(self,data):
        self.switch_to_moudle(u"运维管理",u"组织定义")
        self.regroup.click_left_regroup()
        self.regroup.click_regroup_switch()
        self.regroup.regroup_click_basic_operation(int(data[0]), data[1], data[2])
        self.cmf.click_login_msg_button()
        self.cmf.click_login_msg_button()
    

#-----------------------------资源--------------------------------------------
    u'''填写资源基本信息
            parameters : 
                data[0]:资源类型
                data[1]:资源名称
                data[2]:资源IP
                data[3]:部门
    '''
    def set_resource_info(self,data):
        self.switch_to_moudle(u"运维管理",u"资源")
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        self.resource.click_add_edit_button()
        self.resource.select_resource_type(data[0])
        self.resource.set_resource_name(data[1])
        self.resource.set_resource_ip(data[2])
        if data[3] != 'no':
            time.sleep(5)
            self.resource.set_depart(data[3])
        #选择协议
        if data[4] != "":
            self.resource.select_agreement(data[4])
        if data[5] != "":
            self.resource.click_account_sync()
            self.resource.set_admin_account(data[5])
            self.resource.set_admin_pwd(data[6])
            self.resource.set_confirm_pwd(data[7])
        #提权口令
        if data[8] != "":
            self.resource.click_up_super()
            self.resource.set_super_pwd(data[8])
            self.resource.set_super_confirm_pwd(data[9])
        #填写域名
        if data[10] != "":
            self.databaseElem.set_domain_name(data[10])
        #账号分类
        if data[11] != "":
            self.resource.click_account_sync()
            self.windowsElem.select_account_type(data[11])
        #归属域控主机
        if data[12] != "":
            self.windowsElem.select_attach_domian(data[12])
        #主机名
        if data[13] != "":
            self.databaseElem.set_host_name(data[13])
        
        self.resource.click_save_button()
        self.cmf.click_login_msg_button()
        time.sleep(3)
#        self.driver.implicitly_wait(3)
        self.cmf.back()
    
    u'''填写数据库基本信息'''
    def set_database_res_info(self,data):
        self.switch_to_moudle(u"运维管理",u"资源")
        self.frameElem.from_frame_to_otherFrame("mainFrame")        
        self.resource.click_add_edit_button()
        self.resource.select_resource_type(data[2])
        self.databaseElem.add_edit_database_resource(data)
        self.cmf.click_login_msg_button()
        time.sleep(3)
        self.cmf.back()
    
    u'''删除单一资源'''
    def del_one_resource(self,resName):
        self.switch_to_moudle(u"运维管理", u"资源")
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        self.resource.click_del_button(resName)
        self.cmf.click_login_msg_button()
        self.cmf.click_login_msg_button()        
    
    u'''删除全部资源'''
    def del_resource(self):
        self.switch_to_moudle(u"运维管理", u"资源")
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        self.cmf.check_all()
        self.cmf.bulkdel("delete_resource")
        self.cmf.click_login_msg_button()
        self.cmf.click_login_msg_button()
        
    u'''填写资源账号基本信息
            parameters: 
                data[1]:资源名称
                data[4] : 账号编辑方式
                data[5] : 账号名称
                data[6] : 口令
                data[7] : 确认口令
    '''
    def set_res_account(self,data):
        self.switch_to_moudle(u"运维管理",u"资源")
        self.account.click_account_manage_button(data[0])
        self.account.click_account_add_edit_button(data[2])
        self.account.select_edit_way(data[1])
        if data[2] != "no":
            self.account.set_account_name(data[2])
        self.account.set_account_pwd(data[3])
        self.account.set_account_confirm_pwd(data[4])
        self.account.set_authorize()
        self.account.click_save_account()
        self.cmf.click_login_msg_button()

#-----------------------------授权----------------------------------------
    u'''填写授权基本信息
            parameters:
                data[1]:授权名称
                data[2]:部门名称
                data[3]:状态
    '''
    def set_authorization(self, data):
        self.switch_to_moudle(u'运维管理', u'授权')
        self.authorizationElem.add_button()
        self.authorizationElem.set_auth_name(data[1])
        self.authorizationElem.set_dep(data[2], data[3])
        self.authorizationElem.click_add_user()
        self.authorizationElem.set_select_user_search_button()
        self.authorizationElem.set_user_check_all_button()
        self.authorizationElem.set_ok_button()
        #添加资源
        self.authorizationElem.click_add_res()
        self.authorizationElem.set_select_res_search_button()
        self.authorizationElem.set_res_check_all_button()
        self.authorizationElem.set_ok_button()
        self.authorizationElem.save_button()
        self.cmf.click_login_msg_button()
        self.cmf.back()
#---------------------------------填写应用发布信息----------------------------
    u'''填写应用发布信息'''
    def set_application_info(self,data):
        self.switch_to_moudle(u"系统配置",u"关联服务")
        self.appElem.app_module_button()
        self.appElem.click_add_button()
        self.appElem.set_name(data[0])
        self.appElem.set_ip(data[1])
        self.appElem.set_app_account(data[3])
        self.appElem.set_pwd(data[4])
        self.appElem.set_repwd(data[5])
        self.appElem.ip_is_succ()
        self.appElem.click_save_button()
        self.cmf.click_login_msg_button()

    u'''删除应用发布'''
    def del_application(self):
        self.switch_to_moudle(u"系统配置",u"关联服务")
        self.appElem.app_module_button()
        self.appElem.del_all()
        self.cmf.click_login_msg_button()
        self.cmf.click_login_msg_button()
    
#-------------------------------------客户端-----------------------------------
    u'''填写客户端基本信息'''
    def set_client_info(self,data):
        #self.switch_to_moudle(u"系统配置",u"客户端配置")
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        self.clientElem.add_button()
        self.clientElem.set_client_name(data[2])
        self.clientElem.set_action_stream(data[3])
        self.clientElem.set_database_res_type(data[0],data[1])
        self.clientElem.save_button()
    
    u'''删除客户端'''
    def set_delete_client_info(self,data):
        #self.switch_to_moudle(u"系统配置",u"客户端配置")
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        self.clientElem.select_query_res_type(data[0],data[1])
        self.clientElem.click_query_button()
        self.clientElem.del_operation(data[2])
        self.cmf.click_login_msg_button()
    
#------------------------------资源账号授权------------------------------------
    u'''添加用户和资源账号类型的授权'''
    def set_authorization_info(self,data):
        self.switch_to_moudle(u"运维管理",u"授权")
        self.testAutho.common_part(data)
        self.testAutho.add_user(data)
        self.authorizationElem.click_add_res_account()
        self.authorizationElem.set_select_res_ip(data[6])
        self.authorizationElem.set_select_res_account(data[8])
        self.authorizationElem.set_select_res_search_button()
        self.authorizationElem.set_res_check_all_button()
        self.authorizationElem.set_ok_button()
        self.authorizationElem.res_account_status()
        self.authorizationElem.save_button()
        self.cmf.click_login_msg_button()

    u'''删除授权'''
    def del_authorization(self):
        self.switch_to_moudle(u"运维管理", u"授权")
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        self.authorizationElem.check_all()
        self.authorizationElem.del_button()
        self.cmf.click_login_msg_button()
        self.cmf.click_login_msg_button()

        
#-----------------------------数据----------------------------------------
    u'''获取数据
        Parameters:
            - sheetname:sheet名称
            return：表格数据
    '''
    def get_table_data(self,sheetname):
        filePath = self.dataFile.get_common_suite_test_data_url()
        fileData = self.dataFile.get_data(filePath,sheetname)
        return fileData
    
    u'''添加应用发布'''
    def add_application(self):
        app_data = self.get_table_data('add_application')
        for dataRow in range(len(app_data)):
            data = app_data[dataRow]
            if dataRow != 0:
                self.set_application_info(data)

    u'''初始化用户登录'''
    def isomper_login(self):
        login_data = self.get_table_data('isomper')
        logindata = login_data[1]
        self.loginElem.login(logindata)
    
    u'''添加系统级角色'''   
    def add_sys_role(self):
        role_data = self.get_table_data("add_role")
        roleData = role_data[1]
        self.set_sys_role(roleData)
    
    u'''添加部门级角色'''    
    def add_dep_role(self):
        role_data = self.get_table_data("add_role")
        roleData = role_data[2]
        self.set_dep_role(roleData)
    
    u'''添加用户数据模板'''
    def add_user_data_module(self,rowList):
        self.switch_to_moudle(u"运维管理",u"用户")
        user_data = self.get_table_data("common_user")
        for dataRow in rowList:
            data = user_data[dataRow]
            if dataRow != 0:
                self.set_user_basic_info(data,data[9])
                self.userElem.click_back_button()
        
    u'''添加系统管理员和部门管理员的用户'''
    def add_user_with_role(self):
        rowList = [1]
        self.add_user_data_module(rowList)
        
    u'''登录并切换至角色公用方法
            parameters: 
                login_status ：'no'(登录状态：没有登录)
    '''
    def login_and_switch_to_common(self,login_status='no'):
        login_data = self.get_table_data("common_user")
        logindata = login_data[1]
        if login_status == 'no':
            self.loginElem.login(logindata)
        
        #获取角色
        roleList = logindata[9].split(',')
        return roleList

    u'''使用添加的用户登录并切换至系统级角色'''
    def login_and_switch_to_sys(self):
        roleList = self.login_and_switch_to_common()
        self.cmf.select_role_by_text(roleList[0])
    
    u'''使用添加的用户登录并切换至部门级角色'''
    def login_and_switch_to_dep(self):
        roleList = self.login_and_switch_to_common()
        self.cmf.select_role_by_text(roleList[1])
    
    u'''切换至部门级'''    
    def sys_switch_to_dep(self):
        roleList = self.login_and_switch_to_common("login")
        self.cmf.select_role_by_text(roleList[1])
    
    u'''切换至系统级'''    
    def dep_switch_to_sys(self):
        roleList = self.login_and_switch_to_common("login")
        self.cmf.select_role_by_text(roleList[0]) 
    
    u'''切换至运维操作员'''
    def switch_to_operation(self):
        self.cmf.select_role_by_text(u"运维操作员")
    
    #使用新添加的用户登录
    def use_new_user_login(self):
        login_data = self.get_table_data("common_user")
        logindata = login_data[1]
        time.sleep(2)
        self.loginElem.login(logindata)
    
    u'''运维管理员登录'''
    def sso_user_login(self,rowList):
        login_data = self.get_table_data("common_user")
        logindata = login_data[rowList]
        time.sleep(1)
        self.loginElem.login(logindata)
    
    u'''运维管理员AD域方式登录'''
    def sso_user_ad_login(self,rowList):
        login_data = self.get_table_data("common_user")
        logindata = login_data[rowList]
        self.frameElem.switch_to_content()
        self.loginElem.set_login_method(logindata[2])
        self.loginElem.set_ad_login_username(logindata[3])
        self.loginElem.set_ad_login_pwd(logindata[11])
        time.sleep(1)
        self.loginElem.click_login_button()
        
    u'''添加认证配置'''
    def add_meth_method(self):
        meth_data = self.get_table_data("meth_method")
        methData = meth_data[1]
        
        self.switch_to_moudle(u"策略配置",u"认证强度")
        
        self.authElem.select_all_auth(methData)
    
    u'''会话配置,设置最大登录数'''
    def set_login_max_num(self):
        self.loginElem.set_max_login_count()
    
    u'''添加登录测试数据'''
    def add_login_data(self):
        rowList = [2,3,4,5,6,7]
        self.add_user_data_module(rowList)
    
    u'''添加授权用户'''
    def add_authorization_user(self):
        rowList = [8,9,10,11,12]
        self.add_user_data_module(rowList)
    
    u'''添加应用发布用户'''
    def add_app_user(self):
        rowList = [3]
        self.add_user_data_module(rowList)
    
    u'''添加单点登录用户'''
    def add_sso_user(self):
        rowList = [6,8,9,10,11,13]
        self.add_user_data_module(rowList)
        
    u'''添加部门'''
    def add_dep(self, rowList):
        dep_data = self.get_table_data("add_dep")
        for dataRow in rowList:
            data = dep_data[dataRow]
            if dataRow != 0:
                self.set_dep(data)
    
    u'''删除部门'''
    def del_dep(self, rowList):
        dep_data = self.get_table_data("del_dep")
        for dataRow in rowList:
            data = dep_data[dataRow]
            if dataRow != 0:
                self.set_del_dep(data)
    
    u'''增加资源数据模板'''
    def add_resource_modele(self,rowList):
        res_data = self.get_table_data("add_res")
        for dataRow in rowList:
            data = res_data[dataRow]
            if dataRow != 0:
                self.set_resource_info(data)
    
    u'''添加授权资源'''
    def add_resource(self):
        rowList = [1,2]
        self.add_resource_modele(rowList)
    
    u'''添加sso资源'''
    def add_sso_resource(self):
        #rowList = [1,2,3,4,5,7,8]
        rowList = [1,3,4,5]
        self.add_resource_modele(rowList)
    
    u'''添加依附操作系统'''
    def add_database_resource(self):
        rowList = [2]
        self.add_resource_modele(rowList)
    
    u'''添加资源账号数据模板'''
    def add_res_account_module(self,rowList):
        account_data = self.get_table_data("res_account")
        for dataRow in rowList:
            data = account_data[dataRow]
            if dataRow != 0:
                self.set_res_account(data)    
    
    u'''添加授权资源账号'''
    def add_res_account(self):
        rowList = [1,3]
        self.add_res_account_module(rowList)
    
    u'''添加sso资源账号'''
    def add_sso_res_account(self):
        rowList = [1,2,4,5,6,7]
        #rowList = [1,2,3,4,5,6,7,9,10]
        self.add_res_account_module(rowList)
        
    u'''添加用户组'''
    def add_user_group(self):
        user_group_data = self.get_table_data("add_user_group")
        for dataRow in range(len(user_group_data)):
            data = user_group_data[dataRow]
            if dataRow != 0:
                self.set_add_user_group(data)
    
    u'''删除用户组'''
    def del_user_group(self):
        user_group_data = self.get_table_data("del_user_group")
        for dataRow in range(len(user_group_data)):
            data = user_group_data[dataRow]
            if dataRow != 0:
                self.set_del_user_group(data)
    
    u'''添加资源组'''
    def add_res_group(self):
        res_group_data = self.get_table_data("add_res_group")
        for dataRow in range(len(res_group_data)):
            data = res_group_data[dataRow]
            if dataRow != 0:
                self.set_add_res_group(data)
    
    u'''删除资源组'''
    def del_res_group(self):
        res_group_data = self.get_table_data("del_res_group")
        for dataRow in range(len(res_group_data)):
            data = res_group_data[dataRow]
            if dataRow != 0:
                self.set_del_res_group(data)

    u'''添加授权'''
    def add_authrization(self, rowList):
        auth_data = self.get_table_data("add_authorization")
        for dataRow in rowList:
            data = auth_data[dataRow]
            if dataRow != 0:
                self.set_authorization(data)

    u'''添加授权数据模板'''
    def add_authorization_module(self,rowList):
        autho_data = self.get_table_data("add_account_auth")
        for dataRow in rowList:
            data = autho_data[dataRow]
            if dataRow != 0:
                self.set_authorization_info(data)
                self.authorizationElem.back_button()
                
    u'''添加单点登录授权'''
    def add_sso_authorization(self):
        rowList = [1]
        #rowList = [1,2,3,4,5,6,7]
        self.add_authorization_module(rowList)
    
    u'''添加客户端数据模板'''
    def add_client_module(self,rowList):
        client_data = self.get_table_data("add_client")
        self.switch_to_moudle(u"系统配置",u"客户端配置")
        for dataRow in rowList:
            data = client_data[dataRow]
            if dataRow != 0:
                self.set_client_info(data)
    
    u'''删除客户端数据模板'''
    def del_client_module(self,rowList):
        client_data = self.get_table_data("del_client")
        self.switch_to_moudle(u"系统配置",u"客户端配置")
        for dataRow in rowList:
            data = client_data[dataRow]
            if dataRow != 0:
                self.set_delete_client_info(data)
    
    u'''添加数据库资源模板'''
    def add_database_res_module(self,rowList):
        database_data = self.get_table_data("add_database")
        for dataRow in rowList:
            data = database_data[dataRow]
            if dataRow != 0:
                self.set_database_res_info(data)

#-------------------------------前置条件---------------------------------------
    u'''前置条件通用'''
    def module_common_prefix_condition(self):
        self.isomper_login()
        self.add_sys_role()
        self.add_dep_role()

    u'''后置条件通用'''
    def module_common_post_condition(self):
        #删除角色
        self.del_role()
        #用户退出
        self.user_quit()
        self.isomper_login()
        #删除用户
        self.del_user()
        self.user_quit()
    
#------------------------------用户模块前置条件--------------------------------
    u'''用户模块前置条件'''
    def user_module_prefix_condition(self):
        self.module_common_prefix_condition()
        self.switch_to_moudle(u'运维管理',u'用户')
    
    u'''用户模块后置条件'''
    def user_module_post_condition(self):
        self.del_role()

#--------------------------认证方式前置条件------------------------------------
    u'''认证方式前置条件'''
    def auth_method_prefix_condition(self):
        self.module_common_prefix_condition()
        self.add_user_with_role()
        #初始化用户退出
        self.user_quit()
        #使用添加的用户登录并切换至系统管理员角色
        self.login_and_switch_to_sys()
        self.switch_to_moudle(u"策略配置",u"认证强度")
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        
    u'''认证方式后置条件'''
    def auth_method_post_condition(self):
        #系统管理员退出
        self.user_quit()
        self.isomper_login()
        self.del_user()
        self.del_role()
        self.user_quit()
        
#---------------------------------登录模块前置条件-----------------------------
    u'''登录模块前置条件'''
    def login_module_prefix_condition(self):
        self.module_common_prefix_condition()
        self.add_user_with_role()
        #初始化用户退出
        self.user_quit()
        #使用添加的用户登录并切换至系统管理员角色
        self.login_and_switch_to_sys()
        #配置认证方式
        self.add_meth_method()
        #配置最大登录数
        self.set_login_max_num()
        #添加登录用户数据
        self.add_login_data()
        #改变a的状态为关
        self.userElem.change_user_status_off("a")
        #系统管理员退出
        self.user_quit()
    
    u'''登录模块后置条件'''
    def login_module_post_condition(self):
        self.isomper_login()
        self.del_user()
        self.del_role()
    
#------------------------------授权前置条件-----------------------------------
    def authori_module_prefix_condition(self):
        self.module_common_prefix_condition()
        self.add_user_with_role()
        self.user_quit()
        self.login_and_switch_to_dep()
        self.add_resource()
        self.add_res_account()

        self.add_authorization_user()

        self.add_res_group()
        self.add_user_group()

        self.switch_to_moudle(u'运维管理',u'授权')
        
    def authori_module_post_condition(self):
        self.del_resource()
        self.del_res_group()
        self.del_user_group()
        self.auth_method_post_condition()
    
#-----------------------------客户端配置前置条件------------------------------
    def client_module_prefix_condition(self):
        self.module_common_prefix_condition()
        self.add_user_with_role()
        self.user_quit()
        self.login_and_switch_to_sys()
        self.switch_to_moudle(u"系统配置", u"客户端配置")
    
    def client_module_post_condition(self):
        self.auth_method_post_condition()

#-------------------------------应用发布后置条件-------------------------------
    def application_module_prefix_condition(self):
        self.module_common_prefix_condition()
        self.add_user_with_role()
        self.add_app_user()
        self.user_quit()
        self.login_and_switch_to_sys()
        self.switch_to_moudle(u"系统配置", u"关联服务")

#-----------------------------数据库前置条件----------------------------------
    def database_resource_prefix_condition(self):
        self.module_common_prefix_condition()
        self.add_user_with_role()
        self.user_quit()
        self.login_and_switch_to_sys()
        #添加应用发布
        self.add_application()
        self.user_quit()
        self.login_and_switch_to_dep()
        self.add_database_resource()
        self.switch_to_moudle(u"运维管理",u"资源")
        
    def database_resource_post_condition(self):
        self.user_quit()
        self.login_and_switch_to_sys()
        self.del_application()
        self.auth_method_post_condition()
    
#------------------------------命令单点登录前置条件----------------------------
    u'''单点登录前置条件'''
    def sso_prefix_condition(self):
        self.module_common_prefix_condition()
        self.add_user_with_role()
        self.user_quit()
#        self.login_and_switch_to_sys()
        #配置认证方式
#        self.add_meth_method()
#        self.add_sso_user()
#        self.sys_switch_to_dep()
        self.login_and_switch_to_dep()
        self.add_sso_resource()
        self.add_sso_res_account()
        self.add_sso_authorization()
        self.switch_to_operation()
        #self.user_quit()
        #self.login_and_switch_to_common()
    
    u'''单点登录后置条件'''
    def sso_post_condition(self):
        self.user_quit()
        self.login_and_switch_to_dep()
        self.del_authorization()
        #self.del_one_resource("yunei")
        self.del_resource()
        self.auth_method_post_condition()
        
#------------------------------windows单点登录前置条件-------------------------
    u'''windows单点登录前置条件'''
    def windows_sso_prefix_condition(self):
        self.module_common_prefix_condition()
        self.add_user_with_role()
        self.user_quit()
        self.login_and_switch_to_sys()
        #配置认证方式
        self.add_meth_method()
        self.add_user_data_module([6])
        self.sys_switch_to_dep()
        #self.login_and_switch_to_dep()
        self.add_resource_modele([2,7,8])
        self.add_res_account_module([3,9,10])
        self.add_authorization_module([3,4])
        self.switch_to_operation()
        #self.user_quit()
        #self.login_and_switch_to_common()
    
    u'''单点登录后置条件'''
    def windows_sso_post_condition(self):
        self.user_quit()
        self.login_and_switch_to_dep()
        self.del_authorization()
        self.del_one_resource("yunei")
        self.del_resource()
        self.auth_method_post_condition()

        
#------------------------------数据库单点登录前置条件-------------------------
    u'''数据库单点登录前置条件'''
    def database_sso_prefix_condition(self):
        self.module_common_prefix_condition()
        self.add_user_with_role()
        self.user_quit()
        self.login_and_switch_to_sys()
        #添加应用发布
        self.add_application()
        #添加客户端
        self.add_client_module([1,2])
        #self.add_user_data_module([8])
        self.sys_switch_to_dep()
        #self.login_and_switch_to_dep()
        self.add_database_res_module([1,2,3])
        self.add_res_account_module([11,12,13])
        self.add_authorization_module([5])
        self.switch_to_operation()
    
    u'''数据库单点登录后置条件'''
    def database_sso_post_condition(self):
        self.user_quit()
        self.login_and_switch_to_sys()
        self.del_application()
        self.sys_switch_to_dep()
        self.del_authorization()
        self.del_resource()
        self.dep_switch_to_sys()
        self.del_client_module([1,2])
        self.auth_method_post_condition()


#------------------------------角色前置条件-----------------------------------
    def role_module_prefix_condition(self):
        #初始化用户登录
        self.isomper_login()
        #添加用户
        self.add_user_data_module([2])
        #切换到角色定义页面
        self.switch_to_moudle(u"角色管理", u"角色定义")

    def role_module_post_condition(self):
        #用初始化用户登录删除用户
        self.del_user()
        #用户退出
        self.user_quit()

#------------------------------部门前置条件-----------------------------------
    def depart_module_prefix_condition(self):
        self.module_common_prefix_condition()
        self.add_user_with_role()
        #退出
        self.user_quit()
        #使用添加的用户登录并切换至系统级角色
        self.login_and_switch_to_sys()
        #切换到组织定义
        self.switch_to_moudle(u"运维管理", u"组织定义")

    def depart_module_post_condition(self):
        self.module_common_post_condition()

#------------------------------资源前置条件-----------------------------------
    def resource_module_prefix_condition(self):
        self.module_common_prefix_condition()
        self.add_user_with_role()
        #退出
        self.user_quit()
        #使用添加的用户登录并切换至系统级角色
        self.login_and_switch_to_sys()
        #切换到组织定义
        self.switch_to_moudle(u"运维管理", u"组织定义")
        #添加部门
        self.add_dep([1])
        #切换至部门级角色
        self.sys_switch_to_dep()
        #切换到资源
        self.switch_to_moudle(u"运维管理", u"资源")

    def resource_module_post_condition(self):
        #切换至系统级角色
        self.dep_switch_to_sys()
        #切换到组织定义
        self.switch_to_moudle(u"运维管理", u"组织定义")
        #删除部门
        self.del_dep([1])
        self.module_common_post_condition()

#------------------------------资源组前置条件-----------------------------------
    def regroup_module_prefix_condition(self):
        self.module_common_prefix_condition()
        self.add_user_with_role()
        #退出
        self.user_quit()
        #使用添加的用户登录并切换至部门级角色
        self.login_and_switch_to_dep()
        #切换到资源
        self.switch_to_moudle(u"运维管理", u"资源")
        #添加资源
        self.add_resource_modele([9,6])
        #切换到组织定义
        self.switch_to_moudle(u"运维管理", u"组织定义")

    def regroup_module_post_condition(self):
        #删除资源
        self.del_resource()
        #切换至系统级角色
        self.dep_switch_to_sys()
        self.module_common_post_condition()

#------------------------------用户组前置条件-----------------------------------
    def usergroup_module_prefix_condition(self):
        self.module_common_prefix_condition()
        self.add_user_with_role()
        #添加用户
        self.add_user_data_module([2,3,4,5])
        #退出
        self.user_quit()
        #使用添加的用户登录并切换至部门级角色
        self.login_and_switch_to_dep()
        #切换到组织定义
        self.switch_to_moudle(u"运维管理", u"组织定义")

    def usergroup_module_post_condition(self):
        #切换至系统级角色
        self.dep_switch_to_sys()
        self.module_common_post_condition()

#------------------------------流程前置条件-----------------------------------
    def process_module_prefix_condition(self):
        self.module_common_prefix_condition()
        self.add_user_with_role()
        #添加用户
        self.add_user_data_module([2,3,5,11])
        #退出
        self.user_quit()
        #使用添加的用户登录并切换至部门级角色
        self.login_and_switch_to_dep()
        #切换到资源
        self.switch_to_moudle(u"运维管理", u"资源")
        #添加资源
        self.add_resource_modele([9,6])
        #添加资源账号
        self.add_res_account_module([3,8])
        #切换到授权
        self.switch_to_moudle(u'运维管理', u'授权')
        self.add_authrization([1])

    def process_module_post_condition(self):
        #用户登录切换部门角色
        self.login_and_switch_to_dep()
        #删除授权
        self.del_authorization()
        #删除资源
        self.del_resource()
        #切换至系统级角色
        self.dep_switch_to_sys()
        self.module_common_post_condition()

#------------------------------命令规则前置条件-----------------------------------
    def commandrule_module_prefix_condition(self):
        self.module_common_prefix_condition()
        self.add_user_with_role()
        #添加用户
        self.add_user_data_module([2])
        #退出
        self.user_quit()
        #使用添加的用户登录并切换至部门级角色
        self.login_and_switch_to_dep()
        #切换到资源
        self.switch_to_moudle(u"运维管理", u"资源")
        #添加资源
        self.add_resource_modele([3])
        #添加资源账号
        self.add_res_account_module([4])
        #切换到授权
        self.switch_to_moudle(u'运维管理', u'授权')
        self.add_authorization_module([2])
        #切换到规则定义
        self.switch_to_moudle(u'运维管理', u'规则定义')
        self.command.click_left_rule(0)

    def commandrule_module_post_condition(self):
        #删除授权
        self.del_authorization()
        #删除资源
        self.del_resource()
        #切换至系统级角色
        self.dep_switch_to_sys()
        self.module_common_post_condition()

#------------------------------时间规则前置条件-----------------------------------
    def timerule_module_prefix_condition(self):
        self.module_common_prefix_condition()
        self.add_user_with_role()
        #添加用户
        self.add_user_data_module([2,3,5,11,14])
        #退出
        self.user_quit()
        #使用添加的用户登录并切换至部门级角色
        self.login_and_switch_to_dep()
        #切换到规则定义
        self.switch_to_moudle(u'运维管理', u'规则定义')
        self.command.click_left_rule(1)

    def timerule_module_post_condition(self):
        #切换至系统级角色
        self.dep_switch_to_sys()
        self.module_common_post_condition()




#if __name__ == "__main__":
#    driver = setDriver().set_local_driver()
#    commonDataElem =  CommonSuiteData(driver)
#    commonDataElem.authori_module_prefix_condition()
#    commonDataElem.authori_module_post_condition()
#    commonDataElem.isomper_login()
#    commonDataElem.add_sys_role()
#    commonDataElem.add_dep_role()
#    commonDataElem.add_login_data()
#    commonDataElem.add_user_with_role()
#    commonDataElem.user_quit()
#    commonDataElem.login_and_switch_to_sys()
#    commonDataElem.add_login_data()
#    commonDataElem.login_and_switch_to_dep()
#    commonDataElem.add_res_group()
#    commonDataElem.del_res_group()
#    
#    commonDataElem.add_user_group()
#    commonDataElem.del_user_group()

#
#    commonDataElem.login_and_switch_to_dep()
#    commonDataElem.add_resource()
#    commonDataElem.del_resource()
#    commonDataElem.add_dep()
#    commonDataElem.del_dep()
#    commonDataElem.add_meth_method()
#    commonDataElem.set_login_max_num()
