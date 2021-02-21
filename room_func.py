import logging_file as log_f


def retrieve_room_type(item):
    try:
        container = item.find('div', class_='room_link')
        for room in container.find_all('strong'):
            return room.text
    except Exception:
        log_f.logger.info("could not extract hotel's room type")
        return None