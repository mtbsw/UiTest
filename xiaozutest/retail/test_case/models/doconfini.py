import configparser
# from retail.test_case.models.log import Logger
# from retail.config.conf import *

# log = Logger(__name__)
class DoConfIni(object):
        def __init__(self):
            self.cf = configparser.ConfigParser()

        def getConfValue(self,filename,section,name):
            try:
                self.cf.read(filename)
                value = self.cf.get(section,name)
            except Exception as e:
                # log.logger.info("read file [%s] for [%s] failed , did not get the value"%(filename,section))
                raise e
            else:
                # log.logger.info('read excel value [%s] succeed! ' % value)
                return value
        def writeConfValue(self,filename,section,name,value):
            try:
                self.cf.add_section(section)
                self.cf.set(section,name,value)
                self.cf.write(open(filename,'w'))
            except  Exception :
                # log.logger.exception('section %s has been exist!'%section)
                raise configparser.DuplicateSectionError(section)
            else:
                # log.logger.info('write section'+section+'with value'+value+'successed')
                pass
if __name__=='__main__':
    pass
