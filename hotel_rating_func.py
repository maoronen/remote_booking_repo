import logging_file as log_f
import conf as cfg


def retrieve_hotel_rating(item):
    try:
        return item.select('.sr-hotel__name')[cfg.TEXT].get_text().split('\n')[cfg.NO_SPACE]

    except Exception:
        log_f.logging.info("could not extract hotel's rating")
        return None

