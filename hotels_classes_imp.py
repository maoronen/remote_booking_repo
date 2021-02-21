import requests
from bs4 import BeautifulSoup
import all_urls_func
import get_next_url_func
import hotel_name_func
import hotel_rating_func
import score_title_func
import total_reviews_func
import price_func
import location_func
import meals_func
import room_func
import bed_func
import image_func
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

    def get_hotel_name(self):
        return self._hotel_name

    def get_score_title(self):
        return self._score_title

    def get_total_reviews(self):
        return self._total_reviews

    def get_price(self):
        return int(self._price)

    def get_location(self):
        return self._location

    def get_meals(self):
        return self._meals

    def get_room_type(self):
        return self._room_type

    def get_bed_type(self):
        return self._bed_type

    def get_image_url(self):
        return self._hotel_image


class HotelsManager:
    def __init__(self, url):
        self.url = url
        self.hotels_dict = dict()
        dict_of_hotels = dict()
        all_urls_list = all_urls_func.all_urls(self.url, cfg.HEADERS)
        with open("hotels_list.csv", "w", encoding='utf-8', newline="") as booking_file:
            fieldnames = ["name", "rating", "score", "number of reviews", "price", "location", "meals", "room type",
                          "bed type", "hotel image"]
            writer = csv.DictWriter(booking_file, fieldnames=fieldnames)
            writer.writeheader()

            for link in all_urls_list:
                link = requests.get(link, headers=cfg.HEADERS)
                soup = BeautifulSoup(link.content, "html.parser")
                for item in soup.select('.sr_property_block'):
                    hotel_name = hotel_name_func.retrieve_hotel_name(item)
                    hotel_rating = hotel_rating_func.retrieve_hotel_rating(item)
                    score_title = score_title_func.retrieve_score_title(item)
                    total_reviews = total_reviews_func.retrieve_reviews_num(item)
                    price = price_func.retrieve_price(item)
                    location = location_func.retrieve_hotel_location(item)
                    meals = meals_func.retrieve_meals(item)
                    room_type = room_func.retrieve_room_type(item)
                    bed_type = bed_func.retrieve_bed_type(item)
                    hotel_image = image_func.retrieve_image_url(item)

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
                    self.hotels_dict[hotel_object.get_hotel_name()] = hotel_object

                    writer.writerow({'name': hotel_name,
                                     'rating': hotel_rating,
                                     'score': score_title,
                                     'number of reviews': total_reviews,
                                     'price': price,
                                     'location': location,
                                     'meals': meals,
                                     'room type': room_type,
                                     'bed type': bed_type,
                                     'hotel image': hotel_image})

                    #dict_of_hotels[hotel_object.get_hotel_name()] = {'hotel rating': hotel_rating,
                                                                  #   'score title': score_title,
                                                                   #  'num of reviews': total_reviews,
                                                                    # 'price per week': price,
                                                                     #'location': location,
                                                                    # 'meals': meals,
                                                                    # 'room type': room_type,
                                                                    # 'image url': hotel_image}
            #print(dict_of_hotels)
            #I don't remember why we wanted to do this dict_of_hotels


    def hotels_number(self):
        return len(self.hotels_dict.keys())

    def get_hotels_names(self):
        return self.hotels_dict.keys()

    def most_expensive(self):
        price = 0
        most_expensive = ""
        for item in self.hotels_dict.values():
            if item.get_price() > price:
                price = item.get_price()
                most_expensive = item.get_hotel_name()
        return most_expensive, price


def main():
    manager = HotelsManager(cfg.BOOKING_SEYCHELLES)
    print(manager.most_expensive())
    print(manager.get_hotels_names())
    print(manager.hotels_number())


if __name__ == '__main__':
    main()
