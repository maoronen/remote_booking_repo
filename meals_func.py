import conf as cfg

def retrieve_meals(item):
    try:
        return item.select(cfg.MEALS)[cfg.TEXT].get_text().strip()
    except Exception:
        return None