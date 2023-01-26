#Créer un programme horloge
#Format heure:minutes:secondes
#actualiser/secondes
#MaJ par la fonction "afficher_heure"
#Afficher message heure actuelle=heure alarme

import time
from time import strftime

def sonnerie(heure,minute,seconde):
    ha = 13
    ma = 50
    sa = 20
    if heure == ha and minute == ma and seconde == sa:
        print('Debout!')
        return True

def afficher_heure():
    i = 1  
    heure = int(strftime('%H'))
    minute = int(strftime('%M'))
    seconde = int(strftime('%S'))
    while i > 0:
        if seconde == 60:
            minute += 1
            seconde = 0
        if minute == 60:
            heure += 1
            minute = 0
        print(str(heure).rjust(2, '0')+":"+str(minute).rjust(2, '0')+":"+str(seconde).rjust(2, '0'))
        time.sleep(1)
        seconde += 1
        sonnerie(heure,minute,seconde)

afficher_heure()