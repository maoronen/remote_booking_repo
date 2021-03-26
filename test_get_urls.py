import pytest
import get_urls
import validators
import json


# setup
with open('conf.json') as config_file:
    constants = json.load(config_file)

def test_get_next_url_not_none():
    """Tests if the function get_next_url not returns a None value"""
    # setup
    next_link = get_urls.get_next_url(constants["URLS"]["TESTED_URL"])
    assert next_link  # not None


def test_get_next_url_is_url():
    """Tests if the function get_next_url returns a valid url """
    # setup
    next_link = get_urls.get_next_url(constants["URLS"]["TESTED_URL"])
    valid = validators.url(next_link)
    assert valid


def test_get_next_url_is_none():  # when inserting the last url
    """Tests if the function get_next_url returns None when it receives the last url as an input"""
    # setup
    last_link = get_urls.get_all_urls(constants["URLS"]["TESTED_URL"])[-1]
    next_link = get_urls.get_next_url(last_link)
    assert not next_link


def test_get_all_urls_are_urls():
    """Tests if the function get_all_urls returns a list of valid urls"""
    # setup
    all_links = get_urls.get_all_urls(constants["URLS"]["TESTED_URL"])
    for link in all_links:
        valid = validators.url(link)
        assert valid


def test_get_all_urls_list_type():
    # setup
    all_links = get_urls.get_all_urls(constants["URLS"]["TESTED_URL"])
    assert type(all_links) == list


def test_get_all_urls_not_empty():
    # setup
    all_links = get_urls.get_all_urls(constants["URLS"]["TESTED_URL"])
    assert len(all_links) >= 1


def test_last_page_number_int_type():
    """tests if the function last_page_number returns an int"""
    # setup
    last_link = get_urls.last_page_number(constants["URLS"]["TESTED_URL"])
    assert type(last_link) == int


def test_last_page_number_reliability():
    """tests if the function last_page_number is equal to the length of the list get_all_urls returns"""
    all_links = get_urls.get_all_urls(constants["URLS"]["TESTED_URL"])
    last_link_number = get_urls.last_page_number(constants["URLS"]["TESTED_URL"])
    assert len(all_links) == last_link_number

