import time
from sense_hat import SenseHat 

sh = SenseHat()


g = (0,255,0)
r = (255,0,0)

# sh.set_pixel(0, 0, g)
# sh.set_pixel(1, 0, g)
# sh.set_pixel(2, 0, g)
# sh.set_pixel(3, 0, g)
# sh.set_pixel(4, 0, g)
# sh.set_pixel(5, 0, g)
# sh.set_pixel(6, 0, g)
# sh.set_pixel(7, 0, g)

start = time.time()

while True:
    elapsed = round(time.time() - start)

    if elapsed == 10:
        second = elapsed
        print(str(second) + " second(s) has passed")
        sh.set_pixel(0, 0, r)
    
    if elapsed == 20:
        second = elapsed
        print(str(second) + " second(s) has passed")
        sh.set_pixel(1, 0, r)
    
    if elapsed == 30:
        second = elapsed
        print(str(second) + " second(s) has passed")
        sh.set_pixel(2, 0, r)
    
    if elapsed == 40:
        second = elapsed
        print(str(second) + " second(s) has passed")
        sh.set_pixel(3, 0, r)
    
    if elapsed == 50:
        second = elapsed
        print(str(second) + " second(s) has passed")
        sh.set_pixel(4, 0, r)
    
    if elapsed == 60:
        second = elapsed
        print(str(second) + " second(s) has passed")
        sh.set_pixel(5, 0, r)
    
    if elapsed == 70:
        second = elapsed
        print(str(second) + " second(s) has passed")
        sh.set_pixel(6, 0, r)
    
    if elapsed == 80:
        second = elapsed
        print(str(second) + " second(s) has passed. Time's up!")
        sh.set_pixel(7, 0, r)
        break
    

print("yes")
