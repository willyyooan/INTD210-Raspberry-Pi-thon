from sense_hat import SenseHat
from time import sleep
sh = SenseHat()

# taskSeq = ['up', 'up', 'down', 'down', 'left', 'right', 'left', 'right']
# btnSeq = []

# while True:
#     for e in sh.stick.get_events():
#         if e.action == "pressed":
#             i = e.direction
#             btnSeq.append(i)
#             print(btnSeq)
#             if e.action == "pressed" and e.direction == "middle": #press middle to confirm. this will add "middle" to the btnSeq list
#                 btnSeq.pop() #gets rid of the "middle" that gets appended to the list. We don't need it.
#                 if btnSeq == taskSeq:
#                     taskDone()
#                     nextTask()
#                     del btnSeq[:] #resets list
#                 else:
#                     isGameLose = True
#                     taskFailed()
#                     del btnSeq[:] #resets list



