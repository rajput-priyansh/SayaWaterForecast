import warnings
from fbprophet import Prophet  # from fbprophet
#import prophet
# import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#from prophet import Prophet
#from prophet import Prophet

from Logging import LoggeR
from SendEmail import sendEmailToClient

# Piyush
# import pymssql
warnings.filterwarnings("ignore")
plt.style.use('fivethirtyeight')
from Data import connectionDB, getConfigurationSettings


def main(finaldate,filename,id,df):
    # # Time series analysis and forecasting for water consumption.
    print('In Main')
    print('df Result:', df)
	#'C:/inetpub/wwwroot/SAYAML/f' + filename + '.xlsx', index_col='MeterLocalTime',
    #                   parse_dates=True
	
    # df = pd.read_excel('C:/inetpub/wwwroot/SayaMLForecast/SayaWaterForecast/RawDataDump/f'+ filename + '.xlsx', index_col='MeterLocalTime',
    #                    parse_dates=True)
    if df.empty:
        LoggeR.writeExpceptionToTexFile("No Data Found For this User :" + id.__str__())
        #sendEmailToClient.sendMailForException("No Data Found For this User :" + id.__str__(),"No Data Found For the Customer  "+ id.__str__()+"" )
        print('No Data Found')
    else:
        daily = df.resample('D').sum()
        df = daily.rename(columns={'MeterLocalTime': 'ds', 'Flow': 'y'})
        df.reset_index(inplace=True)
        df = df.rename(columns={'MeterLocalTime': 'ds'})
        data = df[['ds', 'y']]
        data = data.drop(0)
        data.head()
        m = Prophet()
        if data.empty:
            LoggeR.writeExpceptionToTexFile("No Data Found For this User :" + id.__str__()+"After Convert DataFrame")
            #sendEmailToClient.sendMailForException("No Data Found For this User :" + id.__str__(),"No Data Found For the Customer  "+ id.__str__()+"After Convert" )
            print('No Data Found After Convert')

        else:
            # try:
                m.fit(data)
                future = m.make_future_dataframe(periods=30)
                future.tail()
                forecast = m.predict(future)
                forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
                forecast.tail(30)
                forecast['yhat'].tail(30)
                total = forecast['yhat'].tail(30).sum(axis=0, skipna=True)
                fixt = forecast.tail(30).to_numpy()
                print(fixt)
                # Current month data
                # connection For Development
                #connectionSetting = getConfigurationSettings.getconfigurations()
                # connectionObj = connectionDB.connectDatabase(connectionSetting['_dbusername'], connectionSetting['_dbpassword'],
                                                    #    connectionSetting['_hostlive'], connectionSetting['_dbport'],connectionSetting['_dbsaya'])
                connObj = connectionDB.connectDatabase("SayaLive", "Mli$3120$8%(0",
                                               "saya-live.cq6nozddb1mr.us-west-2.rds.amazonaws.com", 5432,
                                               "SAYA")
                                                       #'sayaml')
                #connectionObj = connectionDB.connectDatabase('postgres',
                #                                             'test#123',
                #                                                                                  'localhost', '5432',
                #                                                                                   'sayaml')
                # connectionObj =  connectionDB.connectDatabase(user, password, host, port, database)     connectionSetting['_hostlive']
                cur = connectionObj.cursor();
                LoggeR.writeExpceptionToTexFile(":::---Start Inserting Forecast Data "+ "For User:-->" + id.__str__())
                print('     Date          ' + '      ProjectedConsumption     ')	
                LoggeR.writeExpceptionToTexFile('       Date          ' + '        ProjectedConsumption     ')			
                for idx, val in enumerate(fixt):
                    try:
                        print(fixt[idx][0].__str__() + ' ' + fixt[idx][15].__str__())
                        # if (fixt[idx][15] <= 0):
                        #     fixt[idx][15] = 0;
                        #cur.callproc('InsertDataFromFile',
                        #     ('', float(fixt[idx][15]), bool(1), fixt[idx][0].strftime('%y%m%d'), 1, float(total),id))
                        query = "select * from public.InsertDataFromFile ( ''::text," + float(fixt[idx][15]).__str__() +"::float," + bool(1).__str__() + "::boolean," + fixt[idx][0].strftime('%y%m%d').__str__() + "::varchar(50),1," + float(fixt[idx][15]).__str__() +"::integer," + id.__str__() + "::bigint);"
                        print(query)
                        #print(fixt[idx][0].__str__() + '       ' + fixt[idx][15].__str__())   #here fixt[idx][0] is date and  fixt[idx][15] is projectd consumption which we store daywise for perticular user id in our database and we show the whole month sum as forecast
                        LoggeR.writeExpceptionToTexFile(fixt[idx][0].__str__() + '   ----    ' + fixt[idx][15].__str__())
                        #cur.callproc('InsertDataFromFile', (fixtures[idx].__str__(),
                        #float(gallonsData), bool(1), finaldate,0,0,id))
                        #df = pd.read_sql(query, Connection)
                        cur.execute(query)
                        connectionObj.commit();
                        #cur.nextset()
                    except Exception as Argument:
                        LoggeR.writeExpceptionToTexFile(Argument.__str__() + "FOr User:  " + id.__str__())
                        #LoggeR.writeExpceptionToTexFile(Argument.__str__())
                        pass
                        # LoggeR.critical("Some Exception :   " + Argument.__str__())
                        print("Some Exception :" + Argument.__str__())
                        # LoggeR.logger.error(Argument.__str__(), "For the User :", id.__str__());
                        # sendEmailToClient.sendMailForException(Argument.__str__()+ "And ID:" + id.__str__(),"Error While Inserting Data Date wise for")
                        continue;


                            # 'D:/Python/SayaWaterForecast/RawDataDump/f' + filename + '.xlsx'
                cur.close()
                connectionObj.commit()
                print('Data inserted successfully for the date of ' + finaldate.__str__() + "THis ID : " + id.__str__())
                LoggeR.writeExpceptionToTexFile(":::---End Inserting Forecast Data "+ "For User:-->" + id.__str__())				
                #writer.close()
                #os.remove("C:/inetpub/wwwroot/SayaMLForecast/SayaWaterForecast/RawDataDump/f" + finalEdate.__str__() + id.__str__() + ".xlsx")
                # df.close()
            # except Exception as Argument:
            #     LoggeR.critical("Some Exception :   " + Argument.__str__())
            #     pass
            #     sendEmailToClient.sendMailForException(Argument.__str__())
            #     print(Argument)
			#enterinput = input("Enter your value: ")
