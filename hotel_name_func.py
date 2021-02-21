

def retrieve_hotel_name(item):
    return item.select('.sr-hotel__name')[0].get_text().split('\n')[1]
