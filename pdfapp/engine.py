import re
import requests


def extract_urls_from_text(raw):
    """
    returns a set of urls that appears at the raw text.
    snippet from https://stackoverflow.com/questions/6883049/regex-to-find-urls-in-string-in-python
    """

    # extract URLs using regex
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', raw)
    return set(urls)


def is_url_alive(url):
    """
    check if the given URL is alive (response code 2XX or 3XX)
    """
    # send a GET request to given URL
    try:
        response = requests.get(url)
        status = str(response.status_code)
        return status.startswith('2') or status.startswith('3')

    except requests.exceptions.RequestException as e:
        print e
        return False
