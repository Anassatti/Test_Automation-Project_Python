import configparser

config = configparser.RawConfigParser()
config.read(r"C:\Users\anass\PycharmProjects\E-commerceWebsite\Configurations\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'basURL')
        return url

    @staticmethod
    def getApplicationUsername():
        userName = config.get('common info', 'userName')
        return userName

    @staticmethod
    def getApplicationPassword():
        Password = config.get('common info', 'Password')
        return Password
