from vector3D import Vecteur3D as v3d



class ForceConst(object):
    def __init__(self,value=v3d(),*args):
        self.force=value
        self.agents=list(args)
        
    def __str__(self):
        return 'ForceConst('+str(self.force)+')'
        
    def effect(self,particule):
        if not self.agents:
            return self.force
            
        elif particule in self.agents:  
            return self.force
            
        else :
            return v3d()
    

     
class Gravite(object):
    def __init__(self,direction=v3d()):
        self.direction=direction
        
    def effect(self,particule):
        return particule.masse * self.direction



class Viscosity(object):
    def __init__(self,coef=0):
        self.coef=coef
                
    def effect(self,particule):
        return -particule.getVit() * self.coef
   
    
    
class Ressort(object):
    def __init__(self,p0,p1,raideur=0.,amortissement=.0,l0=0):
        self.raideur = raideur
        self.l0 = l0
        self.p0 = p0 # particule 0
        self.p1 = p1 # particule 1
        self.amortissement=amortissement
        
    def effect(self,particule):
        if particule is self.p0:
            n=self.p1.getPos() - self.p0.getPos() 
            v= (self.p1.getVit() - particule.getVit()) ** n.norm()
        
        elif particule is self.p1:
            n=self.p0.getPos() - self.p1.getPos() 
            v= (self.p0.getVit() - particule.getVit()) ** n.norm()
        
        else: return v3d()
        
        return ((n.mod()-self.l0) * self.raideur + self.amortissement * v) * n.norm() # force
    
    
    
class ForceField(object):
    def __init__(self, G, *args):
        self.G = G
        self.agents = list(args)
    
    def force(self, p0, p1):
        """Calcule la force gravitationnelle exercée par p0 sur p1"""
        r = p1.getPos() - p0.getPos()
        distance = r.mod()
        direction = r.norm()
        force_magnitude = (self.G * p0.masse * p1.masse) / (distance**2)
        return direction * force_magnitude

    def effect(self, particule):
        """Calcule la force résultante exercée sur la particule"""
        force_total = v3d()
        for agent in self.agents:
            if agent != particule:
                force_total += self.force(particule, agent)
        return force_total