import logging_file as log_f
import conf as cfg


def retrieve_hotel_rating(item):
    try:
        return float(item.select('.bui-review-score__badge')[cfg.TEXT].get_text().strip())
    except Exception:
        log_f.logging.info("could not extract hotel's rating")
        return None
