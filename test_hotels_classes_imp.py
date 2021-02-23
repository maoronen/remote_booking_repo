import pytest
import conf as cfg
import hotels_classes_imp as hotel_class


def test_get_hotels_as_dict():
    test_hotel = hotel_class.HotelManager(cfg.BOOKING_SEYCHELLES)
    hotels_dict = test_hotel.get_hotels_as_dict()
    assert type(hotels_dict) == dict
    for i in range(len(hotels_dict.keys())):
        assert type(hotels_dict.keys()[i]) == str
        assert type(hotels_dict.values()[i]) == dict

    # verify all hotel params are as expected
    for constant_key in cfg.ALL_HOTEL_KEYS:
        for val in hotels_dict.values:
            assert constant_key in val.keys()
            assert len(val.keys) == len(cfg.ALL_HOTEL_KEYS)
