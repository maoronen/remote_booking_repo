import requests
from bs4 import BeautifulSoup
#from selenium import webdriver


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
booking_url = 'https://www.booking.com/searchresults.en-gb.html?aid=1610684&label=sc-DnohZU0hasAqOtOM_on3ZwS380886341679%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atiaud-1110454565907%3Akwd-3403945477%3Alp1008000%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YfqnDqqG8nt10AsofPfvtt0&lang=en-gb&sid=2aab057f89707cb8a505e1056b657095&sb=1&sb_lp=1&src=country&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Fcountry%2Fsc.en-gb.html%3Faid%3D1610684%3Blabel%3Dsc-DnohZU0hasAqOtOM_on3ZwS380886341679%253Apl%253Ata%253Ap1%253Ap2%253Aac%253Aap%253Aneg%253Afi%253Atiaud-1110454565907%253Akwd-3403945477%253Alp1008000%253Ali%253Adec%253Adm%253Appccp%253DUmFuZG9tSVYkc2RlIyh9YfqnDqqG8nt10AsofPfvtt0%3Bsid%3D2aab057f89707cb8a505e1056b657095%3B&ss=Seychelles&is_ski_area=0&ssne=Seychelles&ssne_untouched=Seychelles&dest_id=188&dest_type=country&checkin_year=2021&checkin_month=8&checkin_monthday=24&checkout_year=2021&checkout_month=8&checkout_monthday=31&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1'
# url = requests.get(booking_url, headers=headers)
# soup = BeautifulSoup(url.content, "html.parser")


def get_next_url(page_url):
    url = requests.get(page_url, headers=headers)
    soup = BeautifulSoup(url.content, "html.parser")
    c = soup.find('div', class_="bui-pagination")
    try:
        href_list = c.find_all('a', href=True)
        for i, link in enumerate(href_list):
            if "current" in str(link):
                next_url = href_list[i+1]['href']
    except Exception:
        return None
    next_url = "https://www.booking.com" + next_url
    return next_url

def all_urls(first_url):
    """gets the first link and extract the next links that are apart of the hotels search"""
    url_list = []
    next_url = first_url
    while True:
        next_page_url = get_next_url(next_url)
        print(next_page_url)
        if next_page_url is not None:
            next_url = next_page_url
            url_list.append(next_page_url)
        else:
            break
    return url_list


all_urls_list = all_urls(booking_url)
# for item in soup.select('.sr_property_block'):
#     hotel_name = item.select('.sr-hotel__name')[0].get_text().split('\n')[1]
#     score_title = item.select('.bui-review-score__title')[0].get_text().strip()
#     total_reviews = item.select('.bui-review-score__text')[0].get_text().strip()
#     price = item.select('.bui-price-display__value')[0].get_text().split('\n')[1]
#     location = item.select('.bui-link')[0].get_text().split('\n')[1].strip()
#     if item.select('.add-red-tag__amount'):
#         breakfast = item.select('.add-red-tag__amount')[0].get_text().strip()
#     else:
#         breakfast = "Not included"
#     container = item.find('div', class_='room_link')
#     for room in container.find_all('strong'):
#         room_type = room.text
#     bed_type = item.select('.c-beds-configuration')[0].get_text().strip()
#     hotel_pic = item.select('.hotel_image')[0]['data-highres']
#     cancellation = item.select('.free-cancel-persuasion')[0].get_text().strip()
#
#     # extracting the url of the hotel:
#     hotel_link = str(item.select('.sr_item_photo_link')[0])
#     hotel_link = hotel_link.split('href=')
#     hotel_link = hotel_link[1].split('"')[1]
#     hotel_link = "https://www.booking.com" + hotel_link
#     print(hotel_link)



    # print(
    #     f'hotel name: {hotel_name}\nprice: {price}\nscore title: {score_title}\ntotal reviews: {total_reviews}\n'
    #     f'location: {location}\nroom type: {room_type}\nbreakfast: {breakfast}\nbed_type: {bed_type}\n'
    #     f'cancellation policy: {cancellation}\nhotel pic: {hotel_pic}')
    # print("----------------------------------------------------------------")
