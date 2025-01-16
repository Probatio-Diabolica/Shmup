
dialogPath:str ="bin/dialogs.txt"
# print("TEST [dialogs.py]") <- no matter what it'll get executed only once
def getDialog(dialogLINE:int)->str:
    currLine=0
    with open(dialogPath,encoding='utf-8') as f:
        while(currLine<dialogLINE):
            f.readline()
            
            currLine+=1
        dialog= f.readline()
        f.close()
        return dialog
