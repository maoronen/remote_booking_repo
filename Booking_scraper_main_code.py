import requests
from bs4 import BeautifulSoup
import get_urls_func
import scrape_requested_url
import conf as cfg
import csv
import logging_file as log_f
from mysql.connector import MySQLConnection, Error
import mysql


class HotelBlock:
    """The class represent a hotel object.
        attributes:
        hotel_html_item: html code of the hotel
        hotel_dict = a dictionary which contain extracted data from the hotel_html_item"""

    def __init__(self, hotel_html_item):
        self.hotel_html_item = hotel_html_item
        self._hotel_dict = dict()

    def retrieve_hotel_name(self):
        """returns the hotel name"""
        try:
            return self.hotel_html_item.select(cfg.HOTEL_NAME_SCRAPER)[cfg.TEXT].get_text().split('\n')[1]
        except IndexError:
            log_f.logging.info("could not extract hotel's rating")
            return None

    def retrieve_hotel_rating(self):
        """returns the rating of the hotel as a float between 0-10"""
        try:
            return float(self.hotel_html_item.select(cfg.HOTEL_RATING_SCRAPER)[cfg.TEXT].get_text().strip())
        except IndexError:
            log_f.logging.info("could not extract hotel's rating")
            return None

    def retrieve_score_title(self):
        """returns the rating of the hotel as a str"""
        try:
            return self.hotel_html_item.select(cfg.SCORE_TITLE_SCRAPER)[cfg.TEXT].get_text().strip()
        except IndexError:
            log_f.logger.info("could not extract hotel's score title")
            return None

    def retrieve_reviews_num(self):
        """returns the total number of reviews the hotel received"""
        try:
            return int(self.hotel_html_item.select(cfg.TOTAL_REVIEWS_SCRAPER)[cfg.TEXT].get_text().strip().split()[0].replace(",", ""))
        except IndexError:
            log_f.logger.info("could not extract hotel's reviews number")
            return None

    def retrieve_hotel_location(self):
        """returns area / city or island where the hotel is located"""
        try:
            return self.hotel_html_item.select('.bui-link')[cfg.TEXT].get_text().split('\n')[cfg.NO_SPACE].strip()
        except Exception:
            log_f.logging.info("could not extract hotel's location")
            return None

    def retrieve_meals(self):
        """returns which meals (if any) are included in the hotel price"""
        try:
            return self.hotel_html_item.select(cfg.MEALS_SCRAPER)[cfg.TEXT].get_text().strip()
        except Exception:
            return None

    def retrieve_price(self):
        """returns the price as a int of the hotel for the entire requested period"""
        try:
            price = self.hotel_html_item.select(cfg.PRICE_SCRAPER)[cfg.TEXT].get_text().split('\n')[cfg.NO_SPACE].split()[
                cfg.DIGIT]
            price = int(price.replace(",", ""))
        except Exception:
            log_f.logger.info("could not extract hotel's price")
            return None
        return price

    def retrieve_room_type(self):
        """The type of room(str) priced at the hotel price"""
        try:
            container = self.hotel_html_item.find('div', class_='room_link')
            return container.text.strip()
        except Exception:
            log_f.logger.info("could not extract hotel's room type")
            return None

    def retrieve_bed_type(self):
        """returns the bed type/s at the hotel room"""
        try:
            return self.hotel_html_item.select('.c-beds-configuration')[0].get_text().strip()
        except Exception:
            return None


    def retrieve_image_url(self):
        """returns URL for the hotel image or hotel area"""
        try:
            return self.hotel_html_item.select(cfg.HOTEL_IMAGE_SCRAPER)[cfg.TEXT]['data-highres']
        except Exception:
            log_f.logging.info("could not extract hotel's image url")
            return None

    def get_hotel_as_dict(self):
        """returns the hotel methods as a dictionary
        (except for the name of the hotel)"""
        self._hotel_dict = {'hotel rating': self.retrieve_hotel_rating(),
                                'score title': self.retrieve_score_title(),
                                'num of reviews': self.retrieve_reviews_num(),
                                'price': self.retrieve_price(),
                                'location': self.retrieve_hotel_location(),
                                'meals': self.retrieve_meals(),
                                'room type': self.retrieve_room_type(),
                                'bed type': self.retrieve_bed_type(),
                                'image url': self.retrieve_image_url()}
        return self._hotel_dict


class HotelsManager:
    """The class collects all the hotels in the url and creates an object to each hotel.
        attribute:
        'url': str. Booking link according to user requirements """

    def __init__(self, url):
        self._url = url
        self._hotels_dict = dict()
        self._dict_of_hotels = dict()
        all_urls_list = get_urls_func.get_all_urls(self._url)
        with open("hotels_details.csv", "w", encoding='utf-8', newline="") as booking_file:
            fieldnames = [cfg.HOTEL_NAME, cfg.HOTEL_RATING, cfg.SCORE_TITLE, cfg.NUMBER_OF_REVIEWS,
                          cfg.PRICE, cfg.LOCATION, cfg.MEALS, cfg.ROOM_TYPE, cfg.BED_TYPE,
                          cfg.HOTEL_IMAGE]
            writer = csv.DictWriter(booking_file, fieldnames=fieldnames)
            writer.writeheader()

            id = 0
            for link in all_urls_list:
                link = requests.get(link, headers=cfg.HEADERS)
                soup = BeautifulSoup(link.content, "html.parser")

                for item in soup.select(cfg.HOTEL_BLOCK):
                    hotel_object = HotelBlock(item)
                    mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="4817"
                    )

                    cur = mydb.cursor()
                    cur.execute("USE booking_db")
                    cur.execute(
                        "INSERT INTO hotels (id, name, rating, reviews, price) VALUES (%s, %s, %s, %s, %s)",
                        [id, hotel_object.retrieve_hotel_name(), hotel_object.retrieve_hotel_rating(), hotel_object.retrieve_reviews_num(), hotel_object.retrieve_price()])
                    mydb.commit()

                    cur.execute(
                        "INSERT INTO facilities (hotel_id, room_type, bed_type, meals) VALUES (%s, %s, %s, %s)",
                        [id, hotel_object.retrieve_room_type(), hotel_object.retrieve_bed_type(),
                         hotel_object.retrieve_meals()])
                    mydb.commit()

                    cur.execute(
                        "INSERT INTO locations (hotel_id, location) VALUES (%s, %s)",
                        [id, hotel_object.retrieve_hotel_location()])
                    mydb.commit()

                    cur.execute(
                        "INSERT INTO hotel_image (hotel_id, image_url) VALUES (%s, %s)",
                        [id, hotel_object.retrieve_image_url()])
                    mydb.commit()

                    id += 1  # Progressing the hotel id.

                    #self._hotels_dict[hotel_object.retrieve_hotel_name()] = hotel_object
                    # in the line above a dictionary is created where the key is hotel name and the value is an hotel
                    # instance
                    self._dict_of_hotels[hotel_object.retrieve_hotel_name()] = hotel_object.get_hotel_as_dict()
                    # in the line above using a hotel class method named 'get_hotel_as_dict(), each iteration
                    # a dict of specific hotel (with all the hotel's attributes) is added to the dict_of_hotels.
                    writer.writerow({cfg.HOTEL_NAME: hotel_object.retrieve_hotel_name(),
                                     cfg.HOTEL_RATING: hotel_object.retrieve_hotel_rating(),
                                     cfg.SCORE_TITLE: hotel_object.retrieve_score_title(),
                                     cfg.NUMBER_OF_REVIEWS: hotel_object.retrieve_reviews_num(),
                                     cfg.PRICE: hotel_object.retrieve_price(),
                                     cfg.LOCATION: hotel_object.retrieve_hotel_location(),
                                     cfg.MEALS: hotel_object.retrieve_meals(),
                                     cfg.ROOM_TYPE: hotel_object.retrieve_room_type(),
                                     cfg.BED_TYPE: hotel_object.retrieve_bed_type(),
                                     cfg.HOTEL_IMAGE: hotel_object.retrieve_image_url()})

    def get_hotels_as_dict(self):
        """returns a giant dict with all the hotels names as keys and hotel details as a nested dict"""
        return self._dict_of_hotels

    def hotels_number(self):
        """returns the amount of hotels that are available"""
        return len(self._dict_of_hotels.keys())

    def get_hotels_names(self):
        """returns a list of all hotel names"""
        return list(self._hotels_dict.keys())

    def most_expensive(self):
        """returns the most expensive hotel for that search"""
        price = 0
        most_expensive = None
        for item in self._hotels_dict.values():
            if item.retrieve_price() > price:
                price = item.retrieve_price()
                most_expensive = item.retrieve_hotel_name()
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
