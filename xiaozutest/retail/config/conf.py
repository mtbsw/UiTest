import os
import sys
from xiaozutest.retail.test_case.models import doconfini
import time
currenTime = time.strftime('%Y-%m-%d')
#获取当前路径 [0]是目录[1]是文件名
currPath = os.path.split(os.path.realpath(__file__))[0]
#读取配置文件获取项目路径
readConfig = doconfini.DoConfIni()
proPath = readConfig.getConfValue(os.path.join(currPath,'config.ini'),'project','project_path')
#获取日志路径
logPath = os.path.join(proPath,'xiaozutest','retail','report','log')
#测试用例路径
tcPath = os.path.join(proPath,'xiaozutest','retail','test_case','page_obj')
#获取报告路径
reportPath = os.path.join(proPath,'xiaozutest','retail','report','testreport')
#获取测试数据路径
dataPath = os.path.join(proPath,'xiaozutest','retail','data','testdata')
#保存截图路径
#错误截图
failImagePath = os.path.join(proPath,'xiaozutest','retail','report','image','fail','%sfail'%currenTime)
#成功截图
passImagePath = os.path.join(proPath,'xiaozutest','retail','report','image','pass','%spass'%currenTime)

# 被调函数名称
funcName = sys._getframe().f_code.co_name
# 被调函数所在行号
funcNo = sys._getframe().f_back.f_lineno
# 被调函数所在文件名称
funcFile = sys._getframe().f_code.co_filename

if __name__ == '__main__':
    print(funcNo)