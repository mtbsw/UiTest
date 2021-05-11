import selenium
import time
from selenium import webdriver
driver = webdriver.Firefox()
driver.get('https://www.xiaozu365.com/q/index.html#/login')
driver.find_element('xpath','//*[@id="app"]/div/div/div/div/div[1]/form/div[1]/div/div/input').send_keys('15757181215')
driver.find_element('xpath','//*[@id="app"]/div/div/div/div/div[1]/form/div[2]/div/div[1]/input').send_keys('12')
driver.find_element('xpath','//*[@id="app"]/div/div/div/div/div[1]/form/div[3]/div/button/span').click()
time.sleep(0.5)
ino = driver.switch_to.alert()
inoifo = ino.txt
print(inoifo)

