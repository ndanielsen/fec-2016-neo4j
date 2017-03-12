## Loading US FEC 2016 Data into Neo4j

Working with US Elections, campaign finance, and US Congress data.

### Quick start

Start a new python virtualenv

`pip install -r requirements.txt`

Download the data from FEC ftp
`python download.py`

Download the data headers
`python download_headers.py`

Unzip all of the files
`python unzip_data.py`

Make sure that the neo4j database is running

Load the data
`python load_candidates.py`

### To Do
- Create models for the committees and individual contributions
- Add in committtees and individual contributions
- Django-fy this for a web application
