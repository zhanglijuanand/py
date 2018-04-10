#coding=utf-8
u''' 
#文件名：
#被测软件版本号：V2.8.1
#作成人：李择优
#生成日期：2018/1/31
#模块描述：网卡配置
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')

from selenium import webdriver
sys.path.append("/testIsomp/common/")
from _icommon import getElement,selectElement,frameElement,commonFun
from _log import log
from _initDriver import initDriver
from _cnEncode import cnEncode

sys.path.append("/testIsomp/testData/")
from _testDataPath import dataFileName

sys.path.append("/testIsomp/webElement/network/")
from networkElement import Network

sys.path.append("/testIsomp/testSuite")
from common_suite_file import CommonSuiteData,setDriver

class NetworkCard:
    
    def __init__(self,driver):
        self.driver = driver
        self.getElem = getElement(driver)
        self.dataFile = dataFileName()
        self.select = selectElement(driver)
        self.frameElem = frameElement(driver)
        self.cmf = commonFun(driver)
        self.log = log()
        self.cnEnde = cnEncode()
        self.network = Network(driver)
        self.initDriver = initDriver()
        
    u'''获取测试数据
        Parameters:
            sheetname:sheet名称
            return：表格数据
    '''
    def get_table_data(self,sheetname):
        dataFile = dataFileName()
        filePath = dataFile.get_network_test_data_url()
        fileData = dataFile.get_data(filePath,sheetname)
        return fileData
    
    u'''提示框元素路径'''
    def network_msg(self):
        network_msg = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"
        return network_msg
    
    u'''web驱动初始化'''
    def open_driver(self,ipAdd):
        driver = webdriver.Chrome()
        #窗口最大化
        driver.maximize_window()
        #打开IP地址对应的网页
        driver.get("https://" + ipAdd + "/fort/login")
        time.sleep(1)
        #关闭驱动
        driver.quit()
        return driver           
    
    u'''设置网卡'''
    def set_network_card_001(self):
        #日志开始记录
        self.log.log_start("setNetworkCard")
        #获取设置网卡的数据
        network_data = self.get_table_data("set_network_card")
        #点击确定按钮弹出框
        network_msg = self.network_msg()
        #无检查点的测试项标识，如果为True说明通过
        flag = False
        for dataRow in range(len(network_data)):
            data = network_data[dataRow]
            try:
                #如果不是第一行标题，则读取数据
                if dataRow != 0:
                    self.frameElem.from_frame_to_otherFrame("rigthFrame")
                    if dataRow == 1:
                        self.network.set_eth1_ip(data[2])
                        self.network.set_eth1_mask(data[3])
                        self.network.click_eth1_set_button()
                    elif dataRow == 2:
                        self.network.set_eth2_ip(data[2])
                        self.network.set_eth2_mask(data[3])
                        self.network.click_eth2_set_button()
                    elif dataRow == 3:
                        self.network.set_eth3_ip(data[2])
                        self.network.set_eth3_mask(data[3])
                        self.network.click_eth3_set_button()
                    elif dataRow == 4:
                        self.network.gateway(data[4])
                        self.network.click_set_gateWay_button()
                    #返回上级frame
                    self.frameElem.switch_to_content()
                    #判断测试项是否通过
                    self.cmf.test_win_check_point("xpath", network_msg, data, flag)
                    if dataRow == 1:
                        self.open_driver(data[2])
                    elif dataRow == 2:
                        self.open_driver(data[2])
                    elif dataRow == 3:
                        self.open_driver(data[2])
            except Exception as e:
                print ("set network card fail: ") + str(e)
        self.log.log_end("setNetworkCard")
        
    u'''清空网卡'''
    def del_network_card_002(self):
        #日志开始记录
        self.log.log_start("delNetworkCard")
        #获取清空网卡的数据
        network_data = self.get_table_data("del_network_card")
        #点击确定按钮弹出框
        network_msg = self.network_msg()
        #无检查点的测试项标识，如果为True说明通过
        flag = False
        for dataRow in range(len(network_data)):
            data = network_data[dataRow]
            try:
                #如果不是第一行标题，则读取数据
                if dataRow != 0:
                    self.frameElem.from_frame_to_otherFrame("rigthFrame")
                    if dataRow ==1:
                        self.network.click_eth1_del_button()
                    elif dataRow == 2:
                        self.network.click_eth2_del_button()
                    elif dataRow == 3:
                        self.network.click_eth3_del_button()                   
                    self.cmf.click_msg_button(1)
                    self.frameElem.switch_to_content()
                    #判断测试项是否通过
                    self.cmf.test_win_check_point("xpath", network_msg, data, flag)
            except Exception as e:
                print ("del network card fail: ") + str(e)
        self.log.log_end("delNetworkCard")
        
    u'''校验网卡'''
    def check_network_card_003(self):
        #日志开始记录
        self.log.log_start("checkNetworkCard")
        #获取校验网卡的数据
        network_data = self.get_table_data("check_network_card")
        #点击确定按钮弹出框
        network_msg = self.network_msg()
        #无检查点的测试项标识，如果为True说明通过
        flag = False
        for dataRow in range(len(network_data)):
            data = network_data[dataRow]
            try:
                #如果不是第一行标题，则读取数据
                if dataRow != 0:
                    self.frameElem.from_frame_to_otherFrame("rigthFrame")
                    if dataRow == 1:
                        self.network.click_eth0_del_button()
                        self.cmf.click_msg_button(1)
                    elif dataRow == 2:
                        self.network.click_eth1_del_button()
                    elif dataRow > 2:
                        self.network.set_eth1_ip(data[2])
                        self.network.set_eth1_mask(data[3])
                        self.network.click_eth1_set_button()
                    #返回上级frame
                    self.frameElem.switch_to_content()
                    #判断测试项是否通过
                    self.cmf.test_win_check_point("xpath", network_msg, data, flag)
            except Exception as e:
                print ("check network card fail: ") + str(e)
        self.log.log_end("checkNetworkCard")
    

    
    
    
#if __name__ == "__main__":
#    setDriver = setDriver()
#    browser = setDriver.set_local_driver()
#    cmf = commonFun(browser)
#    commonSuite = CommonSuiteData(browser)
#    commonSuite.login_and_switch_to_sys()
#    cmf.select_menu(u"系统配置", u"网络配置")
#    
#    net = NetworkCard(browser)
#    net.set_network_card_001()
#    net.del_network_card_002()
#    net.check_network_card_003()