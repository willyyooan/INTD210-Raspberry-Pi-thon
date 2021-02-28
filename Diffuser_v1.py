from sense_hat import SenseHat
from time import sleep
sh = SenseHat()

sh.clear()
sh.low_light(True)

##COLOURS##
r = [255, 0, 0] #red
g = [0, 255, 0] #green
x = [0, 0, 0] #blank
w = [255, 255, 255]

##SCREENS##
loseScreen = [
    r, r, r, r, r, r, r ,r,
    r, r, r, r, r, r, r ,r,
    r, r, r, r, r, r, r ,r,
    r, r, r, r, r, r, r ,r,
    r, r, r, r, r, r, r ,r,
    r, r, r, r, r, r, r ,r,
    r, r, r, r, r, r, r ,r,
    r, r, r, r, r, r, r ,r
]

winScreen = [
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g
]

