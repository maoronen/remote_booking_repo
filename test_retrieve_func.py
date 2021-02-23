import pytest
import retrieve_func as rf
import conf as cfg
from bs4 import BeautifulSoup
import requests
import testing_common as tc


def test_retrieve_hotel_rating():
    block = tc.block_setup(cfg.BOOKING_SEYCHELLES)
    assert 0 < rf.retrieve_hotel_rating(block) < 10 or rf.retrieve_hotel_rating(block) == None

def test_retrieve_reviews_num():
    block = tc.block_setup(cfg.BOOKING_SEYCHELLES)
    assert type(rf.retrieve_reviews_num(block)) == int or rf.retrieve_reviews_num(block) == None


def
