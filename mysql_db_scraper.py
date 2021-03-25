import mysql.connector
from mysql.connector import Error
import sys
import logging_file as log_f



def create_db(host, user, password, db_name):
    try:
        mydb = mysql.connector.connect(
          host=host,
          user=user,
          password=password)
        log_f.logger.info("Connected to MySQL")

    except Error as e:
        log_f.logger.critical("Error while connecting to MySQL", e)
        #sys.exit(1)


    try:
        cur = mydb.cursor()
        cur.execute(f"CREATE DATABASE {db_name}")
        print("Database {} created successfully.".format(db_name))
        log_f.logger.info("Created")

    except Exception as e:
        log_f.logger.error("Failed creating database: {}, \nOnly a CSV file will be created."
                           " for database creation please run again with different database name".format(e))

    try:
        cur.execute(f"USE {db_name}")
    except Exception as e:
        log_f.logger.error(f"Failed using database {db_name}: {format(e)}")

    try:
        cur.execute("""CREATE TABLE IF NOT EXISTS hotels (id INT NOT NULL PRIMARY KEY,
                        name VARCHAR(255),
                        rating FLOAT,
                        reviews INT,
                        price FLOAT);""")
        log_f.logger.info("hotels table created successfully.")
    except Exception as e:
        log_f.logger.error('Failed creating hotels table')

    try:
        cur.execute("""CREATE TABLE IF NOT EXISTS facilities (hotel_id INT NOT NULL PRIMARY KEY,
                        room_type VARCHAR(255),
                        bed_type VARCHAR(255),
                        meals VARCHAR(255),
                        FOREIGN KEY (hotel_id) REFERENCES hotels (id));""")
        log_f.logger.info("facilities table created successfully.")

    except Exception as e:
        log_f.logger.error('Failed creating facilities table')

    try:
        cur.execute("""CREATE TABLE IF NOT EXISTS locations (hotel_id INT NOT NULL PRIMARY KEY,
                        location VARCHAR(255),
                        FOREIGN KEY (hotel_id) REFERENCES hotels (id));""")
        log_f.logger.info("locations table created successfully.")

    except Exception as e:
        log_f.logger.error('Failed creating locations table')

    try:
        cur.execute("""CREATE TABLE IF NOT EXISTS hotel_image (hotel_id INT NOT NULL PRIMARY KEY,
                          image_url VARCHAR(255),
                          FOREIGN KEY (hotel_id) REFERENCES hotels (id));""")
        log_f.logger.info("hotel_image table created successfully.")

    except Exception as e:
        log_f.logger.error('Failed creating hotel_image table')


