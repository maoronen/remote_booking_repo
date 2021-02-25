import pytest
import get_urls_func
import requests
import validators
import conf as cfg


def test_get_next_url_not_none():
    """Tests if the function get_next_url not returns a None value"""
    # setup
    next_link = get_urls_func.get_next_url(cfg.BOOKING_SEYCHELLES)
    assert next_link  # not None


def test_get_next_url_is_url():
    """Tests if the function get_next_url returns a valid url """
    # setup
    next_link = get_urls_func.get_next_url(cfg.BOOKING_SEYCHELLES)
    valid = validators.url(next_link)
    assert valid


def test_get_next_url_is_none():  # when inserting the last url
    """Tests if the function get_next_url returns None when it receives the last url as an input"""
    # setup
    next_link = get_urls_func.get_next_url(cfg.LAST_PAGE_URL)
    assert not next_link


def test_get_all_urls_success():
    """Tests if the function get_all_urls returns a list with at least 15 elements"""
    # setup
    all_links = get_urls_func.get_all_urls(cfg.BOOKING_SEYCHELLES)
    assert type(all_links) == list
    assert len(all_links) >= cfg.NUM_URLS


def test_get_all_urls_are_urls():
    """Tests if the function get_all_urls returns a list of valid urls"""
    # setup
    all_links = get_urls_func.get_all_urls(cfg.BOOKING_SEYCHELLES)
    for link in all_links:
        valid = validators.url(link)
        assert valid


