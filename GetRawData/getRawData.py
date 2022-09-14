import os
import warnings
import itertools
# import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
from fbprophet import Prophet  # from fbprophet
# Piyush
# import pymssql
import psycopg2
import sys
from Data import config_helper
# from rawDataDownload import getRawData
import dateutil.relativedelta
from datetime import datetime, timedelta
import datetime
import calendar

from Logging import LoggeR
from SendEmail import sendEmailToClient

warnings.filterwarnings("ignore")
plt.style.use('fivethirtyeight')
from dateutil.relativedelta import relativedelta

from Data import connectionDB, getConfigurationSettings
from ForecastingModel import prophetDataModel


def startWaterForecastFileDownload():
    try:
        # sDate = input("Enter Start Date Formate( dd/mm/yyyy ) : ")
        # eDate = input("Enter End Date Formate( dd/mm/yyyy ) : ")
        today = datetime.datetime(2022, 9, 1)  # datetime.today()
        months = calendar.monthrange(today.year, today.month)[1]
        sDate = today + relativedelta(months=-1)
        # months=calendar.monthrange(sDate.year, sDate.month)[1]
        # sDate=datetime.today() + timedelta(days=-months)
        eDate = datetime.datetime(sDate.year, sDate.month, sDate.day) + relativedelta(
            day=31)  # datetime.today() + timedelta(days=-5)  # days=-1 replace -5 with -1 once this file runs ---chirag 05072022
        # startDate = datetime.strptime(sDate, '%d/%m/%Y')
        # endDate = datetime.strptime(eDate, '%d/%m/%Y')
        finaldate = sDate.strftime('%y%m%d')  # sys.argv[2]
        finalEdate = eDate.strftime('%y%m%d')  # sys.argv[3]
        print(finaldate)
        print(finalEdate)
        # if datetime.now().hour == 14 and datetime.now().minute == 55 and datetime.now().second >= 59:
        print("started getting data from server" + finaldate.__str__())
        # finaldate = date.today()
        # yesterdaydate = finaldate.strftime('%y%m%d')
        # Start Exporting in CSV open
        # customerId = [2,165,172,213,214,217,10227,10342,10511,10512,10519]
        #finalIds = [10260]
        connectionSetting = getConfigurationSettings.getconfigurations()
        connObj = psycopg2.connect(user="postgres",
                                  password="test#123",
                                  host="52.40.141.127",
                                  port="5432",
                                  database="SAYA")
        #connObj = connectionDB.connectDatabase(connectionSetting['_dbusername'], connectionSetting['_dbpassword'],
        #                                       connectionSetting['_hostlive'], connectionSetting['_dbport'],
        #                                       connectionSetting['_dbsaya'])
		
        cur = connObj.cursor()
        # conn = ''
        customerIdQuery = 'select "Id" from "Customer" where "AccountType"  in (5,6) and "IsDeleted"  = false and "IsActive"  = true ;';

        with connObj.cursor() as cur:
            cur.execute(customerIdQuery)
            finalIds = cur.fetchall()
            print("Fetched records: %s" % finalIds)
        for id in finalIds:
            try:
                id= str(id)           #uncomment when working with live fetch ids
                id=int(id[1:-2])
                print(id)
                # id = 10260
                query = "select * from GetWaterMeterDataForDataFile ( " + finaldate.__str__() + "::varchar(100)" + "," + finalEdate.__str__() + "::varchar(100)" + "," + id.__str__() + "::bigint" + ")"
                print(query)
                writer = pd.ExcelWriter(
                    'C:/inetpub/wwwroot/SayaMLForecast/SayaWaterForecast/RawDataDump/f' + finalEdate.__str__() + id.__str__() + '.xlsx',
                    engine='xlsxwriter')
                df = pd.read_sql(query, connObj)
                df.to_excel(writer, sheet_name='Sheet1')
                # filedialog.asksaveasfilename(filetypes=[('excel file', '*.xlsx')], defaultextension='.xlsx')
                writer.save()
                # writer.close()
                print('Out from get data')
                prophetDataModel.main(finalEdate, finalEdate + id.__str__(), id, df)
            except Exception as Argument:
                # sendEmailToClient.sendMailForException(Argument.__str__(),"SayaML InsertException for Customer : " + id.__str__())

                # LoggeR.critical("Some Exception :   " + Argument.__str__())
                print("Some Exception :" + Argument.__str__())
                LoggeR.logger.error(Argument.__str__() ,"For the User :" ,id.__str__());
                # sendEmailToClient.sendMailForException(Argument.__str__())
                # logger.error("a")
                pass
                continue
            #finally:
                 # os.close("D:/Python/SayaWaterForecast/RawDataDump/f" + finalEdate.__str__() + id.__str__() + ".xlsx")
                 # os.system('TASKKILL /F /IM excel.exe')
                 #writer.close()
                 #os.remove("C:/inetpub/wwwroot/SayaMLForecast/SayaWaterForecast/RawDataDump/f" + finalEdate.__str__() + id.__str__() + ".xlsx")



    except Exception as Argument:
        # LoggeR.critical("Some Exception :   " + Argument.__str__())
        print("Some Exception :" + Argument.__str__())
        LoggeR.logger.error(Argument.__str__());
        # sendEmailToClient.sendMailForException(Argument.__str__())
        pass
