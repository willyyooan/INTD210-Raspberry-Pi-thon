from sense_hat import SenseHat
from time import sleep
import random
import threading

sh = SenseHat()
event = threading.Event()

sh.clear()

##COLOURS##
r = [255, 0, 0] #red
g = [0, 255, 0] #green
x = [0, 0, 0] #blank
w = [255, 255, 255]
B = [0, 0, 255] #Blue
O = [135,206,250] #Light Blue. was called Orange
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

##VARIABLES, BOOLEANS, AND LISTS##
global isGameOn
global isGameLose
global isGameWin

isGameOn = False
isGameLose = False
isGameWin = False

global i
i = 0

qrtrSec = 0.25
halfSec = 0.5
fullSec = 1

interval = 1

taskCount = 0

up = 'up'
dn = 'down'
lt = 'left'
rt = 'right'

squareSeq = [up, dn, lt, rt]
triangleSeq = [up, lt, rt]
twoSquareSeq = [up, dn, up, up, lt, rt]
yellowSeq = [up, up, up, up, dn, dn, dn, dn]
crossSeq = [dn, dn, dn, dn, dn, dn, up, up, up, lt, lt, lt, rt, rt, rt, rt, rt, rt]
xSeq = [up, dn, dn, lt, lt, lt, rt, rt, rt, rt]

btnSeq = []

##FUNCTIONS##
def nextTask():
    sh.clear()
    del btnSeq[:] #resets list
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
    
def tiltLeft():
    acceleration = sh.get_accelerometer_raw()
    x = acceleration ["x"]
    y = acceleration ["y"]
    z = acceleration ["z"]
    
    x = round(x,0)
    y = round(y,0)
    z = round(z,0)
    
    if x == -1:
        taskDone()
        nextTask()
        print("left")
    elif y == 0:
        pass
    else:
        taskFailed()

def upsideDown():
    acceleration = sh.get_accelerometer_raw()
    x = acceleration ["x"]
    y = acceleration ["y"]
    z = acceleration ["z"]
    
    x = round(x,0)
    y = round(y,0)
    z = round(z,0)
    
    if z == -1:
        taskDone()
        nextTask()
        print("upside down")
    elif y == 0:
        pass

def shake():
    x, y, z = sh.get_accelerometer_raw().values()
    
    x = abs(x)
    y = abs(y)
    z = abs(z)
     
    if x > 2 or y > 2 or z > 2:
        taskDone()
        nextTask()

def taskFailed():
    global isGameLose
    isGameLose = True
    print("BOOM! You died :(")
    del btnSeq[:] #resets list
    while isGameLose == True:
        global isGameOn
        isGameOn = False
        sh.set_pixels(loseScreen)
        
def gameWin():
    global isGameOn
    global isGameWin
    isGameWin = True
    isGameOn = False
    del btnSeq[:] #resets list
    sh.set_pixels(winScreen)
    sleep(qrtrSec)
    sh.clear()
    sleep(qrtrSec)
    sh.set_pixels(winScreen)
    sleep(qrtrSec)
    sh.clear()
    sleep(qrtrSec)
    sh.set_pixels(winScreen)



def timerDisp():
    #timer
    global i
    s = 8

    sh.set_pixel(0, 0, g)
    sh.set_pixel(1, 0, g)
    sh.set_pixel(2, 0, g)
    sh.set_pixel(3, 0, g)
    sh.set_pixel(4, 0, g)
    sh.set_pixel(5, 0, g)
    sh.set_pixel(6, 0, g)
    sh.set_pixel(7, 0, g)

    for i in range(0, s):
        global interval
        event.wait(interval)
        print(str(i))
        sh.set_pixel(i, 0, r)
    
    if i == 7:
      taskFailed()


# def main():
#     thread = threading.Thread(target=timerDisp)
#     thread.start()

def task(i):
    global isGameLose
    sh.set_pixels(i)
    if i == triangleScreen:
        for e in sh.stick.get_events():
            if e.action == "pressed":
                n = e.direction
                btnSeq.append(n) #appends the direction to a list (btnSeq)
                if e.action == "pressed" and e.direction == "middle": #press middle to confirm. this will add "middle" to the btnSeq list
                    btnSeq.pop() #gets rid of the "middle" appended to the btnSeq list. We don't need it.
                    if btnSeq == triangleSeq: #compares btnSeq list (what you did on the joystick) to a pre-described task sequence (see variables)
                        taskDone() #if it matches
                        nextTask()
                    else:
                        isGameLose = True #if it doesn't match
                        taskFailed()
    
    elif i == squareScreen:
        for e in sh.stick.get_events():
            if e.action == "pressed":
                n = e.direction
                btnSeq.append(n)
                if e.action == "pressed" and e.direction == "middle":
                    btnSeq.pop()
                    if btnSeq == squareSeq:
                        taskDone()
                        nextTask()
                    else:
                        isGameLose = True
                        taskFailed()
    
    elif i == circleScreen:
        for e in sh.stick.get_events():
            if e.action == "pressed" and e.direction == "middle":
                taskDone()
                nextTask()
            if e.action == "pressed" and e.direction != "middle":
                isGameLose = True
                taskFailed()
    
    elif i == blueScreen:
        tiltLeft()
    
    elif i == twoSquareScreen:
        for e in sh.stick.get_events():
            if e.action == "pressed":
                n = e.direction
                btnSeq.append(n)
                if e.action == "pressed" and e.direction == "middle":
                    btnSeq.pop()
                    if btnSeq == twoSquareSeq:
                        taskDone()
                        nextTask()
                    else:
                        isGameLose = True
                        taskFailed()

    elif i == yellowScreen:
        for e in sh.stick.get_events():
            if e.action == "pressed":
                n = e.direction
                btnSeq.append(n)
                if e.action == "pressed" and e.direction == "middle":
                    btnSeq.pop() 
                    if btnSeq == yellowSeq:
                        taskDone()
                        nextTask()
                    else:
                        isGameLose = True
                        taskFailed()
    
    elif i == orangeScreen:
        shake()
    
    elif i == crossScreen:
        for e in sh.stick.get_events():
            if e.action == "pressed":
                n = e.direction
                btnSeq.append(n)
                if e.action == "pressed" and e.direction == "middle":
                    btnSeq.pop()
                    if btnSeq == crossSeq:
                        taskDone()
                        nextTask()
                    else:
                        isGameLose = True
                        taskFailed()
    
    elif i == twoLinesScreen:
        upsideDown()
    
    elif i == xScreen:
        for e in sh.stick.get_events():
            if e.action == "pressed":
                n = e.direction
                btnSeq.append(n)
                if e.action == "pressed" and e.direction == "middle":
                    btnSeq.pop() 
                    if btnSeq == xSeq:
                        taskDone()
                        nextTask()
                    else:
                        isGameLose = True
                        taskFailed()
    timerDisp()


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

print("timer is set to " + str(interval*8) + " seconds")


#game loop
while isGameOn == True and i < 7:

    # continue

    # if timer < 10:
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