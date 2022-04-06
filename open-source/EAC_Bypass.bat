@echo off
cls

echo.
ECHO ******************************************
ECHO *Select Your Python Command Added To PATH*
ECHO ******************************************
ECHO.
ECHO 1 - Python
ECHO 2 - Python2
ECHO 3 - Python3
ECHO 4 - EXIT
ECHO.
SET /P M=input:
IF %M%==1 GOTO NOTE
IF %M%==2 GOTO CALC
IF %M%==3 GOTO BOTH
IF %M%==4 GOTO EOF
:NOTE
python NuremX.py
:CALC
python2 NuremX.py
:BOTH
python3 NuremX.py
:EOF
exit