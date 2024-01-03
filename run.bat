@echo off

REM Set the name of the virtual environment
set VENV_NAME=.venv

REM Check if the virtual environment exists
if not exist %VENV_NAME%\Scripts\activate (
    echo Creating virtual environment...
    python -m venv %VENV_NAME%
)

REM Activate the virtual environment
call %VENV_NAME%\Scripts\activate

REM Install dependencies
pip install -r requirements.txt

REM Set Flask environment variables
set FLASK_APP=app\__init__.py
set FLASK_ENV=development

REM Run Flask application
echo Running flask...
python -m flask run

REM Prompt the user to press any key before closing
echo Press any key to close...
pause >nul

REM Deactivate the virtual environment when done
deactivate
