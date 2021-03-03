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
global isGameOn
global isGameLose
global isGameWin

isGameOn = False
isGameLose = False
isGameWin = False

qrtrSec = 0.25
halfSec = 0.5
fullSec = 1

taskCount = 0

##FUNCTIONS##
def nextTask():
    sh.clear()
    random.shuffle(taskArr)
    print(taskArr[0])
    

def taskDone():
    global taskCount
    print("task done! next task")
    sh.set_pixels(flashScreen)
    sleep(0.5)
    sh.clear()
    sh.set_pixels(flashScreen)
    taskCount += 1
    sleep(0.5)
    

def taskFailed():
    global isGameLose
    isGameLose = True
    print("BOOM! You died :(")
    while isGameLose == True:
        global isGameOn
        isGameOn = False
        sh.set_pixels(loseScreen)
        
def gameWin():
    global isGameOn
    global isGameWin
    isGameWin = True
    isGameOn = False
    sh.set_pixels(winScreen)
    sleep(qrtrSec)
    sh.clear()
    sleep(qrtrSec)
    sh.set_pixels(winScreen)
    sleep(qrtrSec)
    sh.clear()
    sleep(qrtrSec)
    sh.set_pixels(winScreen)

def task(i):
    global isGameLose
    sh.set_pixels(i)
    if i == triangleScreen:
        for e in sh.stick.get_events():
            if e.action == "pressed" and e.direction == "middle":           #press 3 times
                taskDone()
                nextTask()
            if e.action == "pressed" and e.direction != "middle":
                isGameLose = True
                taskFailed()
    elif i == squareScreen:
        for e in sh.stick.get_events():
            if e.action == "pressed" and e.direction == "left":
                taskDone()
                nextTask()
            if e.action == "pressed" and e.direction != "left":
                isGameLose = True
                taskFailed()
    elif i == circleScreen:
        for e in sh.stick.get_events():
            if e.action == "pressed" and e.direction == "right":
                taskDone()
                nextTask()
            if e.action == "pressed" and e.direction != "right":
                isGameLose = True
                taskFailed()
    elif i == blueScreen:
        for e in sh.stick.get_events():
            if e.action == "pressed" and e.direction == "down":
                taskDone()
                nextTask()
            if e.action == "pressed" and e.direction != "down":
                isGameLose = True
                taskFailed()
    elif i == twoSquareScreen:
        for e in sh.stick.get_events():
            if e.action == "pressed" and e.direction == "middle":
                taskDone()
                nextTask()
            if e.action == "pressed" and e.direction != "middle":
                isGameLose = True
                taskFailed()
    elif i == yellowScreen:
        for e in sh.stick.get_events():
            if e.action == "pressed" and e.direction == "middle":
                taskDone()
                nextTask()
            if e.action == "pressed" and e.direction != "middle":
                isGameLose = True
                taskFailed()
    elif i == orangeScreen:
        for e in sh.stick.get_events():
            if e.action == "pressed" and e.direction == "middle":
                taskDone()
                nextTask()
            if e.action == "pressed" and e.direction != "middle":
                isGameLose = True
                taskFailed()
    elif i == crossScreen:
        for e in sh.stick.get_events():
            if e.action == "pressed" and e.direction == "middle":
                taskDone()
                nextTask()
            if e.action == "pressed" and e.direction != "middle":
                isGameLose = True
                taskFailed()
    elif i == twoLinesScreen:
        for e in sh.stick.get_events():
            if e.action == "pressed" and e.direction == "middle":
                taskDone()
                nextTask()
            if e.action == "pressed" and e.direction != "middle":
                isGameLose = True
                taskFailed()
    elif i == xScreen:
        for e in sh.stick.get_events():
            if e.action == "pressed" and e.direction == "middle":
                taskDone()
                nextTask()
            if e.action == "pressed" and e.direction != "middle":
                isGameLose = True
                taskFailed()







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



taskArr = ["task_1", "task_2", "task_3", "task_4", "task_5", "task_6", "task_7", "task_8", "task_9", "task_10"]
random.shuffle(taskArr)

while isGameOn == True:
    
    
    
    if taskArr[0] == "task_1": #press 3 times
        task(triangleScreen) 
        
    elif taskArr[0] == "task_2": #left
        task(squareScreen)

    elif taskArr[0] == "task_3": #right
        task(circleScreen)

    elif taskArr[0] == "task_4": #down
        task(blueScreen)

    elif taskArr[0] == "task_5": #middle
        task(twoSquareScreen)

    elif taskArr[0] == "task_6":
        task(yellowScreen)

    elif taskArr[0] == "task_7":
        task(orangeScreen)

    elif taskArr[0] == "task_8":
        task(crossScreen)

    elif taskArr[0] == "task_9":
        task(twoLinesScreen)

    elif taskArr[0] == "task_10":
        task(xScreen)
        
    #task counter condition    
    if taskCount == 4:
        gameWin()
        break
    else:
        continue


print("out of loop")
sleep(2)
sh.clear()