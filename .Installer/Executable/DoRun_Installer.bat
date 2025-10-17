@echo off
setlocal

REM *** Konfiguration ***
set "github_user=Jespermagician"
set "github_repo=DoRun"
set "release_tag=v0.9.1-beta"
REM Just drop the v from the release_tag. Part of Git name convention
set "folder_name=0.9.1-beta"
set "asset_name=v0.9.1-beta.zip"
set "download_dir=%cd%"
set "extract_dir=%~1"
set "Controlled=true"
set "Python_exist=false"
set "TMP_Del=%cd%DoRun_TMP"

echo "Current directory (Start): %cd%"
echo "Main drive : %~dp0"

set "INSTALLER_BASE_DIR=%~dp0"

echo %extract_dir%

if "%extract_dir%" == "" (
    set "Controlled=false"
    set "extract_dir=%INSTALLER_BASE_DIR%\DoRun_TMP"
    echo No installation path provided, using temporary directory: %extract_dir%
) else (
    echo Installation path provided: %extract_dir%
)

if "%Controlled%" == "false" (
    where curl >nul 2>&1
    if errorlevel 1 (
        echo -----------------------------------------------------------------------------
        echo Error:    curl is not found. Make sure that curl is installed in your path.
        echo Solution: Download curl from https://curl.se/download.html and restart the installer afterwards.
        echo -----------------------------------------------------------------------------
        start https://curl.se/download.html
        pause
        exit /b 1
    )

    echo Downloading the release file...
    curl -L -o "%INSTALLER_BASE_DIR%%asset_name%" "https://github.com/%github_user%/%github_repo%/archive/refs/tags/%release_tag%.zip"

    if not exist "%INSTALLER_BASE_DIR%%asset_name%" (
        echo -----------------------------------------------------------------------------
        echo Error:    Download failed.     
        echo Solution: Check if the internet connection is available and try again.
        echo -----------------------------------------------------------------------------
        pause
        exit /b 1
    )

    echo Unzip the file to: "%extract_dir%"
    if not exist "%extract_dir%" mkdir "%extract_dir%"
    powershell -Command "Add-Type -AssemblyName System.IO.Compression.FileSystem; [System.IO.Compression.ZipFile]::ExtractToDirectory('%INSTALLER_BASE_DIR%%asset_name%', '%extract_dir%');"
)

if "%Controlled%" EQU "false" (
    echo Release successfully downloaded and unpacked to: "%extract_dir%".
    
    echo Cleaning up the downloaded ZIP file "%INSTALLER_BASE_DIR%%asset_name%"...
    del "%INSTALLER_BASE_DIR%%asset_name%"

    echo DoRun_TMP successfully created in: "%extract_dir%" loading...

    REM *** Überprüfe, ob Python existiert (mit temporärer Datei) ***
    echo Checking for Python interpreter...
    setlocal enabledelayedexpansion
    
    REM Lokale Variablen innerhalb des setlocal-Blocks
    set "Python_exist=false"
    set "Python_path="

    REM 1. Suche im PATH
    where python >nul 2>&1
    if not errorlevel 1 (
        for /f "delims=" %%i in ('where python') do set "Python_path=%%i"
        set "Python_exist=true"
    )

    REM 2. Falls nicht im PATH, suche auf Systempartition
    if /i "!Python_exist!"=="false" (
        for /R "%SystemDrive%\" %%f in (python.exe) do (
            set "Python_path=%%f"
            set "Python_exist=true"
            goto :found_python
        )
    )

    :found_python
    if /i "!Python_exist!"=="true" (
        echo Python Interpreter found: "!Python_path!"
        echo Configuring Python Virtual Environment...
        set "VENV_PATH=!extract_dir!\\!github_repo!-!folder_name!\\!project_venv_name!"

        echo Creating Virtual Environment at: "!VENV_PATH!"
        "!Python_path!" -m venv "!VENV_PATH!\\"

        if not exist "!VENV_PATH!\Scripts\activate.bat" (
            echo Error: Failed to create Virtual Environment.
            endlocal
            pause
            exit /b 1
        )
        
        pause

        set "VENV_PYTHON=!VENV_PATH!\Scripts\python.exe"

        echo Installing pip in venv...
        "!VENV_PYTHON!" -m pip install --upgrade pip

        echo Installing modules in venv...
        "!VENV_PYTHON!" -m pip install tk
        "!VENV_PYTHON!" -m pip install pillow
        "!VENV_PYTHON!" -m pip install psutil

        echo Starting python GUI with venv interpreter: "!VENV_PYTHON!"
        "!VENV_PYTHON!" "%extract_dir%\%github_repo%-%folder_name%\.Installer\Executable\Installer_GUI.py"
        pause
    ) else (
        echo Python was not found. Opening the download page...
        start https://www.python.org/downloads/
        echo -----------------------------------------------------------------------------
        echo Error:    Python is not found. Please install Python to continue.
        echo Solution: Download Python from the opened page and restart the installer afterwards.
        echo -----------------------------------------------------------------------------
        pause
        endlocal
        exit /b 1
    )
    
    REM Beende den lokalen Block
    endlocal
) else if "%Controlled%" EQU "true" (
    echo "Installer is running in controlled mode."
    if not exist "%extract_dir%" (
        echo Creating installation directory: "%extract_dir%"
        mkdir "%extract_dir%"
    )

    set "TMP_SOURCE_DIR=%INSTALLER_BASE_DIR%\DoRun_TMP\%github_repo%-%release_tag%"
    if exist "%TMP_SOURCE_DIR%" (
        echo "Moving files from temporary directory '%TMP_SOURCE_DIR%' to installation directory: '%extract_dir%'"
        robocopy "%TMP_SOURCE_DIR%" "%extract_dir%" /E /MOVE /MIR /XD "%TMP_SOURCE_DIR%\%project_venv_name%"
        if %errorlevel% geq 8 (
            echo Error during robocopy.
            exit /b 1
        )
    ) else (
        echo Warning: Temporary source directory '%TMP_SOURCE_DIR%' not found for moving.
    )
    
    set "TARGET_VENV_PATH=%extract_dir%\%project_venv_name%"
    if not exist "%TARGET_VENV_PATH%" (
        echo Checking for Python interpreter...
        where python >nul 2>&1
        if not errorlevel 1 (
            for /f "delims=" %%i in ('where python') do set "Python_path=%%i"
            echo Python Interpreter found: "%Python_path%"

            echo Creating Virtual Environment at: "%TARGET_VENV_PATH%"
            "%Python_path%" -m venv "%TARGET_VENV_PATH%"

            if not exist "%TARGET_VENV_PATH%\Scripts\activate.bat" (
                echo Error: Failed to create Virtual Environment in target directory.
                exit /b 1
            )
            
            set "VENV_PYTHON=%TARGET_VENV_PATH%\Scripts\python.exe"
            
            echo Installing pip in venv...
            "!VENV_PYTHON!" -m pip install --upgrade pip

            echo Installing modules in venv...
            "!VENV_PYTHON!" -m pip install tk
            "!VENV_PYTHON!" -m pip install pillow

            echo Virtual Environment and modules successfully set up in installation directory.
        ) else (
            echo Error: Python not found for venv creation in controlled mode.
            exit /b 1
        )
    ) else (
        echo Virtual Environment already exists at: "%TARGET_VENV_PATH%"
    )

    if exist "%TMP_Del%" (
        echo Deleting temporary directory: "%TMP_Del%"
        rmdir "%TMP_Del%" /S /Q
    )
    echo "DoRun_TMP" successfully moved and cleaned up.
)

EXIT /B 0
