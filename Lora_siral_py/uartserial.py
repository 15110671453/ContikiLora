#安装serial easygui for python3
import serial
import sys
import os
import time
import re
 
def wait_for_cmd_OK():
    while True:
        line = ser.readline()
        try:
            print(line.decode('utf-8'),end='')
        except:
            pass
        if ( re.search(b'OK',line)):
            break

def sendAT_Cmd(serInstance,atCmdStr):
    serInstance.write(atCmdStr.encode('utf-8'))
    wait_for_cmd_OK()

#选择串口号及波特率，因为我是在ubuntu下使用，故串口号为/dev/ttyACM0
ser = serial.Serial("/dev/ttyACM0",9600,timeout=30) 
sendAT_Cmd(ser,'AT+CFUN=1\r')
