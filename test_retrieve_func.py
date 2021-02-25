import pytest
import retrieve_func as rf
import conf as cfg
from bs4 import BeautifulSoup
import requests
import validators

def block_setup(link):
    """Receives a booking url and returns the first block of a hotel """
    link = requests.get(link, headers=cfg.HEADERS)
    soup = BeautifulSoup(link.content, "html.parser")
    block_list = soup.select(cfg.HOTEL_BLOCK)
    return block_list[0]


def test_retrieve_hotel_rating():
    """Tests if the function 'retrieve_hotel_rating' returns a float number between zero to ten'"""
    block = block_setup(cfg.BOOKING_SEYCHELLES)
    hotel_rating = rf.retrieve_hotel_rating(block)
    if hotel_rating:  # if not None
        assert 0 < rf.retrieve_hotel_rating(block) <= 10
        assert type(rf.retrieve_hotel_rating(block)) == float


def test_retrieve_hotel_name():
    """Tests if the function 'retrieve_hotel_name' returns a str type variable"""
    block = block_setup(cfg.BOOKING_SEYCHELLES)
    hotel_name = rf.retrieve_hotel_name(block)
    if hotel_name:  # if not None
        assert type(hotel_name) == str


def test_retrieve_reviews_num():
    """Tests if the function retrieve_reviews_num returns an integer greater than zero"""
    block = block_setup(cfg.BOOKING_SEYCHELLES)
    reviews_num = rf.retrieve_reviews_num(block)
    if reviews_num:  # if not None
        assert type(reviews_num) == int
        assert rf.retrieve_reviews_num(block) > 0


def test_retrieve_score_title():
    """Tests if the function 'retrieve_score_title' returns a str type variable"""
    block = block_setup(cfg.BOOKING_SEYCHELLES)
    score = rf.retrieve_score_title(block)
    if score:  # if not None
        assert type(score) == str


def test_retrieve_bed_type():
    """Tests if the function 'retrieve_bed_type' returns a str type variable"""
    block = block_setup(cfg.BOOKING_SEYCHELLES)
    bed = rf.retrieve_bed_type(block)
    if bed:  # if not None
        assert type(bed) == str


def test_retrieve_room_type():
    """Tests if the function 'retrieve_room_type' returns a str type variable"""
    block = block_setup(cfg.BOOKING_SEYCHELLES)
    room = rf.retrieve_room_type(block)
    if room:  # if not None
        assert type(room) == str


def test_retrieve_meals():
    """Tests if the function 'retrieve_meals' returns a str type variable"""
    block = block_setup(cfg.BOOKING_SEYCHELLES)
    meals = rf.retrieve_meals(block)
    if meals:  # if not None
        assert type(meals) == str


def test_retrieve_hotel_location():
    """Tests if the function 'retrieve_hotel_location' returns a str type variable"""
    block = block_setup(cfg.BOOKING_SEYCHELLES)
    location = rf.retrieve_hotel_location(block)
    if location:  # if not None
        assert type(location) == str


def test_retrieve_image_url():
    """Tests if the function 'retrieve_image_url' returns a valid url"""
    block = block_setup(cfg.BOOKING_SEYCHELLES)
    image_url = rf.retrieve_image_url(block)
    valid = validators.url(image_url)
    assert valid


def test_retrieve_price():
    """Tests if the function 'retrieve_price' returns an integer greater than zero"""
    block = block_setup(cfg.BOOKING_SEYCHELLES)
    price = rf.retrieve_price(block)
    assert type(price) == int
    assert price > 0

