import conf as cfg
import logging_file as log_f

# 1
def retrieve_hotel_name(item):
    try:
        return item.select(cfg.HOTEL_NAME)[cfg.TEXT].get_text().split('\n')[1]
    except IndexError:
        log_f.logging.info("could not extract hotel's rating")
        return None

# 2
def retrieve_hotel_rating(item):
    try:
        return float(item.select(cfg.HOTEL_RATING)[cfg.TEXT].get_text().strip())
    except IndexError:
        log_f.logging.info("could not extract hotel's rating")
        return None

# 3
def retrieve_score_title(item):
    try:
        return item.select(cfg.SCORE_TITLE)[cfg.TEXT].get_text().strip()
    except IndexError:
        log_f.logger.info("could not extract hotel's score title")
        return None

# 4
def retrieve_reviews_num(item):
    try:
        return int(item.select(cfg.TOTAL_REVIEWS)[cfg.TEXT].get_text().strip().split()[0].replace(",", ""))
    except IndexError:
        log_f.logger.info("could not extract hotel's reviews number")
        return None

# 5
def retrieve_hotel_location(item):
    try:
        return item.select('.bui-link')[cfg.TEXT].get_text().split('\n')[cfg.NO_SPACE].strip()
    except Exception:
        log_f.logging.info("could not extract hotel's location")
        return None

# 6
def retrieve_meals(item):
    try:
        return item.select(cfg.MEALS)[cfg.TEXT].get_text().strip()
    except Exception:
        return None

# 7
def retrieve_price(item):
    try:
        price = item.select(cfg.PRICE)[cfg.TEXT].get_text().split('\n')[cfg.NO_SPACE].split()[
            cfg.DIGIT]
        price = int(price.replace(",", ""))
    except Exception:
        log_f.logger.info("could not extract hotel's price")
        return None
    return price


#8
def retrieve_room_type(item):
    try:
        container = item.find('div', class_='room_link')
        for room in container.find_all('strong'):
            return room.text
    except Exception:
        log_f.logger.info("could not extract hotel's room type")
        return None


# 9
def retrieve_bed_type(item):
    try:
        return item.select('.c-beds-configuration')[0].get_text().strip()
    except Exception:
        return None

# 10
def retrieve_image_url(item):
    try:
        return item.select(cfg.HOTEL_IMAGE)[cfg.TEXT]['data-highres']
    except Exception:
        log_f.logging.info("could not extract hotel's image url")
        return None



