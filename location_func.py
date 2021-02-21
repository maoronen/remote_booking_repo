

def retrieve_hotel_location(item):
    try:
        return item.select('.bui-link')[0].get_text().split('\n')[1].strip()
    except Exception:
        return None