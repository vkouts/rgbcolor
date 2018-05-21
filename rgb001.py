import random
from time import sleep
import serial

ser = serial.Serial('COM3', 9600, write_timeout=3)
TIMEPERIOD = 5


sleep(2)

def random_color():
    if random.choice([True, False]):
        return random.choice([0, 254])
    else:
        return random.randrange(0,254)

if __name__ == '__main__':
    print('Init')
    print(ser.name)

    while True:
        red = random_color()
        green = random_color()
        blue = random_color()

        out = '{} {} {}'.format(red, green, blue)

        ser.write(bytes(out, encoding='utf-8'))
        print("color = #%X%X%X" % (red, green, blue))
        #sleep(TIMEPERIOD)
        sleep(random.randrange(2,10))