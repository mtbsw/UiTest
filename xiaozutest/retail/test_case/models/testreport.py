from xiaozutest.retail.test_case.models.log import Logger
from xiaozutest.retail.config import conf
import time
import os
import HTMLTestRunner
import unittest
import BeautifulReport
import HTMLTestReportCN

log = Logger(__name__)

def testreport():
    currTime = time.strftime('%Y-%m-%d %H-%M-%S')
    fileName = os.path.join(conf.reportPath,'普通测试报告%s.html'%currTime)
    # fileName = conf.reportPath + r'\report' + currTime + '.html'
    try:
        fp = open(fileName,'wb')
    except Exception:
        log.logger.exception('can not generate test report file %s'%fileName)
    else:
        log.logger.info('generate test report %s succeed'%fileName)
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='测试报告',description=' 处理器:i7 7500u '' 系统:windows10 '' 内存:8g')
        return runner,fp,fileName
def testreportCN():
    currTime = time.strftime('%Y-%m-%d %H-%M-%S')
    fileName = os.path.join(conf.reportPath,'普通测试报告%s.html'%currTime)
    # fileName = conf.reportPath + r'\report' + currTime + '.html'
    try:
        fp = open(fileName,'wb')
    except Exception:
        log.logger.exception('can not generate test report file %s'%fileName)
    else:
        log.logger.info('generate test report %s succeed'%fileName)
        runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,title='测试报告',description=' 处理器:i7 7500u '' 系统:windows10 '' 内存:8g')
        return runner,fp,fileName

def addTc(TCpath= conf.tcPath,rule ='*TC.py'):
    discover = unittest.defaultTestLoader.discover(TCpath,pattern=rule)
    return discover

def runTc(discover):
    currTime = time.strftime('%Y-%m-%d  %H-%M-%S')
    fileName = '美化测试报告'+currTime+'.html'
    try:
        result = BeautifulReport.BeautifulReport(discover)
        result.report(filename = fileName,description='测试报告',report_dir = conf.reportPath)
    except Exception:
        log.logger.exception('failed to generate test report')
    else:
        log.logger.info('succeed to generate test report [%s]'%fileName)
        return fileName
if __name__ == '__main__':
    testreport()
    suite = addTc(rule='*Tc.py')
    # r =testreport()[0]
    # r.run(suite)
    runTc(suite)






