
def retrieve_image_url(item):
    try:
        return item.select('.hotel_image')[0]['data-highres']
    except Exception:
        return None