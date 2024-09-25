import pygame as pgm
import time
from Entity.playables import MC
player = MC(100,100,0.06,pgm.image.load("Assets/Player/Hitbox.png"),370,370)
DEBUG_STR="Worked @ [Game.py]"

    

def run():
    pgm.init()  
    blue=(0,110,255)
    X = 400
    Y = 400
    running=True
    screen = pgm.display.set_mode((X, Y )) 

    pgm.display.set_caption('STAGE 1 TEST')


    while running : 
        screen.fill(blue) 
        player.updates()
        screen.blit(player.getSprite(),player.getCoordinates())

        pgm.display.update()
        for event in pgm.event.get():
            if event.type == pgm.QUIT: running=False

            if(event.type ==pgm.KEYDOWN):
                if(event.key==pgm.K_UP or event.key==pgm.K_KP_8):
                    player.toggleUp()
                    print(DEBUG_STR+"up")
                elif(event.key==pgm.K_DOWN or event.key==pgm.K_KP_2):
                    player.toggleDown()
                    print(DEBUG_STR+"down")
                    # self.__state.choiceChange(factorUD=1,choices=4)
                elif(event.key==pgm.K_RIGHT or event.key==pgm.K_KP_6):
                    player.toggleRight()
                    print(DEBUG_STR+"right")
                elif(event.key==pgm.K_LEFT or event.key==pgm.K_KP_4):
                    player.toggleLeft()
                    print(DEBUG_STR+"Left")
                elif(event.key==pgm.K_ESCAPE or event.key==pgm.K_x):...
                    # print(DEBUG_STR+"up")
                    # self.changeState(menu())

            if(event.type == pgm.KEYUP):
                if(event.key==pgm.K_UP or event.key==pgm.K_KP_8):
                    player.toggleUp()
                    print(DEBUG_STR+"up")
                elif(event.key==pgm.K_DOWN or event.key==pgm.K_KP_2):
                    player.toggleDown()
                    print(DEBUG_STR+"down")
                    # self.__state.choiceChange(factorUD=1,choices=4)
                elif(event.key==pgm.K_RIGHT or event.key==pgm.K_KP_6):
                    player.toggleRight()
                    print(DEBUG_STR+"right")
                elif(event.key==pgm.K_LEFT or event.key==pgm.K_KP_4):
                    player.toggleLeft()
                    print(DEBUG_STR+"Left")







if __name__=="__main__":
    run()