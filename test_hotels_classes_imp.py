import pytest
import conf as cfg
import hotels_classes_imp as hotel_class


def test_get_hotels_as_dict_type():
    """Tests the type of the variable the function 'get_hotels_as_dict' returns"""
    # setup
    test_hotel = hotel_class.HotelsManager(cfg.BOOKING_SEYCHELLES)
    hotels_dict = test_hotel.get_hotels_as_dict()

    assert type(hotels_dict) == dict
    for key, value in hotels_dict.items():
        assert type(key) == str
        assert type(value) == dict


def test_get_hotels_as_dict_keys():
    """Tests if the function 'get_hotels_as_dict' returns a dictionary where the values.keys() are all
        the parameters names that were extract from web parsing and only them """
    # setup
    test_hotel = hotel_class.HotelsManager(cfg.BOOKING_SEYCHELLES)
    hotels_dict = test_hotel.get_hotels_as_dict()

    # verify all hotel params are as expected
    for constant_key in cfg.ALL_HOTEL_KEYS:
        if constant_key == cfg.HOTEL_NAME_KEY:
            continue
        else:
            for val in hotels_dict.values():
                assert constant_key in val.keys()
                assert len(list(val.keys())) == len(cfg.ALL_HOTEL_KEYS)-1   # 'hotel name' is a master key


def test_hotels_number():
    """Tests if the function 'hotels_number' returns a type int variable and that it greater than the 'minimum hotels'
        number', which is a slightly lower number of hotels than the urls contain """
    # setup
    test_hotel = hotel_class.HotelsManager(cfg.BOOKING_SEYCHELLES)
    hotels_number = test_hotel.hotels_number()

    assert type(hotels_number) == int
    assert hotels_number > cfg.MIN_HOTELS_NUMBER


def test_get_hotels_names():
    """tests if the function 'get_hotels_names' returns a list of strings and that the length of the list is
        above the minimum hotels' number, which is a slightly lower number of hotels than the urls contain"""
    # setup
    test_hotel = hotel_class.HotelsManager(cfg.BOOKING_SEYCHELLES)
    hotels_names = test_hotel.get_hotels_names()

    assert type(hotels_names) == list
    assert len(hotels_names) > cfg.MIN_HOTELS_NUMBER
    for i in hotels_names:
        assert type(i) == str


def test_get_most_expensive():
    """Tests if the function 'most_expensive' returns a tuple, when the first element is the hotel
        name and the second one is a number above zero (price)"""
    # setup
    test_hotel = hotel_class.HotelsManager(cfg.BOOKING_SEYCHELLES)
    most_expensive = test_hotel.most_expensive()
    hotels_dict = test_hotel.get_hotels_as_dict()

    assert type(most_expensive) == tuple
    assert most_expensive[cfg.TEXT] in hotels_dict.keys()
    assert most_expensive[cfg.DIGIT] > 0




