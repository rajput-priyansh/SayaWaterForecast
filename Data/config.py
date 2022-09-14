import configparser

# CREATE OBJECT
config_file = configparser.ConfigParser()

# ADD SECTION
config_file.add_section("configurationSettings")
# ADD SETTINGS TO SECTION
config_file.set("configurationSettings", "smtpserver", "smtp.gmail.com")
config_file.set("configurationSettings", "smtpport", "587")
config_file.set("configurationSettings", "smtppassword", "test#123")
config_file.set("configurationSettings","smtpusername","chixkhan728@gmail.com")
config_file.set("configurationSettings", "dbusername", "postgres")
config_file.set("configurationSettings", "dbpassword", "test#123")
config_file.set("configurationSettings", "dbport", "5432")
config_file.set("configurationSettings","dbhostlive","52.40.141.127")
config_file.set("configurationSettings","dbsaya","SAYA")
config_file.set("configurationSettings","dbml","sayaml")
config_file.set("configurationSettings","dbhostlocal","localhost")
# SAVE CONFIG FILE
with open(r"D:/Python/SayaWaterForecast/Configurations/configurations.ini", 'w') as configfileObj:
    config_file.write(configfileObj)
    configfileObj.flush()
    configfileObj.close()

print("Config file 'configurations.ini' created")

# PRINT FILE CONTENT
read_file = open("configurations.ini", "r")
content = read_file.read()
print("Content of the config file are:\n")
print(content)
read_file.flush()
read_file.close()