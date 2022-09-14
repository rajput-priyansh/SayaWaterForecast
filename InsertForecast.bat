SET logfile="C:\inetpub\wwwroot\SAYAML\logs_batch\batch.log"
@echo off
@echo Starting Script at %date% %time% >> %logfile%
call C:\ProgramData\Anaconda3\Scripts\activate.bat
@echo off
cd C:\inetpub\wwwroot\SAYAML
python C:\inetpub\wwwroot\SayaMLForecast\SayaWaterForecast\main.py

cmd /k
@echo finished at %date% %time% >> %logfile%


