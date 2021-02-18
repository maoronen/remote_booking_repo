import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) '
                        'Version/9.0.2 Safari/601.3.9'}
booking_url = 'https://www.booking.com/searchresults.en-gb.html?aid=1610684&label=sc-DnohZU0hasAqOtOM_on3ZwS380886341679%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atiaud-1110454565907%3Akwd-3403945477%3Alp1008000%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YfqnDqqG8nt10AsofPfvtt0&lang=en-gb&sid=1435df31028313dcef54cb9d530a9fcb&sb=1&sb_lp=1&src=country&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Fcountry%2Fsc.en-gb.html%3Faid%3D1610684%3Blabel%3Dsc-DnohZU0hasAqOtOM_on3ZwS380886341679%253Apl%253Ata%253Ap1%253Ap2%253Aac%253Aap%253Aneg%253Afi%253Atiaud-1110454565907%253Akwd-3403945477%253Alp1008000%253Ali%253Adec%253Adm%253Appccp%253DUmFuZG9tSVYkc2RlIyh9YfqnDqqG8nt10AsofPfvtt0%3Bsid%3D1435df31028313dcef54cb9d530a9fcb%3B&ss=Seychelles&is_ski_area=0&ssne=Seychelles&ssne_untouched=Seychelles&dest_id=188&dest_type=country&checkin_year=2021&checkin_month=8&checkin_monthday=24&checkout_year=2021&checkout_month=8&checkout_monthday=31&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&track_hp_back_button=1#hotel_378034-back'
url = requests.get(booking_url, headers=headers)
soup = BeautifulSoup(url.content, 'lxml')
#print(len(soup.select('.sr_property_block')))
count = 0
for item in soup.select('.sr_property_block'):
    try:
        print(f"Hotel name: {item.select('.sr-hotel__name')[0].get_text().strip()}")
        print("Island name: ", item.select('.bui-link')[0].get_text().strip().split('\n')[0])
        print(f"Hotel rating: {item.select('.bui-review-score__badge')[0].get_text().strip()}")
        print(f"Hotel rating title: {item.select('.bui-review-score__title')[0].get_text().strip()}")
        print(f"The Hotel has {item.select('.bui-review-score__text')[0].get_text().strip()}")
        print("Click the link to see the hotel: ", item.select('.hotel_image')[0]['data-highres'])

        # extracting the url of the hotel:
        hotel_link = str(item.select('.sr_item_photo_link')[0])
        hotel_link = hotel_link.split('href=')
        hotel_link = hotel_link[1].split('"')[1]
        hotel_link = "https://www.booking.com" + hotel_link
        print(hotel_link)
        print('*****************')
        if count == 0:  #ignore this. tried to do something that did not worked
            hotel_link_text= requests.get(hotel_link).text
            print(hotel_link_text)
            soup = BeautifulSoup(hotel_link_text, 'lxml')
            print(soup.select('.important_facility')[0].get_text())

            count = 1

        #hotel_link = str(item.select('.sr_item_photo_link')[0])
        #print('**\n', hotel_link)
        container = item.find('div', class_='room_link')
        for room in container.find_all('strong'):
            room_type = room.text
        print(f"Room type: {room_type}")
        print(f"Price for {item.select('.prco-ltr-right-align-helper')[0].get_text().strip()}: {item.select('.bui-price-display__value')[0].get_text().strip()}")
        try:
            if len(item.select('.sr_card_room_policies__container')):
                room_policies = list(filter(None ,item.select('.sr_card_room_policies__container')[0].get_text().strip().split('\n')))
                print('Room policies:')
                for ele in room_policies:
                    print(ele)
            else:
                pass
        except Exception as e:
            print('error')

        #print(item.select('.room_link'))
        #print(soup.find('strong').text)

        print('--------------------------------------------------')
    except Exception as e:
        print('#ERROR')