import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="4817"
)

cur = mydb.cursor()
cur.execute("CREATE DATABASE booking_db")
cur.execute("USE booking_db")

cur.execute("""CREATE TABLE hotels (id INT PRIMARY KEY,
                  name VARCHAR(255),
                  rating FLOAT,
                  reviews INT,
                  price FLOAT);""")

cur.execute("""CREATE TABLE facilities (hotel_id INT PRIMARY KEY,
                  room_type VARCHAR(255),
                  bed_type VARCHAR(255),
                  meals VARCHAR(255),
                  FOREIGN KEY (hotel_id) REFERENCES hotels (id));""")

cur.execute("""CREATE TABLE locations (hotel_id INT PRIMARY KEY,
                  location VARCHAR(255),
                  FOREIGN KEY (hotel_id) REFERENCES hotels (id));""")

cur.execute("""CREATE TABLE hotel_image (hotel_id INT PRIMARY KEY,
                  image_url VARCHAR(255),
                  FOREIGN KEY (hotel_id) REFERENCES hotels (id));""")


