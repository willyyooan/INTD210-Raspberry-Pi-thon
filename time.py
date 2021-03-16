from sense_hat import SenseHat
from time import sleep
import time

sense = SenseHat()

g = (0, 255, 0)
r = (255, 0, 0)
x = (0, 0, 0)

s = 8

timer = []
for i in range(64):
    if i < s:
        timer.append(g)
    else:
        timer.append(x)

sense.set_pixels(timer)

for i in range(0, s):
  sleep(5)
  timer[i] = r
  sense.set_pixels(timer)
