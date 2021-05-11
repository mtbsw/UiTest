from selenium import webdriver
# driver = webdriver.Firefox()
# driver.get("http://www.baidu.com")
# 定位元素方法：find_element("id","sk")==find_element_by_id("sk")
# driver.find_element_by_id("kw").send_keys("bym")
driver.find_element_by_name("wd").send_keys("bym")
# driver.find_element_by_class_name("s_ipt")
# driver.find_element("id","kw").send_keys("bym")
# driver.find_element_by_tag_name("input").send_keys("bym")
# driver.find_element("tag name","input").send_keys("bym")
# driver.find_element("link text","地图").click()
# driver.find_element("partial link text","地").click()
# driver.find_element('xpath','/html/body/div[1]/div[1]/div/div[3]/a[3]').click()
# driver.find_element("css selector","a.mnav:nth-child(3)").click()
# driver.find_element_by_id("su").click()
# 控制浏览器窗口全屏及大小
# driver.maximize_window()
# driver.set_window_size(480,800)
# 控制浏览器前进后退
# driver.back()
# driver.forward()
# 控制浏览器刷新
# driver.refresh()
# 元素操作
# clear()
# send_keys()
# click()
# 邮箱126登录
# driver.get ("http://www.126.com")
# driver.find_element_by_id ("idInput").clear()
# driver.find_element_by_id ("idInput") .send_keys ("username")
# driver.find_element_by_id ("pwdInput") .clear()
# driver.find_element_by_id ("pwdInput").send_keys ("password")
# driver.find_element_by_id ("loginBtn").click()
# driver.quit ()
# webelement元素操作
# 提交
# submit()
# 获取元素的文本
# text
# 获得属性值
# ger_attribute(name)
# 设置该元素是否用户可见
# is_displayed()
# 鼠标交互
# 执行所有actionchains中存储的命令
# perform（）
# 右击
# context_click
# 双击
# double_click
# 拖动
# drag_and_drop()
# 鼠标悬停
# move_to_element
# 加载actionchains类
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.action_chains import ActionChains
# right_click=driver.find_element("id","su")
# ActionChains(driver).context_click(right_click).perform()
# 鼠标拖放操作
# element=driver.find_element_by_id()
# target=driver.find_element_by_id()
# ActionChains(driver).drag_and_drop(element,target).perform()
# 键盘事件
# from selenium.webdriver.common.keys import Keys
# send_keys(Keys,CONTROL,"c")
# 获取title 获取当前页面的网址
# driver.title
# driver.current_url
# 显示等待(每隔一段时间检测一次元素是否存在，超过设置事件抛出异常)
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait as WT
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.expected_conditions import presence_of_element_located
# driver=webdriver.Firefox()
# driver.get("http://www.baidu.com")
# element=WT(driver,5,0.5).until(EC.presence_of_element_located((By.ID,"kw")))
# element.send_keys("selenium")
# # driver.quit()
# context_click
# double_click
# drag_and_drop
# move_to_element
# perform
# send_keys(Keys.ENTER,"v")
# from selenium import webdriver
# from selenium.webdriver import common
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait as WDW
# from selenium.webdriver.support import expected_conditions as EC
# ELEMENT=WDW(driver,5,0.5).until(EC.presence_of_element_located((By.ID,"kw")))
# from selenium import webdriver
# from time import sleep,ctime
# driver= webdriver.Chrome()
# driver.get("http://www.baidu.com")
# print(ctime())
# for i in range(10):
#     try:
#         el=driver.find_element_by_id("kw")
#         if el.is_displayed():
#             break
#     except:
#         pass
#         print("chucizhiwai")
#         sleep(1)
#     else:
#         print(i)
# driver.close()
# print(ctime())
# break:跳出for整个循环 continue：跳出此次循环，继续下个循环。
# for i in range(10):
#     print("-----%d-----" %i)
#     for j in range(10):
#         if j%2==0:
#            continue
#         print(j)
# get_attribute
# is_displayed()
# perform() context_click() double_click() drag_and_drop(element,element)
# from selenium import webdriver
# from selenium.webdriver.common import by
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.expected_conditions import presence_of_element_located
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Firefox()
# driver.get("http://www.baidu.com")
# element=WebDriverWait(driver,5,0.5).until(presence_of_element_located((by.By.ID,"KW")))
# 隐式等待
# from selenium import webdriver
# # from selenium.common.exceptions import NoSuchElementException
# # from time import ctime, sleep
#
# # from time import sleep
# driver=webdriver.Chrome()
# driver.implicitly_wait(10)
# driver.get("http://www.baidu.com")
# try:
#     print(ctime())
#     driver.find_element_by_id("kw22").send_keys("wsda")
# except NoSuchElementException as e:
#     print(e)
# finally:
#     print(ctime())
#     driver.quit()
# sleep(3)
# 获取一组元素
# checkboxes=driver.find_elements_by_xpath()
# 当前页面下有个叫input的标签下有个id名为“kw“的元素
# ("//input[@id='kw']")
# 多表单切换
# driver.switch_to.frame("frame文件名")
# driver.switch_to.parent_frame()
# driver.switch_to.default_content()
# driver.switch_to.window()
# now_handle=driver.current_window_handle
# print(now_handle)
# 多窗口切换
# all_handles=driver.window_handles
# print(all_handles)
# driver=webdriver.Chrome()
# driver.switch_to_alert().accept()
# driver.switch_to.alert().accept()
# send_keys("D:\测试\工具\自动化测试\pip-19.0.2-py2.py3-none-any.whl")
# from selenium import webdrivers
# import os
# fp=webdriver.FirefoxProfile
# 下载文件
# from selenium import webdriver
# import os
# fp=webdriver.FirefoxProfile()
# 设置成0代表下载到浏览器默认下载路径，设置成2则可以保存到指定目录
# fp.set_preference("browser.download.folderlist",2)
# 是否显示开始：ture为显示，false为不显示
# fp.set_preference("browser.download.manager.showWhenStarting",False)
# 用于指定下载文件的目录。os.getcwd()函数不需要传递参数，用于返回当前的目录
# fp.set_preference("browser.download.dir",os.getcwd())
# get_cookies()  获取所有cookie信息
# get_cooke(name)返回字典的“key”为name的cookie的信息
# add_cookie(ccokie_diect) 添加cookie的选项，目前支持的选项包括“路径”，“域”
# delete_all_cookies() 删除所有cookie
from selenium import webdriver
import time
# driver = webdriver.Firefox()
# driver.get("http://www.baidu.com")
# # driver.add_cookie({'name':'name','value':'baoyumeng'})
# # for cookie in driver.get_cookies():
# #     print('%s -> %s'%(cookie['name'],cookie['value']))
# # print(driver.get_cookies())
# # driver.set_window_size(600,600)
# # driver.find_element("id","kw").send_keys("selenium")
# # ActionChains(driver).context_click(driver.find_element_by_id("su")).perform()
# # driver.find_element_by_id("su").click()
# # time.sleep(2)
# 调用javascript
# # js="window.scrollTo(600,600);"
# # driver.execute_script(js)
# # text=input()
# textarea="var sum=document.getElementById('message');sum.value='"+text+124124124124+"';"
# "var sum=document.getElementById('kw');sum.value="'+text+'";"
# "var sum=document.getElementById('kw');sum.value="'+text+'";"
# driver =webdriver.Firefox()
# driver.get("http://videojs.com")
# video=driver.find_element_by_xpath("//*[@id='preview-player']/div[1]")
# video[0]="return arguments[0].currentSrc;"
# url=driver.execute_script(video[0],video)
# driver.execute_script()
from random import randint
from random import random
# time.sleep(2)
# random_number=time.time()
# print(time.time())
# driver.get_screenshot_as_file("D:\\1\\测试截图%d.png"%random_number)
# print(randint(1,10))
# for i in range(10):
#    if i%2==0:
#        print("第%d成功了"%(i+1))
#    else:
#        print("第%d失败了"%(i+1))
x=randint(1000,9999)
print("生成的随机数;%d"%x)
number = input("请输入随机数：")
print(number)
number=int(number)
if number==x:
    print("登录成功！")
elif number==123456:
    print("登录成功！")
else:
    print("验证码输入有误")
