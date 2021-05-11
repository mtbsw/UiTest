# from retail.test_case.page_obj.login_page import LoginPage
import unittest
from retail.test_case.models.myunittest import MyUnitTest
import  time
import sys
from retail.test_case.models.log import Logger
import logging

log = Logger(__name__)
class LoginTc(MyUnitTest):
    def test_login_succeed_correct_user_password(self):
        '''正确的用户名及正确密码'''
        try:
            self.login.goLogin()
            self.login.loginFunc(int(self.login.loginTestDate[0][0]),int(self.login.loginTestDate[0][1]))
            time.sleep(2)
            cuurUrl = self.driver.current_url
            self.assertIn('my',cuurUrl,'登录失败或登录后的默认页面不对')
        except Exception:
            self.login.saveScreenShot('%s_fail.png'%(sys._getframe().f_code.co_name))
            time.sleep(1)
            raise

        else:
            self.login.saveScreenShot('%s_pass.png'%(sys._getframe().f_code.co_name))
            time.sleep(1)
            log.logger.info('%s test completed '%(sys._getframe().f_code.co_name))

    def test_login_succeed_incorrect_user_password(self):
        '''正确的用户名及不正确的密码'''
        try:
            self.login.goLogin()
            self.login.loginFunc(int(self.login.loginTestDate[1][0]),int(self.login.loginTestDate[1][1]))
            alertIfo = self.login.findElement('xpath','/html/body/div[2]').get_attribute('class')
            log.logger.info(alertIfo)
            time.sleep(2)
            self.assertIn('el-message el-message--error',alertIfo,'提示不正确')
        except Exception:
            self.login.saveScreenShot('%s_fail.png'%(sys._getframe().f_code.co_name))
            time.sleep(1)
            raise

        else:
            self.login.saveScreenShot('%s_pass.png'%(sys._getframe().f_code.co_name))
            time.sleep(1)
            log.logger.info('%s test completed '%(sys._getframe().f_code.co_name))
    # def test_login_succeed_empty_user_password(self):
    #     '''正确的用户名及空的密码'''
    #     try:
    #         self.login.goLogin()
    #         self.login.loginFunc(int(self.login.loginTestDate[2][0]),int(self.login.loginTestDate[2][1]))
    #         time.sleep(1)
    #         cuurUrl = self.driver.current_url
    #         self.assertIn('my',cuurUrl,'登录失败或登录后的默认页面不对')
    #     except Exception:
    #         self.login.saveScreenShot('%s_fail.png'%(sys._getframe().f_code.co_name))
    #         time.sleep(1)
    #         raise
    #
    #     else:
    #         self.login.saveScreenShot('%s_pass.png'%(sys._getframe().f_code.co_name))
    #         time.sleep(1)
    #         log.logger.info('%s test completed '%(sys._getframe().f_code.co_name))















