import pytest
import get_urls
import requests
import conf as cfg


def test_get_next_url_error_failure():
    with pytest.raises(requests.ConnectionError):
        requests.get(cfg.WRONG_URL_TEST, headers=cfg.HEADERS)
    print("checking ConnectionError in case of wrong url: succeed")

def test_get_all_urls():



