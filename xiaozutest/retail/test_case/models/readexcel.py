from retail.config.conf import *
import xlrd
from retail.test_case.models.log import Logger
log=Logger(__name__)
class ReadExcel(object):
    def __init__(self,fileName='elementData.xlsx',sheetName='home_page_elements'):
        try:
            self.name=sheetName
            self.dataFile = os.path.join(dataPath,fileName)
            #打开excel
            self.workbook = xlrd.open_workbook(self.dataFile)
            #打开表
            self.sheetName = self.workbook.sheet_by_name(sheetName)
            # self.sheetName = xlrd.open_workbook(self.dataFile).sheet_by_name(sheetName)
        except Exception:
            log.logger.exception('reading %s failed '%sheetName)
            raise
        else:
            log.logger.info('reading %s succeed '%sheetName)

    def readExcel(self,row,column):
        try:
            value = self.sheetName.cell(row,column).value
        except Exception:
            log.logger.exception('read value %s,%s in sheetName %sfailed'%(row,column,self.name))
            raise
        else:
            log.logger.info('read value %s,%s in sheetName %s succeed' % (row, column,self.name))
            return value

if __name__=='__main__':
    doExcel=ReadExcel()
    value = doExcel.readExcel(1,3)
    print(value)



# import xlrd
# from retail.test_case.models.log import Logger
# from retail.config.conf import *
# log = Logger(__name__)
# class DoExcel(object):
#     def __init__(self,fileName='elementData.xlsx',sheetName='home_elementsInfo'):
#         self.name = sheetName
#         self.datafile = os.path.join(dataPath,fileName)
#         self.workbook = xlrd.open_workbook(self.datafile)
#         self.sheetName = self.workbook.sheet_by_name(sheetName)
#
#     def readExcel(self,row,column):
#         try:
#             value = self.sheetName.cell(row,column)
#         except Exception:
#             log.logger.exception('read value %s,%s in sheetname %s failed'%row,column,self.name)
#             raise
#         else:
#             log.logger.info('read value %s,%s in sheetname %s succeed'%row,column,self.name)




