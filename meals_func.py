import conf as cfg

def retrieve_meals(item):
    try:
        return item.select('.add-red-tag__amount')[cfg.TEXT].get_text().strip()
    except Exception:
        return None