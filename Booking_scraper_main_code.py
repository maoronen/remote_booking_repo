import requests
from bs4 import BeautifulSoup
import get_urls_func
import retrieve_func
import scrape_requested_url
import conf as cfg
import csv


class Hotel:
    def __init__(self, hotel_name, hotel_rating, score_title, total_reviews, price,
                 location, meals, room_type, bed_type, hotel_image):
        self._hotel_name = hotel_name
        self._hotel_rating = hotel_rating
        self._score_title = score_title
        self._total_reviews = total_reviews
        self._price = price
        self._location = location
        self._meals = meals
        self._room_type = room_type
        self._bed_type = bed_type
        self._hotel_image = hotel_image
        self._dict_of_hotels = dict()

    def get_hotels_as_dict(self):
        self._dict_of_hotels = {'hotel rating': self._hotel_rating,
                                'score title': self._score_title,
                                'num of reviews': self._total_reviews,
                                'price': self._price,
                                'location': self._location,
                                'meals': self._meals,
                                'room type': self._room_type,
                                'bed type': self._bed_type,
                                'image url': self._hotel_image}
        return self._dict_of_hotels

    def get_hotel_name(self):
        """returns the hotel name"""
        return self._hotel_name

    def get_score_title(self):
        """returns the rating of the hotel as a float"""
        return self._score_title

    def get_total_reviews(self):
        """returns number of reviews as an int"""
        return self._total_reviews

    def get_price(self):
        "returns the price of the accommodation as an int "
        return int(self._price)

    def get_location(self):
        """returns the location of the hotel"""
        return self._location

    def get_meals(self):
        """returns what meals are included with the stay"""
        return self._meals

    def get_room_type(self):
        """returns the room type available at the price offered"""
        return self._room_type

    def get_bed_type(self):
        """returns the bed type the room includes"""
        return self._bed_type

    def get_image_url(self):
        """return a link for a representative image of the listing"""
        return self._hotel_image


class HotelsManager:
    def __init__(self, url):
        self._url = url
        self._hotels_dict = dict()
        self._dict_of_hotels = dict()
        all_urls_list = get_urls_func.get_all_urls(self._url)
        with open("hotels_table.csv", "w", encoding='utf-8', newline="") as booking_file:
            fieldnames = [cfg.HOTEL_NAME_KEY, cfg.HOTEL_RATING_KEY, cfg.SCORE_TITLE_KEY, cfg.NUMBER_OF_REVIEWS_KEY,
                          cfg.PRICE_KEY, cfg.LOCATION_KEY, cfg.MEALS_KEY, cfg.ROOM_TYPE_KEY, cfg.BED_TYPE_KEY,
                          cfg.HOTEL_IMAGE_KEY]
            writer = csv.DictWriter(booking_file, fieldnames=fieldnames)
            writer.writeheader()

            for link in all_urls_list:
                link = requests.get(link, headers=cfg.HEADERS)
                soup = BeautifulSoup(link.content, "html.parser")
                for item in soup.select(cfg.HOTEL_BLOCK):
                    hotel_name = retrieve_func.retrieve_hotel_name(item)
                    hotel_rating = retrieve_func.retrieve_hotel_rating(item)
                    score_title = retrieve_func.retrieve_score_title(item)
                    total_reviews = retrieve_func.retrieve_reviews_num(item)
                    price = retrieve_func.retrieve_price(item)
                    location = retrieve_func.retrieve_hotel_location(item)
                    meals = retrieve_func.retrieve_meals(item)
                    room_type = retrieve_func.retrieve_room_type(item)
                    bed_type = retrieve_func.retrieve_bed_type(item)
                    hotel_image = retrieve_func.retrieve_image_url(item)

                    hotel_object = Hotel(hotel_name=hotel_name,
                                         hotel_rating=hotel_rating,
                                         score_title=score_title,
                                         total_reviews=total_reviews,
                                         price=price,
                                         location=location,
                                         meals=meals,
                                         room_type=room_type,
                                         bed_type=bed_type,
                                         hotel_image=hotel_image)
                    self._hotels_dict[hotel_object.get_hotel_name()] = hotel_object
                    # in the line above a dictionary is created where the key is hotel name and the value is an hotel
                    # instance
                    self._dict_of_hotels[hotel_object.get_hotel_name()] = hotel_object.get_hotels_as_dict()
                    # in the line above using a hotel class method named 'get_hotels_as_dict(), each iteration
                    # a dict of specific hotel (with all the hotel's attributes) is added to the dict_of_hotels.
                    writer.writerow({cfg.HOTEL_NAME_KEY: hotel_name,
                                     cfg.HOTEL_RATING_KEY: hotel_rating,
                                     cfg.SCORE_TITLE_KEY: score_title,
                                     cfg.NUMBER_OF_REVIEWS_KEY: total_reviews,
                                     cfg.PRICE_KEY: price,
                                     cfg.LOCATION_KEY: location,
                                     cfg.MEALS_KEY: meals,
                                     cfg.ROOM_TYPE_KEY: room_type,
                                     cfg.BED_TYPE_KEY: bed_type,
                                     cfg.HOTEL_IMAGE_KEY: hotel_image})

    def get_hotels_as_dict(self):
        """returns a giant dict with all the hotels names as keys and hotel details as a nested dict"""
        return self._dict_of_hotels

    def hotels_number(self):
        """returns the amount of hotels that are available"""
        return len(self._hotels_dict.keys())

    def get_hotels_names(self):
        """returns a list of all hotel names"""
        return list(self._hotels_dict.keys())

    def most_expensive(self):
        """returns the most expensive hotel for that search"""
        price = 0
        most_expensive = None
        for item in self._hotels_dict.values():
            if item.get_price() > price:
                price = item.get_price()
                most_expensive = item.get_hotel_name()
        return most_expensive, price


def main():
    manager = HotelsManager(scrape_requested_url.requested_url())
    print(f'The most expensive hotel is {manager.most_expensive()[cfg.INDEX_HOTEL_TUPLE]}, '
          f'its price is {manager.most_expensive()[cfg.INDEX_PRICE_TUPLE]} NIS')
    print('**************')
    for hotel in manager.get_hotels_names():
        print(hotel)
    print('**************')
    print(f'The numbers of hotels that are available in your destination is {manager.hotels_number()}')



if __name__ == '__main__':
    main()
