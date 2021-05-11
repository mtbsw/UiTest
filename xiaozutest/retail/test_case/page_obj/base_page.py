from retail.test_case.models.log import Logger
from retail.config import conf
from retail.test_case.models.readexcel import  ReadExcel
import  sys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
home_page_elements = ReadExcel()
login_page_elements = ReadExcel(sheetName='login_page_elements')
login_test_date = ReadExcel(sheetName='login_test_date')
log = Logger(__name__)
class BasePage(object):
    menuElement = [
        #登录按钮
        (home_page_elements.readExcel(1,2),home_page_elements.readExcel(1,3)),
        #注册按钮
        (home_page_elements.readExcel(2,2),home_page_elements.readExcel(2,3)),
        #首页
        (home_page_elements.readExcel(3,2),home_page_elements.readExcel(3,3)),
        #全部商品
        (home_page_elements.readExcel(4,2),home_page_elements.readExcel(5,3)),
        #增值服务
        (home_page_elements.readExcel(5,2),home_page_elements.readExcel(5,3)),
        #企业回收
        (home_page_elements.readExcel(6,2),home_page_elements.readExcel(6,3)),
        #个人中心
        (home_page_elements.readExcel(7,2),home_page_elements.readExcel(7,3)),
        #选机指南
        (home_page_elements.readExcel(8,2),home_page_elements.readExcel(8,3)),
        #芝麻信用免押金
        (home_page_elements.readExcel(9,2),home_page_elements.readExcel(9,3)),
        #首页输入框
        (home_page_elements.readExcel(10,2),home_page_elements.readExcel(10,3)),
        #退出按钮
        (home_page_elements.readExcel(11,2),home_page_elements.readExcel(11,3))
    ]
    def __init__(self,driver,url='http://xiaozu365.com'):
        self.driver = driver
        self.url = url

    def _open(self,url):
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
        except Exception as e:
            log.logger.exception(e)
            raise ValueError('adress %s are error'%url)
        else:
            log.logger.info('%s open url %s succeed'%(sys._getframe().f_code.co_name,url))


    def open(self):
        self._open(self.url)
        log.logger.info('open url %s succeed'%self.url)
        return self.url



    def findElement(self,*element):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(element))
        except Exception as e:
            log.logger.exception('find element timeout!')
            raise e
        else:
            log.logger.info('find element succeed')
            return self.driver.find_element(*element)

    def findElements(self,*element):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(element))
        except Exception as e:
            log.logger.exception('find element timeout' )
        else:
            log.logger.info('find element %s succeed' % element)
            return self.driver.find_elements(*element)

    def inputValue(self,element,value):
        inputElement = self.findElement(*element)
        try:
            inputElement.clear()
            inputElement.send_keys(value)
        except Exception as e:
            log.logger.exception('type value error ')
            raise e
        else:
            log.logger.info('element %s has be receive value %s'%(element,value))

    def getValue(self,element):
        elementV = self.findElement(*element)
        try:
            value = elementV.text
        except Exception :
            log.logger.exception(' the element %s type text is error!'%element)
            try:
                value = elementV.get_attribute('value')
            except Exception:
                log.logger.exception(' the element %s attribute value is error!' % element)
            else:
                return value
        else:
            log.logger.info('get element %s value succeed'%element)
            return value

    def getValues(self,element):
        elementsV = self.findElement(*element)
        valueList = []
        try:
            for elementV in elementsV:
                value = elementV.text
                valueList.append(value)
        except Exception :
            log.logger.exception(' the element %s type text is error!'%element)

        else:
            log.logger.info('get element %s value succeed'%element)
            return valueList

    def javeScript(self,src):
        try:
            self.driver.execute_script(src)
        except Exception as e:
            log.logger.exception('execute js %s failed'%src)
            raise e
        else:
            log.logger.info('execute js %s succeed'%src)

    def isElementExist(self,*element):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(element))
        except Exception:
            return False
        else:
            return True

    # def get_windows_img(self,filename):
    #
    #     file_path = conf.failImagePath
    #     # rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    #     # screen_name = file_path +filename
    #     # print(screen_name)
    #     list=filename.split('.')
    #     try:
    #         if 'fail' in list[0].split('_'):
    #             try:
    #                 self.driver.save_screenshot(os.path.join(conf.failImagePath, filename))
    #             except Exception:
    #                 log.logger.exception('save screenshot failed')
    #             else:
    #                 log.logger.info('save screenshot %s succeed' % filename)
    #         elif 'pass' in list[0].split('_'):
    #             try:
    #                 self.driver.save_screenshot(os.path.join(conf.passImagePath, filename))
    #             except Exception:
    #                 log.logger.exception('save screenshot failed')
    #             else:
    #                 log.logger.info('save screenshot %s succeed' % filename)
    #         else:
    #             log.logger.info('save screenshot failed due to [%s] format incorrect' % filename)
    #
    #             self.driver.get_screenshot_as_file(screen_name)
    #             log.logger.info("Had take screenshot and save to folder : /screenshots")
    #     except NameError as e:
    #             log.logger.error("Failed to take screenshot! %s" % e)
    #             self.get_windows_img()




    def saveScreenShot(self,filename):
        # value_list=[]
        list = filename.split('.')
        failImagePath = conf.failImagePath
        if not os.path.exists(failImagePath):
            os.mkdir(failImagePath)
        else:
            pass
        passImagePath = conf.passImagePath
        if not os.path.exists(passImagePath):
            os.mkdir(passImagePath)
        else:
            pass
        # for value in list:
        #     value_list.append(value)
        if list[1] in ['jpg','png']:
            if 'fail' in list[0].split('_'):
                try:

                    imageAddr = os.path.join(failImagePath, filename)
                    self.driver.save_screenshot(imageAddr)
                except Exception:
                    log.logger.exception('save screenshot failed')
                else:
                    print(imageAddr)
                    log.logger.info('save screenshot %s succeed'%filename)
            elif 'pass' in list[0].split('_'):
                try:
                    imageAddr = os.path.join(passImagePath, filename)
                    self.driver.save_screenshot(imageAddr)

                except Exception:
                    log.logger.exception('save screenshot failed')
                else:
                    print(imageAddr)
                    log.logger.info('save screenshot %s succeed'%filename)
            else:
                log.logger.info('save screenshot failed due to [%s] format incorrect' % filename)
        else:
            log.logger.info('save screenshot failed due to [%s] format incorrect' % filename)



    def accept(self,*loc):
        self.findElement(*loc).click()
        log.logger.info('accept waring information succeed')



if __name__ == '__main__':
    pass












