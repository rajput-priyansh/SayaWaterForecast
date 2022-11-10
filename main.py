#!/usr/bin/env python
# coding: utf-8

# In[4]:


import warnings
import itertools
#import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
#from fbprophet import Prophet  # from fbprophet
import prophet
# Piyush
# import pymssql
import psycopg2
import sys
import os
import logging
from Logging import LoggeR
from GetRawData import getRawData

from datetime import datetime, timedelta
import calendar

from SendEmail import sendEmailToClient

warnings.filterwarnings("ignore")
plt.style.use('fivethirtyeight')
from dateutil.relativedelta import relativedelta

if __name__ == "__main__":
    try:
        print("File in running mode....please don't stop it...." + datetime.now().__str__())
        LoggeR.writeExpceptionToTexFile("File in running mode....please don't stop it...6 Months Data Insert!!-->>" + datetime.now().__str__())        
        getRawData.startWaterForecastFileDownload()
    except Exception as Argument:
        # sendEmailToClient.sendMailForException(Argument.__str__(),"SayaML InsertException")
        print("Some Exception :   " + Argument.__str__())
        LoggeR.writeExpceptionToTexFile(Argument.__str__())
        # print(Argument)
        # sendEmailToClient.sendMailForException(Argument.__str__())
        pass
    # finally:
    #    os.remove("C:/inetpub/wwwroot/SayaMLForecast/SayaWaterForecast/RawDataDump")
