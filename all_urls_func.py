import get_next_url_func
import logging_file as log_f

def all_urls(first_url, headers):
    """gets the first link and extract the next links that are apart of the hotels search"""
    url_list = [first_url]
    next_url = first_url
    while True:
        next_page_url = get_next_url_func.get_next_url(next_url, headers)
        if next_page_url is not None:
            next_url = next_page_url
            url_list.append(next_page_url)
        else:
            break
    if len(url_list) < 15:
        log_f.logger.error('could not extract all urls!')
    else:
        log_f.logger.info('successfully extract all urls!')
    return url_list
