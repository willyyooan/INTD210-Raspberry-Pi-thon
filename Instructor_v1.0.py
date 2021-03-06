#from sense_hat import SenseHat
from time import sleep
from guizero import App, Text, PushButton, Window
#sh = SenseHat()

##VARIABLES##
appW = 750 #width of the window
appH = 500 #height of the window
appBG = (112,112,112) #dark grey
if_text = "If the Bomb is showing a:"
instr = "The difuser needs to do:"

##FUNCTIONS##
def gotoScreen0():
    print("Game start!")
    s0.show()
    s1.hide()
    startScr.hide()

def gotoScreen1():
    print("1")
    s0.hide()
    s1.show()
    s2.hide()

def gotoScreen2():
    print("2")
    s1.hide()
    s2.show()
    s3.hide()

def gotoScreen3():
    print("3")
    s2.hide()
    s3.show()
    s4.hide()

def gotoScreen4():
    print("4")
    s3.hide()
    s4.show()
    s5.hide()

def gotoScreen5():
    print("5")
    s4.hide()
    s5.show()
    s6.hide()

def gotoScreen6():
    print("6")
    s5.hide()
    s6.show()
    s7.hide()

def gotoScreen7():
    print("7")
    s6.hide()
    s7.show()
    s8.hide()

def gotoScreen8():
    print("8")
    s7.hide()
    s8.show()
    s9.hide()

def gotoScreen9():
    print("9")
    s8.hide()
    s9.show()

def windowClose():
    print("Game quit!")
    startScr.destroy() #closes the window


##START SCREEN#
startScr = App(
    title="Bomb Difusing Game v1", 
    height=appH, 
    width=appW, 
    bg=(112,112,112),
    )

title = Text(startScr, #Main Welcome Text
    text="Welcome to the Bomb Defusing Game", 
    size="25",
    color="#ffffff", #white
    )

subtitle = Text(startScr, 
    text="Press the start button to begin",
    color="#ffffff", #white
    )

startBtnSpacer = Text(startScr,
    text=" ",
    size=50,
)

startBtn = PushButton(startScr, 
    text="Start Game", 
    command=gotoScreen0,
    padx=0,
    pady=0,
    )
startBtn.bg = "#e0e0e0" #light grey
startBtn.width = 25
startBtn.height = 1
startBtn.text_size = 15

endBtnSpacer = Text(startScr,
    text=" ",
    size=25,
    align="bottom"
)

endBtn = PushButton(startScr, 
    text="Quit", 
    command=windowClose,
    align="bottom",
    padx=0,
    pady=0,
    )
endBtn.width = 10
endBtn.height = 1
endBtn.text_color = "#ffffff" #white

#SECOND WINDOW
#TRIANGLE
s0 = Window(startScr, title="Instructions", height=appH, width=appW, bg=appBG)
s0.hide() #hides this window until player clicks on start button
Text(s0, text="What is showing on the Bomb?", color="#ffffff", size=25) #colour: white
Text(s0, text="", size=10) #spacer
Text(s0, text=if_text)
Text(s0, text="", size=10) #spacer
Text(s0, text="Triangle", size=50)
Text(s0, text="", size=10) #spacer
Text(s0, text=instr)
Text(s0, text="", size=15) #spacer
Text(s0, text="Press the joystick 3 times", size=25)
Text(s0, text="", size=15) #spacer
PushButton(s0, text="Next Page", command=gotoScreen1)

#THIRD WINDOW
#FULL BLUE
s1 = Window(startScr, title="Instructions", height=appH, width=appW, bg=appBG)
s1.hide() #hides this window until player clicks on start button
Text(s1, text="What is showing on the Bomb?", color="#ffffff", size=25) #colour: white
Text(s1, text="", size=10) #spacer
Text(s1, text=if_text)
Text(s1, text="", size=10) #spacer
Text(s1, text="Full Blue", size=50)
Text(s1, text="", size=10) #spacer
Text(s1, text=instr)
Text(s1, text="", size=15) #spacer
Text(s1, text="Press the joystick up 5 times", size=25)
Text(s1, text="", size=15) #spacer
PushButton(s1, text="Next Page", command=gotoScreen2)
PushButton(s1, text="Previous Page", command=gotoScreen0)

#FOURTH WINDOW
#SQAURE
s2 = Window(startScr, title="Instructions", height=appH, width=appW, bg=appBG)
s2.hide() #hides this window until player clicks on start button
Text(s2, text="What is showing on the Bomb?", color="#ffffff", size=25) #colour: white
Text(s2, text="", size=10) #spacer
Text(s2, text=if_text)
Text(s2, text="", size=10) #spacer
Text(s2, text="Square", size=50)
Text(s2, text="", size=10) #spacer
Text(s2, text=instr)
Text(s2, text="", size=15) #spacer
Text(s2, text="Press the joystick left 7 times", size=25)
Text(s2, text="", size=15) #spacer
PushButton(s2, text="Next Page", command=gotoScreen3)
PushButton(s2, text="Previous Page", command=gotoScreen1)

#FITH WINDOW
#TWO LINES
s3 = Window(startScr, title="Instructions", height=appH, width=appW, bg=appBG)
s3.hide() #hides this window until player clicks on start button
Text(s3, text="What is showing on the Bomb?", color="#ffffff", size=25) #colour: white
Text(s3, text="", size=10) #spacer
Text(s3, text=if_text)
Text(s3, text="", size=10) #spacer
Text(s3, text="Two lines", size=50)
Text(s3, text="", size=10) #spacer
Text(s3, text=instr)
Text(s3, text="", size=15) #spacer
Text(s3, text="Shake the bomb", size=25)
Text(s3, text="", size=15) #spacer
PushButton(s3, text="Next Page", command=gotoScreen4)
PushButton(s3, text="Previous Page", command=gotoScreen2)

#SIXTH WINDOW
#CIRCLE
s4 = Window(startScr, title="Instructions", height=appH, width=appW, bg=appBG)
s4.hide() #hides this window until player clicks on start button
Text(s4, text="What is showing on the Bomb?", color="#ffffff", size=25) #colour: white
Text(s4, text="", size=10) #spacer
Text(s4, text=if_text)
Text(s4, text="", size=10) #spacer
Text(s4, text="Circle", size=50)
Text(s4, text="", size=10) #spacer
Text(s4, text=instr)
Text(s4, text="", size=15) #spacer
Text(s4, text="Press the joystick up once then down once", size=25)
Text(s4, text="", size=15) #spacer
PushButton(s4, text="Next Page", command=gotoScreen5)
PushButton(s4, text="Previous Page", command=gotoScreen3)

#SEVENTH WINDOW
#2 SQUARE
s5 = Window(startScr, title="Instructions", height=appH, width=appW, bg=appBG)
s5.hide() #hides this window until player clicks on start button
Text(s5, text="What is showing on the Bomb?", color="#ffffff", size=25) #colour: white
Text(s5, text="", size=10) #spacer
Text(s5, text=if_text)
Text(s5, text="", size=10) #spacer
Text(s5, text="2 Squares", size=50)
Text(s5, text="", size=10) #spacer
Text(s5, text=instr)
Text(s5, text="", size=15) #spacer
Text(s5, text="Press the joystick right 4 times", size=25)
Text(s5, text="", size=15) #spacer
PushButton(s5, text="Next Page", command=gotoScreen6)
PushButton(s5, text="Previous Page", command=gotoScreen4)

#EIGHTH WINDOW
#ALL YELLOW
s6 = Window(startScr, title="Instructions", height=appH, width=appW, bg=appBG)
s6.hide() #hides this window until player clicks on start button
Text(s6, text="What is showing on the Bomb?", color="#ffffff", size=25) #colour: white
Text(s6, text="", size=10) #spacer
Text(s6, text=if_text)
Text(s6, text="", size=10) #spacer
Text(s6, text="All Yellow", size=50)
Text(s6, text="", size=10) #spacer
Text(s6, text=instr)
Text(s6, text="", size=15) #spacer
Text(s6, text="Tilt the bomb away from you", size=25)
Text(s6, text="", size=15) #spacer
PushButton(s6, text="Next Page", command=gotoScreen7)
PushButton(s6, text="Previous Page", command=gotoScreen5)

#NINTH WINDOW
#ALL ORANGE
s7 = Window(startScr, title="Instructions", height=appH, width=appW, bg=appBG)
s7.hide() #hides this window until player clicks on start button
Text(s7, text="What is showing on the Bomb?", color="#ffffff", size=25) #colour: white
Text(s7, text="", size=10) #spacer
Text(s7, text=if_text)
Text(s7, text="", size=10) #spacer
Text(s7, text="All Orange", size=50)
Text(s7, text="", size=10) #spacer
Text(s7, text=instr)
Text(s7, text="", size=15) #spacer
Text(s7, text="Press the joystick 9 times", size=25)
Text(s7, text="", size=15) #spacer
PushButton(s7, text="Next Page", command=gotoScreen8)
PushButton(s7, text="Previous Page", command=gotoScreen6)

#TENTH WINDOW
#CROSS
s8 = Window(startScr, title="Instructions", height=appH, width=appW, bg=appBG)
s8.hide() #hides this window until player clicks on start button
Text(s8, text="What is showing on the Bomb?", color="#ffffff", size=25) #colour: white
Text(s8, text="", size=10) #spacer
Text(s8, text=if_text)
Text(s8, text="", size=10) #spacer
Text(s8, text="Cross", size=50)
Text(s8, text="", size=10) #spacer
Text(s8, text=instr)
Text(s8, text="", size=15) #spacer
Text(s8, text="Up Up Down Down Left Right Left Right", size=25)
Text(s8, text="", size=15) #spacer
PushButton(s8, text="Next Page", command=gotoScreen9)
PushButton(s8, text="Previous Page", command=gotoScreen7)

#ELEVENTH WINDOW
#X
s9 = Window(startScr, title="Instructions", height=appH, width=appW, bg=appBG)
s9.hide() #hides this window until player clicks on start button
Text(s9, text="What is showing on the Bomb?", color="#ffffff", size=25) #colour: white
Text(s9, text="", size=10) #spacer
Text(s9, text=if_text)
Text(s9, text="", size=10) #spacer
Text(s9, text="X", size=50)
Text(s9, text="", size=10) #spacer
Text(s9, text=instr)
Text(s9, text="", size=15) #spacer
Text(s9, text="Shake then press the joystick", size=25)
Text(s9, text="", size=15) #spacer
PushButton(s9, text="Previous Page", command=gotoScreen8)

startScr.display()

