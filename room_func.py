
def retrieve_room_type(item):
    try:
        container = item.find('div', class_='room_link')
        for room in container.find_all('strong'):
            return room.text
    except Exception:
        return None