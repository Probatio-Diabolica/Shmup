from Entity.Entity import img,Surface

from .basePlayer import MC

class characterA(MC):
    def __init__(self, x: float, y: float, spd: float, surface: Surface )-> None:
        # super().__init__(x, y, spd, surface,48,623)
        super().__init__(x, y, spd, surface)

        # self.__bulletType=playerBullet(self.getCoordinates(),20,img.load("Assets/Bullets/playerB/one.png"),20)
        self.__fireRate=90

"""
class CharacterA2(MC):
    def __init__(self, x: float, y: float, spd: float, surface: Surface) -> None:
        super().__init__(x, y, spd, surface)        
        self.__bulletType=self.__bulletType=playerBullet(self.getCoordinates(),20,img.load(""),30 )
        self.fireRate=100

class characterB(MC):
    def __init__(self, x: float, y: float, spd: float, surface: Surface) -> None:
        super().__init__(x, y, spd, surface)
        self.__bulletType=self.__bulletType=playerBullet(self.getCoordinates(),20,img.load(""),40 )
        self.__fireRate=150

class CharacterB2(MC):
    def __init__(self, x: float, y: float, spd: float, surface: Surface) -> None:
        super().__init__(x, y, spd, surface)        
        self.__bulletType=self.__bulletType=playerBullet(self.getCoordinates(),20,img.load(""),30 )
        self.__fireRate=90
"""