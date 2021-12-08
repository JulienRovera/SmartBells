
from machine import I2C, Pin, UART
from math import sqrt, atan2, pi, copysign, sin, cos
from mpu9250 import MPU9250
from time import sleep
from generator import csv_help
import os

# addresses 
MPU = 0x68
id = 0
sda = Pin(20)
scl = Pin(21)
rx = Pin(17)
tx = Pin(16)
baudrate = 9600
uart = UART(id = 0, baudrate = baudrate, tx = tx, rx = rx, txbuf = 100)
# create the I2C
i2c = I2C(id=id, scl=scl, sda=sda)

# Scan the bus
print(i2c.scan())
m = MPU9250(i2c)

# Calibration and bias offset
m.ak8963.calibrate(count=50)
pitch_bias = 0.0
roll_bias = 0.0

# For low pass filtering
filtered_x_value = 0.0 
filtered_y_value = 0.0

# declare csv for writing to csv file
csv = csv_help()

# declination = 40

def degrees_to_heading(degrees):
    heading = ""
    if (degrees > 337) or (degrees >= 0 and degrees <= 22):
            heading = 'N'
    if degrees >22 and degrees <= 67:
        heading = "NE"
    if degrees >67 and degrees <= 112:
        heading = "E"
    if degrees >112 and degrees <= 157:
        heading = "SE"
    if degrees > 157 and degrees <= 202:
        heading = "S"
    if degrees > 202 and degrees <= 247:
        heading = "SW"
    if degrees > 247 and degrees <= 292:
        heading = "W"
    if degrees > 292 and degrees <= 337:
        heading = "NW"
    return heading

def get_reading()->float:
    ''' Returns the readings from the sensor '''
    global filtered_y_value, filtered_x_value
    x = m.acceleration[0] 
    y = m.acceleration[1]
    z = m.acceleration[2]
    
    accel_vals = [x, y, z]

    # Pitch and Roll in Radians
    roll_rad = atan2(-x, sqrt((z*z)+(y*y)))
    pitch_rad = atan2(z, copysign(y,y)*sqrt((0.01*x*x)+(y*y)))

    # Pitch and Roll in Degrees
    pitch = pitch_rad*180/pi
    roll = roll_rad*180/pi

    # Get soft_iron adjusted values from the magnetometer
    mag_x, mag_y, magz = m.magnetic

    filtered_x_value = low_pass_filter(mag_x, filtered_x_value)
    filtered_y_value = low_pass_filter(mag_y, filtered_y_value)

    mag_vals = [filtered_x_value, filtered_y_value, magz]
    az =  90 - atan2(filtered_y_value, filtered_x_value) * 180 / pi

    # make sure the angle is always positive, and between 0 and 360 degrees
    if az < 0:
        az += 360
        
    # Adjust for original bias
    pitch -= pitch_bias
    roll -= roll_bias

    heading = degrees_to_heading(az)
    
    gyro_vals = m.gyro

    return x, y, z, pitch, roll, az, heading, accel_vals, gyro_vals , mag_vals

def low_pass_filter(raw_value:float, remembered_value):
    ''' Only applied 20% of the raw value to the filtered value '''
    
    # global filtered_value
    alpha = 0.8
    filtered = 0
    filtered = (alpha * remembered_value) + (1.0 - alpha) * raw_value
    return filtered

def show():
    ''' Shows the Pitch, Rool and heading '''
    x, y, z, pitch, roll, az, heading_value, accel_vals, gyro_vals, mag_vals = get_reading()
    #csv.writeToCSV(pitch, roll, az, heading_value, accel_vals, gyro_vals, mag_vals)
   
    #print(values)
    f_x_acc = "{:.7f}".format(accel_vals[0])
    f_y_acc = "{:.7f}".format(accel_vals[1])
    f_z_acc = "{:.7f}".format(accel_vals[2])
    f_x_rot = "{:.7f}".format(gyro_vals[0])
    f_y_rot = "{:.7f}".format(gyro_vals[1])
    f_z_rot = "{:.7f}".format(gyro_vals[2])
    f_x_mag = "{:.7f}".format(mag_vals[0])
    f_y_mag = "{:.7f}".format(mag_vals[1])
    f_z_mag = "{:.7f}".format(mag_vals[2])
    values = f_x_rot + "," + f_y_rot + "," + f_z_rot + "," + f_x_acc + "," + f_y_acc + "," + f_z_acc + "," + f_x_mag + "," + f_y_mag + "," + f_z_mag + "\n"
    #print(uart.write(values))
    print(values)

# reset orientation to zero
x,y,z, pitch_bias, roll_bias, az, az_raw, accel_vals, gyro_vals, mag_vals = get_reading()


# main loop
i = 0
while i <= 100:
    show()
    i += 1
    print(i)
    
    
    
