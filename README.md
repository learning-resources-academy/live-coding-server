# live-coding-server

## set up the environment
python -m venv venv
venv\Scripts\activate

## build command
pip install -r requirements.txt

## start command
uvicorn main:app --host 0.0.0.0 --port $PORT

## URL Deploy
https://live-coding-server.onrender.com