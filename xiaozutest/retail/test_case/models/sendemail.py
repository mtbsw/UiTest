# from retail.test_case.models.log import Logger
# from retail.config import conf
# import os
# from email.mime.text import MIMEText
# from email.header import  Header
# import smtplib
#
# log = Logger(__name__)
# class SendEmail(object):
#     def __init__(self,receivertext='mail_receiver.txt',subject='测试报告',server='smtp.qq.com',fromuser='1138940167@qq.com',frompassword='dpvakwxfgjyohdbc',sender='1138940167@qq.com'):
#         self._server = server
#         self._fromuser=fromuser
#         self._frompassword=frompassword
#         self._sender=sender
#         self._subject=subject
#         try:
#             openReceiver = open(os.path.join(conf.dataPath, receivertext))
#         except Exception:
#             log.logger.exception('open or read file [%s] failed' % openReceiver)
#         else:
#             log.logger.info('open file [%s] succeed' % openReceiver)
#             for line in openReceiver:
#                 msg = [i.strip() for i in line.split(',')]
#                 log.logger.info('reading file succeed')
#                 self._receiver = msg
#
#
#     def sendEmail(self,fileName):
#         #打开报告文件读取文件内容
#         try:
#             filePath = os.path.join(conf.reportPath,fileName)
#             openFile = open(filePath,'rb')
#             fileMessage = openFile.read()
#         except Exception:
#             log.logger.exception('can not find file [%s] in path '%filePath)
#             raise
#         else:
#             log.logger.info('open and read file [%s] succeed '%filePath)
#             openFile.close()
#             #设置邮件
#             #内容/主题/发送人
#             msg = MIMEText(fileMessage,'html','utf-8')
#             msg['subject'] = Header(self._subject,'utf-8')
#             msg['from'] =self._sender
#             #连接服务器,登录/发送
#             try:
#                 smtp = smtplib.SMTP()
#                 smtp.connect(self._server)
#                 smtp.login(self._fromuser,self._frompassword)
#             except Exception:
#                 log.logger.exception('can not connect server %s or username and password is wrong!'%self._server)
#                 raise
#             else:
#                 log.logger.info('connect %s and login succeed'%self._server)
#                 try:
#                     smtp.sendmail(self._sender,self._receiver,msg.as_string())
#                 except Exception:
#                     log.logger.exception('send email failed')
#                 else:
#                     log.logger.info('send email succeed')

# def getReceiverInfo(fileName):
#     try:
#         openFile = open(os.path.join(conf.dataPath,fileName))
#     except Exception:
#         log.logger.exception('open or read file [%s] failed'%openFile)
#     else:
#         log.logger.info('open file [%s] succeed'%openFile)
#         for line in openFile:
#             msg = [i.strip() for i in line.split(',')]
#             log.logger.info('reading file succeed')
#             return msg

# if __name__ == '__main__':
#     # readMsg =  getReceiverInfo('mail_receiver.txt')
#     SendEmail().sendEmail('G7其他6国表达对世卫组织支持，美国“断供”后英国迅速“打脸”.html')

from retail.test_case.models.log import Logger
from retail.config import conf
import smtplib
from email.mime.text import MIMEText
import os
from email.header import  Header

log = Logger(__name__)
class SendEmail(object):
    def __init__(self,receiverText='mail_receiver.txt',subject='测试报告',server='smtp.qq.com',fromuser='1138940167@qq.com',frompassword='dpvakwxfgjyohdbc',sender='1138940167@qq.com'):
        self._subject = subject
        self._fromuser=fromuser
        self._frompassword = frompassword
        self._sender=sender
        self._server = server
        try:
            receiverMsg = open(os.path.join(conf.dataPath,receiverText))
        except Exception:
            log.logger.exception('can not find receiver file %s'%receiverText)
        else:
            for line in receiverMsg:
                msg = [i.strip() for i in line.split(',')]
                log.logger.info('read receiver address succeed!')
                self._receiver = msg

    def sendEmail(self,fileName):
        try:
            contect = os.path.join(conf.reportPath,fileName)
            openFile = open(contect,'rb')
            meg = openFile.read()
        except Exception:
            log.logger.exception('read file %s failed'%contect)
        else:
            log.logger.info('read file %s succeed'%contect)
            openFile.close()

            mimetext = MIMEText(meg, 'html', 'utf-8')
            mimetext['subject'] = Header(self._subject,'utf-8')
            mimetext['from'] = self._sender
            try:
                smtp = smtplib.SMTP()
                smtp.connect(self._server)
                smtp.login(self._fromuser,self._frompassword)
            except Exception:
                log.logger.exception('can not connect %s or user and password is wrong!'%self._server)
            else:
                log.logger.info('eamil server login succeed! ')
                try:
                    smtp.sendmail(self._sender,self._receiver,mimetext.as_string())
                except Exception:
                    log.logger.exception('sendemail failed')
                else:

                     log.logger.info('send email succeed!')
if __name__=='__main__':
    SendEmail().sendEmail('G7其他6国表达对世卫组织支持，美国“断供”后英国迅速“打脸”.html')









