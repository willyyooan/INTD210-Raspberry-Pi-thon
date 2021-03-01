from sense_hat import SenseHat
from time import sleep
import random
sh = SenseHat()

sh.clear()

##COLOURS##
r = [255, 0, 0] #red
g = [0, 255, 0] #green
x = [0, 0, 0] #blank
w = [255, 255, 255]
B = [0, 0, 255] #Blue
O = [255, 180, 0] #Orange
Y = [255, 255, 0] #Yellow
						

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

flashScreen = [
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w
]

squareScreen = [
    x, x, x, x, x, x, x, x,
    x, w, w, w, w, w, w, x,
    x, w, x, x, x, x, w, x,
    x, w, x, x, x, x, w, x,
    x, w, x, x, x, x, w, x,
    x, w, x, x, x, x, w, x,
    x, w, w, w, w, w, w, x,
    x, x, x, x, x, x, x, x
]

triangleScreen = [
    x, x, x, x, x, x, x, x,
    x, x, x, x, x, x, x, x,
    x, x, x, w, w, x, x, x,
    x, x, w, x, x, w, x, x,
    x, w, x, x, x, x, w, x,
    w, x, x, x, x, x, x, w,
    w, w, w, w, w, w, w, w,
    x, x, x, x, x, x, x, x
]

circleScreen = [
    x, x, x, x, x, x, x, x,
    x, x, x, w, w, x, x, x,
    x, x, w, x, x, w, x, x,
    x, w, x, x, x, x, w, x,
    x, w, x, x, x, x, w, x,
    x, x, w, x, x, w, x, x,
    x, x, x, w, w, x, x, x,
    x, x, x, x, x, x, x, x,
]

blueScreen = [
    x, x, x, x, x, x, x, x,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B
]

twoSquareScreen = [
    x, x, x, x, x, x, x, x,
    w, w, w, w, x, x, x, x,
    w, x, x, w, x, x, x, x,
    w, x, x, w, x, x, x, x,
    w, w, w, w, w, w, w, w,
    x, x, x, x, w, x, x, w,
    x, x, x, x, w, x, x, w,
    x, x, x, x, w, w, w, w
]

yellowScreen = [
    x, x, x, x, x, x, x, x,
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, Y, Y, Y, Y, Y, Y, Y
]

orangeScreen = [
    x, x, x, x, x, x, x, x,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O
]

crossScreen = [
    x, x, x, x, x, x, x, x,
    x, x, x, w, w, x, x, x,
    x, x, x, w, w, x, x, x,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    x, x, x, w, w, x, x, x,
    x, x, x, w, w, x, x, x,
    x, x, x, w, w, x, x, x
]

twoLinesScreen = [
    x, x, x, x, x, x, x, x,
    x, x, x, x, x, x, x, x,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    x, x, x, x, x, x, x, x,
    x, x, x, x, x, x, x, x,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w
]

xScreen = [
    x, x, x, x, x, x, x, x,
    x, w, x, x, x, x, w, x,
    x, x, w, x, x, w, x, x,
    x, x, x, w, w, x, x, x,
    x, x, x, w, w, x, x, x,
    x, x, w, x, x, w, x, x,
    x, w, x, x, x, x, w, x,
    w, x, x, x, x, x, x, w
]

##VARIABLES AND BOOLEANS
isGameOn = False
isGameLose = False
isGameWin = False

qrtrSec = 0.25
halfSec = 0.5
fullSec = 1

##FUNCTIONS##

def nextTask():
    print("next task!")

def taskDone():
    print("task done!")
    sh.set_pixels(flashScreen)
    sleep(halfSec)
    sh.set_pixels(flashScreen)
    sleep(halfSec)
    nextTask()

def taskFailed():
    print("BOOM! You died :(")
    while isGameLose == True:
        isGameOn = False
        sh.set_pixels(loseScreen)



##GAME##

while True:
    if isGameOn == False:
        sh.set_pixels(flashScreen)
        #MVP 1: press the joystick to begin 
        #MVP 2: MQTT, the GUI will start the game
        for e in sh.stick.get_events():
            if e.action == "pressed" and e.direction == "middle":
                sh.clear()
                isGameOn = True
                break
            break
    elif isGameOn == True:
      break


taskArr = ["task_1", "task_2", "task_3", "task_4", "task_5"]#, "task_6", "task_7", "task_8", "task_9", "task_10"]
random.shuffle(taskArr)
print(taskArr[0:4])

if taskArr[0] == "task_1":
    while isGameOn == True:
        sh.set_pixels(triangleScreen)
        for e in sh.stick.get_events():
            if e.action == "pressed" and e.direction == "up":
                print("task done")
                print(taskArr[1])
            if e.action == "pressed" and e.direction != "up":
                print("task failed")
                isGameLose = True
                taskFailed()

elif taskArr[0] == "task_2":
    while isGameOn == True:
        sh.set_pixels(squareScreen)
        for e in sh.stick.get_events():
            if e.action == "pressed" and e.direction == "up":
                print("task done")
                print(taskArr[1])
            if e.action == "pressed" and e.direction != "up":
                print("task failed")
                isGameLose = True
                taskFailed()

elif taskArr[0] == "task_3":
    sh.set_pixels(circleScreen)
    while isGameOn == True:
        for e in sh.stick.get_events():
            if e.action == "pressed" and e.direction == "up":
                print("task done")
                print(taskArr[1])
            if e.action == "pressed" and e.direction != "up":
                print("task failed")
                isGameLose = True
                taskFailed()

elif taskArr[0] == "task_4":
    sh.set_pixels(blueScreen)
    while isGameOn == True:
        for e in sh.stick.get_events():
            if e.action == "pressed" and e.direction == "up":
                print("task done")
                print(taskArr[1])
            if e.action == "pressed" and e.direction != "up":
                print("task failed")
                isGameLose = True
                taskFailed()

elif taskArr[0] == "task_5":
    sh.set_pixels(twoSquareScreen)
    while isGameOn == True:
        for e in sh.stick.get_events():
            if e.action == "pressed" and e.direction == "up":
                print("task done")
                print(taskArr[1])
            if e.action == "pressed" and e.direction != "up":
                print("task failed")
                isGameLose = True
                taskFailed()

# elif taskArr[0] == "task_6":
#     sh.set_pixels(yellowScreen)
#     while isGameOn == True:
#         for e in sh.stick.get_events():
#             if e.action == "pressed" and "up":
#                 print("task done, moving on")

# elif taskArr[0] == "task_7":
#     sh.set_pixels(orangeScreen)
#     while isGameOn == True:
#         for e in sh.stick.get_events():
#             if e.action == "pressed" and "up":
#                 print("task done, moving on")

# elif taskArr[0] == "task_8":
#     sh.set_pixels(crossScreen)
#     while isGameOn == True:
#         for e in sh.stick.get_events():
#             if e.action == "pressed" and "up":
#                 print("task done, moving on")

# elif taskArr[0] == "task_9":
#     sh.set_pixels(twoLinesScreen)
#     while isGameOn == True:
#         for e in sh.stick.get_events():
#             if e.action == "pressed" and "up":
#                 print("task done, moving on")

# elif taskArr[0] == "task_10":
#     sh.set_pixels(xScreen)
#     while isGameOn == True:
#         for e in sh.stick.get_events():
#             if e.action == "pressed" and "up":
#                 print("task done, moving on")


print("out of loop")   