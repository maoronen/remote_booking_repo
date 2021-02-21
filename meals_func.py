

def retrieve_meals(item):
    try:
        return item.select('.add-red-tag__amount')[0].get_text().strip()
    except Exception:
        return None