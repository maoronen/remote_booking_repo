import mysql.connector

def db_tables(host, user, password, db_name):
  mydb = mysql.connector.connect(
    host=host,
    user=user,
    password=password
  )

  cur = mydb.cursor()
  cur.execute('%s' %db_name)
  cur.execute("USE %s" %db_name)

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


db_tables("localhost", "root", "root", "hi")