from Generateur import *
from Particule import *
from Univers import *

from random import random, randint


# Création du simulateur avec pas de temps de 10ms, une largeur de 1000 et une hauteur de 700
Monde = Univers(step=0.01, W=1000, H=700)

# Une particule pivot fixe au centre de l'écran:
center = Particule(pos=v3d(0.5, 0.5, -5.),name='center',color='black',fix=True)  # fixe: déplacements bloqués
# center = Particule(pos=v3d(0.5, 0.5, -5.),name='center',color='black',fix=True)  # fixe: déplacements bloqués
Monde.addAgent(center)
Monde.addSource(Gravite(v3d(0,-9.81)))

for t in range(10):
    name = 'Particule'+str(t)
    x = random()
    y= random()
    
    r = random()
    g = random()
    b = random()
    rgb = (r,g,b,1)
      
    particule=Particule(pos=v3d(x,y),name=name,color=rgb,fix=False)
    
    Monde.addAgent(particule)

# On va ajouter une force de d'attraction entre center et les autres particules:
for particule in Monde.population:
    Monde.addSource(ForceField(1.,particule,center))

# Initialiser l'affichage & lancer
Monde.gameInit(1000,700,background='white',scale=1000) # échelle 1000 -> 1 pixel = 1 mm

while Monde.run:
    Monde.gameUpdate()
sys.exit()