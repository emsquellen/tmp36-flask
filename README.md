# TMP36 Flask dashboard
> *Flask implementation of a simple dashboard + server for viewing ESP32-tmp36 data*

## How to use?

> Setup:

```bat
mkdir flask-tmp36

git clone https://github.com/emsquellen/tmp36-flask.git

cd tmp36-flask

python -m venv venv

.\venv\Scripts\activate

pip install -r requirements.txt

```

> Run:

`py run.py`

For usage with gunicorn/linux you can do `sh run_linux.sh`.