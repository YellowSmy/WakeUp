import serial
import time

def _vive():
    ser = serial.Serial('COM9',9600)
    time.sleep(2)
    ser.write(b'1')
    time.sleep(2)
    ser.close()        

_vive();

