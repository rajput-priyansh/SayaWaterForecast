from Logging import LoggeR
from Data import config_helper
_config = config_helper.read_config()
def getconfigurations():
    try:
        _hostlive               = _config.get('configurationSettings','hostlive')
        _hostdev                = _config.get('configurationSettings', 'hostdev')
        _hostlocal              = _config.get('configurationSettings', 'hostlocal')
        _dbusername             = _config.get('configurationSettings','dbusername')
        _dbpassword           = _config.get('configurationSettings','dbpassword')
        _dbusernameaws = _config.get('configurationSettings', 'dbusernameaws')
        _dbpasswordaws = _config.get('configurationSettings', 'dbpasswordaws')
        _dbsaya           = _config.get('configurationSettings','dbsaya')
        _dbml = _config.get('configurationSettings', 'dbml')
        _dbport               =  _config.get('configurationSettings','dbport')
        _localpath = _config.get('configurationSettings', 'localpath')
        _deployedpath = _config.get('configurationSettings', 'deployedpath')

        # mail settings
        _smptserver         = _config.get('configurationSettings','smtppserver')
        _smptport           = _config.get('configurationSettings','smtpport')
        _isSSL              = _config.get('configurationSettings','smptpenablessltrue')
        _from               = _config.get('configurationSettings','from')
        _mailPassword       =  _config.get('configurationSettings','mailpassword')
        _useDefaultCreds    = _config.get('configurationSettings','smtpusedefaultcredentials')
        print(_hostlive )
        print(_hostdev )
        print(_hostlocal)
        print(_dbusername)
        print(_dbpassword)
        print(_dbusernameaws)
        print(_dbpasswordaws)
        print(_dbsaya)
        print(_localpath)
        print(_deployedpath)
        print(_dbml)
        print(_dbport)
        print(_smptserver)
        print(_smptport)
        print(_isSSL)
        print(_from )
        print(_mailPassword)
        print(_useDefaultCreds)
        return {'_hostlive': _hostlive,'_hostdev':_hostdev,'_hostlocal':_hostlocal,'_dbusername':_dbusername,
                '_dbpassword':_dbpassword,'_dbusernameaws':_dbusernameaws,
                '_dbpasswordaws':_dbpasswordaws,'_dbsaya':_dbsaya,'_dbport':_dbport,'_dbml':_dbml,
                '_smptserver':_smptserver,'_smptport':_smptport,'_isSSL':_isSSL,
                '_from':_from,'_mailPassword':_mailPassword,'useDefCreds':_useDefaultCreds,'localpath':_localpath,'deployedpath':_deployedpath}
    except Exception as Argument:
        LoggeR.writeExpceptionToTexFile(Argument.__str__())
        print(Argument.__str__())
        pass