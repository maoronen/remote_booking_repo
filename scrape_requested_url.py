import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import argparse_scraping as arg_scr

url = "https://www.booking.com"


def url_for_parsing(destination, checkin, checkout, adults, children, rooms):
    """The function receive the configuration parameters and modified the booking url accordingly """
    # Initialize webdriver and put the path where download the driver
    driver = webdriver.Chrome(ChromeDriverManager().install())

    # Launch Chrome and pass the url
    driver.get(url)

    search = driver.find_element_by_id("ss")
    search.send_keys(destination)
    search.send_keys(Keys.RETURN)
    destination_url = driver.current_url

    # url manipulation in order to insert the requested date.

    # first step: inserting checking_monthday to the url
    destination_url = destination_url.split("checkin_month=&")
    first_url = destination_url[0] + "checkin_month=&checkin_monthday=&"
    second_url = destination_url[1].split("checkout_month=&")
    second_url = second_url[0] + "checkout_month=&checkout_monthday=&" + second_url[1]

    destination_url = first_url + second_url

    # second, inserting the days, month, year, adults, children and rooms to the url
    filter_dict = {r"checkin_monthday=": f"checkin_monthday={checkin.day}",
                   r"checkout_monthday=": f"checkout_monthday={checkout.day}",
                   r"checkin_month=": f"checkin_month={checkin.month}",
                   r"checkout_month=": f"checkout_month={checkout.month}",
                   r"checkin_year=": f"checkin_year={checkin.year}",
                   r"checkout_year=": f"checkout_year={checkout.year}",
                   r"rooms=\d+": f"rooms={rooms}",
                   r"adults=\d+": f"adults={adults}",
                   r"children=\d+": f"children={children}"}

    for key, val in filter_dict.items():
        modified_url = re.sub(key, val, destination_url)
        destination_url = modified_url

    return modified_url


def requested_url():
    """returns a booking url according to the user configuration input"""
    args = arg_scr.args_parse()
    requested_url = url_for_parsing(args.destination, args.checkin, args.checkout, args.adults, args.children, args.rooms)
    return requested_url
