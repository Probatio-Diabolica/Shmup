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

    def render(self,a:Surface)->None:
        a.blit(self.__sprite,self.getCoordinates())
    
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
    
class MC(Entity):
    """
        -> primitive Player, Derived from Entity. 
    """

    def __init__(self, x: float, y: float,spd:float, surface: Surface) -> None:
        self.__Left         :bool   =   False
        self.__Right        :bool   =   False
        self.__Up           :bool   =   False
        self.__Down         :bool   =   False
        self.__fire         :bool   =   False
        self.__fireRate     :int    =   100
        self.__bullet       :list   =   []
        self.__bulletType   :bullet
        self.__Lives        :int
        self._Xpos          :float  =   100
        self._Ypos          :float  =   600
        self.__Lives        :int    =   3
        super().__init__(x, y,spd, surface)
        
        #self.__fireRate=redBullet.getFireRate()

    def Move(self,x:float=0,y:float=0)->None:
        self.Xpos+=x
        self.Ypos+=y
            
    def fireReady(self)->bool:
        if(self.__fireRate==100):
            self.__fireRate-=1
            return True
        elif(self.__fireRate<0):
            self.__fireRate=100
            return False
        self.__fireRate-=1
        return False

    def minus(self)->None:
        self.__Lives-=1
    
    def reset(self)->None:
        self.Xpos=100
        self.Ypos=400

    def playerMove(self)->None:
        if(self.__Left and self.getX()>-1):
            self.Move(-1*(self.__speed),0)
        if(self.__Right and self.getX()<700):
            self.Move(self.__speed,0)
        if(self.__Up and self.getY()>-1):
            self.Move(0,-1*(self.__speed))
        if(self.__Down and self.getY()<500):
            self.Move(0,self.__speed)
    
    def shot(self)->None:
        if(self.__fire and self.fireReady()):
            self.__bullet.append(self.__bulletType)

    def bulletUpdate(self)->None:
        self.shot()
        for i in range(0,len(self.__bullet)):
            self.__bullet[i].move()
        index:int =0
        while(index<len(self.__bullet) and (self.__bullet[index].getY()<=0 or self.__bullet[index].isremoved()) ):    
            del self.__bullet[index]
    
    def getBulletList(self)->list:
        return self.__bullet

class Enemy(Entity):
    __fireRate:int=100
    __bullet:list=[]
    __Hp:int
    def __init__(self, x: float, y: float, spd: float, s: Surface,hp:int) -> None:
        super().__init__(x, y, spd, s)
        self.__Hp=hp
    
    def Collision(self,p:bullet)->bool:
        distance=math.sqrt(math.pow(p.getX()-self.__Xpos,2)+ math.pow(p.getY()-self.__Ypos,2))
        if(distance<27 and distance>0):
            p.remove()
            self.__Hp-=p._dmg
            return True
        return False

    def death(self)->None:
        if(self.__Hp==0): self.destroy()

    def Move(self,x:float=0,y:float=0)->None:
        self.__Xpos+=x
        self.__Ypos+=y
    
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

    
    

