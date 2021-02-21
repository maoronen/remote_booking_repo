
def retrieve_score_title(item):
    try:
        return item.select('.bui-review-score__title')[0].get_text().strip()
    except Exception:
        return None