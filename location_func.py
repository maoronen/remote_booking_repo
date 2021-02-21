import logging_file as log_f
import conf as cfg

def retrieve_hotel_location(item):
    try:
        return item.select('.bui-link')[cfg.TEXT].get_text().split('\n')[cfg.NO_SPACE].strip()

    except Exception:
        log_f.logging.info("could not extract hotel's location")
        return None

