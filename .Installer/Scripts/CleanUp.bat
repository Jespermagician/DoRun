@echo off
REM --- Deletes the folder "DoRun_TMP" in a passed path ---

REM Check if a path was passed as a parameter (%1)
if "%~1" == "" (
    echo ERROR: No path argument was provided.
    echo.
    echo Usage: %~nx0 "C:\Path\to\Target"
    pause
    exit /b 1
)

set "INPUT_PATH=%~1"
set "FOLDER_TO_DELETE=%INPUT_PATH%"

REM --- LOGIC MODIFICATION START (Handles both full path or parent path) ---

REM 1. Normalize the path: remove a trailing backslash if one exists.
if "%FOLDER_TO_DELETE:~-1%"=="\" set "FOLDER_TO_DELETE=%FOLDER_TO_DELETE:~0,-1%"

REM 2. Check if the path does NOT end with "\DoRun_TMP" (length of "\DoRun_TMP" is 10).
REM If the last 10 characters are NOT "\DoRun_TMP" (case-insensitive), we append it.
if /i not "%FOLDER_TO_DELETE:~-10%"=="\DoRun_TMP" (
    REM Append "\DoRun_TMP" to the original input path
    set "FOLDER_TO_DELETE=%INPUT_PATH%\DoRun_TMP"
) else (
    REM Path already ends with "\DoRun_TMP", use the original input path as is.
    set "FOLDER_TO_DELETE=%INPUT_PATH%"
)
REM --- LOGIC MODIFICATION END ---


echo -------------------------------------------------------------------
echo Target path: %FOLDER_TO_DELETE%
echo -------------------------------------------------------------------

REM 1. INCORPORATE WAIT TIME (15 seconds)
echo Waiting 15 seconds to ensure all processes are terminated...
timeout /t 15 /nobreak>nul

REM 2. CHECK IF THE TARGET FOLDER EXISTS
if exist "%FOLDER_TO_DELETE%" (
    echo Folder found. Starting deletion process...
    
    REM Deleting the folder (recursively and without prompt)
    rmdir /s /q "%FOLDER_TO_DELETE%"
    
    REM 3. CHECK IF DELETION WAS SUCCESSFUL
    if not exist "%FOLDER_TO_DELETE%" (
        echo SUCCESS: "%FOLDER_TO_DELETE%" was deleted.
    ) else (
        echo ERROR: "%FOLDER_TO_DELETE%" could NOT be deleted (maybe still in use).
    )
) else (
    echo NOTE: "%FOLDER_TO_DELETE%" does not exist or was already deleted.
)

echo.
exit /b 0
