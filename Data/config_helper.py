import configparser
# method to read config settings
def read_config():
    try:
        config= configparser.ConfigParser()
        config.read('Configurations\configurations.ini')
        return config
    except Exception as Argument:
        print("Some Exception :" + Argument.__str__())
