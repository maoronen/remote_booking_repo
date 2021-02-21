
def retrieve_hotel_rating(item):
    try:
        return float(item.select('.bui-review-score__badge')[0].get_text().strip())
    except Exception:
        return None
