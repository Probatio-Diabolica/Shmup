from Entity.Entity import Enemy,Surface,img

class Dragon(Enemy):
    def __init__(self, x: float, y: float, spd: float, s: Surface=img.load("Assets/Enemy/dragon.png")) -> None:
        super().__init__(x, y, spd, s,100)
        
class e2(Enemy):
    def __init__(self, x: float, y: float, spd: float, s: Surface, hp: int) -> None:
        super().__init__(x, y, spd, s, hp)

class e3(Enemy):
    def __init__(self, x: float, y: float, spd: float, s: Surface, hp: int) -> None:
        super().__init__(x, y, spd, s, hp)

class e4(Enemy):
    def __init__(self, x: float, y: float, spd: float, s: Surface, hp: int) -> None:
        super().__init__(x, y, spd, s, hp)

class e5(Enemy):
    def __init__(self, x: float, y: float, spd: float, s: Surface, hp: int) -> None:
        super().__init__(x, y, spd, s, hp)

class e6(Enemy):
    def __init__(self, x: float, y: float, spd: float, s: Surface, hp: int) -> None:
        super().__init__(x, y, spd, s, hp)

class e7(Enemy):
    def __init__(self, x: float, y: float, spd: float, s: Surface, hp: int) -> None:
        super().__init__(x, y, spd, s, hp)

class e8(Enemy):
    def __init__(self, x: float, y: float, spd: float, s: Surface, hp: int) -> None:
        super().__init__(x, y, spd, s, hp)
