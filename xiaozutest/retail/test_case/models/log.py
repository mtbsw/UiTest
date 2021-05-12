import logging
import time
from xiaozutest.retail.config import conf
import os
class Logger(object):
    def __init__(self,loggername,CmdLevel=logging.INFO,FileLevel=logging.INFO):
        self.logger = logging.getLogger(loggername)
        self.logger.setLevel(logging.DEBUG)
        #日志输出格式
        fmt = logging.Formatter('%(asctime)s-%(filename)s:[%(lineno)s]-[%(levelname)s]-%(message)s')
        #日志文件名称
        currTime = time.strftime("%Y-%m-%d")
        self.loggerFileName = conf.logPath+'\log'+currTime+'.log'
        #设置控制台输出
        #sh = logging.StreamHandler()
        #sh.setFormatter(fmt)
        #sh.setLevel(CmdLevel)
        #设置文件输出
        fh = logging.FileHandler(self.loggerFileName)
        fh.setFormatter(fmt)
        fh.setLevel(FileLevel)
        self.logger.addHandler(fh)


if __name__ == '__main__':
    testLogger = Logger("test")
    testLogger.logger.info("test succeed")


# class Logger(object):
#     def __init__(self,loggername,FileLevel,CmdLevel):
#         self.logger=logging.getLogger(loggername)
#         self.logger.setLevel(logging.INFO)
#         fm = logging.Formatter('%(asctime)s -[%(filename)s]-%(module)s-%(funcName)s-%(message)s')
#         currtime = time.strftime('%Y-%m-%d')
#         self.filename = r'D:\PycharmProjects\xiaozutest\retail\report\log\log'+currtime+'.log'
#
#         hd=logging.FileHandler(self.filename)
#         hd.setFormatter(fm)
#         hd.setLevel(FileLevel)
#
#         self.logger.addHandler(hd)