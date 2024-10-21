from State import baseWindow
from pygame import Surface,image,Rect,surfarray
from .Fonts import menuFont,font_Default_Color,black,msgPair,white
from Scripts import getDialog
from typing import final
from .stateConf import menuTestPath,homeTestPath,BLACK_BG,CHAR_B_TEST,difficultyPath,CHAR_A
from .UI_Panels import HEADER,EASY,NORMAL,HARD,LUNATIC,EASY_LOW,NORMAL_LOW,HARD_LOW,LUNATIC_LOW
# import numpy as np
# from random import randrange
TOP=1
EZ=11
EZ_T=12
N=22
N_T=23
H=33
H_T=34
L=44
L_T=45

# !! char select is now the most unoptimized part
@final
class Character(baseWindow):
    _ID=21
    __TEXT      : msgPair    =   msgPair(getDialog(0),(222,222))
    _choice     : int        =   0
    __netPages  : int        =   2
    _page       : int        =   -1
    __player    : int        =   0   
    def __init__(self, Background: Surface = image.load(homeTestPath), value: int = 0) -> None:
        # !! fix one
        self.__UI_panels={TOP:HEADER.convert_alpha(),EZ:EASY.convert(),EZ_T:EASY_LOW.convert_alpha(),N:NORMAL.convert(),N_T:NORMAL_LOW.convert_alpha(),H:HARD.convert(),H_T:HARD_LOW.convert_alpha(),L:LUNATIC.convert(),L_T:LUNATIC_LOW.convert_alpha()}
        print("<Char class> [Loc: in State module] ID = ", self._ID)
        self.backgrounds={-1:"home",0:"char A", 1:"char 2"}
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
            self.changeBackground(self.backgroundt.convert())
            
            if(self._choice==0):
                screen.blit(self.__UI_panels[TOP],   (250,0))
                screen.blit(self.__UI_panels[EZ],   (230,90))
                screen.blit(self.__UI_panels[N_T],   (230,230))
                screen.blit(self.__UI_panels[H_T],   (230,360))
                screen.blit(self.__UI_panels[L_T],   (230,490))
            elif(self._choice==1):
                screen.blit(self.__UI_panels[TOP],(250,0))
                screen.blit(self.__UI_panels[EZ_T],(230,90))
                screen.blit(self.__UI_panels[N],(230,230))
                screen.blit(self.__UI_panels[H_T],(230,360))
                screen.blit(self.__UI_panels[L_T],(230,490))
            elif(self._choice==2):
                screen.blit(self.__UI_panels[TOP],(250,0))
                screen.blit(self.__UI_panels[EZ_T],(230,90))
                screen.blit(self.__UI_panels[N_T],(230,230))
                screen.blit(self.__UI_panels[H],(230,360))
                screen.blit(self.__UI_panels[L_T],(230,490))
            else:
                screen.blit(self.__UI_panels[TOP],(250,0))
                screen.blit(self.__UI_panels[EZ_T],(230,90))
                screen.blit(self.__UI_panels[N_T],(230,230))
                screen.blit(self.__UI_panels[H_T],(230,360))
                screen.blit(self.__UI_panels[L],(230,490))   
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
