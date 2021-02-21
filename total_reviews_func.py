import logging_file as log_f
import conf as cfg

def retrieve_reviews_num(item):
    try:
        return item.select('.bui-review-score__text')[cfg.TEXT].get_text().strip()
    except Exception:
        log_f.logger.info("could not extract hotel's reviews number")
        return None

