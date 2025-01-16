from pygame import Surface,image,surfarray
import numpy as np
from .stateConf import difficultyPath
class UI:
    __factor    : float = 1
    __surface   : Surface
    def __init__(self,texture:Surface) -> None:...

    def manageContrast(self,factor:float)->Surface:...
    
    def manageTransperancy(self,factor:float)->Surface:...

    def fadeIn(self,time:int,dirMov:float)->None:...
    def fadeOut(self,time:int,dirMov:float)->None:...

#------------------------------Difficulty selection--------------------------------------------------

HEADER_PATH     =   difficultyPath + "CharacterSelectionTab.png"
EASY_PATH       =   difficultyPath + "Easy.png"   
NORMAL_PATH     =   difficultyPath + "Normal.png"
HARD_PATH       =   difficultyPath + "Hard.png"
LUNATIC_PATH    =   difficultyPath + "Lunatic.png"
HEADER  :   Surface     =image.load(HEADER_PATH)
EASY    :   Surface     =image.load(EASY_PATH)
NORMAL  :   Surface     =image.load(NORMAL_PATH)
HARD    :   Surface     =image.load(HARD_PATH)
LUNATIC :   Surface     =image.load(LUNATIC_PATH)

def contrastManager(surface, factor:float=0.5):
    # arr = surfarray.pixels3d(surface)
    arr = surfarray.pixels3d(surface)
    mean = np.mean(arr, axis=(0, 1))
    arr = (arr - mean) * factor + mean
    return surfarray.make_surface(arr.astype('uint8'))

EASY_LOW    :Surface = contrastManager(EASY)
NORMAL_LOW  :Surface = contrastManager(NORMAL)
HARD_LOW    :Surface = contrastManager(HARD)
LUNATIC_LOW :Surface = contrastManager(LUNATIC)
EASY_LOW.set_alpha(128)
NORMAL_LOW.set_alpha(128)
HARD_LOW.set_alpha(128)
LUNATIC_LOW.set_alpha(128)

# CS_UI:tuple = (image.load(HEADER_PATH),image.load(EASY_PATH),image.load(NORMAL_PATH),image.load(HEADER_PATH),image.load(LUNATIC_PATH))
#-----------------------------Player Assets------------------------------------------------------------

#-----------------------------Enemy Assets ------------------------------------------------------------



