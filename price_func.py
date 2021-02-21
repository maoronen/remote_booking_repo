import logging_file as log_f
import conf as cfg


def retrieve_price(item):
    try:
        price = item.select(cfg.PRICE)[cfg.TEXT].get_text().split('\n')[cfg.NO_SPACE].split()[
            cfg.DIGIT]
        price = int(price.replace(",", ""))
    except Exception:
        log_f.logger.info("could not extract hotel's price")
        return None

    return price
