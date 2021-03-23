import conf as cfg
import logging_file as log_f


def retrieve_hotel_name(item):
    try:
        return item.select(cfg.HOTEL_NAME_SCRAPER)[cfg.TEXT].get_text().split('\n')[1]
    except IndexError:
        log_f.logging.info("could not extract hotel's rating")
        return None


def retrieve_hotel_rating(item):
    try:
        return float(item.select(cfg.HOTEL_RATING_SCRAPER)[cfg.TEXT].get_text().strip())
    except IndexError:
        log_f.logging.info("could not extract hotel's rating")
        return None


def retrieve_score_title(item):
    try:
        return item.select(cfg.SCORE_TITLE_SCRAPER)[cfg.TEXT].get_text().strip()
    except IndexError:
        log_f.logger.info("could not extract hotel's score title")
        return None


def retrieve_reviews_num(item):
    try:
        return int(item.select(cfg.TOTAL_REVIEWS_SCRAPER)[cfg.TEXT].get_text().strip().split()[0].replace(",", ""))
    except IndexError:
        log_f.logger.info("could not extract hotel's reviews number")
        return None


def retrieve_hotel_location(item):
    try:
        return item.select('.bui-link')[cfg.TEXT].get_text().split('\n')[cfg.NO_SPACE].strip()
    except Exception:
        log_f.logging.info("could not extract hotel's location")
        return None


def retrieve_meals(item):
    try:
        return item.select(cfg.MEALS_SCRAPER)[cfg.TEXT].get_text().strip()
    except Exception:
        return None


def retrieve_price(item):
    try:
        price = item.select(cfg.PRICE_SCRAPER)[cfg.TEXT].get_text().split('\n')[cfg.NO_SPACE].split()[
            cfg.DIGIT]
        price = int(price.replace(",", ""))
    except Exception:
        log_f.logger.info("could not extract hotel's price")
        return None
    return price



def retrieve_room_type(item):
    try:
        container = item.find('div', class_='room_link')
        for room in container.find_all('strong'):
            return room.text
    except Exception:
        log_f.logger.info("could not extract hotel's room type")
        return None



def retrieve_bed_type(item):
    try:
        return item.select('.c-beds-configuration')[0].get_text().strip()
    except Exception:
        return None


def retrieve_image_url(item):
    try:
        return item.select(cfg.HOTEL_IMAGE_SCRAPER)[cfg.TEXT]['data-highres']
    except Exception:
        log_f.logging.info("could not extract hotel's image url")
        return None



