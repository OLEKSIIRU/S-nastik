def loe_failist(fail:str)->list:
   jarjend=[] 
   raagi=""
   f=open(fail,'r',encoding="utf-8")
   for rida in f:
        jarjend.append(rida.strip()) # В кавычках можно укказывать знак разделения
        raagi+=rida
   f.close()
   return jarjend,raagi


def Kirjuta_failisse(fail:str,jarjend:list):
    f=open(fail,'w',encoding="utf-8")
    for item in jarjend:
        f.write(item+'\n')      
    f.close()
test_to_speech=""#---------------
paevad, test_to_speech=loe_failist("Paevad.txt")#------------
print(paevad)

list_=[]
for i in range(5):
    nimi=input(str(i+1)+".Nimi ")
    list_.append(nimi)
Kirjuta_failisse("Nimed.txt",list_)

with open('Nimed.txt', 'r') as f:
    print(f.read())
    
from os import *
if path.isfile("Nimi.txt"):   #path.isdir(kaust)
    remove("Nimed.txt") #faili kustutamine, kui ta on olemas
    from gtts import gTTS

from gtts import gTTS
def Heli(text:str,keel:str):
    obj=gTTS(text=text,lang=keel,slow=False).save("heli.mp3")
    system("heli.mp3")

Heli(test_to_speech,"et")