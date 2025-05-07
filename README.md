# url-repo-local
_This is a Local Version of the URL Repository Web App._

[ Original URL Repo ](https://github.com/sadieedwin/url-repo/tree/main)

## Setup: 

1. Install Python (if not yet installed)
```text
Download from python.org and install it.
Make sure python and pip commands work in your terminal/cmd.
```
2. Clone this repo
```
git clone https://github.com/sadieedwin/url-repo-local.git
```
3. Go to the url-repo-local folder
```
cd url-repo-local
```
4. Setup a virtual environment
```
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```
5. Install Flask and SQLAlchemy
```
pip install flask flask_sqlalchemy
```
7. Run the Flask app
```
flask run
or
flask run --host=0.0.0.0 --port=5001
```
8. Access your app Open your browser and visit: `http://127.0.0.1:5001`
