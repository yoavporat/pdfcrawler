web: bin/gunicorn_django --workers=4 --bind=0.0.0.0:$PORT crawler/settings.py; gunicorn crawler.wsgi --log-file -