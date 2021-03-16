from sense_hat import SenseHat
from time import sleep
from guizero import App, Text, PushButton, Window
sh = SenseHat()

# appW = 750 #width of the window
# appH = 500 #height of the window

# sWin = App(title="You Win!", height=appH, width=appW, bg=(0, 255, 0))
# # sWin.hide() #hides this window until player clicks on start button
# Text(sWin, text="", size=50) #spacer
# Text(sWin, text="BOMB DEFUSED", size=50)
# Text(sWin, text="Great work!", size=25)
# Text(sWin, text="", size=25) #spacer
# menuBtn = PushButton(sWin, text="Main Menu")
# menuBtn.bg = "#e0e0e0" #light grey

# sWin.display()

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

sh.set_pixels(squareScreen)
