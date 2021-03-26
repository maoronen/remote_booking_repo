import argparse
from datetime import date, timedelta


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
    parser.add_argument('db_name', help="database name", type=str)
    parser.add_argument('destination', help='destination', type=str)
    parser.add_argument('checkin', help='date in ISO format', type=valid_date)
    parser.add_argument('checkout', help='date in ISO format', type=valid_date)
    parser.add_argument('--adults', help='number of adults', type=int, default=2)
    parser.add_argument('--children', help="number of children", default=0)
    parser.add_argument('--rooms', help='number of rooms', type=int, default=1)

    parser.add_argument('--host', help="mysql host", type=str, default="localhost")
    parser.add_argument('--user', help="mysql user", type=str, default="root")
    parser.add_argument('--password', help="mysql password", type=str, default="root")


    args = parser.parse_args()
    if args.checkin > args.checkout:
        args.checkout = args.checkin + timedelta(days=1)  # if checkout < checkin, calculate one night only
    return args