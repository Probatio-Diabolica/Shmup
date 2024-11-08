from .gameConf import gameHeight,gameWidth
from State.State import baseWindow,home,menu,dummyState,msgPair
from State.Play import play
from State.CharacterSelection import Character
# from Entity.Entity import Entity
# from Entity.playables import MC
from Entity.playables.Player import characterA
# from State.stateConf import CHAR_B_TEST,BLACK_BG
import pygame as pgm
import time
INST = None

HOME=1
MENU=2
# START=21
OPTIONS=22
GAMEPLAY=100
CHAR_SELECTION=21



# ---------------------------------------------------------------------------------------------------------------------------------------
DEBUG_STR="Worked @ [Game.py]"
# Code needs heavy optimization here, also objects that are not annoted by self are static by default
class Game:
    __state      :  baseWindow          
    __running    :  bool   
    __background :  pgm.Surface         
    __height     :  int           = gameHeight
    __width      :  int           = gameWidth
    __screen     :  pgm.Surface
    #//////////////////////////////////////////////////////////////////////////////////
    # note: temp vars                                       #//////////////////////////
    high                          = 0                    #/////////////////////////////
    low                           = 1000              #////////////////////////////////
    #//////////////////////////////////////////////////////////////////////////////////
    
    # __MC         :  Player              
    def __init__(self) -> None:
        pgm.init()
        global INST
        INST=self
        self.__player=None
        self.__running=True #running 

        # self.__screen=pgm.display.set_mode((self.__width,self.__height),flags=pgm.FULLSCREEN) # "flags=pgm.FULLSCREEN"  ,also :set_mode = (W,H) 
        self.__screen=pgm.display.set_mode((self.__width,self.__height)) # "flags=pgm.FULLSCREEN"  ,also :set_mode = (W,H) 
        pgm.mouse.set_visible(False)
        pgm.display.set_caption(f"Shump Game || fps :{120} | ups : {0} ||")
        
        self.home = home()
        self.menu = menu()
        self.char = Character()
        self.play= play(self.__player)
        self.__stateDist={self.home.getID():self.home , self.menu.getID():self.menu,self.char.getID():self.char,self.play.getID():self.play}
        
        self.__state=self.__stateDist[HOME]
        # self.__state=state #the state or screen we are in
        self.__background=self.__state.getBackground() # background of the window
        self.__screen.blit(self.__background,(0,0))
        self.__state.pageAnim(self.__screen)
        

    
    def changeState(self,state:baseWindow) -> None :
        self.__screen.fill((0,0,0))
        self.__state=state
        self.__background=state.getBackground()
        self.__screen.blit(self.__background,(0,0)) #type: ignore
        self.__state.pageAnim(self.__screen)
        if(self.__state.getID()==100): self.__player=self.__state.getPlayer()

    def run(self)->None:
        self.__running=True
        __lastTime:int=time.time_ns()
        __timer : int = int(time.time_ns() / 1000000)
        __nanosecs:float=1000000000.0/60.0
        __delta:float=0.0
        __updates:int =0
        __frames:int =0
        while (self.__running):
            __now=time.time_ns()
            __delta+= (__now-__lastTime)/__nanosecs
            __lastTime=__now
            while(__delta>=1):
                self.update()
                __delta-=1 
                __updates+=1  
            if(self.__state._ID==100):self.renderStage()
            else:self.render()
            __frames+=1

            if(int(time.time_ns()/1000000) - __timer>1000):
                __timer+=1000
                if(__frames>self.high): self.high = __frames
                if(__frames<self.low): self.low   = __frames
                self.showGameHealth(__frames,__updates)
                __frames=0
                __updates=0
        # if loop ends 
        self.closeGame()

    def update(self)->None:
        self.events()
        self.__state.updates() 
        # print("TEST @ UPDATE/GAME.PY current state :",self.__state.getID())       
        
    def render(self)->None:
        pgm.display.update() #!!most imp line don't forget it        
        self.__state.render(self.__screen)

    def renderStage(self)->None:
        self.__screen.fill((0,0,0,))
        self.__state.render(self.__screen)
        self.__screen.blit(self.__player.getSprite(),self.__player.getCoordinates()) #type:ignore
        pgm.display.update() #!!most imp line don't forget it 

    def showGameHealth(self,frames:int,updates:int)->None:
        pgm.display.set_caption(f"Shump Game || fps :{frames} | ups : {updates} || heightFPS {self.high} | lowest fps {self.low}")

    def events(self)->None:
        """Checks the ID and then does the event handling"""
        # print(f" state == {self.__state.getID()}")
        if(self.__state.getID()==HOME):self.eventsForHome()
        elif(self.__state.getID() ==MENU ): self.eventsForMenu()
        elif(self.__state.getID() == GAMEPLAY):
            self.eventsforPlay()
            self.__player.updates()#type:ignore
        elif(self.__state.getID() == CHAR_SELECTION):self.eventsForCharacterSelection()
        elif(self.__state.getID()==404): self.eventsForDummy()

    def eventsForHome(self) -> None:
        """Events at home screen"""
        for event in pgm.event.get():
            if event.type == pgm.QUIT: self.__running=False
            if event.type ==pgm.KEYDOWN:
                if(event.key==pgm.K_z or event.key==pgm.K_SPACE):  
                    self.changeState(self.__stateDist[MENU])

    def eventsForMenu(self) -> None:
        """Events at menu screen"""
        for event in pgm.event.get():
            if event.type ==pgm.KEYDOWN:

                if(event.key==pgm.K_UP or event.key==pgm.K_KP_8):
                    self.__state.choiceChange(factorUD=-1) # it is under minus bc we want to go up and in order to go up we can just subtract from choices
                    
                if(event.key==pgm.K_DOWN or event.key==pgm.K_KP_2):
                    self.__state.choiceChange(factorUD=1)  # same thing, however we are increasing to go down
                    
                # If ok button is pressed
                if(event.key==pgm.K_z ):
                    
                    # Start
                    if(self.__state.getChoice()==0):
                        self.changeState(self.__stateDist[CHAR_SELECTION]) #<-later
                        # self.changeState(play())
                    
                    # Practice
                    elif(self.__state.getChoice()==1):
                        self.changeState(dummyState())
                    
                    # Options
                    elif(self.__state.getChoice()==2):
                        self.changeState(dummyState())
                    
                    # Records
                    elif(self.__state.getChoice()==3):
                        self.changeState(dummyState())

                    #exit
                    elif(self.__state.getChoice()==4):
                        self.__running=False
                if(event.key==pgm.K_ESCAPE) or (event.key==pgm.K_x) :  
                    self.changeState(self.__stateDist[HOME])
            elif event.type == pgm.QUIT: self.__running=False

    def eventsForCharacterSelection(self) -> None:
            for event in pgm.event.get():
                if event.type == pgm.QUIT: self.__running=False
                if(event.type ==pgm.KEYDOWN):
                    if( self.__state.getPage()==-1):
                        if(event.key==pgm.K_UP or event.key==pgm.K_KP_8):
                            self.__state.choiceChange(factorUD=-1,choices=4) 
                            
                        elif(event.key==pgm.K_DOWN or event.key==pgm.K_KP_2):
                            self.__state.choiceChange(factorUD=1,choices=4)
                        
                        elif(event.key==pgm.K_ESCAPE or event.key==pgm.K_x): 
                            self.changeState(self.menu)
                    else:
                        print(self.__state.getPage())
                        if(event.key==pgm.K_LEFT or event.key==pgm.K_KP_4):
                            self.__state.changePage(direction=-1)
                        
                        elif(event.key==pgm.K_RIGHT or event.key==pgm.K_KP_6):
                            self.__state.changePage(direction=1)

                        elif(event.key==pgm.K_ESCAPE or event.key==pgm.K_x): 
                            self.__state._page=-1 
                        
                    if(event.key==pgm.K_z):
                        if(self.__state.getPage()==-1):
                            print("difficulty chosen[GAME.py]")
                            self.__state.changePage(direction=1)

                            self.__state.resetChoice()
                        else:
                            self.changeState(play(characterA((623-48)/2,696-100,5,pgm.image.load("Assets/Player/Hitbox.png"))))
                            self.__player=self.__state.getPlayer()
                        
                if(event.type == pgm.KEYUP):...
                
    def eventsForOptions(self) -> None:
        for event in pgm.event.get():
            if event.type == pgm.QUIT: self.__running=False

    def eventsForPractice(self) -> None:
        for event in pgm.event.get():
            if event.type == pgm.QUIT: self.__running=False

    def eventsForDummy(self) -> None:
        for event in pgm.event.get():
            if event.type == pgm.QUIT: self.__running=False
            if event.type == pgm.KEYDOWN:...
            if event.type == pgm.KEYUP:...

    def eventsforPlay(self)->None:
        #!! to solve the issue of player updates we need to set up new update for every type of update. This is the only way to do it
        for event in pgm.event.get():
            if event.type == pgm.QUIT: self.__running=False

            if(event.type ==pgm.KEYDOWN):
                if(event.key==pgm.K_UP or event.key==pgm.K_KP_8):
                    self.__player.toggleUp() #type:ignore
                    
                elif(event.key==pgm.K_DOWN or event.key==pgm.K_KP_2):
                    self.__player.toggleDown()#type:ignore
                    # self.__state.choiceChange(factorUD=1,choices=4)
                elif(event.key==pgm.K_RIGHT or event.key==pgm.K_KP_6):
                    self.__player.toggleRight() #type:ignore
                elif(event.key==pgm.K_LEFT or event.key==pgm.K_KP_4):
                    self.__player.toggleLeft() #type:ignore
                elif(event.key==pgm.K_ESCAPE or event.key==pgm.K_x):
                    self.__running=False
                    # print(DEBUG_STR+"up")
                    # self.changeState(menu())

            if(event.type == pgm.KEYUP):
                if(event.key==pgm.K_UP or event.key==pgm.K_KP_8):
                    self.__player.toggleUp() #type:ignore
                elif(event.key==pgm.K_DOWN or event.key==pgm.K_KP_2):
                    self.__player.toggleDown() #type:ignore
                    # self.__state.choiceChange(factorUD=1,choices=4)
                elif(event.key==pgm.K_RIGHT or event.key==pgm.K_KP_6):
                    self.__player.toggleRight() #type:ignore
                elif(event.key==pgm.K_LEFT or event.key==pgm.K_KP_4):
                    self.__player.toggleLeft() # type: ignore

    #__depricate
    def WindowIsOpen(self)->bool:
        return self.__running

    def closeGame(self)->None:
        pgm.quit()
        
