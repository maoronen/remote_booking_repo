import pytest
import get_urls
import requests
import validators
import conf as cfg


def test_get_next_url_error_failure():
    with pytest.raises(requests.ConnectionError):
        get_urls.get_next_url(cfg.WRONG_URL_TEST)
    print("checking ConnectionError in case of invalid url: succeed")


def test_get_next_url_not_none():
    # setup
    next_link = get_urls.get_next_url(cfg.BOOKING_SEYCHELLES)
    assert next_link  # not None


def test_get_next_url_is_url():
    # setup
    next_link = get_urls.get_next_url(cfg.BOOKING_SEYCHELLES)
    valid = validators.url(next_link)
    assert valid == True


def test_get_next_url_is_none():  # when inserting the last url
    # setup
    next_link = get_urls.get_next_url(cfg.LAST_PAGE_URL)
    assert not next_link


def test_get_all_urls_error_failure():  # in case inserting invalid url
    with pytest.raises(requests.exceptions.SSLError):
        get_urls.get_all_urls(cfg.WRONG_URL_TEST)
    # print("checking ConnectionError in case of invalid url: succeed")


def test_get_all_urls_success():
    # setup
    all_links = get_urls.get_all_urls(cfg.BOOKING_SEYCHELLES)
    assert type(all_links) == list
    assert len(all_links) >= cfg.NUM_URLS


def test_get_all_urls_are_urls():
    # setup
    all_links = get_urls.get_all_urls(cfg.BOOKING_SEYCHELLES)
    for link in all_links:
        valid = validators.url(link)
        assert valid == True


