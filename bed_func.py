
def retrieve_bed_type(item):
    try:
        return item.select('.c-beds-configuration')[0].get_text().strip()
    except Exception:
        return None