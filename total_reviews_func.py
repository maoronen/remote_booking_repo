

def retrieve_reviews_num(item):
    try:
        return item.select('.bui-review-score__text')[0].get_text().strip()
    except Exception:
        return None