Write-Output "Configuration of the frontend started."
Start-Sleep -Seconds 4
$frontendPath = (Get-Item $PSScriptRoot).Parent.FullName

$frontendPath = $frontendPath + "\Frontend\frontend"
Write-Output "Frontend-Pfad: $frontendPath"

Set-Location -Path $frontendPath

Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
npm install
npm update