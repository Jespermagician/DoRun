# Backend Contribution Guide

Language:   Python 
Framework:  Django
SQL-Server: PostgreSQL

<hr>

# Logging
- A Logging class is defined in `BackendApp\BackendApp\logs.py`
- An instance of the class is called in `BackendApp\BackendApp\settings.py`
- Please use the Instance via `from BackendApp import settings as set`
- Now you can print formatted Console Logs. Example: `set.logger.print("Server Started")`