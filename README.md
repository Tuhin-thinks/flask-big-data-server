# Flask Big Data Server

Flask application to retrieve and process data

### Endpoints:

- `/fetch-data`: Fetch data from third party API service; returns **data_id**
- `/get-processed-data?data_id={{data_id}}`: Get processed data by **data_id**

### How to run:

1. Clone the repository

2. Create a virtualenv and activate it:


**[Install virtualenv package](https://pypi.org/project/virtualenv/)**
```bash
pip install virtualenv
```

**Setup the virtualenv and activate it:**

**For Windows:**

```ps1
python -m virtualenv venv

venv\Scripts\activate
```

**For Linux:**

```bash
python3 -m virtualenv venv

source venv/bin/activate
```

2. Install the dependencies: `pip install -r requirements.txt`
3. Run the application: `python run.py`
4. Access the endpoints using the base URL: `http://localhost:5000`

