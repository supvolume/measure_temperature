"""
Read the sensor temperature and write on the file
"""

# Import
from datetime import datetime
import csv
import time
import sys

# Location variables
# To use this code, insert the sensor and file path here
sensor_location = ""
file_location = ""

while True:
    # Get time
    date_time = datetime.now()

    # File name
    record_file_lo = file_location\
                     + str(date_time.date())\
                     +".txt"
    
    # Open file
    temp_record = open(record_file_lo, "a+")

    # Get temp
    read_sensor = open(sensor_location, "r")

    # Change the reading temp to writable form
    lines = str(read_sensor.readlines())
    temp = lines[76:78]+"."+lines[78:81]

    # Write temp
    temp_record.write(str(date_time.date()) \
                      +","\
                      +str(date_time.time()) \
                      +","\
                      + temp+"\n")
    print(date_time.time(), temp)
    temp_record.close()

    try:
        time.sleep(600)
    except KeyboardInterrupt:
        print("stop")
        sys.exit()
