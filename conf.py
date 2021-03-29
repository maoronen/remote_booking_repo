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


<div class="sr_item sr_item_new sr_item_default sr_property_block sr_flex_layout" data-class="0" data-et-click="" data-hotelid="1222849" data-score="">
<div class="sr_item_photo sr_card_photo_wrapper" id="hotel_1222849">
<svg aria-hidden="true" class="bk-icon -iconset-heart" focusable="false" height="128" role="presentation" style="display:none;" viewbox="0 0 128 128" width="128"><path d="M64 112a3.6 3.6 0 0 1-2-.5 138.8 138.8 0 0 1-44.2-38c-10-14.4-10.6-26-9.4-33.2a29 29 0 0 1 22.9-23.7c11.9-2.4 24 2.5 32.7 13a33.7 33.7 0 0 1 32.7-13 29 29 0 0 1 22.8 23.7c1.3 7.2.6 18.8-9.3 33.3-9.1 13.1-24 25.9-44.2 37.9a3.6 3.6 0 0 1-2 .5z"></path></svg>
<svg aria-hidden="true" class="bk-icon -iconset-loading" focusable="false" height="128" role="presentation" style="display:none;" viewbox="0 0 128 128" width="128"><path d="m64 8a4.67 4.67 0 0 1 4.67 4.67v18.66a4.67 4.67 0 0 1 -4.67 4.67 4.67 4.67 0 0 1 -4.67-4.67v-18.66a4.67 4.67 0 0 1 4.67-4.67z" opacity=".75"></path><path d="m92 15.48a4.67 4.67 0 0 1 1.71 6.37l-9.34 16.15a4.67 4.67 0 0 1 -6.37 1.72 4.67 4.67 0 0 1 -1.71-6.37l9.33-16.17a4.67 4.67 0 0 1 6.38-1.7z" opacity=".2"></path><path d="m112.52 36a4.67 4.67 0 0 1 -1.71 6.37l-16.16 9.34a4.67 4.67 0 0 1 -6.37-1.71 4.67 4.67 0 0 1 1.72-6.37l16.17-9.33a4.67 4.67 0 0 1 6.35 1.7z" opacity=".25"></path><path d="m120 64a4.67 4.67 0 0 1 -4.67 4.67h-18.66a4.67 4.67 0 0 1 -4.67-4.67 4.67 4.67 0 0 1 4.67-4.67h18.67a4.67 4.67 0 0 1 4.66 4.67z" opacity=".3"></path><path d="m112.52 92a4.67 4.67 0 0 1 -6.37 1.71l-16.15-9.34a4.67 4.67 0 0 1 -1.72-6.37 4.67 4.67 0 0 1 6.37-1.71l16.17 9.33a4.67 4.67 0 0 1 1.7 6.38z" opacity=".35"></path><path d="m92 112.52a4.67 4.67 0 0 1 -6.37-1.71l-9.34-16.16a4.67 4.67 0 0 1 1.71-6.37 4.67 4.67 0 0 1 6.37 1.72l9.33 16.17a4.67 4.67 0 0 1 -1.7 6.35z" opacity=".4"></path><path d="m64 120a4.67 4.67 0 0 1 -4.67-4.67v-18.66a4.67 4.67 0 0 1 4.67-4.67 4.67 4.67 0 0 1 4.67 4.67v18.67a4.67 4.67 0 0 1 -4.67 4.66z" opacity=".45"></path><path d="m36 112.52a4.67 4.67 0 0 1 -1.71-6.37l9.34-16.15a4.67 4.67 0 0 1 6.37-1.72 4.67 4.67 0 0 1 1.71 6.37l-9.33 16.17a4.67 4.67 0 0 1 -6.38 1.7z" opacity=".5"></path><path d="m15.48 92a4.67 4.67 0 0 1 1.71-6.37l16.17-9.33a4.67 4.67 0 0 1 6.36 1.7 4.67 4.67 0 0 1 -1.72 6.37l-16.15 9.34a4.67 4.67 0 0 1 -6.37-1.71z" opacity=".55"></path><path d="m8 64a4.67 4.67 0 0 1 4.67-4.67h18.66a4.67 4.67 0 0 1 4.67 4.67 4.67 4.67 0 0 1 -4.67 4.67h-18.66a4.67 4.67 0 0 1 -4.67-4.67z" opacity=".6"></path><path d="m15.48 36a4.67 4.67 0 0 1 6.37-1.71l16.15 9.34a4.67 4.67 0 0 1 1.72 6.37 4.67 4.67 0 0 1 -6.37 1.71l-16.17-9.34a4.67 4.67 0 0 1 -1.7-6.37z" opacity=".65"></path><path d="m36 15.48a4.67 4.67 0 0 1 6.37 1.71l9.33 16.17a4.67 4.67 0 0 1 -1.7 6.36 4.67 4.67 0 0 1 -6.37-1.72l-9.34-16.15a4.67 4.67 0 0 1 1.71-6.37z" opacity=".7"></path></svg>
<div class="wl-entry-container"></div>
<a aria-hidden="true" class="sr_item_photo_link sr_hotel_preview_track" data-et-click="" focusable="false" href="/hotel/il/leonardo-almog-apartmets.en-gb.html?label=gen173nr-1FCAEoggI46AdIM1gEaGqIAQGYAQm4ARfIAQzYAQHoAQH4AQuIAgGoAgO4At7q94IGwAIB0gIkMzU0MzE5MzUtODUyNC00YWZjLTlmMTEtMmUxNDI4ZmRkYWU22AIG4AIB&amp;sid=fa7ca96eacdc875addb349dc21d55240&amp;age=12&amp;age=12&amp;age=12&amp;all_sr_blocks=122284907_295807509_6_2_0&amp;checkin=2021-12-12&amp;checkout=2022-01-02&amp;dest_id=-780112&amp;dest_type=city&amp;from_beach_non_key_ufi_sr=1&amp;group_adults=2&amp;group_children=3&amp;hapos=1&amp;highlighted_blocks=122284907_295807509_6_2_0&amp;hpos=1&amp;no_rooms=1&amp;req_adults=2&amp;req_age=12&amp;req_age=12&amp;req_age=12&amp;req_children=3&amp;room1=A%2CA%2C12%2C12%2C12&amp;sr_order=popularity&amp;sr_pri_blocks=122284907_295807509_6_2_0__1680000&amp;srepoch=1616770415&amp;srpvid=c2c668b77a3700fa&amp;ucfs=1&amp;from=searchresults#hotelTmpl" rel="noopener" tabindex="-1" target="_blank">
<img alt="Haifa Beach Apartments by Master" class="hotel_image" data-google-track="Click/sr_item_main_photo/0" data-highres="https://cf.bstatic.com/xdata/images/hotel/square600/174838917.jpg?k=b30612fd4775d38266d707e2aabc11ffb66de812e67e5edce47ea625da89b7bd&amp;o=" height="200" src="https://cf.bstatic.com/xdata/images/hotel/square200/174838917.jpg?k=b30612fd4775d38266d707e2aabc11ffb66de812e67e5edce47ea625da89b7bd&amp;o=" width="200"/>
<span class="invisible_spoken">Opens in new window</span>
</a>
</div>
<div class="sr_item_content sr_item_content_slider_wrapper">
<div class="sr_property_block_main_row">
<div class="sr_item_main_block">
<div class="sr-hotel__title-wrap">
<h3 class="sr-hotel__title">
<a class="js-sr-hotel-link hotel_name_link url" href="
/hotel/il/leonardo-almog-apartmets.en-gb.html?label=gen173nr-1FCAEoggI46AdIM1gEaGqIAQGYAQm4ARfIAQzYAQHoAQH4AQuIAgGoAgO4At7q94IGwAIB0gIkMzU0MzE5MzUtODUyNC00YWZjLTlmMTEtMmUxNDI4ZmRkYWU22AIG4AIB&amp;sid=fa7ca96eacdc875addb349dc21d55240&amp;age=12&amp;age=12&amp;age=12&amp;all_sr_blocks=122284907_295807509_6_2_0&amp;checkin=2021-12-12&amp;checkout=2022-01-02&amp;dest_id=-780112&amp;dest_type=city&amp;from_beach_non_key_ufi_sr=1&amp;group_adults=2&amp;group_children=3&amp;hapos=1&amp;highlighted_blocks=122284907_295807509_6_2_0&amp;hpos=1&amp;no_rooms=1&amp;req_adults=2&amp;req_age=12&amp;req_age=12&amp;req_age=12&amp;req_children=3&amp;room1=A%2CA%2C12%2C12%2C12&amp;sr_order=popularity&amp;sr_pri_blocks=122284907_295807509_6_2_0__1680000&amp;srepoch=1616770415&amp;srpvid=c2c668b77a3700fa&amp;ucfs=1&amp;from=searchresults
;highlight_room=#hotelTmpl" rel="noopener" target="_blank">
<span class="sr-hotel__name" data-et-click="   ">
Haifa Beach Apartments by Master
</span>
<span class="invisible_spoken">Opens in new window</span>
</a>
</h3>
<span class="sr-hotel__title-badges">
<span class="c-accommodation-classification-rating">
<span class="c-accommodation-classification-rating__badge c-accommodation-classification-rating__badge--tiles c-accommodation-classification-rating__badge--with-tooltip" data-component="accommodation-classification-rating" title="&lt;p&gt;Awarded to &lt;strong&gt;home and apartment-like properties&lt;/strong&gt; by Booking.com. These represent quality ratings based on factors including facilities, size, location and service.&lt;/p&gt;">
<span aria-label="4 out of 5" class="bui-rating bui-rating--smaller" role="img">
<span aria-hidden="true" class="bui-icon bui-rating__item bui-icon--medium" role="presentation">
<svg aria-hidden="true" focusable="false" role="img" viewbox="0 0 112 128" xmlns="http://www.w3.org/2000/svg">
<path d="M96 8H16A16 16 0 0 0 0 24v96h96a16 16 0 0 0 16-16V24A16 16 0 0 0 96 8zM56 88a24 24 0 1 1 24-24 24 24 0 0 1-24 24z"></path>
</svg>
</span>
<span aria-hidden="true" class="bui-icon bui-rating__item bui-icon--medium" role="presentation">
<svg aria-hidden="true" focusable="false" role="img" viewbox="0 0 112 128" xmlns="http://www.w3.org/2000/svg">
<path d="M96 8H16A16 16 0 0 0 0 24v96h96a16 16 0 0 0 16-16V24A16 16 0 0 0 96 8zM56 88a24 24 0 1 1 24-24 24 24 0 0 1-24 24z"></path>
</svg>
</span>
<span aria-hidden="true" class="bui-icon bui-rating__item bui-icon--medium" role="presentation">
<svg aria-hidden="true" focusable="false" role="img" viewbox="0 0 112 128" xmlns="http://www.w3.org/2000/svg">
<path d="M96 8H16A16 16 0 0 0 0 24v96h96a16 16 0 0 0 16-16V24A16 16 0 0 0 96 8zM56 88a24 24 0 1 1 24-24 24 24 0 0 1-24 24z"></path>
</svg>
</span>
<span aria-hidden="true" class="bui-icon bui-rating__item bui-icon--medium" role="presentation">
<svg aria-hidden="true" focusable="false" role="img" viewbox="0 0 112 128" xmlns="http://www.w3.org/2000/svg">
<path d="M96 8H16A16 16 0 0 0 0 24v96h96a16 16 0 0 0 16-16V24A16 16 0 0 0 96 8zM56 88a24 24 0 1 1 24-24 24 24 0 0 1-24 24z"></path>
</svg>
</span>
</span>
</span>
</span>
<span data-et-view="TPOaXGZCHQGPGJIMADXRT:1"></span>
<svg aria-hidden="true" class="bk-icon -iconset-thumbs_up_square pp-icon-valign--tbottom js-preferred-property-copy-cached" data-bui-component="Tooltip" data-et-mouseenter="
customGoal:TPOaXGZCHQGPGJIMADXRT:1
" data-tooltip-follow="true" data-tooltip-position="bottom" data-tooltip-text="..." fill="#FEBB02" focusable="false" height="20" rel="300" role="presentation" viewbox="0 0 128 128" width="20"><path d="M112 8H16a8 8 0 0 0-8 8v96a8 8 0 0 0 8 8h96a8 8 0 0 0 8-8V16a8 8 0 0 0-8-8zM48 96H24V58h24zm56-25a8.7 8.7 0 0 1-2 6 8.9 8.9 0 0 1 1 4 6.9 6.9 0 0 1-5 7c-.5 4-4.8 8-9 8H56V58l10.3-23.3a5.4 5.4 0 0 1 10.1 2.7 10.3 10.3 0 0 1-.6 2.7L72 52h23c4.5 0 9 3.5 9 8a9.2 9.2 0 0 1-2 5.3 7.5 7.5 0 0 1 2 5.7z"></path></svg>
</span>
</div>
<div class="sr_card_address_line">
<a class="bui-link" data-coords="34.9572989000001,32.8062096176718" data-google-track="Click/Action: sr_map_link_used" data-map-caption="" href="
/hotel/il/leonardo-almog-apartmets.en-gb.html?label=gen173nr-1FCAEoggI46AdIM1gEaGqIAQGYAQm4ARfIAQzYAQHoAQH4AQuIAgGoAgO4At7q94IGwAIB0gIkMzU0MzE5MzUtODUyNC00YWZjLTlmMTEtMmUxNDI4ZmRkYWU22AIG4AIB&amp;amp;amp;sid=fa7ca96eacdc875addb349dc21d55240&amp;amp;amp;age=12&amp;amp;amp;age=12&amp;amp;amp;age=12&amp;amp;amp;all_sr_blocks=122284907_295807509_6_2_0&amp;amp;amp;checkin=2021-12-12&amp;amp;amp;checkout=2022-01-02&amp;amp;amp;dest_id=-780112&amp;amp;amp;dest_type=city&amp;amp;amp;from_beach_non_key_ufi_sr=1&amp;amp;amp;group_adults=2&amp;amp;amp;group_children=3&amp;amp;amp;hapos=1&amp;amp;amp;highlighted_blocks=122284907_295807509_6_2_0&amp;amp;amp;hpos=1&amp;amp;amp;no_rooms=1&amp;amp;amp;req_adults=2&amp;amp;amp;req_age=12&amp;amp;amp;req_age=12&amp;amp;amp;req_age=12&amp;amp;amp;req_children=3&amp;amp;amp;room1=A%2CA%2C12%2C12%2C12&amp;amp;amp;sr_order=popularity&amp;amp;amp;sr_pri_blocks=122284907_295807509_6_2_0__1680000&amp;amp;amp;srepoch=1616770415&amp;amp;amp;srpvid=c2c668b77a3700fa&amp;amp;amp;ucfs=1&amp;amp;amp;from=searchresults;map=1&amp;amp;amp;msd=1
#hotelTmpl" rel="noopener" target="_blank">
 Haifa
<span class="sr_card_address_line__item">
<span class="sr_card_address_line__dot-separator"></span>
Show on map</span>
</a>
<span class="sr_card_address_line__dot-separator"></span>
<span data-bui-component="Tooltip" data-tooltip-follow="" data-tooltip-light="" data-tooltip-position="top" title="This is the straight-line distance on the map. Actual travel distance may vary.">
4.1 km from centre
</span>
<span class="pub_trans sr_card_address_line__item" data-bui-component="Tooltip" data-tooltip-follow="" data-tooltip-light="" data-tooltip-position="top" title="Not far from: Carmel Beach,  Dado Beach">
<span class="sr_card_address_line__dot-separator"></span>
Beach nearby
</span>
</div>
</div>
<div class="sr_item_review_block">
<div class="reviewFloater reviewFloaterBadge__container">
<div class="sr-review-score">
<a class="sr-review-score__link" href="/hotel/il/leonardo-almog-apartmets.en-gb.html?label=gen173nr-1FCAEoggI46AdIM1gEaGqIAQGYAQm4ARfIAQzYAQHoAQH4AQuIAgGoAgO4At7q94IGwAIB0gIkMzU0MzE5MzUtODUyNC00YWZjLTlmMTEtMmUxNDI4ZmRkYWU22AIG4AIB&amp;amp;sid=fa7ca96eacdc875addb349dc21d55240&amp;amp;age=12&amp;amp;age=12&amp;amp;age=12&amp;amp;all_sr_blocks=122284907_295807509_6_2_0&amp;amp;checkin=2021-12-12&amp;amp;checkout=2022-01-02&amp;amp;dest_id=-780112&amp;amp;dest_type=city&amp;amp;from_beach_non_key_ufi_sr=1&amp;amp;group_adults=2&amp;amp;group_children=3&amp;amp;hapos=1&amp;amp;highlighted_blocks=122284907_295807509_6_2_0&amp;amp;hpos=1&amp;amp;no_rooms=1&amp;amp;req_adults=2&amp;amp;req_age=12&amp;amp;req_age=12&amp;amp;req_age=12&amp;amp;req_children=3&amp;amp;room1=A%2CA%2C12%2C12%2C12&amp;amp;sr_order=popularity&amp;amp;sr_pri_blocks=122284907_295807509_6_2_0__1680000&amp;amp;srepoch=1616770415&amp;amp;srpvid=c2c668b77a3700fa&amp;amp;ucfs=1&amp;amp;from=searchresults;from_sr_review=1;#hotelTmpl" target="_blank">
<div class="bui-review-score c-score bui-review-score--end">
<div aria-label="Scored 9.1 " class="bui-review-score__badge">
9.1
</div>
<div class="bui-review-score__content">
<div class="bui-review-score__title">
Superb
</div>
<div class="bui-review-score__text">
151 reviews
</div>
</div>
</div>
<span class="invisible_spoken">Opens in new window</span>
</a>
<a href="/hotel/il/leonardo-almog-apartmets.en-gb.html?label=gen173nr-1FCAEoggI46AdIM1gEaGqIAQGYAQm4ARfIAQzYAQHoAQH4AQuIAgGoAgO4At7q94IGwAIB0gIkMzU0MzE5MzUtODUyNC00YWZjLTlmMTEtMmUxNDI4ZmRkYWU22AIG4AIB&amp;amp;amp;sid=fa7ca96eacdc875addb349dc21d55240&amp;amp;amp;age=12&amp;amp;amp;age=12&amp;amp;amp;age=12&amp;amp;amp;all_sr_blocks=122284907_295807509_6_2_0&amp;amp;amp;checkin=2021-12-12&amp;amp;amp;checkout=2022-01-02&amp;amp;amp;dest_id=-780112&amp;amp;amp;dest_type=city&amp;amp;amp;from_beach_non_key_ufi_sr=1&amp;amp;amp;group_adults=2&amp;amp;amp;group_children=3&amp;amp;amp;hapos=1&amp;amp;amp;highlighted_blocks=122284907_295807509_6_2_0&amp;amp;amp;hpos=1&amp;amp;amp;no_rooms=1&amp;amp;amp;req_adults=2&amp;amp;amp;req_age=12&amp;amp;amp;req_age=12&amp;amp;amp;req_age=12&amp;amp;amp;req_children=3&amp;amp;amp;room1=A%2CA%2C12%2C12%2C12&amp;amp;amp;sr_order=popularity&amp;amp;amp;sr_pri_blocks=122284907_295807509_6_2_0__1680000&amp;amp;amp;srepoch=1616770415&amp;amp;amp;srpvid=c2c668b77a3700fa&amp;amp;amp;ucfs=1&amp;amp;amp;from=searchresults;from_sr_review=1;#hotelTmpl" target="_blank">
<div class="search-secondary-review-score">
<span class="review-score-widget review-score-widget__superb review-score-widget__text-only review-score-widget__right review-score-widget__14 review-score-widget__no-subtext">
<span aria-label="Rated superb" class="review-score-widget__text">
Comfort
</span>
<span aria-label="Scored 9.2 " class="review-score-badge">
9.2
</span>
</span>
</div>
<span class="invisible_spoken">Opens in new window</span>
</a>
</div>
</div>
</div>
</div>
<div class="sr-badges__row">
<span data-et-view="ZVYSFXcLfOFfOBJOTXNAJbaOQQBC:1"></span>
</div>
<div class="sr_rooms_table_block clearfix sr_card_rooms_container">
<div class="room_details">
<div class="sr_gr sr-group_recommendation" data-et-click="  ">
<div class="sr-group-wrap">
<div class="sr-group-wrap__main">
<table cellspacing="0" class="featuredRooms sr_room_table sr-group_recommendation sr_rms_tbl_bdr" role="presentation">
<tbody>
<tr class="roomrow entire_row_clickable" data-link="/hotel/il/leonardo-almog-apartmets.en-gb.html?label=gen173nr-1FCAEoggI46AdIM1gEaGqIAQGYAQm4ARfIAQzYAQHoAQH4AQuIAgGoAgO4At7q94IGwAIB0gIkMzU0MzE5MzUtODUyNC00YWZjLTlmMTEtMmUxNDI4ZmRkYWU22AIG4AIB&amp;sid=fa7ca96eacdc875addb349dc21d55240&amp;age=12&amp;age=12&amp;age=12&amp;all_sr_blocks=122284907_295807509_6_2_0&amp;checkin=2021-12-12&amp;checkout=2022-01-02&amp;dest_id=-780112&amp;dest_type=city&amp;from_beach_non_key_ufi_sr=1&amp;group_adults=2&amp;group_children=3&amp;hapos=1&amp;highlighted_blocks=122284907_295807509_6_2_0&amp;hpos=1&amp;no_rooms=1&amp;req_adults=2&amp;req_age=12&amp;req_age=12&amp;req_age=12&amp;req_children=3&amp;room1=A%2CA%2C12%2C12%2C12&amp;sr_order=popularity&amp;sr_pri_blocks=122284907_295807509_6_2_0__1680000&amp;srepoch=1616770415&amp;srpvid=c2c668b77a3700fa&amp;ucfs=1&amp;from=searchresults;show_room=122284907#RD122284907" data-target="_blank" tabindex="0">
<td class="maxPersonsLeft maxPersonsLeft--compact">
<div class="c-occupancy-icons c-occupancy-icons--no-plus">
<span aria-hidden="true" class="c-occupancy-icons__adults c-occupancy-icons--with-mutiplier">
<svg aria-hidden="true" class="bk-icon -iconset-person_half" fill="#000000" focusable="false" height="16" role="presentation" viewbox="0 0 128 128" width="16"><path d="M104 120H24a8 8 0 0 1-8-8V93.5a4 4 0 0 1 1-2.7C21.3 86.4 36.9 72 64 72s42.8 14.4 47 18.8a4 4 0 0 1 1 2.7V112a8 8 0 0 1-8 8zM64 8a28 28 0 1 0 28 28A28 28 0 0 0 64 8z"></path></svg>
<span class="c-occupancy-icons__multiplier">×</span>
<span class="c-occupancy-icons__multiplier-number">6</span>
</span>
<span class="bui-u-sr-only">
Max adults: 6
</span>
</div>
</td>
<td class="roomName">
<div class="roomNameInner">
<div class="room_link room_link--bigger">
<span role="link" tabindex="0">
Two-Bedroom Apartment
</span>
</div>
<div data-et-view="NAFLeOeJAETfJUIcIKHVPTdMZbGXNcXaO:8"></div>
<div class="c-unit-configuration">
<div class="c-unit-configuration--dots c-unit-configuration--mt" data-component="tooltip" data-tooltip-position="bottom start" data-tooltip-text='
&lt;div class="m-rs-bed-display m-rs-bed-display--grouped c-bed-display--table c-bed-display--table-inline"&gt;
&lt;div class="m-rs-bed-display__block" data-name-en="Beds"&gt;
&lt;div class="m-rs-bed-display__label"&gt;
Bedroom 1:
&lt;/div&gt;
&lt;div class="m-rs-bed-display__bed-list"&gt;
&lt;div class="m-rs-bed-display__bed-list-item"&gt;
&lt;span class="m-rs-bed-display__bed-type-name"&gt;
1 large double bed&lt;/span&gt;
&lt;/div&gt;
&lt;/div&gt;
&lt;/div&gt;
&lt;div class="m-rs-bed-display__block" data-name-en="Beds"&gt;
&lt;div class="m-rs-bed-display__label"&gt;
Bedroom 2:
&lt;/div&gt;
&lt;div class="m-rs-bed-display__bed-list"&gt;
&lt;div class="m-rs-bed-display__bed-list-item"&gt;
&lt;span class="m-rs-bed-display__bed-type-name"&gt;
1 large double bed&lt;/span&gt;
&lt;/div&gt;
&lt;/div&gt;
&lt;/div&gt;
&lt;div class="m-rs-bed-display__block" data-name-en="Beds"&gt;
&lt;div class="m-rs-bed-display__label"&gt;
Living room:
&lt;/div&gt;
&lt;div class="m-rs-bed-display__bed-list"&gt;
&lt;div class="m-rs-bed-display__bed-list-item"&gt;
&lt;span class="m-rs-bed-display__bed-type-name"&gt;
1 sofa bed&lt;/span&gt;
&lt;/div&gt;
&lt;/div&gt;
&lt;/div&gt;
&lt;/div&gt;
'>
<span class="c-unit-configuration__item c-unit-configuration__item-name">Entire apartment ­</span>
•­
<span class="c-unit-configuration__item">2 bedrooms</span>
•­
<span class="c-unit-configuration__item">1 living room</span>
•­
<span class="c-unit-configuration__item">1 bathroom</span>
•­
<span class="c-unit-configuration__item">90m²</span>
</div>
</div>
<div class="c-beds-configuration">
3 beds
(1 sofa bed, 2 large doubles)
</div>
<sup class="sr_room_reward sr_room_reward--bold e2e-free-cancellation">FREE cancellation
</sup>

<sup class="sr_room_reward e2e-cancel-later">
<script data-hash="OQREFYWEIFcIOEIbKCBZFBXPWe" type="track_copy"></script>You can cancel later, so lock in this great price today.
</sup>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div class="sr-group-wrap__aside">
<div class="prco-wrapper bui-price-display prco-sr-default-assembly-wrapper prc-d-sr-wrapper">
<div class="prco-ltr-right-align-helper">
<div class="bui-price-display__label prco-inline-block-maker-helper">3 weeks, 2 adults, 3 children</div>
</div>
<div class="prco-ltr-right-align-helper">
<div class="prco-inline-block-maker-helper">
<div aria-hidden="true" class="bui-price-display__value prco-inline-block-maker-helper" data-et-mouseenter="
customGoal:cCcCcCDUfcXIFbcDcbNXGDJae:1
goal:desktop_sr_hover_over_price
">
₪ 16,800
</div>
<span class="bui-u-sr-only">
Price
₪ 16,800
</span>
</div>
</div>
<div class="prco-ltr-right-align-helper">
<div class="prd-taxes-and-fees-under-price prco-inline-block-maker-helper blockuid-" data-cur-stage="4" data-excl-charges-raw="">
Additional charges may apply
</div>
</div>
</div>
<div class="sr_gr_footer">
<div class="sr-cta-button-row" data-et-click="">
<div>
<a class="txp-cta bui-button bui-button--primary sr_cta_button" data-click-store-id="sr-compset-1222849" data-et-click="customGoal:OQLOLOLOMSVSRQbVKKMadMUWe:1 customGoal:OQLOLOLOMSVSRQbVKKMadMUWe:3 customGoal:OLGZGNMQcCVKLLYBJdBbAdPVT:1" href="/hotel/il/leonardo-almog-apartmets.en-gb.html?label=gen173nr-1FCAEoggI46AdIM1gEaGqIAQGYAQm4ARfIAQzYAQHoAQH4AQuIAgGoAgO4At7q94IGwAIB0gIkMzU0MzE5MzUtODUyNC00YWZjLTlmMTEtMmUxNDI4ZmRkYWU22AIG4AIB&amp;sid=fa7ca96eacdc875addb349dc21d55240&amp;age=12&amp;age=12&amp;age=12&amp;all_sr_blocks=122284907_295807509_6_2_0&amp;checkin=2021-12-12&amp;checkout=2022-01-02&amp;dest_id=-780112&amp;dest_type=city&amp;from_beach_non_key_ufi_sr=1&amp;group_adults=2&amp;group_children=3&amp;hapos=1&amp;highlighted_blocks=122284907_295807509_6_2_0&amp;hpos=1&amp;no_rooms=1&amp;req_adults=2&amp;req_age=12&amp;req_age=12&amp;req_age=12&amp;req_children=3&amp;room1=A%2CA%2C12%2C12%2C12&amp;sr_order=popularity&amp;sr_pri_blocks=122284907_295807509_6_2_0__1680000&amp;srepoch=1616770415&amp;srpvid=c2c668b77a3700fa&amp;ucfs=1&amp;from=searchresults;hptv=do" target="_blank">
<span class="bui-button__text js-sr-cta-text">
See availability
</span>

<div class="txp-arr bui-button__icon">
<svg aria-hidden="true" class="bk-icon -streamline-arrow_nav_right" focusable="false" height="16" role="presentation" viewbox="0 0 24 24" width="16"><path d="M9.45 6c.2 0 .39.078.53.22l5 5c.208.206.323.487.32.78a1.1 1.1 0 0 1-.32.78l-5 5a.75.75 0 0 1-1.06 0 .74.74 0 0 1 0-1.06L13.64 12 8.92 7.28a.74.74 0 0 1 0-1.06.73.73 0 0 1 .53-.22zm4.47 5.72zm0 .57z"></path></svg>
</div>
</a>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>