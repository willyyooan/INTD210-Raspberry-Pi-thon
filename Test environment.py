# from sense_hat import SenseHat
# from time import sleep
from guizero import App, Text, PushButton, Window
# sh = SenseHat()

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

appW = 750 #width of the window
appH = 500 #height of the window

sWin = App(title="You Win!", height=appH, width=appW, bg=(0, 255, 0))
# sWin.hide() #hides this window until player clicks on start button
Text(sWin, text="", size=50) #spacer
Text(sWin, text="BOMB DEFUSED", size=50)
Text(sWin, text="Great work!", size=25)
Text(sWin, text="", size=25) #spacer
menuBtn = PushButton(sWin, text="Main Menu")
menuBtn.bg = "#e0e0e0" #light grey

sWin.display()
