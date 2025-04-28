# Navigate to project directory
cd "C:\Users\Edwin.Sadie\Desktop\URL Repo"

# Activate virtual environment
& "venv\Scripts\Activate.ps1"

# Run Flask app in background (hidden window)
Start-Process -WindowStyle Hidden powershell -ArgumentList "flask run --host=0.0.0.0 --port=5001"
