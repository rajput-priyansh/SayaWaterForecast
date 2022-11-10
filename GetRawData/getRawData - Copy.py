import os
import warnings
import itertools
# import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
#import prophet
from fbprophet import Prophet # from fbprophet
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
        today = datetime.datetime(2022, 7, 1)  # datetime.today()
        months = calendar.monthrange(today.year, today.month)[1]
        #sDate = today + relativedelta(months=-5)
        sDate = datetime.datetime(2022, 2, 1)
        # months=calendar.monthrange(sDate.year, sDate.month)[1]
        # sDate=datetime.today() + timedelta(days=-months)
        #eDate = datetime.datetime(sDate.year, sDate.month, sDate.day) + relativedelta(
        #    months=6)  # datetime.today() + timedelta(days=-5)  # days=-1 replace -5 with -1 once this file runs ---chirag 05072022
        # startDate = datetime.strptime(sDate, '%d/%m/%Y')
        # endDate = datetime.strptime(eDate, '%d/%m/%Y')
        eDate =datetime.datetime(2022, 8,31)
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
        # connObj = psycopg2.connect(user="postgres",
        #                           password="test#123",
        #                           host="52.40.141.127",
        #                           port="5432",
        #                           database="SAYA")
        connObj = connectionDB.connectDatabase(connectionSetting['_dbusername'], connectionSetting['_dbpassword'],
                                               connectionSetting['_hostlive'], connectionSetting['_dbport'],
                                               connectionSetting['_dbsaya'])
        
        cur = connObj.cursor()
        customerIdQueryFor6MonthData = "SELECT x.\"Id\"  FROM public.\"Customer\" x WHERE cast(\"CreatedDate\"  as date) <=cast('2022-02-01' as date) and \"IsParent\" =false and \"IsActive\" = true and \"IsDeleted\" = false";
        # conn = ''
        #customerIdQuery = 'select "Id" from "Customer" where "AccountType"  in (5,6) and "IsDeleted"  = false and "IsActive"  = true ;';
		
		#218,10856
        finalIds = [218,10856,219,220,221,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,288,289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,10229,10230,10231,10232,10233,10234,10236,10237,10238,10239,10240,10241,10242,10243,10244,10245,10246,10247,10248,10249,10250,10251,10252,10253,10254,10255,10256,10257,10258,10259,10260,10261,10262,10263,10264,10265,10266,10267,10268,10269,10270,10271,10272,10273,10274,10275,10276,10277,10278,10279,10280,10281,10282,10283,10284,10285,10286,10287,10288,10289,10290,10291,10292,10293,10294,10295,10296,10297,10298,10299,10300,10301,10302,10303,10304,10305,10306,10307,10308,10309,10310,10311,10312,10313,10314,10315,10316,10317,10318,10319,10,20,10321,10322,10323,10324,10325,10326,10327,10328,10329,10330,10331,10332,10333,10334,10335,10336,10337,10338,10339,10340,10341,10345,10346,10347,10348,10349,10350,10351,10352,10353,10354,10356,10357,10358,10359,10360,10361,10362,10363,10364,10365,10366,10367,10368,10369,10370,10371,10372,10373,10374,10375,10376,10377,10378,10379,10380,10381,10382,10383,10384,10385,10386,10387,10388,10389,10390,10391,10392,10393,10394,10395,10396,10397,10398,10399,10400,10401,10402,10403,10404,10405,10406,10407,10408,10409,10410,10411,10412,10413,10414,10415,10416,10417,10418,10419,10420,10421,10422,10423,10424,10425,10426,10427,10428,10429,10430,10431,10432,10433,10434,10435,10436,10437,10438,10439,10440,10441,10442,10444,10445,10446,10447,10448,10449,10450,10451,10452,10453,10454,10455,10456,10457,10458,10459,10460,10461,10462,10463,10464,10465,10466,10467,10468,10470,10471,10472,10473,10474,10475,10476,10477,10478,10479,10480,10481,10482,10483,10484,10485,10486,10487,10488,10489,10490,10491,10492,10494,10495,10496,10497,10498,10499,10500,10502,10503,10504,10520,10521,10522,10523,10524,10525,10526,10527,10528,10529,10530,10531,10540,10541,10542,10543,10544,10545,10546,10547,10548,10549,10550,10551,10552,10553,10554,10555,10556,10557,10558,10559,10560,10561,10562,10563,10564,10565,10566,10567,10568,10569,10570,10571,10575,10576,10577,10578,10579,10580,10581,10582,10583,10584,10585,10586,10587,10588,10589,10591,10592,10593,10594,10595,10596,10605,10606,10607,10608,10610,10611,10612,10613,10627,10628,10629,10630,10631,10632,10633,10634,10635,10636,10637,10638,10639,10640,10641,10642,10643,10644,10645,10646,10647,10652,10653,10654,10655,10656,10657,10659,10660,10662,10724,10725,10726,10729,10730,10731,10732,10733,10736,10739,10745,10746,10747,10748,10750,10754,10777,10778,10779,10780,10781,10782,10783,10784,10826,10827,10828,10830,10831,10832,10833,10834,10835,10836,10837,10838,10839,10841,10842,10843,10844,10845,10846,10847,10848,10849,10850,10851,10852,10853,10854,10855,10859,10861,10862,10864,10865,10866,10868,10869,10870,10871,10873,10874,10875,10876,10878,10879,10882,10885,10889,10890,10891,10892,10893,10894,10898,10899,10900,10902,10903,10904,10906,10907,10908,10910,10912,10917,10918,10919,10920,10923,10927,10928,10929,10932,10933,10935,10936,10938,10939,10944,10946,10947,11004,11016,11017,11018,11019,11020,11030,11061,11065,11066]
        with connObj.cursor() as cur:
            cur.execute(customerIdQueryFor6MonthData)
            #finalIds = cur.fetchall()
            print("Fetched records: %s" % finalIds)
        for id in finalIds:
            try:
                #id=str(id)           #uncomment when working with live fetch ids
                #id=int(id[1:-2])
                #print(id)
                #id = 10856
                query = "select * from GetWaterMeterDataForDataFile ( " + finaldate.__str__() + "::varchar(100)" + "," + finalEdate.__str__() + "::varchar(100)" + "," + id.__str__() + "::bigint" + ")"
                print(query)
                # writer = pd.ExcelWriter(
                #     'C:/inetpub/wwwroot/SayaMLForecast/SayaWaterForecast/RawDataDump/f' + finalEdate.__str__() + id.__str__() + '.xlsx',
                #     engine='xlsxwriter')
                df = pd.read_sql(query, connObj, index_col='MeterLocalTime', parse_dates=True)
                #df.to_excel(writer, sheet_name='Sheet1')
                ## filedialog.asksaveasfilename(filetypes=[('excel file', '*.xlsx')], defaultextension='.xlsx')
                #writer.save()
                # writer.close()
                print('Out from get data')
                prophetDataModel.main(finalEdate, finalEdate + id.__str__(), id, df)
            except Exception as Argument:
                # sendEmailToClient.sendMailForException(Argument.__str__(),"SayaML InsertException for Customer : " + id.__str__())

                # LoggeR.critical("Some Exception :   " + Argument.__str__())
                print("Some Exception :" + Argument.__str__())
                #LoggeR.logger.error(Argument.__str__() ,"For the User :" ,id.__str__());
                LoggeR.writeExpceptionToTexFile(Argument.__str__()+"For CustomerId::>"+id.__str__())
                # sendEmailToClient.sendMailForException(Argument.__str__())
                # logger.error("a")
                pass
                continue
            finally:
                LoggeR.writeExpceptionToTexFile("Done ForecastData Insert for the Month:-->"+ datetime.datetime.now().month.__str__())				   
                 # os.close("D:/Python/SayaWaterForecast/RawDataDump/f" + finalEdate.__str__() + id.__str__() + ".xlsx")
                 # os.system('TASKKILL /F /IM excel.exe')
                 #writer.close()
                 #os.remove("C:/inetpub/wwwroot/SayaMLForecast/SayaWaterForecast/RawDataDump/f" + finalEdate.__str__() + id.__str__() + ".xlsx")



    except Exception as Argument:
        # LoggeR.critical("Some Exception :   " + Argument.__str__())
        print("Some Exception :" + Argument.__str__())
        LoggeR.writeExpceptionToTexFile(Argument.__str__())
        #LoggeR.logger.error(Argument.__str__());
        # sendEmailToClient.sendMailForException(Argument.__str__())
        pass
