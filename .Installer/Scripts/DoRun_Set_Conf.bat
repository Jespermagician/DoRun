@echo off

:main
	goto :check_deependencys
	pause
	goto :Conf_Frontend
	pause
	goto :Conf_Backend
	pause
EXIT

:check_deependencys
	set "NodeJs_exist=false"
	set "Postgresql_exist=false"
	
	REM *** Überprüfen, ob node existiert ***
	for /R "%SystemDrive%:\Program Files\" %%f in (*node.exe) do (
		set "NodeJs_exist=true"
		echo "%%f"
		goto:eof_node
	)
	:eof_node

	if "%NodeJs_exist%" == "false" (
		REM *** Öffne die Node.js-Website ***
		echo Node.js ist nicht gefunden. Öffne die Download-Seite...
		start https://nodejs.org/en

		echo Bitte laden Sie Node.js herunter.
	)

	for /R "%SystemDrive%:\Program Files\" %%f in (*psql.exe) do (
		set "Postgresql_exist=true"
		echo "%%f"
		goto :eof_psql
	)
	:eof_psql

	REM *** Überprüfen, ob Postgresql existiert ***
	if "%Postgresql_exist%" == "false" (
		REM *** Öffne die Postgresql-Website ***
		echo Postgresql ist nicht gefunden. Öffne die Download-Seite...
		start https://www.postgresql.org/download/windows/

		echo Bitte laden Sie Postgresql herunter.
	)

	echo "Deependencycheck done!"

REM Setup for the frontend
:Conf_Frontend
	REM Füge das PowerShell-Verzeichnis zum PATH hinzu (falls es nicht bereits vorhanden ist)
	set "PowerShellDir=%SystemRoot%\system32\WindowsPowerShell\v1.0\"
	echo "%PATH%" | find /I "%PowerShellDir%" > nul
	if errorlevel 1 (
    	set "Path=%PowerShellDir%;%Path%"
    	echo "PowerShell-Verzeichnis zum PATH hinzugefügt."
	)
	echo "%~dp0"
	Powershell.exe -NoProfile -executionpolicy remotesigned -File "%~dp0Frontend_Conf.ps1"

	pause

REM Setup  for the backend
:Conf_Backend
	REM Füge das PowerShell-Verzeichnis zum PATH hinzu (falls es nicht bereits vorhanden ist)
	set "PowerShellDir=%SystemRoot%\system32\WindowsPowerShell\v1.0\"
	echo "%PATH%" | find /I "%PowerShellDir%" > nul
	if errorlevel 1 (
    	set "Path=%PowerShellDir%;%Path%"
    	echo "PowerShell-Verzeichnis zum PATH hinzugefügt."
	)
	Powershell.exe -NoProfile -executionpolicy remotesigned -File "%~dp0Backend_Conf.ps1"

	pause