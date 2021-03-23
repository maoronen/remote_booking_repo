# Scraping Booking.com
This repository contains various files regarding web-scraping Booking.com 
for a one week vacation in August in exotic Seychelles.

## Installation
The program operates on any OS and uses python 3.8.3
* Create virtual environment and run:
    pip install -r requirements.txt
* Run the booking script:
    Booking_scraper_main_code.py
 
## Usage
* The program scrapes data from booking.com website regarding the hotels that 
are available during the the specific dates in Seychelles. 
* The data is stored in a csv file and contain the hotel name, its rating, price,
 location, what meals are included, room details and a representative image of the listing.
 
 ## Content of the repository
 1. Booking_scraper_main_code.py - main code file 
 2. retrieve_func.py - a script containing all functions used to retrieve a specific detail
 3. get_urls_func.py - a script containing the functions that retrieve the urls of all hotels found suitable for the specific search
 4. conf.py - configuration file with constants used in the repository's files
 5. logging_file - a tracking file that follows the smooth and errorless progress of the scraping but also notifies errors and problems.
 6. test_Booking_scraper - a pytest test file for the main code.
 7. test_get_urls - a pytest test file for validating the functions that are in charge of retrieve all the necessary urls.
 8. test_retrieve_func - a pytest test for validating the functions in charge of scraping various data from Booking.comm
 9. requirements.txt - list of all necessary packages to install for proper usage.
 
## Disclaimer
Data fetched from booking is only for personal use, you are not
allowed to copy and paste content from Booking.com on to your own or third 
party pages (including social media pages such as Facebook, Twitter, Instagram etc.).

This applies to all types of content that can be found on Booking.com pages, 
including but not limited to hotel descriptions, reviews, hotel and room photos, 
hotel facility information, and prices.