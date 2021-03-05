from sense_hat import SenseHat
import time

sense = SenseHat()

sense.clear()

g = [0, 255, 0]
r = [0, 0,0]
o = [255, 180, 0]

Win = [
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g
]

Nothing = [
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r
]

upsideDown = [
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o
]


while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration ["x"]
    y = acceleration ["y"]
    z = acceleration ["z"]
    
    x=round(x,0)
    y=round(y,0)
    z=round(z,0)
    
    if x == -1:
        sense.set_pixels(Win)
        print("left")
        time.sleep(1)
        
    elif y == 0:
        sense.set_pixels(Nothing)
        print("nothing")
        time.sleep(1)
        
    elif z == -1:
        print("upsidedown")
        sense.set_pixels(upsideDown)
        time.sleep(1)
