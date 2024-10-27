@echo off
REM Install dependencies
pip install -r requirements.txt

REM Create a shortcut in the Startup folder
set SHORTCUT_NAME=WiproSmartExtensionAutomate
set STARTUP_FOLDER=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup

REM Create the shortcut
powershell -Command "$s=(New-Object -COM WScript.Shell).CreateShortcut('%STARTUP_FOLDER%\%SHORTCUT_NAME%.lnk');$s.TargetPath='%CD%\start.bat';$s.WorkingDirectory='%CD%';$s.Save()"

echo Installation complete. Shortcut created in the Startup folder.

REM Execute start.bat
call start.bat

pause