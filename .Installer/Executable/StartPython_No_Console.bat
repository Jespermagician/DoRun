start /wait PowerShell.exe -WindowStyle Hidden-Command "{& Start-Process '%~1' -ArgumentList '%~2' '%~3' -WindowStyle Hidden}"
REM EXIT 1