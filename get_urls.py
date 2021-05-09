import requests
from bs4 import BeautifulSoup
import sys
import logging_file as log_f
import json

# importing the constant variables from conf.json
with open('conf.json') as config_file:
    constants = json.load(config_file)


def creating_soup(url):
    try:
        url = requests.get(url, headers=constants["URLS"]["HEADERS"])
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
    next_url = constants["URLS"]["BOOKING_COM"] + next_url
    log_f.logger.info(f'successfully extract next URL: {next_url}')
    return next_url


def get_all_urls(first_url):
    """gets the first link and extract the next links that are apart of the hotels search"""

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

def API_url(latitude, longitude):
    """ The function receive latitude and longitude of the hotel as floats and retrieve a modified url for the API
        website (weatherbit)"""
    try:
        API_url = f"https://api.weatherbit.io/v2.0/current?lat={latitude}&lon={longitude}&key=cff96ab9574948a39c318e9b6c3831ef&include=minutely"
        headers = {
            'x-rapidapi-key': "b0e0e2263cmsha50e96d375ad81dp145af4jsn7c1765ced274",
            'x-rapidapi-host': "weatherbit-v1-mashape.p.rapidapi.com"
        }

        response = requests.request("GET", API_url, headers=headers)
        return response.json()
    except Exception:
        log_f.logger.warning("could not extract URL for API")
        return None


