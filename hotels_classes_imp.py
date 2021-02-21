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

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
booking_url = 'https://www.booking.com/searchresults.en-gb.html?aid=1610684&label=sc-DnohZU0hasAqOtOM_on3ZwS380886341679%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atiaud-1110454565907%3Akwd-3403945477%3Alp1008000%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YfqnDqqG8nt10AsofPfvtt0&lang=en-gb&sid=2aab057f89707cb8a505e1056b657095&sb=1&sb_lp=1&src=country&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Fcountry%2Fsc.en-gb.html%3Faid%3D1610684%3Blabel%3Dsc-DnohZU0hasAqOtOM_on3ZwS380886341679%253Apl%253Ata%253Ap1%253Ap2%253Aac%253Aap%253Aneg%253Afi%253Atiaud-1110454565907%253Akwd-3403945477%253Alp1008000%253Ali%253Adec%253Adm%253Appccp%253DUmFuZG9tSVYkc2RlIyh9YfqnDqqG8nt10AsofPfvtt0%3Bsid%3D2aab057f89707cb8a505e1056b657095%3B&ss=Seychelles&is_ski_area=0&ssne=Seychelles&ssne_untouched=Seychelles&dest_id=188&dest_type=country&checkin_year=2021&checkin_month=8&checkin_monthday=24&checkout_year=2021&checkout_month=8&checkout_monthday=31&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1'


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
        all_urls_list = all_urls_func.all_urls(self.url, headers)

        for link in all_urls_list:
            link = requests.get(link, headers=headers)
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
                dict_of_hotels[hotel_object.get_hotel_name()] = {'hotel rating': hotel_rating,
                                                                 'score title': score_title,
                                                                 'num of reviews': total_reviews,
                                                                 'price per week': price,
                                                                 'location': location,
                                                                 'meals': meals,
                                                                 'room type': room_type,
                                                                 'image url': hotel_image}
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
    manager = HotelsManager(booking_url)
    print(manager.most_expensive())
    print(manager.get_hotels_names())
    print(manager.hotels_number())


if __name__ == '__main__':
    main()
