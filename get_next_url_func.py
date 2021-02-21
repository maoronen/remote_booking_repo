import requests
from bs4 import BeautifulSoup

def get_next_url(page_url, headers):
    next_url = None
    url = requests.get(page_url, headers=headers)
    soup = BeautifulSoup(url.content, "html.parser")
    c = soup.find('div', class_="bui-pagination")
    try:
        href_list = c.find_all('a', href=True)
        for i, link in enumerate(href_list):
            if "current" in str(link):
                next_url = href_list[i + 1]['href']
    except Exception:
        return None
    next_url = "https://www.booking.com" + next_url
    return next_url
