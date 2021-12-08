
import random
import time

class csv_help():
    def __init__(self) -> None:
        
        self.times = 0
        self.pitch = 0
        self.roll = 0
        self.yaw = 0
        self.cardinal = ''
        self.accel_vals = []
        self.gyro_vals = []
        self.mag_vals = []

        header = 'reading,pitch,roll,yaw (compass),cardinal direction,accel x,accel y,accel z,gyro x,gyro y,gyro z,mag x, mag y, mag z'

        #Write headers
        with open('data.csv', 'w') as csv_file:
            csv_file.write(header + '\n')

    def writeToCSV(self, new_pitch, new_roll, new_yaw, new_cardinal, new_accel_vals, new_gyro_vals, new_mag_vals):
        with open('data.csv', 'a') as csv_file:

            self.times += 1
            self.pitch = new_pitch
            self.roll = new_roll
            self.yaw = new_yaw
            self.cardinal = new_cardinal
            self.accel_vals = new_accel_vals
            self.gyro_vals = new_gyro_vals
            self.mag_vals = new_mag_vals

            csv_file.write(str(self.times) + ',' + str(self.pitch)+ ',' + str(self.roll) + ',' + str(self.yaw) + ',' + self.cardinal
                           + ',' + str(self.accel_vals[0]) + ',' + str(self.accel_vals[1]) + ',' + str(self.accel_vals[2])
                           + ',' + str(self.gyro_vals[0]) + ',' + str(self.gyro_vals[1]) + ',' + str(self.gyro_vals[2])
                           + ',' + str(self.mag_vals[0]) + ',' + str(self.mag_vals[1]) + ',' + str(self.mag_vals[2]) + '\n')
            return
