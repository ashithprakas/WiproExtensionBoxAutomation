@echo off
REM Define the path to the directory containing the PID file
set "TEMP_DIR=%TEMP%\clipboard_image_saver.temp"
set "PID_FILE=%TEMP_DIR%\clipboard_image_saver.pid"

REM Check if PID file exists
if not exist "%PID_FILE%" (
    echo PID file not found.
    exit /b 1
)

REM Read PID from file
set /p PID=<"%PID_FILE%"

REM Validate that PID is not empty
if "%PID%"=="" (
    echo PID is empty in the PID file.
    exit /b 1
)

REM Terminate the process
taskkill /PID %PID% /F

REM Check if termination was successful
if %ERRORLEVEL% neq 0 (
    echo Failed to terminate process with PID %PID%.
    exit /b 1
)

REM Remove PID file
del "%PID_FILE%"

echo Process terminated.