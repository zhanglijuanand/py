#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from threading import Thread

sys.path.append("/testIsomp/common/")
from _excelRead import excelRead
from _cnEncode import cnEncode
from _transCoding import jsonTranscoding

sys.path.append("/testIsomp/testData/")
from _testDataPath import dataFileName

sys.path.append("/testIsomp/webElement/login/")
from loginElement import *

sys.path.append("/testIsomp/common")
from _icommon import commonFun
from _icommon import log
from _fileRead import fileRead
from _initDriver import initDriver
from _log import log

class testLogin(object):
    
    def __init__(self,driver):
        self.driver = driver
        self.log = log()
        self.loginFun = loginPage(self.driver)
        self.cmf = commonFun(self.driver)
        self.dataFile = dataFileName()

    u'''获取测试数据
    	Parameters:
    		- sheetname:sheet名称
    		return：表格数据
    '''
    def get_table_data(self,sheetname):
    	filePath = self.dataFile.get_login_test_data_url()
    	loginData = self.dataFile.get_data(filePath,sheetname)
    	return loginData
    	
    u'''登陆的div弹窗的xpath'''
    def login_msg(self):
    	login_msg = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"
    	return login_msg
    
    u'''根据访问方式类型登录测试
            parameters:
                sheetname : 表单名称
    '''
    def login_type(self,sheetname):
        loginMes = self.login_msg()
        loginData = self.get_table_data(sheetname)
        #无检查点的测试项标识，如果为True说明通过
        flag = False
        for dataRow in range(len(loginData)):
            #把单行的数据赋值给列表data
            data = loginData[dataRow]
            
            try:
                #如果不是第一行标题，则读取数据
                if dataRow != 0:
                    if sheetname == 'default':
                        self.loginFun.login(data)
#                           if dataRow == 1:
#                               loginFun.set_max_login_count()
                    elif sheetname == 'ad':
                        self.loginFun.ad_login(data)
                    elif sheetname == 'pwd_ad':
                        self.loginFun.ad_pwd_login(data)
                    elif sheetname == 'radius':
                        self.loginFun.radius_pwd_login(data)
                        
                        #如果登陆成功，点击退出
                    if self.loginFun.is_login_success():
                        self.loginFun.quit()
                        #设定没有检查点的测试项通过
                        flag = True
                        
                    self.cmf.test_win_check_point("xpath",loginMes,data,flag)
                    
                    #清空标识状态
                    flag = False
                    
            except Exception as e: 
                print ("User login fail: ") + str(e)
                #self.log.print_detail("login type error",e)

    #登陆测试
    def login(self):
        self.log.log_start("login")
        u'''可以循环设定数据测试系统登录'''
        sheets_name = ['default','ad','pwd_ad','radius']#'default','ad','pwd_ad','radius'
        for sheetname in sheets_name:
            self.login_type(sheetname)
        self.log.log_end("login")
        
        
#if __name__ == "__main__":#internet explorer
#    browser = setDriver().set_driver()
#    testLogin = testLogin(browser)
#    testLogin.login()

    
    '''
    lists = jsonTranscoding().set_brower()
    threads = []
    
    def execute_case(host,brower):
        driver = initDriver().remote_open_driver(host,brower)
        testLogin(driver).login()
        initDriver().close_driver(driver)
        
    for host,brower in lists.items():
        th = Thread(target=execute_case,args=(host,brower))
        th.start()
        threads.append(th)
            
    for th in threads:
        th.join()
    '''
        

    
    

        
        