# AAU-BioPass Starter
Local academic prototype. Python 3.12 + Django 5.2 + SQLite.

## Windows PowerShell setup
1. Install Python 3.12 (enable Add Python to PATH) and VS Code.
2. Extract this folder and open it in VS Code.
3. Run:
```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
4. Open http://127.0.0.1:8000/ and http://127.0.0.1:8000/admin/.

If activation is blocked, run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` in that PowerShell session, then activate again.

## Important
Fingerprint/RFID are not connected. Any later simulation must be labelled simulation; real matching requires compatible hardware and SDK testing. Never store raw fingerprint images. This is not a production security system.
