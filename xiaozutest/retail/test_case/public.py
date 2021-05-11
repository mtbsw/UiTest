from selenium import webdriver
import time
#登录
class Common():
  def __init__(self):
      #uname用户名称元素、密码元素、登录元素、昵称元素、登出元素
      self.ul1="http://kjs.qibanbao.cn/kjs/res/mpjk/index.html#/login?redirect=%2Fdashboard"
      self.xp_username="/html/body/div/div/form/div[2]/div/div/input"
      self.xp_password="/html/body/div/div/form/div[3]/div/div/input"
      self.xp_login="/html/body/div/div/form/button"
      self.xp_name="/html/body/div/div/div/div[1]/div/div/span"
      self.xp_logout="/html/body/ul/li/span"
  def open_browser(self):
      self.driver = webdriver.Firefox()
      self.driver.get(self.ul1)
      return self.driver
  #登录
  def user_login(self):
      driver=Common().open_browser()
      #读取文件中账号、密码、昵称
      user_file = open('xiaozutest_info.txt', 'r', encoding='UTF-8')
      #读取行
      lines = user_file.readlines()
      user_file.close()
      for line in lines:
          #分解行，注意“，”为中文字符
          username = line.split("，")[0]
          password = line.split("，")[1]
          name = line.split("，")[2]
      #登录
      driver.find_element_by_xpath(self.xp_username).clear()
      driver.find_element_by_xpath(self.xp_username).send_keys(username)
      driver.find_element_by_xpath(self.xp_password).clear()
      driver.find_element_by_xpath(self.xp_password).send_keys(password)
      driver.find_element_by_xpath(self.xp_login).click()
      return driver,name
  # 验证登录后的账号信息是否正确
  def verify(self):
      info=Common().user_login()
      driver=info[0]
      name=info[1]
      nametwo = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div/div/span').text
      if nametwo==name:
         print("账号名称正确")
      else:
         print("账号与用户名不匹配")

  def user_logout(self):
      driver=Common().user_login()[0]
      driver.find_element_by_xpath(self.xp_name).click()
      driver.find_element_by_xpath(self.xp_logout).click()


  def order(self,driver):
     #点击到“发单”页面
     driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/ul/li[1]").click()
     #判断企业名称输入最大字符串限制
     company_element=driver.find_element_by_xpath("/html/body/div/div/div/div[2]/section/form/div[1]/div/div/input")
     company_length=company_element.get_attribute("maxlength")
     company_info = company_element.get_attribute("placeholder")
     if company_length<=100:
         # 判断企业名称是否带有输入提示：如请输入。。。。
         if company_info in "请输入企业名称":
             print("提示信息正确")
             company_element.clear()
             company_element.send_keys("杭州小租")
         else:
             print("提示信息错误")
     else:
        print("企业名称最多输入100个字！")






     # #企业联系人
     # company_contacts=driver.find_element_by_xpath("/html/body/div/div/div/div[2]/section/form/div[2]/div/div/input")
     # company_contacts.


