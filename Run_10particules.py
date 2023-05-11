from Generateur import *
from Particule import *
from Univers import *

from random import random, randint


# Création du simulateur avec pas de temps de 1ms (nécessaire pour bien simuler le ressort)
Monde = Univers(step=0.001)

center = Particule(pos=v3d(0.5, 0.5, -5.),name='center',color='black',fix=True)  # fixe: déplacements bloqués
Monde.addAgent(center)

for t in range(10):
    name = 'Particule'+str(t)
    x = random()*10
    y= random()*7
    
    r = random()
    g = random()
    b = random()
    rgb = (r,g,b,1)
      
    particule=Particule(v3d(x,y),name=name,color=rgb,fix=False)
    
    Monde.addAgent(particule)


# On va ajouter une force de d'attraction entre center et les autres particules:
for t in Monde.population[1:]:
    Monde.addSource(ForceField(t,center,9.81))
    
# Monde.addSource(Gravite(v3d(0,-9.81)))

# Initialiser l'affichage & lancer
Monde.gameInit(1024,768,background='gray',scale=1000) # échelle 1000 -> 1 pixel = 1 mm

while Monde.run:
        
# 
    Monde.gameUpdate()

sys.exit()