@echo off
REM Activate virtual environment
call venv\Scripts\activate

REM Run Flask app in a new command window
start cmd /k "flask run --host=0.0.0.0 --port=5001"
