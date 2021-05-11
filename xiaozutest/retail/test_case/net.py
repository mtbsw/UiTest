代码如下：

import os

import time

import xlrd

from selenium.webdriver.common.action_chainsimport ActionChains

from selenium.webdriver.supportimport expected_conditionsas EC

from selenium.webdriver.support.waitimport WebDriverWait

from selenium.common.exceptionsimport WebDriverException

from utils.configimport REPORT_PATH

from utils.logimport logger

from selenium.webdriver.support.uiimport Select

# from UI_AUTOMATION.test.testcase.gb_pc_form_case import FormTestCase

from timeimport sleep

class BasePage:

def __init__(self, driver):

self.driver = driver

def get(self, url, maximize_window=True, time_sync=30):

self.driver.get(url)

if maximize_window:

self.driver.maximize_window()

self.driver.implicitly_wait(time_sync)

return self

    def is_element_exist(self, *xpath):#快速定位元素是否存在，不等待。

        flag =True

        browser =self.driver

try:

browser.find_element_by_xpath(xpath)

return flag

except:

flag =False

            return flag

def find_element_now(self, *loc):

try:

self.driver.find_element_by_xpath(loc)

return True

        except AttributeError:

print(u"%s 页面中未能找到 %s 元素" % (self, loc))

return False

    def find_element(self, *loc):

try:

WebDriverWait(self.driver, 4).until(EC.visibility_of_element_located(loc))# 等待元素在页面可见

            return self.driver.find_element(*loc)

except AttributeError:

print(u"%s 页面中未能找到 %s 元素" % (self, loc))

def find_elements(self, *loc):

try:

items = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(loc))# 等待元素在DOM都出现

            return items

except AttributeError:

print(u"%s 页面中未能找到 %s 元素" % (self, loc))

def elements_text(self, *loc):

items = []

items_elements =self.find_elements(*loc)

for itemin items_elements:

items.append(item.text.strip())

return items

def move_to_element(self, *loc):

aim_loc =self.find_element(*loc)

ActionChains(self.driver).move_to_element(aim_loc).perform()

def click(self, *loc):

try:

self.find_element(*loc).click()

except Exception as msg:

self.save_screen_shot()

# self.driver.get_screenshot_as_base64()

            logger.error("Element {} is not clickable".format(loc))

def clickn(self, n=2, *loc):

try:

self.find_element(*loc)[n].click()

except Exception as msg:

self.save_screen_shot()

logger.error("Element {} is not clickable".format(loc))

def send_keys(self, value, *loc):

sleep(0.3)

element =self.find_element(*loc)

element.click()

element.clear()

element.send_keys(value)

def send_Skeys(self,  value, *loc):

sleep(0.3)

element = Select(self.find_element(*loc))

element.select_by_value(value)

def add_img(self):

self.imgs.append(self.driver.get_screenshot_as_base64())

return True

    # def save_screen_shot(self):

    def save_screen_shot(self, name='screen_shot'):

day = time.strftime('%Y%m%d', time.localtime(time.time()))

screenshot_path = REPORT_PATH +'\screenshot_%s' % day

if not os.path.exists(screenshot_path):

os.makedirs(screenshot_path)

tm = time.strftime('%H%M%S', time.localtime(time.time()))

screenshot =self.driver.save_screenshot(screenshot_path +'\\%s_%s.png' % (name, tm))

return screenshot

# self.imgs.append(self.driver.get_screenshot_as_base64())

# return True

    def find_title(self, *loc):

try:

WebDriverWait(self.driver, 4).until(EC.visibility_of_element_located(loc))# 等待元素在页面可见

            return self.driver.find_element(*loc)

except AttributeError:

print(u"%s 页面中未能找到 %s 元素" % (self, loc))

def in_pages(self, txt):

return txtin self.driver.page_source

def switch_frame(self, loc):

self.driver.switch_to.frame(loc)

def default_content(self):

self.driver.switch_to.default_content()

def switch_window(self, n=1):

# 打开顺序：1,2,3,4,5

        # 句柄顺序：0,4,3,2,1

        newest_window =self.driver.window_handles[n]

self.driver.switch_to.window(newest_window)

@staticmethod

    def get_latest_file(download_dir):

"""获取最新的文件"""

        lists = os.listdir(download_dir)

lists.sort(key=lambda fn: os.path.getmtime(download_dir +'\\' + fn))

file_path = os.path.join(download_dir, lists[-1])

return file_path

@staticmethod

    def get_data(file_path):

book = xlrd.open_workbook(file_path)

sheet = book.sheet_by_index(0)

rows = []

cols = []

for jin range(0, sheet.nrows):

rows.append(list(sheet.row_values(j, 0, sheet.ncols)))

for iin range(0, sheet.ncols):

cols.append(list(sheet.col_values(i, 0, sheet.nrows)))

return rows, cols, book.sheet_names()

# 返回3个列表组成的元组



五，业务分离，元素分离，数据分离。

首先数据为什么要分离，安全，代码不冗余，便于维护，较少后期维护成本。

业务分离：


部分代码入下：

from UI_AUTOMATION.utils.configimport Config

from selenium.webdriver.support.uiimport Select

import pymysql

from UI_AUTOMATION.test.page.pageconfig.haoseleniumimport *

from UI_AUTOMATION.utils.configimport Config

from selenium.webdriver.support.waitimport WebDriverWait

from UI_AUTOMATION.test.page.pageconfig.connectimport GBConnect

from UI_AUTOMATION.test.page.base_pageimport *

from UI_AUTOMATION.test.page.PC.pc_locatorsimport *

from UI_AUTOMATION.test.page.PC.pc_home_pageimport *

class GBBaseCase(BasePage):

def __init__(self, driver):

self.Connection ='keep-alive'

        self.driver = driver

c = Config().get('GB')

self.ua = c.get('UA')

self.url = c.get('GBURL')

self.username = c.get('GBusername')

self.password = c.get('GBpassword')

self.GBloginURL = c.get('GBloginURL')

self.GBgood = c.get('GBgood')

self.PPusername = c.get('PPusername')

self.PPpassword = c.get('PPpassword')

self.GBselfcenter = c.get('GBselfcenter')

self.userId = c.get('userId')

c = Config().get('mysql')

self.host = c.get('host')

self.post = c.get('post')

self.user = c.get('user')

self.passwd = c.get('passwd')

self.db = c.get('db')

# print(self.userId)

    def add_img(self):

self.imgs.append(self.get_screenshot_as_base64())

return True

    def gb_login(self):

# self.headers = {'User-Agent': self.ua}

# self.driver = driver

        pc = HomePage(self.driver)

lg = LoginPage(self.driver)

pc.get(self.GBloginURL)

# self.add_img()

        # pc.close_pop_win()  #关闭弹窗

        # pc.sign_in()      #点击进入登录页面

        lg.login(self.username, self.password)

# WebDriverWait(self.driver, 10).until(EC.title_is("GearBest: Online Shopping - Best Gear at Best Prices"))

        sleep(1)

def gb_goodtobuy(self):

# self.driver.refresh()

        sleep(0.5)

# self.driver.set_page_load_timeout(5)

        try:

self.driver.get(self.GBgood)

b =0

            while b !=5:

try:

self.find_element(*GoodsInfoPageLoc.buy_button)

b =5

                except:

b = b +1

                    self.driver.refresh()

except TimeoutException:

self.driver.execute_script('window.stop()')

# self.driver.execute_script("var q=document.body.scrollTop=300")

        self.find_element(*GoodsInfoPageLoc.buy_button)

try:

self.click(*GoodsInfoPageLoc.num_plus)

self.click(*GoodsInfoPageLoc.buy_button)

except:

self.driver.refresh()

self.click(*GoodsInfoPageLoc.num_plus)

self.click(*GoodsInfoPageLoc.buy_button)

sleep(5)

def gb_goodtopaypal(self):

self.driver.set_page_load_timeout(5)

self.driver.refresh()

sleep(2)

try:

self.get(self.GBgood)

b =0

            while b !=5:

try:

self.find_element_now(*GoodsInfoPageLoc.paypal_button)

self.click(*GoodsInfoPageLoc.paypal_button)

b =5

                except:

b = b +1

                    self.driver.refresh()

except TimeoutException:

self.driver.execute_script('window.stop()')

self.find_element(*GoodsInfoPageLoc.paypal_button)

try:

self.click(*GoodsInfoPageLoc.num_plus)

self.click(*GoodsInfoPageLoc.paypal_button)

except:

self.driver.refresh()

self.click(*GoodsInfoPageLoc.num_plus)

self.click(*GoodsInfoPageLoc.paypal_button)

sleep(5)

def gb_placeorder(self):

# self.headers = {'User-Agent': self.ua}

# self.driver.execute_script("var q=document.documentElement.scrollTop=500")

        sleep(1)

try:

self.driver.switch_to.alert

self.driver.switch_to.alert.accept()# 点击弹出上面的X按钮

        except:

pass

        try:

self.click(*PlaceInfoPageLoc.place_button)# pleace your order

        except:

self.driver.refresh()

sleep(1)

self.driver.execute_script("var q=document.documentElement.scrollTop=500")

try:

self.click(*PlaceInfoPageLoc.place_button)# pleace your order

            except:

self.driver.refresh()

sleep(1)

self.click(*PlaceInfoPageLoc.place_button)# pleace your order

        sleep(4)

def get_payurl(self):

# self.headers = {'User-Agent': self.ua}

        url = GBConnect().GB_payurl()

self.get(url)

self.driver.maximize_window()

self.find_element(*PaymentInfoPageLoc.pay_button)

self.driver.refresh()

print('收银台url：', self.driver.current_url)

sleep(0.5)

def get_payurl_m(self):

# self.headers = {'User-Agent': self.ua}

        url = GBConnect().GB_payurl()

self.get(url)

# self.driver.maximize_window()

# self.find_element(*PaymentInfoPageLoc.pay_button)

# self.driver.refresh()

        print('收银台url：', self.driver.current_url)

sleep(0.5)

def paymentplatform(self):

# self.headers = {'User-Agent': self.ua}

        self.find_element(*PaymentInfoPageLoc.pay_button)

print('收银台url：', self.driver.current_url)

try:

self.click(*PaymentInfoPageLoc.paypal_src)

self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()# 点击购买placeOrder btn block toPayBtn

        except Exception as msg:

print(u"异常原因%s" % msg)

pamentordersn =self.driver.find_element_by_xpath("//*[@class='pc_orderinf']/dl[1]/dd").text

print("收银台订单号：", pamentordersn)

# BaseTestCase.add_img()

            self.add_img()

raise

        sleep(2)

def obs_credit_channel(self, channel1):

js ='window.open("http://www.obs-pay.com");'  # 通过执行js，开启一个新的窗口

        self.driver.execute_script(js)

pay_windows =self.driver.current_window_handle

window_1 =self.driver.current_window_handle

# 获得打开的所有的窗口句柄

        windows =self.driver.window_handles

# 切换到最新的窗口

        for current_windowin windows:

if current_window != window_1:

self.driver.switch_to.window(current_window)

# self.get("http://www.obs-pay.com")

        sleep(1)

# obs_handle = self.driver.current_window_handle

# self.obs_handle = obs_handle

# sleep(0.5)

        self.driver.find_element_by_xpath("//*[@name='username']").send_keys("zhangwei")

self.driver.find_element_by_xpath("//*[@name='password']").send_keys("zhang1wei")

sleep(0.5)

self.driver.find_element_by_xpath("//input[@type='submit']").click()

sleep(1)

self.driver.get("http://www.obs-pay.com/#/pay/channel-platform-country/list")

sleep(1.5)

self.driver.find_element_by_xpath("//*[contains(text(),'Turkey')]/../../td[5]/div/button[1]/span").click()

sleep(0.5)

start_ele ='//*[contains(text(), "%s")]' % channel1

end_ele ='//*[contains(text(), "%s")]/../li[1]' % channel1

start =self.driver.find_element_by_xpath(start_ele)

end =self.driver.find_element_by_xpath(end_ele)

actions = ActionChains(self.driver)

actions.drag_and_drop(start, end)

actions.perform()

sleep(0.5)

self.driver.find_element_by_xpath("//*[contains(text(),'确定')]").click()

sleep(0.5)

self.driver.close()

self.driver.switch_to.window(pay_windows)

def payment_creditcard(self):

self.find_element(*PaymentInfoPageLoc.pay_button)

self.driver.refresh()

sleep(0.5)

print('收银台url：', self.driver.current_url)

self.obs_credit_channel("checkout_credit")

# pay_windows = self.driver.current_window_handle

# GBBaseCase.obs_creditcard()

# sleep(0.5)

# self.driver.switch_to.window(pay_windows)

        self.click(*PaymentInfoPageLoc.creditcard_src)

self.send_keys("hao", *PaymentInfoPageLoc.creditcard_holder)

self.send_keys("6111111111117", *PaymentInfoPageLoc.creditcard_Number)

self.send_keys("10", *PaymentInfoPageLoc.creditcard_Code)

self.send_Skeys("4", *PaymentInfoPageLoc.creditcard_mouth)

self.send_Skeys("2035", *PaymentInfoPageLoc.creditcard_day)

sleep(0.8)

self.click(*PaymentInfoPageLoc.pay_button)

sleep(4)

def gb_checkorder(self):

        paymentresult =self.driver.find_element_by_xpath("//*[@class='pay_title']").text

print("支付结果提示语：", paymentresult)

global ordersn

try:

ordersn =self.driver.find_element_by_xpath("//*[@class='payOnline_sucess']/p[2]/b[1]").text# paid

        except:

try:

ordersn =self.driver.find_element_by_xpath(

"//*[@class='payOnline_padding']/p[1]/b[1]").text# pending

            except:

try:

ordersn =self.driver.find_element_by_xpath(

"//*[@class='payOffline_default']/p[1]/b[1]").text# Appreciate

                except:

try:

ordersn =self.driver.find_element_by_xpath(

"//*[@class='pay_title']/em[1]").text# Submitting

                    except:

print("fail or no_result")

ordersn =str(ordersn)

if len(ordersn) ==20:

pass

        else:

ordersn = ordersn[:-1]

print("订单号为：", ordersn)

connect = pymysql.connect(host=self.host, port=self.post, user=self.user, passwd=self.passwd, db=self.db,

                                  charset='utf8')

cursor = connect.cursor()

cursor.execute("SELECT pay_status FROM pay_gateway_16 WHERE parent_order_sn=('%s')" % (ordersn))

status = cursor.fetchall()

status =str(status)

status = status[2:3]

print("此订单状态为：【%s】" % (status), " (0-未支付 1-处理中 2-已支付 3-退款中 4-退款成功 5退款失败 6支付失败)")

cursor.close()

# self.driver.refresh()

    except Exception as msg:

print(u"异常原因%s" % msg)

# self.add_img()

        self.save_screen_shot()

raise



元素分离：


部分代码入下：

from selenium.webdriver.common.byimport By

class PublicLoc:

"""公共组件"""

class LoginPageLoc:

"""登录"""

    email = (By.ID, "email")

password = (By.ID, "password")

sign_in = (By.ID, "js-btnSubmit")

class HomePageLoc:

"""首页"""

    # 标题栏

    user_info = (By.CSS_SELECTOR, "a.siteHeader_userAccountLink")

sign_in = (By.CSS_SELECTOR, "a.siteHeader_userLinkLogin")

my_fav = (By.XPATH, "//header/div[2]/div[3]/div[1]/div[1]/div[1]/p/a")

cart = (By.XPATH, "//header/div[2]/div[3]/div[3]/a[2]/p")

# 用户信息菜单

    my_order = (By.XPATH, "//ul/li[2]/a")

my_tickets = (By.XPATH, "//ul/li[3]/a")

my_message = (By.XPATH, "//ul/li[4]/a")

my_wallet = (By.XPATH, "//ul/li[5]/a")

my_points = (By.XPATH, "//ul/li[6]/a")

my_profile = (By.XPATH, "//ul/li[7]/a")

my_coupon = (By.XPATH, "//ul/li[8]/a")

logout = (By.CLASS_NAME, "js-logout")

# 弹窗

    new_user_pop = (By.CLASS_NAME, "newUserPop")

close_pop = (By.CLASS_NAME, "layui-layer-setwin")

class UserInfoPageLoc:

"""用户信息页"""

    goods_images = (By.CSS_SELECTOR, "a.orderItem_thumb")

goods_names = (By.CSS_SELECTOR, "a.orderItem_title")

class GoodsInfoPageLoc:

"""商品详情页"""

    qty = (By.CLASS_NAME, "compInputNumber_input")

num_plus = (By.CLASS_NAME, "compInputNumber_reduce")

num_reduce = (By.CLASS_NAME, "compInputNumber_plus")

buy_button = (By.XPATH, "//*[@class='goodsIntro_btnWrap js-buyBtnWrap']/a[2]")

paypal_button = (By.XPATH, "//*[@class='goodsIntro_btnWrap js-buyBtnWrap']/a[2]")

class PlaceInfoPageLoc:

"""订单确认页"""

    # place_button = (By.XPATH, "//a[@class='ckOl_totalBtn btn middle strong']")

    place_button = (By.XPATH, "//a[contains(text(),'Place Your Order')]")

class PaymentInfoPageLoc:

"""收银台"""

    pay_button = (By.XPATH, "//*[@class='placeOrder btn block toPayBtn']")

pay_currencyselect = (By.XPATH, "//*[@class='currency_select']")

pay_currencyconfirm = (By.XPATH, "//*[@class='currency_select']/option[2]")

Wallet_ele = (By.XPATH, "//span[contains(text(),'My Wallet')]")

Wallet_input = (By.XPATH, "//*[@placeholder='Please enter the Wallet password']")

paypal_src = (By.XPATH, '//*[@src="https://uidesign.zafcdn.com/ZF/image/z_promo/20190418_9285/PayPal@2x.png"]')

creditcard_src = (By.XPATH, '//*[@src="https://uidesign.gbtcdn.com/GB/images/others/check_out/57x35/visa.png?imbypass=true"]')

creditcard_holder = (By.XPATH, "//*[@placeholder='Card Holder']")

creditcard_Number = (By.XPATH, "//*[@placeholder='Card Number']")

creditcard_Code = (By.XPATH, "//*[@placeholder='Security Code']")

creditcard_mouth = (By.XPATH, '//*[@curchannel="CREDITCARD"]/div[2]/div/select')

creditcard_day = (By.XPATH, '//*[@curchannel="CREDITCARD"]/div[3]/div/select')

ebanxinstalment_src = (By.XPATH, '//*[@src="https://uidesign.gbtcdn.com/GB/images/others/check_out/57x35/elo.png?imbypass=true"]/../../em[1]/img')

ebanxinstalment_installments = (By.XPATH, '//*[@class="formList_select installments"]/option[2]')

ebanxinstalment_CPF = (By.XPATH, "//*[@placeholder='CPF']")

ebanxinstalment_Titular = (By.XPATH, "//*[@placeholder='Titular do cartão']")

ebanxinstalment_Nmero = (By.XPATH, "//*[@placeholder='Número de cartão']")

ebanxinstalment_Cdigo = (By.XPATH, "//*[@placeholder='Código de segurança']")

ebanxinstalment_Month = (By.XPATH, '//*[@name="expirationMonth"]')

ebanxinstalment_Year = (By.XPATH, '//*[@name="expirationYear"]')

MXCC_Cdigo = (By.XPATH, "//*[@placeholder='Código de seguridad']")

BEBC_holder = (By.XPATH, '//*[@curchannel="ADN_BEBC"]/div[4]/div/input')

EPS_src = (By.XPATH, '//*[@src="https://icss1.gearbest.com/imagecache/GB2/images/domeimg/pay_method/eps.jpg"]')

SOFORT_src = (By.XPATH, '//*[@src="https://uidesign.gbtcdn.com/GB/images/others/check_out/sofort.png?02"]')

DEGP_src = (By.XPATH, '//*[@src="https://icss1.gearbest.com/imagecache/GB2/images/domeimg/pay_method/giropay.jpg"]')

LipaPay_src = (By.XPATH, '//*[@src="https://uidesign.gbtcdn.com/check_out/Lipapay.png?impolicy=ture"]')

MYOB_src = (By.XPATH, '//*[@src="https://uidesign.gbtcdn.com/check_out/ADN_MYOB.png?impolicy=high"]')

THOB_src = (By.XPATH, '//*[@src="https://css.zafcdn.com/imagecache/ZF_V2/images/domeimg/pay_method/ADN_THOB.jpg"]')

BANK_TRANSFER_src = (By.XPATH, '//*[@src="https://icss1.gearbest.com/imagecache/GB2/images/domeimg/pay_method/WiredTransfer.jpg"]')

WESTERN_src = (By.XPATH, '//*[@src="https://icss1.gearbest.com/imagecache/GB2/images/domeimg/pay_method/WesternUnion.jpg"]')

EBX_SVPG_src = (By.XPATH, '//*[@src="https://uidesign.gbtcdn.com/check_out/Servipag.png?impolicy=high"]')

EBX_SVPG_doc = (By.XPATH, "//*[@curchannel='EBX_SVPG']/div[1]/div/select")

EBX_SVPG_number = (By.XPATH, "//*[@curchannel='EBX_SVPG']/div[2]/div/input")

ADN_TRSP_src = (By.XPATH, '//*[@src="https://uidesign.gbtcdn.com/check_out/Trustpay.png?impolicy==true"]')

ADN_TRSP_issuerId = (By.XPATH, "//*[@name='issuerId']")

Postepay_src = (By.XPATH, '//*[@src="https://uidesign.gbtcdn.com/GB/images/others/check_out/postepay.jpg"]')

PagoEfectivo_src = (By.XPATH, '//*[@src="https://icss1.gearbest.com/imagecache/GB2/images/domeimg/pay_method/pagoefectivo.png"]')

SQ_ESCC1_src = (By.XPATH, '//*[@src="https://uidesign.gbtcdn.com/check_out/SQ_ESCC1.png"]')

poli_src = (By.XPATH, '//*[@src="https://uidesign.gbtcdn.com/check_out/poli_m.png?impolicy=high"]')

Webmoney_src = (By.XPATH, '//*[@src="https://icss1.gearbest.com/imagecache/GB2/images/domeimg/pay_method/webmoney.jpg"]')

WPG_Pay_src = (By.XPATH, '//*[@src="https://uidesign.gbtcdn.com/check_out/Gpay.png?03"]')

class ThirdInfoPageLoc:

"""支付第三方"""

    mainSubmit = (By.XPATH, "//*[@id='mainSubmit']")

GC_password = (By.XPATH, "//*[@type='password']")

GC_Entry = (By.XPATH, "//*[@name='UsernamePasswordEntry']")

poli_continue = (By.XPATH, "//*[@name='continue']")

poli_Username= (By.XPATH, "//*[@name='Username']")

poli_Password = (By.XPATH, "//*[@name='Password']")

poli_LoginButton = (By.XPATH, "//*[@name='LoginButton']/../button")

poli_textContinue = (By.XPATH, "//*[contains(text(),'Continue')]")

poli_primarybutton = (By.XPATH, "//*[@class='button stp-button primary-button']")

poli_ConfirmButton = (By.XPATH, "//*[@name='ConfirmButton']/../button")

WPG_Pay_email = (By.XPATH, "//*[@type='email']")



数据分离：敏感数据


六，一个测试用例代码的实现，整个流程。

1.写testcase，基础case测试用例脚本。

比如登录：

def gb_login(self):

# self.headers = {'User-Agent': self.ua}

 pc = HomePage(self.driver)   

 lg = LoginPage(self.driver)

 pc.get(self.GBloginURL)

 lg.login(self.username, self.password)

其中取入下数据：


上图取这里的数据：

class LoginPageLoc:

"""登录"""

    email = (By.ID, "email")

password = (By.ID, "password")

sign_in = (By.ID, "js-btnSubmit")

综上：完成了一个登录。

第二步：

登录脚本case加入suilt套件：




import unittest

from seleniumimport webdriver

from UI_AUTOMATION.test.page.PC.gb_pc_base_caseimport GBBaseCase

from UI_AUTOMATION.test.page.pageconfig.connectimport GBConnect

# from UI_AUTOMATION.test.page.form

# from ..page.form.form_pc import *

# unittest.TestCase

class BaseTestCase(unittest.TestCase):

@classmethod

    def setUpClass(cls):

# option = webdriver.ChromeOptions()

# option.add_argument('headless')  # 静默模式

# cls.driver = webdriver.Chrome(chrome_options=option)

        cls.driver = webdriver.Chrome()

@classmethod

    def tearDownClass(cls):

# cls.driver.quit()

        pass

    # def add_img(self):

#    self.imgs.append(self.driver.get_screenshot_as_base64())

#    return True

    def setUp(self):

# 在是python3.x 中，如果在这里初始化driver ，因为3.x版本 unittest 运行机制不同，会导致用力失败时截图失败

        self.imgs = []

self.addCleanup(self.cleanup)

def cleanup(self):

pass

    def login_GB(self):

GBBaseCase(self.driver).gb_login()

def test_GB_wallet(self):

'''电子钱包支付'''

GBConnect().GB_adress_Turkey()

GBBaseCase(self.driver).gb_goodtobuy()

GBBaseCase(self.driver).gb_placeorder()

GBBaseCase(self.driver).payment_wallet()

GBBaseCase(self.driver).gb_checkorder()

def test_GB_paypal(self):

if __name__ =="__main__":

unittest.main()

第三步，run启动程序脚本


import time

import unittest

from UI_AUTOMATION.test.testcase.gb_pc_caseimport BaseTestCase

from UI_AUTOMATION.utils.configimport REPORT_PATH

from UI_AUTOMATION.utils.haoemailimport Email

from UI_AUTOMATION.test.page.pageconfig.CIimport GBConnect

# # 构造测试集

suite = unittest.TestSuite()

suite.addTest(BaseTestCase('login_GB'))

'''

def create_test_suite():

test_list_path = "../testcase"

test_unit = unittest.TestSuite()

discover = unittest.defaultTestLoader.discover(test_list_path, pattern="test_*cii.py")

for test_suite in discover:

for test_case in test_suite:

test_unit.addTest(test_case)

print(test_case)

return test_unit

all_test = create_test_suite()

'''

now_time = time.strftime('%Y%m%d-%H%M%S', time.localtime())

report = REPORT_PATH +'\\' +'PAY_Report '+ now_time +'.html'

# print(report)

### 从代码执行结果里面获取数据      HTMLTestRunner

with open(report,"wb")as outfile:

 runner = HTMLTestRunner(stream=outfile,title=u"GB-PC-PAY_UITest",description=u"用例执行情况：",verbosity=2,retry=0,save_last_try=False)

aa = runner.run(suite)

e = Email(path=report,message='''

本邮件是支付UI自动化测试报告，请下载或者使用浏览器查看附件内容.

如果有任何问题，请及时联系：测试组. Thank you!

--------------------------------------------

深圳市环球易购电子商务有限公司

技术中心\电子项目部\质量管控组

姜家豪

TEL：18682436420

Email：jiangjiahao@globalegrow.com

''')

e.send()

'''***CI确认发送：‘y’***"

***CI不发送：‘n’***'''

while 1:

choose =input('输入命令：')

if choose =='y' and 'Y':

print("CI已发送！")

break

    if choose =='n' and 'N':

print("CI已取消发送，并程序结束！！！")

exit(0)

else:

print("输入命令有误，请重新输入!")

e = Email(path=report,message='''

本邮件是支付UI自动化测试报告，请下载或者使用浏览器查看附件内容.

如果有任何问题，请及时联系：测试组. Thank you!

--------------------------------------------

深圳市环球易购电子商务有限公司

技术中心\电子项目部\质量管控组

姜家豪

TEL：18682436420

Email：jiangjiahao@globalegrow.com

''')

e.send()

conn = GBConnect()##发CI接口

conn.CI_pc_date(runner, aa)

### 通过打开报告，从页面获取数据

# with open(report, "wb") as outfile:

#    runner = HTMLTestRunner(stream=outfile, title=u"GB-PC-PAY_UITest", description=u"用例执行情况：", verbosity=2, retry=0, save_last_try=False)

#    runner.run(suite)

#    conn = GBConnect()

#    conn.CI_pc_page(report, runner)



作者：hao0_0
链接：https://www.jianshu.com/p/3aad32ed83bf
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。