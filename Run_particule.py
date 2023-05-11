from Generateur import ForceConst, Gravite, Viscosity, Ressort
from Particule import *
from Univers import *

from random import random, randint

pivot = Particule(pos=v3d(0.5, 0.5, -5.),name='center',color='black',fix=True)  # fixe: déplacements bloqués
masse2 = Particule(name='masse-2',pos=v3d(0.5,0.1),color='red')

# Création du simulateur avec pas de temps de 1ms (nécessaire pour bien simuler le ressort)
Monde = Univers(step=0.001)

# Monde.addAgent(boule,boule2)
Monde.addAgent(pivot,masse2)




Monde.addSource(Gravite(v3d(0,-10)), Viscosity(0.2))

# Initialiser l'affichage & lancer
Monde.gameInit(1024,768,background='gray',scale=1000) # échelle 1000 -> 1 pixel = 1 mm

while Monde.run:
        
# 
    Monde.gameUpdate()

sys.exit()