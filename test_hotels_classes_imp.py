import pytest
import conf as cfg
import hotels_classes_imp as hotel_class


def test_get_hotels_as_dict_type():
    # setup
    test_hotel = hotel_class.HotelsManager(cfg.BOOKING_SEYCHELLES)
    hotels_dict = test_hotel.get_hotels_as_dict()

    assert type(hotels_dict) == dict
    for key, value in hotels_dict.items():
        assert type(key) == str
        assert type(value) == dict


def test_get_hotels_as_dict_keys():
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
                assert len(list(val.keys())) == len(cfg.ALL_HOTEL_KEYS) - 1  # 'hotel name' is a master key


def test_hotels_number():
    # setup
    test_hotel = hotel_class.HotelsManager(cfg.BOOKING_SEYCHELLES)
    hotels_number = test_hotel.hotels_number()

    assert type(hotels_number) == int
    assert hotels_number > cfg.MIN_HOTELS_NUMBER


def test_get_hotels_names():
    # setup
    test_hotel = hotel_class.HotelsManager(cfg.BOOKING_SEYCHELLES)
    hotels_names = test_hotel.get_hotels_names()

    assert type(hotels_names) == list
    assert len(hotels_names) > cfg.MIN_HOTELS_NUMBER
    for i in hotels_names:
        assert type(i) == str


def test_get_most_expensive():
    # setup
    test_hotel = hotel_class.HotelsManager(cfg.BOOKING_SEYCHELLES)
    most_expensive = test_hotel.most_expensive()
    hotels_dict = test_hotel.get_hotels_as_dict()

    assert type(most_expensive) == tuple
    assert most_expensive[cfg.TEXT] in hotels_dict.keys()
    assert most_expensive[cfg.DIGIT] > 0




