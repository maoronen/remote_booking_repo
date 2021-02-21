
def retrieve_hotel_rating(item):
    try:
        return item.select('.sr-hotel__name')[0].get_text().split('\n')[1]
    except Exception:
        return None
