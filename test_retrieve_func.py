import pytest
from bs4 import BeautifulSoup
import requests
import validators
import json
import Booking_scraper_main_code as booking


def hotel_obj_setup(link):
    """Receives a booking url and returns the first hotel in the page as a class object """
    link = requests.get(link, headers=booking.constants["URLS"]["HEADERS"])
    soup = BeautifulSoup(link.content, "html.parser")
    block_list = soup.select(booking.constants["SCRAPER"]["HOTEL_BLOCK"])
    hotel_obj = booking.HotelBlock(block_list[0])
    return hotel_obj


def test_retrieve_hotel_rating():
    """Tests if the function 'retrieve_hotel_rating' returns a float number between zero to ten'"""
    hotel_obj = hotel_obj_setup(booking.constants["URLS"]["TESTED_URL"])
    hotel_rating = hotel_obj.retrieve_hotel_rating()
    if hotel_rating:  # if not None
        assert 0 < hotel_rating <= 10
        assert type(hotel_rating) == float


def test_retrieve_hotel_name():
    """Tests if the function 'retrieve_hotel_name' returns a str type variable"""
    hotel_obj = hotel_obj_setup(booking.constants["URLS"]["TESTED_URL"])
    hotel_name = hotel_obj.retrieve_hotel_name()
    if hotel_name:  # if not None
        assert type(hotel_name) == str


def test_retrieve_reviews_num():
    """Tests if the function retrieve_reviews_num returns an integer greater than zero"""
    hotel_obj = hotel_obj_setup(booking.constants["URLS"]["TESTED_URL"])
    reviews_num = hotel_obj.retrieve_reviews_num()
    if reviews_num:  # if not None
        assert type(reviews_num) == int
        assert reviews_num > 0


def test_retrieve_score_title():
    """Tests if the function 'retrieve_score_title' returns a str type variable"""
    hotel_obj = hotel_obj_setup(booking.constants["URLS"]["TESTED_URL"])
    score = hotel_obj.retrieve_score_title()
    if score:  # if not None
        assert type(score) == str


def test_retrieve_bed_type():
    """Tests if the function 'retrieve_bed_type' returns a str type variable"""
    hotel_obj = hotel_obj_setup(booking.constants["URLS"]["TESTED_URL"])
    bed = hotel_obj.retrieve_bed_type()
    if bed:  # if not None
        assert type(bed) == str


def test_retrieve_room_type():
    """Tests if the function 'retrieve_room_type' returns a str type variable"""
    hotel_obj = hotel_obj_setup(booking.constants["URLS"]["TESTED_URL"])
    room = hotel_obj.retrieve_room_type()
    if room:  # if not None
        assert type(room) == str


def test_retrieve_meals():
    """Tests if the function 'retrieve_meals' returns a str type variable"""
    hotel_obj = hotel_obj_setup(booking.constants["URLS"]["TESTED_URL"])
    meals = hotel_obj.retrieve_meals()
    if meals:  # if not None
        assert type(meals) == str


def test_retrieve_hotel_location():
    """Tests if the function 'retrieve_hotel_location' returns a str type variable"""
    hotel_obj = hotel_obj_setup(booking.constants["URLS"]["TESTED_URL"])
    location = hotel_obj.retrieve_hotel_location()
    if location:  # if not None
        assert type(location) == str


def test_retrieve_image_url():
    """Tests if the function 'retrieve_image_url' returns a valid url"""
    hotel_obj = hotel_obj_setup(booking.constants["URLS"]["TESTED_URL"])
    image_url = hotel_obj.retrieve_image_url()
    valid = validators.url(image_url)
    assert valid


def test_retrieve_price():
    """Tests if the function 'retrieve_price' returns an integer greater than zero"""
    hotel_obj = hotel_obj_setup(booking.constants["URLS"]["TESTED_URL"])
    price = hotel_obj.retrieve_price()
    assert type(price) == int
    assert price > 0

