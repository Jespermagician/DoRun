#Set-Locatzion = cd
Write-Output "Configuration of the backend started."
Set-Location -Path ..

py -m pip install pip
py -m pip install --upgrade pip

#py -m pip install virtualenv
#py -m pip install virtualenv --upgrade

#$Path_To_Interpreter = Get-Content -Path .\installer\buffer.txt
$backendPath = (Get-Item $PSScriptRoot).Parent.FullName
$backendPath = $backendPath + "\Backend\BackendApp"
Set-Location -Path backendPath

#py -m virtualenv --python $Path_To_Interpreter venv

#.venv\Scripts\activate

#Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

py -m pip install -r requirements.txt
