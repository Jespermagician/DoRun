 REM *** Überprüfe, ob Python existiert ***
    for /R "%SystemDrive%" %%f in (*python.exe) do (
        set "Python_exist=true"
        set "Python_path=%%f"
        goto :eof_py
    ) 
    :eof_py
    echo Python Interpreter found under: "%Python_path%"

    REM *** Überprüfen, ob Postgresql existiert ***
    if "%Python_exist%" == "false" (
        REM *** Öffne die Postgresql-Website ***
        echo Python was not found. Opening the download page...
        start https://www.python.org/downloads/
            
        echo -----------------------------------------------------------------------------
        echo Error:    Python is not found. Make sure that Python is installed on your drive: "%SystemDrive%"
        echo Solution: Please download Python to continue. You can restart the installer afterwards.
        echo -----------------------------------------------------------------------------
        pause
    )
    if "%Python_exist%" == "true" (
        "%Python_path%" -m pip install --upgrade pip

        echo Starting python with interpreter: "%Python_path%"
        "%Python_path%" "%cd%\.Installer\DoRun_GUI.py"        
    )
    else (
        pause
    )