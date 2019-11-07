#!/usr/bin/python
import sys
import Adafruit_DHT
import mysql.connector
import time

timestamp = time.time()

mydb = mysql.connector.connect(
    host="",
    user="",
    passwd="",
    database=""
)

mycursor = mydb.cursor()

sql = "INSERT INTO raspberrypi_temp (`date`, temp, humid, room) VALUES (%s, %s, %s, %s)"
humidity, temperature = Adafruit_DHT.read_retry(11, 4)
print(humidity, temperature)
val = (timestamp, temperature, humidity, "buero")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted")
