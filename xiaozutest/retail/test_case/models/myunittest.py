from retail.test_case.models.log import Logger
from retail.config import conf
import unittest
from retail.test_case.models.driver import WebDriver
from retail.test_case.page_obj.login_page import LoginPage
log = Logger(__name__)
import time

class MyUnitTest(unittest.TestCase):
    @classmethod
    # 一个测试类(文件)执行一次打开浏览器, 节约每个用例打开一次浏览器的时间
    def setUpClass(cls):
        cls.driver=WebDriver().fireFoxDriver()
        cls.driver.maximize_window()
        log.logger.info('open the browser succeed')

    def setUp(self):
        self.login = LoginPage(self.driver)
        self.login.open()
        log.logger.info(
            'start run test case'
        )
    def tearDown(self):
        self.login.clearLocalStorage()
        log.logger.info(
            'test case run completed'
        )
    @classmethod
    def tearDownClass(cls):
        # time.sleep(2)
        cls.driver.quit()
        log.logger.info(
            'quit the browser succeed'
        )
if __name__ == '__main__':
    unittest.main()



