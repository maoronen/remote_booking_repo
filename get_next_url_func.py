import requests
from bs4 import BeautifulSoup
import sys
import logging_file as log_f
import conf as cfg

def get_next_url(page_url, headers):
    next_url = None
    try:
        url = requests.get(page_url, headers=headers)
    except requests.ConnectionError:
        log_f.logger.critical('URL does not exist on internet!')
        sys.exit(1)
    soup = BeautifulSoup(url.content, "html.parser")
    c = soup.find('div', class_="bui-pagination")
    try:
        href_list = c.find_all('a', href=True)
        for i, link in enumerate(href_list):
            if "current" in str(link):
                next_url = href_list[i + 1]['href']
    except Exception:
        return None

    next_url = cfg.BOOKING_COM + next_url
    log_f.logger.info(f'successfully extract next URL: {next_url}')
    return next_url

