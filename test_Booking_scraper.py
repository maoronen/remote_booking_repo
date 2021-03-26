import pytest
import Booking_scraper_main_code as booking
import pandas as pd
import numpy


def test_get_hotels_names_df():
    """tests if the function 'get_hotels_names' returns a pandas DataFrame"""
    # setup
    test_hotel = booking.HotelsManager(booking.constants["URLS"]["TESTED_URL"])
    hotels_names_df = test_hotel.get_hotels_names()
    assert type(hotels_names_df) == pd.Series


def test_get_hotels_names_object_type():
    """tests if the function 'get_hotels_names' returns hotels names column as object type"""
    test_hotel = booking.HotelsManager(booking.constants["URLS"]["TESTED_URL"])
    hotels_names_df = test_hotel.get_hotels_names()
    assert hotels_names_df.dtype == object


def test_get_most_expensive_tuples():
    """Tests if the function 'most_expensive' returns a tuple (hotel name, price)"""
    # setup
    test_hotel = booking.HotelsManager(booking.constants["URLS"]["TESTED_URL"])
    most_expensive = test_hotel.most_expensive()
    assert type(most_expensive) == tuple


def test_get_most_expensive_type_first_items():
    """Tests if the function 'most_expensive' returns a tuple, when the first element (most expensive hotel)
     is from type str"""
    test_hotel = booking.HotelsManager(booking.constants["URLS"]["TESTED_URL"])
    most_expensive_hotel = test_hotel.most_expensive()
    assert type(most_expensive_hotel[0]) == str


def test_get_most_expensive_type_second_items():
    """Tests if the function 'most_expensive' returns a tuple, when the second element (price) is from type int"""
    test_hotel = booking.HotelsManager(booking.constants["URLS"]["TESTED_URL"])
    most_expensive_hotel = test_hotel.most_expensive()
    assert type(most_expensive_hotel[1]) == numpy.int64


def test():
    test_get_hotels_names_df()
    test_get_hotels_names_object_type()
    test_get_most_expensive_tuples()
    test_get_most_expensive_type_first_items()
    test_get_most_expensive_type_second_items()


test()