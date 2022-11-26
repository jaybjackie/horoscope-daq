# horoscope-daq

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