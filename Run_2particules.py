from Generateur import *
from Particule import *
from Univers import *

from random import random, randint


# Création du simulateur avec pas de temps de 1ms (nécessaire pour bien simuler le ressort)
Monde = Univers(step=0.01)

center = Particule(pos=v3d(0.5, 0.5, -5.),name='center',color='black',fix=True)  # fixe: déplacements bloqués
Monde.addAgent(center)
Monde.addSource(Gravite(v3d(0,-9.81)))

# particule=Particule(pos=v3d(.2, .2),name='particule',color='red',fix=False)
# particule2=Particule(pos=v3d(.2, .3),name='particule',color='blue',fix=False)
# Monde.addAgent(center,particule)

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
print(Monde.population)
# On afffiche les positions des particules:
# for t in Monde.population:
    

# On va ajouter une force de d'attraction entre center et les autres particules:
for particule in Monde.population:
    Monde.addSource(ForceField(2.,particule,center))
    

# Monde.addSource(ForceField(2.,particule,center))
# Monde.addSource(ForceField(1.,particule2,center))

# Initialiser l'affichage & lancer
Monde.gameInit(1000,700,background='white',scale=1000) # échelle 1000 -> 1 pixel = 1 mm

while Monde.run:
    Monde.gameUpdate()
sys.exit()