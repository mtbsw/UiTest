from xiaozutest.retail.test_case.models.log import Logger
from selenium import webdriver
import sys
log = Logger(__name__)
class WebDriver(object):

    def fireFoxDriver(self):
        try:
            self.driver = webdriver.Firefox()
        except Exception as e:
            log.logger.exception('FireFoxDriverServer.exe executable needs to be in PATH. Please download!',exc_info=True)
            raise e
        else:
            log.logger.info('%s:found the Firefox driver [%s] succeed !' % (sys._getframe().f_code.co_name, self.driver))
            return self.driver

    def chromeDriver(self):
        try:
            self.driver = webdriver.Chrome()
        except Exception:
            log.logger.exception('chrome driver must be download in right path')
            raise
        else:
            log.logger.info('found the chrome driver succeed')
            return self.driver

    def ieDriver(self):
         try:
            self.driver = webdriver.Ie()
         except Exception as e:
            log.logger.exception('IEDriverServer.exe executable needs to be in PATH. Please download!',exc_info=True)
            raise e
         else:
            log.logger.info('%s:found the IE driver [%s] succeed !' % (sys._getframe().f_code.co_name, self.driver))
            return self.driver

if __name__== '__main__':
    driver=WebDriver().fireFoxDriver()
    driver.get('http://www.baidu.com')

