# PDFCrawler #

_Written by Yoav Porat for Comeet_  

Deployed at https://pdfcrawler.herokuapp.com/

### Usage:

* Upload file to https://pdfcrawler.herokuapp.com/upload  
  The file's key should be `file` (see `assumptions.txt`) and the `POST` request should carry the file as `form-data`

* List all uploaded documents with https://pdfcrawler.herokuapp.com/all

* List all URLs in a specific document with https://pdfcrawler.herokuapp.com/doc/<doc_name>  
  Replace the desired document's name with `<doc_name>`

* List all URLs with https://pdfcrawler.herokuapp.com/urls

### Deploy locally

1. Install dependencies with `pip install -r requirements.txt`  
2. run local django web server with `python manage.py runserver`  
3. Use according to the usage above, replacing the host with localhost:8000, or manually specify host on (2).  

### Notes

* I've used an SQLite DB for simplicity and left the test data I used inside.  
* Admin site is on, user is `admin` and password is `zubur123`  
  Since I don't serve static files (no UI is required) it looks bad, but still functional.  
* The work with the PDF files is done by the PyPDF2 package.  
