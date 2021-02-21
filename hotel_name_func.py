import conf as cfg

def retrieve_hotel_name(item):
    return item.select(cfg.HOTEL_NAME)[cfg.TEXT].get_text().split('\n')[1]


