
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import argparse_scraping as arg_scr
from pyvirtualdisplay import Display
from selenium.webdriver.chrome.options import Options #added
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = "https://www.booking.com"


def url_for_parsing(destination, checkin, checkout, adults, children, rooms):
    """The function receive the configuration parameters and modified the booking url accordingly """
    # Initialize webdriver and put the path where download the driver
    
    
    
    display = Display(visible=0, size=(800, 800)) #these 3 lines were Asi's suggestion instead of the line above that is now commented out
    display.start()
    

    chrome_options = webdriver.ChromeOptions()
    #chrome_options = Options()
    #chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'en-gb'})
    
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument("--user-agent=Mozilla...")
    #chrome_options.add_argument("--window-size=1920,1080")
    #chrome_options.add_argument('--disable-dev-shm-usage')
    
    #driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
      
    
    
    
    driver = webdriver.Chrome("/home/ubuntu/remote_booking_repo/chromedriver", chrome_options=chrome_options)
    print('#######', driver.get_window_size(), flush=True)
    # Launch Chrome and pass the url
    driver.get(url)
    search = driver.find_element_by_id("ss")
    search.send_keys(destination)
    
    search.send_keys(Keys.RETURN)
    #time.sleep(10)
    destination_url = driver.current_url
    #destination_url = wait.until(EC.text_to_be_present_in_element("checkin"), driver.current_url)
    #destination_url = destination_url + "?label=gen173nr-1FCAEoggI46AdIM1gEaGqIAQGYATG4ARfIAQzYAQHoAQH4AQKIAgGoAgO4Ao6Ym4UGwAIB0gIkMTRiNGU4MDktZTMwZC00Yjk1LTg4YmItZTVhMDE4NWU2MDBh2AIF4AIB&sid=82c0207e68a5a09fcc427ed70f807e58&sb=1&sb_lp=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.html%3Flabel%3Dgen173nr-1FCAEoggI46AdIM1gEaGqIAQGYATG4ARfIAQzYAQHoAQH4AQKIAgGoAgO4Ao6Ym4UGwAIB0gIkMTRiNGU4MDktZTMwZC00Yjk1LTg4YmItZTVhMDE4NWU2MDBh2AIF4AIB%3Bsid%3D82c0207e68a5a09fcc427ed70f807e58%3Bsb_price_type%3Dtotal%26%3B&ss=asdod&is_ski_area=0&checkin_year=&checkin_month=&checkout_year=&checkout_month=&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1"
    

    # url manipulation in order to insert the requested date.

    # first step: inserting checking_monthday to the url
    destination_url = destination_url.split("checkin_month=&")
    print("*******************************:",destination_url)
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
    display.stop()
    return modified_url


def requested_url():
    """returns a booking url according to the user configuration input"""
    args = arg_scr.args_parse()
    requested_url = url_for_parsing(args.destination, args.checkin, args.checkout, args.adults, args.children, args.rooms)
    return requested_url
