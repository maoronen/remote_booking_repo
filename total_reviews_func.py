

def retrieve_reviews_num(item):
    try:
        return int(item.select('.bui-review-score__text')[0].get_text().strip().split()[0].replace(",", ""))
    except Exception:
        return None