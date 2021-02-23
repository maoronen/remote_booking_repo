import conf as cfg
from bs4 import BeautifulSoup
import requests


def block_setup(link):
    link = requests.get(link, headers=cfg.HEADERS)
    soup = BeautifulSoup(link.content, "html.parser")
    block_list = soup.select(cfg.HOTEL_BLOCK)
    return block_list[0]