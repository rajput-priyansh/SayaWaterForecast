import logging
from datetime import datetime

from Data import getConfigurationSettings

def writeExpceptionToTexFile(Argument):
    try:
        settings = getConfigurationSettings.getconfigurations();
        f = open(settings['deployedpath'] +"/Logs/"+"LogException.txt", "a")

        # writing in the file
        f.write(datetime.now().__str__() +"---->"+str(Argument)+"\n")
        # closing the file
        f.close()
    except Exception as Argument:
        logging.error(Argument.__str__())
