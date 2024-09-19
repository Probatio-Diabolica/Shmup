from State import baseWindow
from pygame import Surface,image
from typing import final
from .stateConf import HUD
from Entity import characterA,MC




@final
class play(baseWindow):
    """
    playing space   
    x= 48 |  48 | 623 | 623 \n
    y= 25 | 696 | 696 |  25

    note: make sure to minus the sprite lenght from this playing space
    """
    _ID         : int       = 100
    __stageID   : int       = 0

    _Player     : MC
    """
        * 1 -> stage 1
        * 2 -> stage 2
        * 3 -> stage 3
        * 4 -> stage 4
        * 5 -> stage 5
        * 6 -> stage 6
        * 7 -> extra stage
    """
    __Right     : bool      = False
    __Left      : bool      = False
    __Up        : bool      = False
    __Down      : bool      = False
    __Score     : int       = 0
    __HighScore : int       # import from high score

    def getPlayer(self)->MC:
        return self._Player
    
    def __init__(self,player ,Background: Surface = image.load(HUD), value: int = 0) -> None:
        super().__init__(Background, value)
        # self._Player=characterA((623-48)/2,696-100,5,image.load("Assets/Player/Hitbox.png"))
        self._Player=player        


    def changeStage(self,screen:Surface,stageID:int,practice:bool=False)-> None:
        change:bool
        self.__stageID=stageID
        if(practice): change=False
        else: change = True

        if(self.__stageID==1):
            self.Stage1(screen,change)
        elif(self.__stageID==2):
            self.Stage2(screen,change)
        elif(self.__stageID==3):
            self.Stage3(screen,change)
        elif(self.__stageID==4):
            self.Stage4(screen,change)
        elif(self.__stageID==5):
            self.Stage5(screen,change)
        elif(self.__stageID==6):
            self.Stage6(screen)
        elif(self.__stageID==7):
            self.StageEX(screen)
            


    #!! if change is "True", then it means we are actually playing not practicing. 
    def Stage1(self,screen:Surface,change:bool=False)->None:...
    def Stage2(self,screen:Surface,change:bool=False)->None:...
    def Stage3(self,screen:Surface,change:bool=False)->None:...
    def Stage4(self,screen:Surface,change:bool=False)->None:...
    def Stage5(self,screen:Surface,change:bool=False)->None:...
    def Stage6(self,screen:Surface)->None:...
    def StageEX(self,screen:Surface)->None:...

    def renderActivity(self, screen: Surface) -> None:
        screen.blit(self._Player.getSprite(),self._Player.getCoordinates())
        # self.Stage1(screen)
        # self.Stage2(screen)
        # self.Stage3(screen)
        # self.Stage4(screen)
        # self.Stage5(screen)
        # self.Stage6(screen)