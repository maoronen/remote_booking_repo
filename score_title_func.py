import logging_file as log_f
import conf as cfg

def retrieve_score_title(item):
    try:
        return item.select('.bui-review-score__title')[cfg.TEXT].get_text().strip()
    except Exception:
        log_f.logger.info("could not extract hotel's score title")
        return None