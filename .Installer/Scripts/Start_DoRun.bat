echo off
set "PathThreeLevelsUp=%~dp0..\..\" 
for %%A in ("%PathThreeLevelsUp%") do set "ParentPath=%%~fA"

set "Python=%ParentPath%.Installer\Executable\DoRun_GUI.py"
REM ONLY use pythonw.exe NEVER python.exe else you will get a cmd-prompt
set "ParentPath=%ParentPath%venv_installer\Scripts\pythonw.exe"
start /b "%ParentPath%.Installer\Executable\StartPython_No_Console.bat" "%ParentPath%" "%Python%"  