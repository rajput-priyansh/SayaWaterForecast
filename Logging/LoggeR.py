import logging

# Gets or creates a logger
logger = logging.getLogger(__name__)

# set log level
logger.setLevel(logging.WARNING)

# define file handler and set formatter
file_handler = logging.FileHandler('C:/inetpub/wwwroot/SayaMLForecast/SayaWaterForecast/Logs.log')
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)

# add file handler to logger
logger.addHandler(file_handler)



# import logging
# import sys
# from logging.handlers import QueueHandler
# from Data import  getConfigurationSettings
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
#
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
# consoleHandler = logging.StreamHandler(sys.stdout)
# consoleHandler.setLevel(logging.DEBUG)
# consoleHandler.setFormatter(formatter)
#
# fileHandler = logging.handlers.RotatingFileHandler(filename="D:/Python/SayaWaterForecast/Logs/error.log",maxBytes=1024000, backupCount=10, mode="a")
# # fileHandler = logging.FileHandler(filename="D:/Python/SayaWaterForecast/Logs/error.log")
# fileHandler.setLevel(logging.INFO)
# fileHandler.setLevel(logging.debug)
# fileHandler.setLevel(logging.error)
# fileHandler.setFormatter(formatter)
# mailsettings= getConfigurationSettings.getconfigurations()
# # smtpHandler = logging.handlers.SMTPHandler(
# #               mailhost = ('smtp.gmail.com',587),
# #               fromaddr = mailsettings['fromMail'],
# #               toaddrs =   'chirag.parmar@sayalife.in',  #mailsettings['to'],
# #               subject = "Logging test mail!"
# #             )
# # smtpHandler.setLevel(logging.CRITICAL)
# # smtpHandler.setFormatter(formatter)
#
# logger.addHandler(consoleHandler)
# logger.addHandler(fileHandler)
# # logger.addHandler(smtpHandler)