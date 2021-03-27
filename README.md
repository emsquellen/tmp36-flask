# TMP36 Flask dashboard
> *Flask implementation of a simple dashboard + server for viewing ESP32-tmp36 data*

## How to use?

### Setup:

```bat
mkdir flask-tmp36

git clone https://github.com/emsquellen/tmp36-flask.git

cd tmp36-flask

python -m venv venv

.\venv\Scripts\activate

pip install -r requirements.txt

```

Don't forget to change the IP in `config.ini` to your IP address!

### Run:

`py run.py`


#### Gunicorn
For usage with gunicorn/linux, firstly move all the files from `.linux` to the parent directory, then you can do `sh run_linux.sh`.