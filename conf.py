"""config file for hotel_classes_imp.py file"""

BOOKING_COM = "https://www.booking.com"
WRONG_URL_TEST = "https://www.bookin.com"
BOOKING_SEYCHELLES = 'https://www.booking.com/searchresults.en-gb.html?aid=1610684&label=sc-DnohZU0hasAqOtOM_on3ZwS380886341679%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atiaud-1110454565907%3Akwd-3403945477%3Alp1008000%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YfqnDqqG8nt10AsofPfvtt0&lang=en-gb&sid=2aab057f89707cb8a505e1056b657095&sb=1&sb_lp=1&src=country&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Fcountry%2Fsc.en-gb.html%3Faid%3D1610684%3Blabel%3Dsc-DnohZU0hasAqOtOM_on3ZwS380886341679%253Apl%253Ata%253Ap1%253Ap2%253Aac%253Aap%253Aneg%253Afi%253Atiaud-1110454565907%253Akwd-3403945477%253Alp1008000%253Ali%253Adec%253Adm%253Appccp%253DUmFuZG9tSVYkc2RlIyh9YfqnDqqG8nt10AsofPfvtt0%3Bsid%3D2aab057f89707cb8a505e1056b657095%3B&ss=Seychelles&is_ski_area=0&ssne=Seychelles&ssne_untouched=Seychelles&dest_id=188&dest_type=country&checkin_year=2021&checkin_month=8&checkin_monthday=17&checkout_year=2021&checkout_month=8&checkout_monthday=24&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1'
LAST_PAGE_URL = "https://www.booking.com/searchresults.en-gb.html?aid=1610684&label=sc-DnohZU0hasAqOtOM_on3ZwS380886341679%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atiaud-1110454565907%3Akwd-3403945477%3Alp1008000%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YfqnDqqG8nt10AsofPfvtt0&sid=2aab057f89707cb8a505e1056b657095&tmpl=searchresults&checkin_month=8&checkin_monthday=24&checkin_year=2021&checkout_month=8&checkout_monthday=31&checkout_year=2021&class_interval=1&dest_id=188&dest_type=country&dtdisc=0&from_sf=1&group_adults=2&group_children=0&inac=0&index_postcard=0&label_click=undef&no_rooms=1&postcard=0&raw_dest_type=country&room1=A%2CA&sb_price_type=total&shw_aparth=1&slp_r_match=0&src=country&src_elem=sb&srpvid=eb0e4fc792850028&ss=Seychelles&ss_all=0&ssb=empty&sshis=0&ssne=Seychelles&ssne_untouched=Seychelles&top_ufis=1&rows=25&offset=350"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
NUM_URLS = 15
TEXT = 0
NO_SPACE = 1
DIGIT = 1
HOTEL_BLOCK = '.sr_property_block'

# for most_expensive() of hotelsManager class
INDEX_HOTEL_TUPLE = 0
INDEX_PRICE_TUPLE = 1

# search variables
HOTEL_NAME_SCRAPER = '.sr-hotel__name'
HOTEL_RATING_SCRAPER = '.bui-review-score__badge'
HOTEL_IMAGE_SCRAPER = '.hotel_image'
MEALS_SCRAPER = '.add-red-tag__amount'
PRICE_SCRAPER = '.bui-price-display__value'
SCORE_TITLE_SCRAPER = '.bui-review-score__title'
TOTAL_REVIEWS_SCRAPER = '.bui-review-score__text'

# constant keys for the hotels dictionary
HOTEL_NAME = "hotel name"
HOTEL_RATING = "hotel rating"
SCORE_TITLE = 'score title'
NUMBER_OF_REVIEWS = 'num of reviews'
PRICE = "price"
LOCATION = "location"
MEALS = "meals"
ROOM_TYPE = "room type"
BED_TYPE = "bed type"
HOTEL_IMAGE = "image url"


ALL_HOTEL_KEYS = [HOTEL_NAME, HOTEL_RATING, SCORE_TITLE, NUMBER_OF_REVIEWS, PRICE, LOCATION, MEALS, ROOM_TYPE, BED_TYPE, HOTEL_IMAGE]

MIN_HOTELS_NUMBER = 340

# variables dictionary
config = {'HOTEL_NAME_SCRAPER': '.sr-hotel__name',
               'HOTEL_RATING_SCRAPER': '.bui-review-score__badge',
               'HOTEL_IMAGE_SCRAPER': '.hotel_image',
               'MEALS_SCRAPER': '.add-red-tag__amount',
               'PRICE_SCRAPER': '.bui-price-display__value',
               'SCORE_TITLE_SCRAPER': '.bui-review-score__title',
               'TOTAL_REVIEWS_SCRAPER': '.bui-review-score__text',
               'HOTEL_NAME': "hotel name",
               'HOTEL_RATING': "hotel rating",
               'SCORE_TITLE': "score title",
               'NUMBER_OF_REVIEWS': 'num of reviews',
               'PRICE': "price",
               'LOCATION': "location",
               'MEALS': "meals",
               'ROOM_TYPE': "room type",
               'BED_TYPE': "bed type",
               'HOTEL_IMAGE': "image url",
               'INDEX_HOTEL_TUPLE': 0,
               'INDEX_PRICE_TUPLE': 1,
               'HOTEL_BLOCK': '.sr_property_block',
               'DIGIT': 1,
               'NO_SPACE': 1,
               'TEXT': 0,
               'HEADERS': {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'},
               'WRONG_URL_TEST': "https://www.bookin.com",
               'BOOKING_COM': "https://www.booking.com"}

