
from pygame import Surface

from Entity.Entity import Entity
"""
class MC(Entity):
    
        # -> primitive Player, Derived from Entity. 
    

    def __init__(self, x: float, y: float,spd:float, surface: Surface) -> None:
        self.__Left         :bool   =   False
        self.__Right        :bool   =   False
        self.__Up           :bool   =   False
        self.__Down         :bool   =   False
        self.__fire         :bool   =   False
        self.__fireRate     :int    =   100
        self.__bullet       :list   =   []
        self.__bulletType   :list
        self.__Lives        :int
        self._Xpos          :float  =   100
        self._Ypos          :float  =   600
        self.__Lives        :int    =   3
        self.__speed        :float  =   spd
        super().__init__(x, y,spd, surface)
        
        #self.__fireRate=redBullet.getFireRate()
    def toggleUp(self):
        if(self.__Up): self.__Up=False
        else : self.__Up=True

    def toggleDown(self):
        if(self.__Down): self.__Down=False
        else : self.__Down=True

    def toggleLeft(self):
        if(self.__Left): self.__Left=False
        else : self.__Left=True

    def toggleRight(self):
        if(self.__Right): self.__Right=False
        else : self.__Right=True

    def updates(self):
        self.playerMove()
    def Move(self,x:float=0,y:float=0)->None:
        self._Xpos+=x
        self._Ypos+=y
            
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
"""

class MC:
    def __init__(self, x: float, y: float,spd:float, surface: Surface,xlimL:float=48,xLimR:float=623,yLimU:float=25,yLimD:float=696) -> None:
        self.__Left         :bool       =   False
        self.__Right        :bool       =   False
        self.__Up           :bool       =   False
        self.__Down         :bool       =   False
        self.__fire         :bool       =   False
        self.__fireRate     :int        =   100
        self.__bullet       :list       =   []
        self.__bulletType   :list   
        self.__Lives        :int    
        self.__Xpos         :float      =   x
        self.__Ypos         :float      =   y
        self.__Lives        :int        =   3
        self.__speed        :float      =   spd
        self.__sprite       :Surface    =   surface
        self.__xLimL        :float      =   xlimL
        self.__xLimR        :float      =   xLimR
        self.__yLimU        :float      =   yLimU   
        self.__yLimD        :float      =   yLimD

    def getX(self):
        return self.__Xpos
    
    def getY(self):
        return self.__Ypos
    
    def getCoordinates(self) -> tuple:
        return (self.__Xpos,self.__Ypos)
    
    def getSprite(self):
        return self.__sprite
    
    def toggleUp(self):
        if(self.__Up): self.__Up=False
        else : self.__Up=True

    def toggleDown(self):
        if(self.__Down): self.__Down=False
        else : self.__Down=True

    def toggleLeft(self):
        if(self.__Left): self.__Left=False
        else : self.__Left=True

    def toggleRight(self):
        if(self.__Right): self.__Right=False
        else : self.__Right=True

    def updates(self):
        self.playerMove()

    def Move(self,x:float=0,y:float=0)->None:
        self.__Xpos+=x
        self.__Ypos+=y
    
    def playerMove(self)->None:
        if(self.__Left and self.getX()>self.__xLimL+3):
            self.Move(-1*(self.__speed),0)
        if(self.__Right and self.getX()<self.__xLimR-12):
            self.Move(self.__speed,0)
        if(self.__Up and self.getY()>self.__yLimU+3):
            self.Move(0,-1*(self.__speed))
        if(self.__Down and self.getY()<self.__yLimD-12):
            self.Move(0,self.__speed)
    
