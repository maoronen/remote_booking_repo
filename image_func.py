import logging_file as log_f
import conf as cfg


def retrieve_image_url(item):
    try:
        return item.select(cfg.HOTEL_IMAGE)[cfg.TEXT]['data-highres']
    except Exception:
        log_f.logging.info("could not extract hotel's image url")
        return None