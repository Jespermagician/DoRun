@echo off
setlocal

REM *** Konfiguration ***
set "github_user=KeineSchere"
set "github_repo=Synch_Directorys"
set "release_tag=V1.1"
set "asset_name=V1.1.zip"
set "download_dir=%cd%"
set "extract_dir=%1"
set "Controlled=true"
set "Python_exist=false"
set "TMP_Del=%cd%\DoRun_TMP"

echo Current directory (Start): %cd%

REM Navigiere zum Basisverzeichnis des Installationsprogramms.
REM Die nachfolgenden cd.. Befehle sind gefährlich und könnten die Batch-Datei
REM unerwartet verschieben. Stattdessen sollten wir von der Position ausgehen,
REM von der aus die Batch-Datei gestartet wird, und relative Pfade verwenden.
REM Da der GUI-Installer die Batch-Datei aus "%SCRIPT_DIR%\Executable\" aufruft,
REM ist %cd% (oder %~dp0, der Laufwerksbuchstabe und Pfad der Batch-Datei)
REM der Startpunkt.

REM Ersetze die unsicheren 'cd..' Befehle
REM Wenn der GUI-Installer die Batch-Datei aus '...\.Installer\Executable\' startet,
REM und die Batch-Datei selbst in '...\.Installer\Executable\DoRun_Installer.bat' liegt.
REM Dann ist %~dp0 (oder %cd% zu Beginn) '...\.Installer\Executable\'

REM Der 'extract_dir' ist der Zielpfad (z.B. C:\Program Files\DoRun)
REM Die heruntergeladenen Dateien landen zuerst in '%download_dir%\%github_repo%-%release_tag%\'
REM Und dort liegt dann der .Installer\Installer_GUI.py

set "INSTALLER_BASE_DIR=%~dp0" REM Pfad, in dem die Batch-Datei liegt (z.B. ...\.Installer\Executable\)

REM Wenn extract_dir nicht vom GUI übergeben wird, ist es standardmäßig der temporäre Ordner.
if "%extract_dir%" == "" (
    set "Controlled=false"
    set "extract_dir=%INSTALLER_BASE_DIR%\DoRun_TMP"
    echo No installation path provided, using temporary directory: %extract_dir%
) else (
    echo Installation path provided: %extract_dir%
)


if "%Controlled%" == "false" (
    REM *** Überprüfen, ob curl verfügbar ist ***
    where curl >nul 2>&1
    if errorlevel 1 (
        echo -----------------------------------------------------------------------------
        echo Error:     curl is not found. Make sure that curl is installed in your path.
        echo Solution: Download curl from https://curl.se/download.html and restart the installer afterwards.
        echo -----------------------------------------------------------------------------
        start https://curl.se/download.html
        pause
        exit /b 1
    )

    REM *** Download der Datei ***
    echo Downloading the release file...
    REM Stellen Sie sicher, dass der download_dir der aktuelle Ordner ist, in dem die Batch-Datei läuft.
    curl -L -o "%INSTALLER_BASE_DIR%%asset_name%" "https://github.com/%github_user%/%github_repo%/archive/refs/tags/%release_tag%.zip"

    if not exist "%INSTALLER_BASE_DIR%%asset_name%" (
        echo -----------------------------------------------------------------------------
        echo Error:     Download failed.
        echo Solution: Check if the internet connection is available and try again.
        echo -----------------------------------------------------------------------------
        pause
        exit /b 1
    )

    REM *** Entpacken der Datei ***
    echo Unzip the file to: "%extract_dir%"

    if not exist "%extract_dir%" mkdir "%extract_dir%"
    powershell -Command "Add-Type -AssemblyName System.IO.Compression.FileSystem; [System.IO.Compression.ZipFile]::ExtractToDirectory('%INSTALLER_BASE_DIR%%asset_name%', '%extract_dir%');"
)

REM Other stuff (Dieser Block wird ausgeführt, wenn Controlled="false" war)
if "%Controlled%" EQU "false" (
    echo Release successfully downloaded and unpacked to: "%extract_dir%".
    
    REM Aufräumen der heruntergeladenen ZIP-Datei
    echo Cleaning up the downloaded ZIP file "%INSTALLER_BASE_DIR%%asset_name%"...
    del "%INSTALLER_BASE_DIR%%asset_name%"

    echo DoRun_TMP successfully created in: "%extract_dir%" loading...

    REM *** Überprüfe, ob Python existiert (Systemweit oder in PATH) ***
    echo Checking for Python interpreter...
    REM *** Überprüfe, ob Python existiert ***
    for /R "%SystemDrive%" %%f in (*python.exe) do (
        set "Python_exist=true"
        set "Python_path=%%f"
        goto :eof_py
    ) 
    :eof_py
    echo Python Interpreter found under: "%Python_path%"
    where python >nul 2>&1
    if errorlevel 0 (
        set "Python_exist=true"
        for /f "delims=" %%i in ('where python') do set "Python_path=%%i"
        echo Python Interpreter found: "%Python_path%"
    ) else (
        set "Python_exist=false"
        echo Python not found in system PATH.
    )

    if "%Python_exist%" == "false" (
        REM *** Öffne die Python-Download-Website ***
        echo Python was not found. Opening the download page...
        start https://www.python.org/downloads/
            
        echo -----------------------------------------------------------------------------
        echo Error:     Python is not found. Please install Python to continue.
        echo Solution: Download Python from the opened page and restart the installer afterwards.
        echo -----------------------------------------------------------------------------
        pause
        exit /b 1
    )
    
    if "%Python_exist%" == "true" (
        echo Configuring Python Virtual Environment...
        set "VENV_PATH=%extract_dir%\%github_repo%-%release_tag%\%project_venv_name%" REM Pfad zum venv
        
        REM Erstelle das Virtual Environment
        echo Creating Virtual Environment at: "%VENV_PATH%"
        "%Python_path%" -m venv "%VENV_PATH%"

        if not exist "%VENV_PATH%\Scripts\activate.bat" (
            echo Error: Failed to create Virtual Environment.
            exit /b 1
        )
        
        REM Aktiviere das Virtual Environment (ohne explizit zu aktivieren, da wir die Pfade direkt verwenden)
        set "VENV_PYTHON=%VENV_PATH%\Scripts\python.exe"
        
        echo Installing pip in venv...
        "%VENV_PYTHON%" -m pip install --upgrade pip

        echo Installing modules in venv...
        "%VENV_PYTHON%" -m pip install tk
        "%VENV_PYTHON%" -m pip install pillow
        
        REM Optional: Installieren Sie hier weitere Module, die Ihr Projekt benötigt
        REM "%VENV_PYTHON%" -m pip install requests
        REM "%VENV_PYTHON%" -m pip install numpy

        echo Starting python GUI with venv interpreter: "%VENV_PYTHON%"
        "%VENV_PYTHON%" "%extract_dir%\%github_repo%-%release_tag%\.Installer\Installer_GUI.py"
    )

) else ( REM Dieser Block wird ausgeführt, wenn Controlled="true" war (vom GUI aufgerufen)
    if "%Controlled%" EQU "true" (
        echo "Installer is running in controlled mode."
        REM Wenn das Zielverzeichnis (extract_dir) noch nicht existiert, erstellen Sie es.
        if not exist "%extract_dir%" (
            echo Creating installation directory: "%extract_dir%"
            mkdir "%extract_dir%"
        )

        REM Files nach %1 verschieben (von TMP_Del nach extract_dir)
        REM Hier müssen wir wissen, wo DoRun_TMP tatsächlich erstellt wurde.
        REM Wenn Controlled="false" den Download macht, wird TMP_Del auf "%INSTALLER_BASE_DIR%\DoRun_TMP" gesetzt.
        REM Daher ist TMP_Del der Pfad, aus dem wir verschieben wollen.
        set "TMP_SOURCE_DIR=%INSTALLER_BASE_DIR%\DoRun_TMP\%github_repo%-%release_tag%"

        if exist "%TMP_SOURCE_DIR%" (
            echo "Moving files from temporary directory '%TMP_SOURCE_DIR%' to installation directory: '%extract_dir%'"
            robocopy "%TMP_SOURCE_DIR%" "%extract_dir%" /E /MOVE /MIR /XD "%TMP_SOURCE_DIR%\%project_venv_name%" REM Exkludiere das Venv aus dem Verschieben, wenn es bereits erstellt wurde
            if %errorlevel% geq 8 (
                echo Error during robocopy.
                exit /b 1
            )
        ) else (
            echo Warning: Temporary source directory '%TMP_SOURCE_DIR%' not found for moving.
        )
        
        REM Venv sollte nur einmal erstellt werden, entweder im temporären Ordner (wenn Controlled=false)
        REM oder später direkt im Zielordner (wenn das Venv nicht verschoben wird)

        REM Erstelle Venv und installiere Module direkt im Zielordner, WENN Controlled=true
        REM UND WENN das Venv noch nicht da ist.
        set "TARGET_VENV_PATH=%extract_dir%\%project_venv_name%"
        if not exist "%TARGET_VENV_PATH%" (
            echo Checking for Python interpreter...
            where python >nul 2>&1
            if errorlevel 0 (
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
                "%VENV_PYTHON%" -m pip install --upgrade pip

                echo Installing modules in venv...
                "%VENV_PYTHON%" -m pip install tk
                "%VENV_PYTHON%" -m pip install pillow
                REM Fügen Sie hier weitere Module hinzu
                
                echo Virtual Environment and modules successfully set up in installation directory.
            ) else (
                echo Error: Python not found for venv creation in controlled mode.
                exit /b 1
            )
        ) else (
            echo Virtual Environment already exists at: "%TARGET_VENV_PATH%"
        )

        REM Löschen Sie den temporären Ordner nur, wenn er existiert
        if exist "%TMP_Del%" (
            echo Deleting temporary directory: "%TMP_Del%"
            rmdir "%TMP_Del%" /S /Q
        )
        echo "DoRun_TMP" successfully moved and cleaned up.
    )
)

EXIT /B 0

endlocal