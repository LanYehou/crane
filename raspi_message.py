import serial
#coding=utf-8
ser = serial.Serial('/dev/ttyUSB0', 9600,timeout=1);

def send_text(text):
    while 1 :
        ser.write(text.encode("utf-8"))
        reply = ser.read(32)
        reply = reply.decode("utf-8")
        if reply == text :
            print(text)
            return ('1')

def receive_text():
    while 1 :
        text = ser.read(32)
        if text :
            reply = text
            ser.write(reply.encode("utf-8"))
            text=text.decode("utf-8")
            print(text)
            return (text)
