from sense_hat import SenseHat
import time

sense = SenseHat()
 
sense.clear()

g = (0, 255, 0)

win = [
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g
]
 
while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration["x"]
    y = acceleration["y"]
    z = acceleration["z"]
    
    x = abs(x)
    y = abs(y)
    z = abs(z)
     
    if x > 1.5 or y > 1.5 or z > 1.5:
        sense.set_pixels(win)
        print("shake")
        time.sleep(1)
        sense.clear()