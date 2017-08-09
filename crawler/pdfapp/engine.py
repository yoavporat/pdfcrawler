import re


def extract_urls_from_text(raw):
    """
    returns a set of urls that appears at the raw text.
    snippet from https://stackoverflow.com/questions/6883049/regex-to-find-urls-in-string-in-python
    """
    print raw

    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', raw)
    print urls
    return set(urls)
