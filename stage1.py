import pygame as pgm
import time
from Entity.playables import MC
from Entity.Enemies import e1
player = MC(100,100,0.06,pgm.image.load("Assets/Player/Hitbox.png"),xlimL=0,xLimR=390,yLimU=0,yLimD=390)
Enemy=e1(x=170,y=20,spd=0.2,pathway=((10,20),(20,30),(20,30),(4,40)),repeat=False)
DEBUG_STR="Worked @ [Game.py]"

interim=0 

def enem_update():...
    # global interim
    # if(interim==0):
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
        screen.blit(Enemy.getSprite(),Enemy.getCoordinates())
        screen.blit(player.getSprite(),player.getCoordinates())
        pgm.display.update()
        for event in pgm.event.get():
            if event.type == pgm.QUIT: running=False

            if(event.type ==pgm.KEYDOWN):
                if(event.key==pgm.K_UP or event.key==pgm.K_KP_8):
                    player.toggleUp()
                elif(event.key==pgm.K_DOWN or event.key==pgm.K_KP_2):
                    player.toggleDown()
                    # self.__state.choiceChange(factorUD=1,choices=4)
                elif(event.key==pgm.K_RIGHT or event.key==pgm.K_KP_6):
                    player.toggleRight()
                elif(event.key==pgm.K_LEFT or event.key==pgm.K_KP_4):
                    player.toggleLeft()
                elif(event.key==pgm.K_ESCAPE or event.key==pgm.K_x):...
                    # print(DEBUG_STR+"up")
                    # self.changeState(menu())

            if(event.type == pgm.KEYUP):
                if(event.key==pgm.K_UP or event.key==pgm.K_KP_8):
                    player.toggleUp()
                elif(event.key==pgm.K_DOWN or event.key==pgm.K_KP_2):
                    player.toggleDown()
                    # self.__state.choiceChange(factorUD=1,choices=4)
                elif(event.key==pgm.K_RIGHT or event.key==pgm.K_KP_6):
                    player.toggleRight()
                elif(event.key==pgm.K_LEFT or event.key==pgm.K_KP_4):
                    player.toggleLeft()

run()

