import configparser
# method to read config settings
def read_config():
    try:
        config= configparser.ConfigParser()
        config.read('C:\inetpub\wwwroot\SayaMLForecast\SayaWaterForecast09162022\SayaWaterForecast\Configurations\configurations.ini')
        return config
    except Exception as Argument:
        print("Some Exception :" + Argument.__str__())
