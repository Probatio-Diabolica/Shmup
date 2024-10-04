from Entity.Entity import Enemy,Surface,img

class e1(Enemy):
    def __init__(self, x: float, y: float, spd: float,pathway:tuple, repeat:bool,s: Surface=img.load("Assets/Enemy/enemy.png")) -> None:
        super().__init__(x, y, spd, surface=s,path=pathway,rep=repeat,hp=100)
        
# class e2(Enemy):
#     def __init__(self, x: float, y: float, spd: float, s: Surface, hp: int) -> None:
#         super().__init__(x, y, spd, s, hp)

# class e3(Enemy):
#     def __init__(self, x: float, y: float, spd: float, s: Surface, hp: int) -> None:
#         super().__init__(x, y, spd, s, hp)

# class e4(Enemy):
#     def __init__(self, x: float, y: float, spd: float, s: Surface, hp: int) -> None:
#         super().__init__(x, y, spd, s, hp)

# class e5(Enemy):
#     def __init__(self, x: float, y: float, spd: float, s: Surface, hp: int) -> None:
#         super().__init__(x, y, spd, s, hp)

# class e6(Enemy):
#     def __init__(self, x: float, y: float, spd: float, s: Surface, hp: int) -> None:
#         super().__init__(x, y, spd, s, hp)

# class e7(Enemy):
#     def __init__(self, x: float, y: float, spd: float, s: Surface, hp: int) -> None:
#         super().__init__(x, y, spd, s, hp)

# class e8(Enemy):
#     def __init__(self, x: float, y: float, spd: float, s: Surface, hp: int) -> None:
#         super().__init__(x, y, spd, s, hp)
