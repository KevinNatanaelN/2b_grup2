import serial

def getData():
    ser = serial.Serial('COM3',9600)
    print(ser.readline().decode("utf-8").strip('\n').strip('\r'))

getData()

import serial
import csv

def writeCsv():
    ser = serial.Serial('COM3',9600)
    with open('speedometer.csv', mode='w') as csv_file:
        fieldnames = ['speed']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
        writer.writeheader()
        while (1):
            data = ser.readline().decode("utf-8").strip('\n').strip('\r')
            writer.writerow({'speed': data})
            
writeCsv()
