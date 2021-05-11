from retail.test_case.page_obj.base_page import  BasePage,login_page_elements,login_test_date
from retail.test_case.models.log import  Logger
import time
import sys
from selenium.webdriver.common.action_chains import ActionChains
# from retail.test_case.models.readexcel import  ReadExcel

log = Logger(__name__)
class LoginPage(BasePage):
    loginPageElements = [
        #登录页-用户名
        (login_page_elements.readExcel(1,2),login_page_elements.readExcel(1,3)),
        #登录页-密码
        (login_page_elements.readExcel(2,2),login_page_elements.readExcel(2,3)),
        #登录页-点击登录按钮
        (login_page_elements.readExcel(3,2),login_page_elements.readExcel(3,3)),
        #登录页-忘记密码按钮
        (login_page_elements.readExcel(4,2),login_page_elements.readExcel(4,3)),
        #更改密码-去登录按钮
        (login_page_elements.readExcel(5,2),login_page_elements.readExcel(5,3)),
        #更改密码-用户名
        (login_page_elements.readExcel(6,2),login_page_elements.readExcel(6,3)),
        #更改密码-图形验证码
        (login_page_elements.readExcel(7,2),login_page_elements.readExcel(7,3)),
        #更改密码-切换图形验证码
        (login_page_elements.readExcel(8,2),login_page_elements.readExcel(8,3)),
        #更改密码-密码
        (login_page_elements.readExcel(9,2),login_page_elements.readExcel(9,3)),
        #更改密码-确认密码
        (login_page_elements.readExcel(10,2),login_page_elements.readExcel(10,3)),
        #更改密码-立即注册
        (login_page_elements.readExcel(11,2),login_page_elements.readExcel(11,3)),
        #手机快捷登录
        (login_page_elements.readExcel(12,2),login_page_elements.readExcel(12,3)),
        #手机登录-用户名
        (login_page_elements.readExcel(13,2),login_page_elements.readExcel(13,3)),
        #手机登录-图形验证码
        (login_page_elements.readExcel(14,2),login_page_elements.readExcel(14,3)),
        #手机登录-切换图形验证码
        (login_page_elements.readExcel(15,2),login_page_elements.readExcel(15,3)),
        #手机验证码
        (login_page_elements.readExcel(16,2),login_page_elements.readExcel(16,3)),
        #获取手机验证码按钮
        (login_page_elements.readExcel(17,2),login_page_elements.readExcel(17,3)),
        #退出按钮
        (login_page_elements.readExcel(31,2),login_page_elements.readExcel(31,3)),
    ]
    loginTestDate = [
        #正确用户名,正确密码
        (login_test_date.readExcel(1,2),login_test_date.readExcel(1,3)),
        #正确用户名,错误密码
        (login_test_date.readExcel(2,2),login_test_date.readExcel(2,3)),
        #正确用户名, 空密码
        (login_test_date.readExcel(3,2),login_test_date.readExcel(3,3)),
        #错误用户名, 正确密码
        (login_test_date.readExcel(4,2),login_test_date.readExcel(4,3)),
        #错误用户名, 正确密码
        (login_test_date.readExcel(5,2),login_test_date.readExcel(5,3))
    ]
    def clickLogin(self):
        element = self.findElement(*self.loginPageElements[2])
        element.click()
        log.logger.info('%s logging ....'%sys._getframe().f_code.co_name)

    def getAlertText(self,*loc):
        alert = self.findElement(*loc)
        alertText =  self.driver.switch_to_alert().text
        return alertText

    def inputUser(self,user):
        self.inputValue(self.loginPageElements[0],user)

    def inputPassword(self,password):
        self.inputValue(self.loginPageElements[1],password)

    def goLogin(self):
        self.findElement(*self.menuElement[0]).click()

    def loginFunc(self,user,password):
        self.inputUser(user)
        self.inputPassword(password)
        self.clickLogin()

    def quit(self):
        self.findElement(*self.loginPageElements[18]).click()
        log.logger.info('user quit succeed!')
    def clearLocalStorage(self):
        #清缓存
        # cookies = self.driver.localStorage.clear()
        # pri(f"main: cookies = {cookies}")
        js= 'window.localStorage.clear()'
        self.driver.execute_script(js)

if __name__ == '__main__':
    # print(LoginPage.loginPageElements[1])
    # print(LoginPage.loginTestDate[0][0])
    pass















