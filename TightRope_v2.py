from sense_hat import SenseHat
from time import sleep
sh = SenseHat()

sh.clear()
sh.low_light = True


#COLOURS#
o = [255, 255, 0] #yellow path
x = [0, 0, 0] #blank
b = [0, 0, 255] #blue
r = [255, 0, 0] #red
g = [0, 255, 0] #green

#LED#
path = [
    o,o,o,o,x,x,x,x,
    o,o,o,o,x,x,x,x,
    x,x,o,o,x,x,x,x,
    x,x,o,o,o,o,o,x,
    x,x,o,o,o,o,o,x,
    x,x,x,x,x,o,o,x,
    x,x,x,x,x,o,o,x,
    x,x,x,x,x,g,g,x
    ]

gameOver = [
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r
    ]

gameWin = [
    g,g,g,g,g,g,g,g,
    g,g,g,g,g,g,g,g,
    g,g,g,g,g,g,g,g,
    g,g,g,g,g,g,g,g,
    g,g,g,g,g,g,g,g,
    g,g,g,g,g,g,g,g,
    g,g,g,g,g,g,g,g,
    g,g,g,g,g,g,g,g
    ]


#PLAYER#
charX = 0
charY = 0



#STARTING BOOLEANS#
isGameOn = True
isGameWin = False
isGameLose = False


#GAME#
while True:
    
    #resets the gyroscope
    pitch = sh.get_orientation()['pitch']
    roll = sh.get_orientation()['roll']
    
    #only runs if you lose the game
    if isGameOn == False:
        if isGameLose == True: #press the joystick to restart
            for e in sh.stick.get_events():
                if e.action == 'pressed' and e.direction == 'middle':
                    print("Restart game")
                    isGameLose = False #resets booleans
                    isGameOn = True
                    charX = 0
                    charY = 0
        elif isGameWin == True: #press the joystick to restart
            for e in sh.stick.get_events():
                if e.action == 'pressed' and e.direction == 'middle':
                    print("Restart game")
                    isGameWin = False #resests booleans
                    isGameOn = True
                    charX = 0
                    charY = 0
        

    
    #Game is on. Should run right away
    while isGameOn == True:
                
        sh.set_pixels(path) #creates path as made above
        sh.set_pixel(charX, charY, b) #sets the player as blue and its starting position

        pitch = sh.get_orientation()['pitch']
        roll = sh.get_orientation()['roll']
        
        #sets how much you need to tilt Pi
        if 300 < pitch < 345 and charX < 7:
            charX += 1
        if 15 < pitch < 45 and charX > 0:
            charX -= 1
        if 15 < roll < 45 and charY < 7:
            charY += 1
        if 300 < roll < 345 and charY > 0:
            charY -= 1
        
        current = sh.get_pixel(charX, charY)

        #if you go off the path
        if current == x:
            isGameLose = True #game ends
            print("lose")
        
        #if you reach the goal
        if sh.get_pixel(5,7) == [0, 0, 248]:
            isGameWin = True
            print("win")
        elif sh.get_pixel(6,7) == [0, 0, 248]:
            isGameWin = True
            print("win")
        
        #game ends, screen turns red.       
        if isGameLose == True:
            isGameOn = False
            sh.set_pixels(gameOver)

        #game ends, screen turns green
        if isGameWin == True:
            isGameOn = False
            sh.set_pixels(gameWin)
         

            
        sleep(0.1) #slows game down
    
    



        
        

    







