import logging_file as log_f
import conf as cfg

def retrieve_reviews_num(item):
    try:
        return int(item.select(cfg.TOTAL_REVIEWS)[cfg.TEXT].get_text().strip().split()[0].replace(",", ""))
    except Exception:
        log_f.logger.info("could not extract hotel's reviews number")
        return None

