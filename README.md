# horoscope-daq

To Get the `stub` folder
1. Drag `horosocpe-api.yaml` in [edittor.swagger](https://editor.swagger.io)

2. Click `Generate Server` at the top of [edittor.swagger](https://editor.swagger.io)

3. Select `python-flask`, it will be downloaded.

4. Rename the folder to `stub`.

5. Drag into the root folder.

To run REST API Server

1. Create virtual environment
`python -m venv env`

2. Activate virtual environment
`. env/bin/active`

3. Install packages from `requirements.txt` on virtual environment.
`pip install -r requirements.txt`

4. Create `config.py` from `config.py.example`

5. Start the REST API server
`python app.py`

Test the API at 

http://localhost:8080/horoscope-api/v1/ui/