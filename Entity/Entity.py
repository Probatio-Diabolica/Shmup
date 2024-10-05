import math
import pygame as pgm
from pygame import Surface
from pygame import image as img
# --------------------------------------------------------------------------------------------------------------------------------------------
#////////////////////////////////// LOW LEVEL AREA //////////////////////////////////////////////////////////////////////////////////////////
class Entity:
    def __init__(self,x:float,y:float,spd:float,s:Surface) -> None:
        self.__Xpos:float=x
        self.__Ypos:float=y
        self.__speed:float=spd
        self.__sprite:Surface=s

    def getSprite(self)->Surface:
        return self.__sprite
    
    def getCoordinates(self)->tuple[float,float]:
        return (self.__Xpos,self.__Ypos)
    
    def getY(self)->float:
        return self.__Ypos

    def getX(self)->float:
        return self.__Xpos
    
    def getSPD(self)->float:
        return self.__speed
    
    def remove(self)->None:
        self.__removed=True
    
    def isremoved(self)->bool:
        return self.__removed

    def render(self,screen:Surface)->None:
        screen.blit(self.__sprite,self.getCoordinates())
    
    def destroy(self)->None:
        self.remove()
        del self
# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# ///////////////////////////////////////// BASIC IDENTITY AREA ///////////////////////////////////////////////////////////////////////////////////////////////
"""    
$ This one is one step above Low-level. however, it maintains the border of having indentity and having none.
!! will work as a base for other playable characters
// put it simply, it marks the first steps towards their real identity, something as Kingdoms,Classes,Species,etc in biology, 
-> if you took that perspective, you could say this steps actually defines  
"""
class bullet(Entity):
    _FireRate:int
    _dmg:int
    def __init__(self, x: float, y: float, spd: float, s: Surface,firerate:int) -> None:
        super().__init__(x, y, spd, s)
        self._FireRate=firerate


class Enemy(Entity):
    __fireRate:int=100
    __bullet:list=[]
    __Hp:int
    def __init__(self, x: float, y: float, spd: float,path:tuple, surface: Surface,hp:int,rep:bool=False) -> None:
        super().__init__(x, y, spd, surface)
        self.__Hp=hp
        self.__pathVar:int=0
    
    def Collision(self,p:bullet)->bool:
        distance=math.sqrt(math.pow(p.getX()-self.__Xpos,2)+ math.pow(p.getY()-self.__Ypos,2))
        if(distance<27 and distance>0):
            p.remove()
            self.__Hp-=p._dmg
            return True
        return False

    def death(self)->None:
        if(self.__Hp==0): self.destroy()

    def Move(self)->None:
        match self.__pathVar:
            case 0:
                ...

    
    def update(self,p:bullet)->None:
        self.Collision(p)
        self.death()
    
    def getBulletList(self)->list:
        return self.__bullet

#---------------------------------------------------------------------------------------------------------------------------------------------------------- 
# #///////////////////////////////////////////////////////// Static entities ////////////////////////////////
# class playerBullet(bullet):
#     _dmg:int
#     def __init__(self, t:tuple, spd: float, s: Surface,dmg:int) -> None:
#         x=t[0] + 12
#         y=t[1]
#         self._dmg=dmg
#         super().__init__(x, y, spd, s,10)
        
#     def move(self)->None:
#         if(self.__Ypos-self.__speed >-1):
#             self.__Ypos-=self.__speed


# class enemyBullet(bullet):
#     def __init__(self, x: float, y: float, spd: float, s:Surface, firerate: int) -> None:
#         super().__init__(x, y, spd, s, firerate)
    
#     def move(self)->None:
#         if(self.__Ypos-self.__speed >-1):
#             self.__Ypos+=self.__speed
    

# # --------------------------------------------------------------------------------------------------------------------------

# class redBullet(playerBullet):
#     __fireRate:int=10
#     def __init__(self, t: tuple, spd: float, s:Surface= img.load("Assets/bullets/playerB/two.png")) -> None:
#         super().__init__(t, spd, s,40)
    
#     def getFireRate(self)->int:
#         return self.__fireRate

    
    

