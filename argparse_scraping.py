import argparse
from datetime import date, timedelta
import json
import sys
import logging_file as log_f

with open('conf.json') as config_file:
    constants = json.load(config_file)

def valid_date(d):
    try:
        check_date = date.fromisoformat(d)
        if check_date >= date.today():
            return check_date
        else:
            raise ValueError
    except ValueError:
        msg = f"Not a valid date: {d}"
        raise argparse.ArgumentTypeError(msg)


def args_parse():
    parser = argparse.ArgumentParser(description='hotels filter')
    parser.add_argument('db_name', help="database name of the current search result", type=str)
    parser.add_argument('destination', help='Trip destination', type=str)
    parser.add_argument('checkin', help='check-in date at the hotel in ISO format (yyyy-mm-dd)', type=valid_date)
    parser.add_argument('checkout', help='check-out date at the hotel in ISO format (yyyy-mm-dd)', type=valid_date)
    parser.add_argument('--adults', help='number of adults in the reservation', type=int, default=2)
    parser.add_argument('--children', help="number of children in the reservation", default=0)
    parser.add_argument('--rooms', help='number of rooms required (Should not be higher than number of adults!)', type=int, default=1)

    parser.add_argument('--host', help="mysql host", type=str, default=constants["SQL"]["HOST"])
    parser.add_argument('--user', help="mysql user", type=str, default=constants["SQL"]["USER"])
    parser.add_argument('--password', help="mysql password", type=str, default=constants["SQL"]["PASSWORD"])


    args = parser.parse_args()
    if args.checkin > args.checkout:
        args.checkout = args.checkin + timedelta(days=1)  # if checkout < checkin, calculate one night only

    if args.rooms > args.adults:
        log_f.logger.critical('Number of rooms can not be higher than number of adults!')
        sys.exit(1)

    return args