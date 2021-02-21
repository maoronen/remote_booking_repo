"""config file for hotel_classes_imp.py file"""

BOOKING_COM = "https://www.booking.com"
BOOKING_SEYCHELLES = 'https://www.booking.com/searchresults.en-gb.html?aid=1610684&label=sc-DnohZU0hasAqOtOM_on3ZwS380886341679%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atiaud-1110454565907%3Akwd-3403945477%3Alp1008000%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YfqnDqqG8nt10AsofPfvtt0&lang=en-gb&sid=2aab057f89707cb8a505e1056b657095&sb=1&sb_lp=1&src=country&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Fcountry%2Fsc.en-gb.html%3Faid%3D1610684%3Blabel%3Dsc-DnohZU0hasAqOtOM_on3ZwS380886341679%253Apl%253Ata%253Ap1%253Ap2%253Aac%253Aap%253Aneg%253Afi%253Atiaud-1110454565907%253Akwd-3403945477%253Alp1008000%253Ali%253Adec%253Adm%253Appccp%253DUmFuZG9tSVYkc2RlIyh9YfqnDqqG8nt10AsofPfvtt0%3Bsid%3D2aab057f89707cb8a505e1056b657095%3B&ss=Seychelles&is_ski_area=0&ssne=Seychelles&ssne_untouched=Seychelles&dest_id=188&dest_type=country&checkin_year=2021&checkin_month=8&checkin_monthday=24&checkout_year=2021&checkout_month=8&checkout_monthday=31&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
TEXT = 0
NO_SPACE = 1
DIGIT = 1

# search variables
HOTEL_NAME = '.sr-hotel__name'
HOTEL_RATING = '.bui-review-score__badge'
HOTEL_IMAGE = '.hotel_image'
MEALS = '.add-red-tag__amount'
PRICE = '.bui-price-display__value'
SCORE_TITLE = '.bui-review-score__title'
TOTAL_REVIEWS = '.bui-review-score__text'