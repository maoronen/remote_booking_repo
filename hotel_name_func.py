import conf as cfg

def retrieve_hotel_name(item):
    return item.select('.sr-hotel__name')[cfg.TEXT].get_text().split('\n')[1]
