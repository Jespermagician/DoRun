#Start Django
cd..
Set-Location Backend/BackendApp

python manage.py runserver

# Start Database
$PSQL = Get-Service "postgresql*"
Start-Service -Name $PSQL