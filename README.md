# VirusTestBackend
## Back-end application of test assignment for BEST Hackaton


### Deployment
* Install python 3.10.11 or above from [official site](https://www.python.org/downloads/release/python-31011/)
* Create python virtual environment</br>
`python -m venv venv` from project direcotry
* Enable venv</br>
(linux) `source venv/bin/activate`</br>
(windows) `venv/Scripts/activate.bat`
* Install dependencies</br>
`pip install -r requirements.txt`
* Configure environment file `.env` (create it in project directory if it is absend). It should look like:
`
DB_URL=your_db_uri(postgresql+asyncpg)
SECRET_KEY=your_application_secret_key
HOST=host_to_run_app_on
PORT=port_to_run_app_on
SSL_CERTFILE_PATH=your.crt_file_path
SSL_KEYFILE_PATH=your.key_file_path
SSL_CA_BUNDLE_FILE_PATH=your_ca_bundle_file_path
`
* Start the application</br>
`python main.py`

