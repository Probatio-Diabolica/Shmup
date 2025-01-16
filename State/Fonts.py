from pygame import font,Surface,Rect
from typing import final
font.init()

# Fonts
# menuFont= font.Font("Assets/Fonts/menuFont1.TTF",20)
# menuFont= font.Font("Assets/Fonts/menuFont3.TTF",20)
# menuFont= font.Font("Assets/Fonts/menuFont4.TTF",20)
# menuFont= font.Font("Assets/Fonts/menuFont5.TTF",20)
# menuFont= font.Font("Assets/Fonts/menuFont6.TTF",20)
# menuFont= font.Font("Assets/Fonts/menuFont7.TTF",20)
menuFont= font.Font("Assets/Fonts/menuFont8.TTF",20)
# menuFont= font.Font("Assets/Fonts/menuFont9.TTF",20)
# menuFont= font.Font("Assets/Fonts/menuFont10.TTF",20)
# FonrColors
font_Default_Color=(255,255,255,255)
font_Selected_Color=(255,255,0,255)
black=(0,0,0,0)
white = (255,255,255,255)

@final
class msgPair:
    __text          : str
    __location      : tuple[int,int] # [width , height]
    # __width         : float
    # __height        : float
    __surface       : Surface
    __surfaceRect   : Rect
    __color         : tuple[int,int,int,int]   
    
    def __init__(self,text:str,location:tuple[int,int],color:tuple[int,int,int,int]=white) ->None:
        self.__text=text
        self.__location=location
        # self.__width=location[0]
        # self.__height=location[1]
        self.__color = color
        self.__surface = menuFont.render(self.__text,True,self.__color,None)
        self.__surfaceRect=self.__surface.get_rect()
        self.__surfaceRect.center=location #Location = (width,height)

    
    def getMsg(self)->str:
        return self.__text
    
    def getLocation(self)->tuple:
        return self.__location
    
    def getWidth(self)->int:
        return self.__location[0]
    
    def getHeight(self)->int:
        return self.__location[1]
    
    def getSurface(self)->Surface:
        return self.__surface
    
    def changeColor(self,color:tuple[int,int,int,int])->None:
        self.__surface = menuFont.render(self.__text,True,color,None)
    
    def setText(self,text:str)->None:
        self.__text=text
        self.__surface = menuFont.render(self.__text,True,self.__color,None)
        self.__surfaceRect=self.__surface.get_rect()
    # def render(self,screen)->None:
    #     screen.blit(self.__surface,self.__location)
    #     pgm.display.update()
    
    # def move(self,byWidth:float)->None:
    #     self.__width-=byWidth
    #     self.__location=(int(self.__width),int(self.__height))
    #     self.__surfaceRect.center=(int(self.__width),int(self.__height))
    # def move(self,onWidth=0,onHeight=0):
    #     self.__location

