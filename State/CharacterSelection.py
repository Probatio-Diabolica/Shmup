from State import baseWindow
from pygame import Surface,image,Rect,surfarray
from .Fonts import menuFont,font_Default_Color,black,msgPair,white
from Scripts import getDialog
from typing import final
from .stateConf import menuTestPath,homeTestPath,BLACK_BG,CHAR_B_TEST,difficultyPath,CHAR_A
from .UI_Panels import HEADER,EASY,NORMAL,HARD,LUNATIC,EASY_LOW,NORMAL_LOW,HARD_LOW,LUNATIC_LOW
import numpy as np
from random import randrange

@final
class Character(baseWindow):
    _ID=21
    __TEXT      : msgPair    =   msgPair(getDialog(0),(222,222))
    _choice     : int        =   0
    __netPages  : int        =   2
    _page       : int        =   -1
    __player    : int        =   0   
    def __init__(self, Background: Surface = image.load(homeTestPath), value: int = 0) -> None:
        print("<Char class> [Loc: in State module] ID = ", self._ID)
        self.backgroundt=image.load(homeTestPath)
        super().__init__(Background, value)

    def getPage(self) -> int:
        return  self._page
    
    def changeBackground(self,background:Surface)   -> None:
        self._background=background

    def changePage(self, direction: int)  ->None:
        self._page=(self._page+direction)%self.__netPages

    # def renderUI(self, screen) -> None:
            
    def renderActivity(self, screen: Surface) -> None:    
        if(self._page==-1):
            self.changeBackground(self.backgroundt)
            
            if(self._choice==0):
                screen.blit(HEADER,(250,0))
                screen.blit(EASY,(230,90))
                screen.blit(NORMAL_LOW,(230,230))
                screen.blit(HARD_LOW,(230,360))
                screen.blit(LUNATIC_LOW,(230,490))
            elif(self._choice==1):
                screen.blit(HEADER,(250,0))
                screen.blit(EASY_LOW,(230,90))
                screen.blit(NORMAL,(230,230))
                screen.blit(HARD_LOW,(230,360))
                screen.blit(LUNATIC_LOW,(230,490))
            elif(self._choice==2):
                screen.blit(HEADER,(250,0))
                screen.blit(EASY_LOW,(230,90))
                screen.blit(NORMAL_LOW,(230,230))
                screen.blit(HARD,(230,360))
                screen.blit(LUNATIC_LOW,(230,490))
            else:
                screen.blit(HEADER,(250,0))
                screen.blit(EASY_LOW,(230,90))
                screen.blit(NORMAL_LOW,(230,230))
                screen.blit(HARD_LOW,(230,360))
                screen.blit(LUNATIC,(230,490))   
        if(self._page==0): #choice 1
            self.changeBackground(image.load(CHAR_A).convert())
            self.__player=0
            if(self._choice==0):...
            else:...
        else:#choice 2
            self.changeBackground(image.load(CHAR_B_TEST).convert())
            self.__player   = 1

    @final
    def getPlayer(self) ->  int:
        return self.__player
