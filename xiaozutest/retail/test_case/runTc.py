import unittest
from BeautifulReport import BeautifulReport
from retail.config.conf import *
from retail.test_case.models.testreport import testreportCN,testreport
import time
from retail.test_case.models.sendemail import SendEmail

if __name__ == '__main__':
    runner,fp,filename = testreportCN()
    # runner1, fp1, filename1 = testreport()
    test_suite = unittest.defaultTestLoader.discover(tcPath,pattern = '*Tc.py')
    runner.run(test_suite)
    fp.close()
    SendEmail().sendEmail(filename)


    #
    # test_suite = unittest.defaultTestLoader.discover(tcPath,pattern = '*Tc.py')
    # runTc(test_suite)
    # fp.close()