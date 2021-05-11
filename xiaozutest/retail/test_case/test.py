from retail.test_case.models.readexcel import  ReadExcel
from retail.test_case.models.log import Logger
from retail.test_case.models.driver import WebDriver

log =   Logger(__name__)
eleDate =  ReadExcel()
menulist = [
    (eleDate.readExcel(1, 2), eleDate.readExcel(1, 3)),
    (eleDate.readExcel(2, 2), eleDate.readExcel(2, 3)),
    (eleDate.readExcel(3, 2), eleDate.readExcel(3, 3)),
    (eleDate.readExcel(4, 2), eleDate.readExcel(5, 3)),
    (eleDate.readExcel(5, 2), eleDate.readExcel(5, 3)),
    (eleDate.readExcel(6, 2), eleDate.readExcel(6, 3)),
    (eleDate.readExcel(7, 2), eleDate.readExcel(7, 3)),
    (eleDate.readExcel(8, 2), eleDate.readExcel(8, 3)),
    (eleDate.readExcel(9, 2), eleDate.readExcel(9, 3)),
    (eleDate.readExcel(10, 2), eleDate.readExcel(10, 3)),
    (eleDate.readExcel(11, 2), eleDate.readExcel(11, 3))
]


def sd(*ad):
    print(ad)
def sd3(ad):
    print(ad)
def sd4(*ad):
    return sd(*ad)


# def sd4(ad):
#     print(*ad)
# def sd2(add):
#     try:
#         h = 1/add
#         print(h)
#     except Exception as e:
#         log.logger.exception('failed')
#         raise e
#     else:
#         pass

# sd3(menulist[0][0],menulist[0][1])
# sd3(menulist[0])
# sd4(menulist[0][0],menulist[0][1])

# sd(menulist[0][0],menulist[0][1])
# sd3(menulist[0][0],menulist[0][1])
from retail.test_case.page_obj.base_page import BasePage
# sd2(0)
# driver = WebDriver().fireFoxDriver()
a=BasePage.menuElement[0][0]
b=BasePage.menuElement[0][1]
c=(a,b)
print(c)
print(*c)
print(*BasePage.menuElement[0])
# a=BasePage(driver,'http://www.baidu.com')
# a.open()
# a.findElement(*c).send_keys('八十多')

# driver.self.findElement(menulist[0]).send_keys('八十多')
# def saveScreenShot(filename):
#         # value_list=[]
#         list = filename.split('.')
#
#         # for value in list:
#         #     value_list.append(value)
#         if list[1] in ['jpg','png']:
#             print('1')
#         else:
#             print('2')
# saveScreenShot('asdghi.png')