import mysql.connector
from mysql.connector import Error
import sys
import logging_file as log_f
import argparse

def args_parse():
    parser = argparse.ArgumentParser(description='hotels filter')
    parser.add_argument('db_name', help='destination', type=str)
    args = parser.parse_args()
    return args

args = args_parse()
DB_NAME = f"{args.db_name}"



try:
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="4817")
    log_f.logger.info("Connected to MySQL")

except Error as e:
    print("Error while connecting to MySQL", e)
    sys.exit(1)


try:
    cur = mydb.cursor()
    cur.execute(f"CREATE DATABASE {DB_NAME}")
    print("Database {} created successfully.".format(DB_NAME))
    log_f.logger.info("Created")

except Error as e:
    log_f.logger.error("Failed creating database: {}, \nPlease run again with different name".format(e))
    sys.exit(1)

try:
    cur.execute(f"USE {DB_NAME}")
except Error as e:
    log_f.logger.error(f"Failed using database {DB_NAME}: {format(e)}")

try:
    cur.execute("""CREATE TABLE IF NOT EXISTS hotels (id INT NOT NULL PRIMARY KEY,
                    name VARCHAR(255),
                    rating FLOAT,
                    reviews INT,
                    price FLOAT);""")
    log_f.logger.info("hotels table created successfully.")
except Error as e:
    log_f.logger.error('Failed creating hotels table')

try:
    cur.execute("""CREATE TABLE IF NOT EXISTS facilities (hotel_id INT NOT NULL PRIMARY KEY,
                    room_type VARCHAR(255),
                    bed_type VARCHAR(255),
                    meals VARCHAR(255),
                    FOREIGN KEY (hotel_id) REFERENCES hotels (id));""")
    log_f.logger.info("facilities table created successfully.")

except Error as e:
    log_f.logger.error('Failed creating facilities table')

try:
    cur.execute("""CREATE TABLE IF NOT EXISTS locations (hotel_id INT NOT NULL PRIMARY KEY,
                    location VARCHAR(255),
                    FOREIGN KEY (hotel_id) REFERENCES hotels (id));""")
    log_f.logger.info("locations table created successfully.")

except Error as e:
    log_f.logger.error('Failed creating locations table')

try:
    cur.execute("""CREATE TABLE IF NOT EXISTS hotel_image (hotel_id INT NOT NULL PRIMARY KEY,
                      image_url VARCHAR(255),
                      FOREIGN KEY (hotel_id) REFERENCES hotels (id));""")
    log_f.logger.info("hotel_image table created successfully.")

except Error as e:
    log_f.logger.error('Failed creating hotel_image table')

