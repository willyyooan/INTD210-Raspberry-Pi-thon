from sense_hat import SenseHat
from time import sleep
sh = SenseHat()

# timesPressed = 0
# 
# while True:
#     for e in sh.stick.get_events():
#         if e.action == "pressed" and e.direction == "middle":
#             timesPressed = timesPressed+1
#             print(timesPressed)
#             
#     if timesPressed == 3:
#         print("yes")
#     elif timesPressed == 6:
#         print("maybe")
#     elif timesPressed == 9:
#         print("win!")

btnSeq = []
while True:
    for e in sh.stick.get_events():
        if e.action == "pressed":
            i = e.direction
            btnSeq.append(i)
            
    if btnSeq == ['up', 'up', 'down', 'down', 'left', 'right', 'left', 'right']:
        print("yes")

        

