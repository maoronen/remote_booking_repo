import requests
from bs4 import BeautifulSoup
import get_urls
import scrape_requested_url as sru
import csv
import logging_file as log_f
from mysql.connector import MySQLConnection, Error
import mysql_db_scraper
import mysql
import pandas as pd
import json
import argparse_scraping as arg_src

# importing the constant variables from conf.json
with open('conf.json') as config_file:
    constants = json.load(config_file)


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
            return self.hotel_html_item.select(constants["SCRAPER"]["HOTEL_NAME"])[constants["NUMBERS"]["TEXT"]].get_text().split('\n')[1]
        except IndexError:
            log_f.logger.info("could not extract hotel's rating")
            return None

    def retrieve_hotel_rating(self):
        """returns the rating of the hotel as a float between 0-10"""
        try:
            return float(self.hotel_html_item.select(constants["SCRAPER"]["HOTEL_RATING"])[constants["NUMBERS"]["TEXT"]].get_text().strip())
        except IndexError:
            log_f.logger.info("could not extract hotel's rating")
            return None

    def retrieve_score_title(self):
        """returns the rating of the hotel as a str"""
        try:
            return self.hotel_html_item.select(constants["SCRAPER"]["SCORE_TITLE"])[constants["NUMBERS"]["TEXT"]].get_text().strip()
        except IndexError:
            log_f.logger.info("could not extract hotel's score title")
            return None

    def retrieve_reviews_num(self):
        """returns the total number of reviews the hotel received"""
        try:
            return int(self.hotel_html_item.select(constants["SCRAPER"]["TOTAL_REVIEWS"])[constants["NUMBERS"]["TEXT"]].get_text().strip().split()[0].replace(",", ""))
        except IndexError:
            log_f.logger.info("could not extract hotel's reviews number")
            return None

    def retrieve_hotel_location(self):
        """returns area / city or island where the hotel is located"""
        try:
            return self.hotel_html_item.select('.bui-link')[constants["NUMBERS"]["TEXT"]].get_text().split('\n')[constants["NUMBERS"]["NO_SPACE"]].strip()
        except Exception:
            log_f.logger.info("could not extract hotel's location")
            return None

    def retrieve_meals(self):
        """returns which meals (if any) are included in the hotel price"""
        try:
            return self.hotel_html_item.select(constants["SCRAPER"]["MEALS"])[constants["NUMBERS"]["TEXT"]].get_text().strip()
        except Exception:
            return None

    def retrieve_price(self):
        """returns the price as a int of the hotel for the entire requested period"""
        try:
            price = self.hotel_html_item.select(constants["SCRAPER"]["PRICE"])[constants["NUMBERS"]["TEXT"]].get_text().split('\n')[constants["NUMBERS"]["NO_SPACE"]].split()[
                constants["NUMBERS"]["DIGIT"]]
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
            return self.hotel_html_item.select(constants["SCRAPER"]["BED"])[0].get_text().strip()
        except Exception:
            return None

    def retrieve_image_url(self):
        """returns URL for the hotel image or hotel area"""
        try:
            return self.hotel_html_item.select(constants["SCRAPER"]["HOTEL_IMAGE"])[constants["NUMBERS"]["TEXT"]]['data-highres']
        except Exception:
            log_f.logger.info("could not extract hotel's image url")
            return None

    def get_coordinates(self):
        """returns coordinates of the hotel location"""
        try:
            coor = self.hotel_html_item.select(constants["SCRAPER"]["COORDINATES"])[0]
            coor = str(coor).split("data-coords=")[1].split()[0]
            coor1 = coor.split(",")
            longitude = float(coor1[0][1:])
            latitude = float(coor1[1][:-1])
            return (latitude, longitude)
        except Exception:
            log_f.logger.info("could not extract hotel's coordinates")
            return None


    def get_timezone(self):
        """returns the timezone of the hotel"""
        try:
            my_dict = get_urls.API_url(self.get_coordinates()[0], self.get_coordinates()[1])
            time_zone = my_dict['data'][0]['timezone']
            return time_zone
        except Exception:
            log_f.logger.info("could not extract the timezone")
            return None


    def get_temperature(self):
        "returns the current temperature at the hotel surrounding "
        try:
            my_dict = get_urls.API_url(self.get_coordinates()[0], self.get_coordinates()[1])
            temperature = my_dict['data'][0]['temp']
            return temperature
        except Exception:
            log_f.logger.info("could not extract the current temperature")
            return None



class HotelsManager:
    """The class collects all the hotels in the url and creates an object to each hotel.
        attribute:
        'url': str. Booking link according to user requirements """

    def __init__(self, url):
        self._url = url
        all_urls_list = get_urls.get_all_urls(self._url)
        with open(constants["HOTEL_DETAILS"]["CSV_FILE_NAME"], "w", encoding='utf-8', newline="") as booking_file:
            fieldnames = [constants["HOTEL_DETAILS"]["HOTEL_NAME"],
                          constants["HOTEL_DETAILS"]["HOTEL_RATING"],
                          constants["HOTEL_DETAILS"]["SCORE_TITLE"],
                          constants["HOTEL_DETAILS"]["NUMBER_OF_REVIEWS"],
                          constants["HOTEL_DETAILS"]["PRICE"],
                          constants["HOTEL_DETAILS"]["LOCATION"],
                          constants["HOTEL_DETAILS"]["MEALS"],
                          constants["HOTEL_DETAILS"]["ROOM_TYPE"],
                          constants["HOTEL_DETAILS"]["BED_TYPE"],
                          constants["HOTEL_DETAILS"]["HOTEL_IMAGE"],
                          constants["HOTEL_DETAILS"]["TIMEZONE"],
                          constants["HOTEL_DETAILS"]["TEMPERATURE"]]
            writer = csv.DictWriter(booking_file, fieldnames=fieldnames)
            writer.writeheader()

            id_counter = 0
            id_loc_counter = 0
            location_dict = {}
            args = arg_src.args_parse() # in order to extract host, user, password and db_name
            for link in all_urls_list:
                link = requests.get(link, headers=constants["URLS"]["HEADERS"])
                soup = BeautifulSoup(link.content, "html.parser")

                for item in soup.select(constants["SCRAPER"]["HOTEL_BLOCK"]):
                    hotel_object = HotelBlock(item)
                    try:
                        mydb = mysql.connector.connect(
                            host=args.host,
                            user=args.user,
                            password=args.password
                        )
                    except Error as e:
                        log_f.logger.critical("Error while connecting to MySQL", e)

                    if hotel_object.retrieve_hotel_location() in location_dict: # if the location is already in the dict, take location PK from dict
                        location_PK = location_dict[hotel_object.retrieve_hotel_location()]
                    else: # if this is the first time, this location appears, insert it to the dict and take location_PK from the counter
                        location_dict[hotel_object.retrieve_hotel_location()] = id_loc_counter
                        location_PK = id_loc_counter
                        id_loc_counter += 1

                    try:
                        db_name = args.db_name
                        cur = mydb.cursor()
                        cur.execute(f"USE {db_name}")
                        cur.execute(
                            "INSERT INTO locations (id, location) VALUES (%s, %s)",
                            [location_PK, hotel_object.retrieve_hotel_location()])
                        mydb.commit()
                        log_f.logger.info("Record inserted successfully into locations table")
                    except Exception as e:
                        log_f.logger.warning("Failed to insert record into locations table {}".format(e))

                    try:
                        cur.execute(
                            "INSERT INTO hotels (id, name, location_id, rating, reviews, price_ILS, timezone, current_temperature) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                            [id_counter, hotel_object.retrieve_hotel_name(), location_PK, hotel_object.retrieve_hotel_rating(), hotel_object.retrieve_reviews_num(), hotel_object.retrieve_price(), hotel_object.get_timezone(), hotel_object.get_temperature()])
                        mydb.commit()
                        log_f.logger.info("Record inserted successfully into hotels table")
                    except Exception as e:
                        log_f.logger.warning("Failed to insert record into hotels table {}".format(e))


                    try:
                        cur.execute(
                            "INSERT INTO facilities (hotel_id, room_type, bed_type, meals) VALUES (%s, %s, %s, %s)",
                            [id_counter, hotel_object.retrieve_room_type(), hotel_object.retrieve_bed_type(),
                             hotel_object.retrieve_meals()])
                        mydb.commit()
                        log_f.logger.info("Record inserted successfully into facilities table")
                    except Exception as e:
                        log_f.logger.warning("Failed to insert record into facilities table {}".format(e))

                    try:
                        cur.execute(
                            "INSERT INTO hotel_image (hotel_id, image_url) VALUES (%s, %s)",
                            [id_counter, hotel_object.retrieve_image_url()])
                        mydb.commit()
                        log_f.logger.info("Record inserted successfully into hotel_image table")
                    except Exception as e:
                        log_f.logger.warning("Failed to insert record into hotel_image table {}".format(e))

                    id_counter += 1  # Progressing the hotel id.

                    writer.writerow({constants["HOTEL_DETAILS"]["HOTEL_NAME"]: hotel_object.retrieve_hotel_name(),
                                     constants["HOTEL_DETAILS"]["HOTEL_RATING"]: hotel_object.retrieve_hotel_rating(),
                                     constants["HOTEL_DETAILS"]["SCORE_TITLE"]: hotel_object.retrieve_score_title(),
                                     constants["HOTEL_DETAILS"]["NUMBER_OF_REVIEWS"]: hotel_object.retrieve_reviews_num(),
                                     constants["HOTEL_DETAILS"]["PRICE"]: hotel_object.retrieve_price(),
                                     constants["HOTEL_DETAILS"]["LOCATION"]: hotel_object.retrieve_hotel_location(),
                                     constants["HOTEL_DETAILS"]["MEALS"]: hotel_object.retrieve_meals(),
                                     constants["HOTEL_DETAILS"]["ROOM_TYPE"]: hotel_object.retrieve_room_type(),
                                     constants["HOTEL_DETAILS"]["BED_TYPE"]: hotel_object.retrieve_bed_type(),
                                     constants["HOTEL_DETAILS"]["HOTEL_IMAGE"]: hotel_object.retrieve_image_url(),
                                     constants["HOTEL_DETAILS"]["TIMEZONE"]: hotel_object.get_timezone(),
                                     constants["HOTEL_DETAILS"]["TEMPERATURE"]: hotel_object.get_temperature()})

    def get_hotels_number(self):
        """returns the amount of hotels that are available"""
        df = pd.read_csv(constants["HOTEL_DETAILS"]["CSV_FILE_NAME"])
        return len(df.index)

    def get_hotels_names(self):
        """returns a list of all hotel names"""
        df = pd.read_csv(constants["HOTEL_DETAILS"]["CSV_FILE_NAME"])
        return df[constants["HOTEL_DETAILS"]["HOTEL_NAME"]]

    def most_expensive(self):
        """returns the most expensive hotel for that search"""
        df = pd.read_csv(constants["HOTEL_DETAILS"]["CSV_FILE_NAME"])
        max_price = df[constants["HOTEL_DETAILS"]["PRICE"]].max()
        return df[df[constants["HOTEL_DETAILS"]["PRICE"]] == max_price][constants["HOTEL_DETAILS"]["HOTEL_NAME"]].item(), max_price


def main():
    args = arg_src.args_parse()
    mysql_db_scraper.create_db(args.host, args.user, args.password, args.db_name)
    manager = HotelsManager(sru.requested_url())
    print(f'The most expensive hotel is {manager.most_expensive()[constants["NUMBERS"]["INDEX_HOTEL_TUPLE"]]}, '
          f'its price is {manager.most_expensive()[constants["NUMBERS"]["INDEX_PRICE_TUPLE"]]} NIS')
    print('**************')
    for hotel in manager.get_hotels_names():
        print(hotel)
    print('**************')
    print(f'The numbers of hotels that are available in your destination is {manager.get_hotels_number()}')


if __name__ == '__main__':
    main()