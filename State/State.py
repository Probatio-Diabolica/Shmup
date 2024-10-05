from pygame import Surface,image,Rect
import time
from .stateConf import menuTestPath,homeTestPath,MENU_BACKGROUND_PATH,BLACK_BG,HUD,CHAR_B_TEST
from .Fonts import menuFont,font_Default_Color,black,msgPair,white
from typing import final
import pygame as pgm
from functools import cache

from Entity.playables import MC

HOME=1
MENU=2
START=21
OPTIONS=22

# Windows will have a background, each window differs by their functionality and background
class baseWindow:
    _ID:int                     =0 #Each state has a unique id associated with it
    _font:Surface
    _fontRect:Rect
    _choice:int
    _choiceLR:int               =0
    _background :Surface
    _page:int                   =0
    def __init__(self,Background:Surface,value:int=0) -> None:
        self._background = Background
        self._startTime:float   
        self._currentTime:float
    
    def updates(self) -> None:...

    def renderActivity(self,screen:Surface)->None:...

    def pageAnim(self,screen)->None:...
    
    def changeBackground(self,background:Surface):...

    def changePage(self,direction:int)->None:...
    
    def getPage(self)->int:...
    
    def getPlayer(self)->MC:...

    def render(self, screen: Surface) -> None:
        # screen.blit(self._background,(0,0))
        self.renderActivity(screen)
        self.renderUI(screen)
        pgm.display.update()

    def renderUI(self,screen)->None:...
    @final
    def renderText(self,screen:Surface,msg:msgPair,location:tuple[int,int]=(-100,-100))->None:
        if(location[0]==-100 and location[1]==-100):
            screen.blit(msg.getSurface(), msg.getLocation())
        else:
            screen.blit(msg.getSurface(), location)

    @final
    def resetChoice(self)->None:
        """Resets our choice"""
        self._choice=0

    @final
    def getID(self) -> int:
        """    Each state has a unique id associated with it,and this function returns that"""
        return self._ID
    
    @final
    def getBackground(self) -> Surface:
        return self._background

    @final
    def choiceChange(self,factorUD:int=0,factorLR:int=0,pages:int=2,choices:int=5)->None:
        self._choice= (self._choice + factorUD)%choices
        self._choiceLR= (self._choiceLR + factorLR)%pages
        
    @final
    def getChoice(self)->int:
        return self._choice
    
    @final
    def getChoiceLR(self)->int:
        return self._choiceLR
    
    @final
    def getElapsedTime(self)->float:
        return round(self._currentTime-self._startTime,2)
    
    @final
    def getRawElapsedTime(self)->float:
        return self._currentTime-self._startTime
    
    @final
    def moveFont(self,screen,msg:Surface,location:tuple)->None:
        screen.blit(msg,location)
    
    @final
    def switchPage(self,factor:int =1):
        self._page += factor
        print("[base window]current page : " , self._page)

@final
class home(baseWindow):
    _ID:int=1
    __msg:msgPair=msgPair("Begin the adventure",(325,400))

    def __init__(self, Background: Surface = image.load("Assets/INSp/Something.png")) -> None:
        print("<HOME class> [Loc: in State module] ID = ", self._ID)
        super().__init__(Background)

    def renderActivity(self,screen):
        self.renderText(screen,msg=self.__msg) # 325 = width , 400 = depth / height
    
    def pageAnim(self, screen:Surface) -> None:
        leftToRight:int= 60
        self.__msg.changeColor(black)
        while(leftToRight<=self.__msg.getWidth()):
            # optimize this by smooth transition
            screen.blit(self.getBackground(),(0,0))
            self.renderText(screen,self.__msg,(leftToRight,self.__msg.getHeight()))
            leftToRight+=1
            pgm.display.update()
            time.sleep(1/400)
        # Lets do it this way , we will wait for home time to pass for like 2 seconds
        

@final
class menu(baseWindow):
        _ID         : int        = 2
        _choice     : int        = 0
        __tPlay     : msgPair    = msgPair("START",(500,100)) #we will go 550
        __tPractice : msgPair    = msgPair("PRACTICE",(500,150))
        __tOptions  : msgPair    = msgPair("OPTIONS",(500,200))
        __tRecords  : msgPair    = msgPair("RECORDS",(500,250))
        __tExit     : msgPair    = msgPair("EXIT",(500,300))
        
        def __init__(self, Background: Surface = image.load(menuTestPath)) -> None:
            print("<MENU class> [Loc: in State module] ID = ", self._ID)
            super().__init__(Background)
            self._startTime = time.time()
            self._page=1

        def renderText(self,screen:Surface)->None:
            screen.blit(self.__tPlay.getSurface(), self.__tPlay.getLocation())
            screen.blit(self.__tPractice.getSurface(), self.__tPractice.getLocation())
            screen.blit(self.__tOptions.getSurface(), self.__tOptions.getLocation())
            screen.blit(self.__tRecords.getSurface(), self.__tRecords.getLocation())
            screen.blit(self.__tExit.getSurface(), self.__tExit.getLocation())

        def renderActivity(self, screen):
            """ 
                This renders the message at their unique location.  \n
                This has the achitecture of :                       \n.
                page No > Choice > renderText(Where ?, Message ?,Message's Location , Color (if selected) ).
            """
            #PLAY
            if(self._choice==0):
                self.__tPlay.changeColor(black)
                self.renderText(screen)
                self.__tPlay.changeColor(white)
            
            #PRACTICE
            elif(self._choice==1):
                self.__tPractice.changeColor(black)
                self.renderText(screen)
                self.__tPractice.changeColor(white)

            #OPTIONS
            elif(self._choice==2):
                self.__tOptions.changeColor(black)
                self.renderText(screen)
                self.__tOptions.changeColor(white)
            
            #RECORDS
            elif(self._choice==3):
                self.__tRecords.changeColor(black)
                self.renderText(screen)
                self.__tRecords.changeColor(white)
            
            #EXIT
            else: 
                self.__tExit.changeColor(black)
                self.renderText(screen)
                self.__tExit.changeColor(white)



@final
class options(baseWindow):
    _ID     :int        = 22    
    _choice :int        = 0
    # _text   :msgPair    =msgPair()
    def __init__(self, Background: Surface = image.load(MENU_BACKGROUND_PATH)) -> None:
            print("Option class [Loc: in State module]")
            super().__init__(Background)

    

        

class dummyState(baseWindow):
    _ID=404
    def __init__(self, Background: Surface = image.load(MENU_BACKGROUND_PATH), value: int = 0) -> None:
        super().__init__(Background, value)
        print("dummy reached : can't switch states now [LOC : dummyState >> State.py]")

        
from Scripts import getDialog
from .UI_Panels import HEADER
