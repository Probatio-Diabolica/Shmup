#----------------------------------------------------------------------------------------------------------------------
# !! PATHS

from cryptography.fernet import Fernet

key =Fernet.generate_key()
configPath="bin/Settings.conf"


#
gameHeight:int 
gameWidth:int 

with open(configPath,encoding='utf-8') as f:
    gameWidth=int(f.readline())
    gameHeight=int(f.readline())

# print("this gets executed [Loc gameConf.py]") 
# !! indeed this gets executed first for some odd reasons. I think it just runs and complies each and everyFile that gets imported
#NOTE: there's a catch to it, that is; the imported file will get interpreted only once in each time the applicatiion has been booted up
# !! those which are not imported will not get interpreted, obvi :V