#coding=utf-8
import serial

ser = serial.Serial('/dev/ttyUSB0', 9600,timeout=1);

def send_text(text):
    while 1 :
        conut=ser.inWaiting
        if conut !=0 :
            ser.write(text.encode("utf-8"))
            reply = ser.readline()
            ser.flushInput()
            reply = reply.decode("utf-8")
            if reply == text :
                print('sent:'+text)
                return ('1')

def receive_text():
    while 1 :
        count=ser.inWaiting
        if count !=0 :
            text = ser.readline()
            ser.flushInput()
            if text :
                reply = text
                ser.write(reply)
                text=text.decode("utf-8")
                print('receive:'+text)
                return (text)
