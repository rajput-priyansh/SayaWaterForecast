# Python code to illustrate Sending mail from
# your Gmail account
import smtplib
from Data import config_helper
from Logging import LoggeR


def sendMailForException(exMessage,subject):
    try:
        _config = config_helper.read_config()
        # host = _config.get('MailSetting','host')
        # print(host)
        # print(_config.get('ConnectionString', 'pycon'))
        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login("chirag.maxlink@gmail.com", "taonjsoeypiimhzv")

        # message to be sent

        message =  exMessage


        # sending the mail
        s.sendmail("chirag.maxlink@gmail.com", "chirag.parmar@sayalife.in", message)

        # terminating the session
        s.quit()
        return True
    except Exception as Argument:
        LoggeR.critical("Some Exception :   " + Argument.__str__())
        print(Argument)
        return  False

