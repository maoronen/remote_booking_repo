import requests
from bs4 import BeautifulSoup
import sys
import logging_file as log_f
import conf as cfg


def creating_soup(url):
    try:
        url = requests.get(url, headers=cfg.HEADERS)
    except requests.exceptions.SSLError:
        log_f.logger.critical('URL does not exist on internet!')
        sys.exit(1)

    soup = BeautifulSoup(url.content, "html.parser")
    return soup


def get_next_url(page_url):
    """gets url and returns the next page url if exist, if not returns None"""
    next_url = None
    soup = creating_soup(page_url)
    c = soup.find('div', class_="bui-pagination")
    try:
        href_list = c.find_all('a', href=True)
        for i, link in enumerate(href_list):
            if "current" in str(link):
                next_url = href_list[i + 1]['href']
    except IndexError:
        return None
    next_url = cfg.BOOKING_COM + next_url
    log_f.logger.info(f'successfully extract next URL: {next_url}')
    return next_url


def get_all_urls(first_url):
    """gets the first link and extract the next links that are apart of the hotels search"""
    # try:  # test if the input is valid url
    #     first_link = requests.get(first_url, headers=cfg.HEADERS)
    # except requests.ConnectionError:
    #     log_f.logger.critical('URL does not exist on internet!')
    #     sys.exit(1)
    url_list = [first_url]
    next_url = first_url
    while True:
        next_page_url = get_next_url(next_url)
        if next_page_url is not None:
            next_url = next_page_url
            url_list.append(next_page_url)
        else:
            break
    if len(url_list) < last_page_number(first_url):
        log_f.logger.error('could not extract all urls!')
    else:
        log_f.logger.info('successfully extract all urls!')
    return url_list


def last_page_number(page_url):
    """scrape the number of the last link/page of the requested url"""
    soup = creating_soup(page_url)
    last_page_num = soup.find_all('div', class_="bui-u-inline")
    return int(last_page_num[-1].text)


