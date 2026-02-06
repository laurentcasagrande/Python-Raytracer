from Klasse_Vektor3 import *
from RTBefehle import *
import numpy as np
import math

class Kugel:
    def __init__(self, m, r, material):
        """
        Die material Daten geben an, wie das Licht reflektiert wird:
        C ist ein np.array: die Farbe
        0<=ka<=1: ambienter Koeffizient
        0<=kd<=1: diffuser Koeffizient
        Oft: ka=kd
        In dieser Version wird kein Licht reflektiert.
        0<=ks<=1: spekularer Koeffizient
        kp: Phong--Exponent
        material=[C,ka,kd,ks,kp]"""
        self.m = m
        self.r = r
        self.material = material

    def Schnittpunkt(self, a, v):
        alpha=sp(v,v)
        beta=2*sp(v,a)-2*sp(v,self.m)
        gamma=sp(a,a)+sp(self.m,self.m)-2*sp(a,self.m)-self.r**2
        
        diskr=(beta**2-4*alpha*gamma)

        if diskr<0:
            return Fernpunkt
        
        else:
            t1=(-beta+diskr**0.5)*(1/(2*alpha))
            t2=(-beta-diskr**0.5)*(1/(2*alpha))

            if t1 > 0 and t2 > 0:
                return a+t2*v
            elif t1 > 0 and t2 < 0:
                return a+t1*v
            else:
                return Fernpunkt

    
    def Normalenvektor(self, p):
        return Normieren(p-self.m)
    
    def Rotiert(self, achsex, achsey, theta):
        
        ZPunkt = self.m
        
        cost = np.cos(theta/180*math.pi)
        sint = np.sin(theta/180*math.pi)
        
        tx = ZPunkt.x - achsex
        ty = ZPunkt.y - achsey
        tz = ZPunkt.z
        
        
        newx = achsex + tx * cost - ty * sint
        newy = achsey + tx * sint + ty * cost
        newz = tz
        
        self.m = Vektor3(newx, newy, newz)
        
        return self


class Ebene:
    def __init__(self, punkt, normale, material):
        """
        punkt ist ein Punkt der Ebene, normale ein Normalenvektor.
        material=[F, ka, kd, kg, kexp].
        """
        self.punkt = punkt
        self.normale = normale
        self.material = material

    def Schnittpunkt(self, a, v):
        """
        Der Strahl a+v*t wird mit dem Objekt geschnitten.
        Zurückgegeben wird dieser Schnittpunkt (als Vektor3).
        Falls es keinen Schnittpunkt gibt, wird "Fernpunkt" zurückgegeben.
        """
        epsilon = 10 ** (-6)
        pkt, nvek = self.punkt, self.normale
        nenner = sp(v, nvek)
        ## Falls nenner fast 0 ist:
        if np.abs(nenner) < epsilon:
            return Fernpunkt
        else:
            t = (sp(nvek, pkt-a))/(sp(nvek,v))
            if t >= 0:
                return a+t*v
            else:
                return Fernpunkt
    
    def Normalenvektor(self,p):
        """
        Zurückgegeben wird ein Normalenvektor n der Tangentialebene im Punkt p.
        """
        return Normieren(self.normale)

class Dreieck:
    def __init__ (self,a,b,c,material):
        self.a=a
        self.b=b
        self.c=c
        self.material=material
        self.normale=vp(b-a,c-a)

    def Schnittpunkt(self,a,v):
        
        p1=self.a
        p2=self.b
        p3=self.c
        epsilon = 10 ** (-6)
        nvek = self.normale
        nenner = sp(v, nvek)

        ## Falls nenner fast 0 ist:
        if np.abs(nenner) < epsilon:
            return Fernpunkt
        else:
            t = (sp(nvek, p1-a))/(sp(nvek,v))

            if t > 0:
                s=a+t*v
                if Abstand(p1,s) < epsilon or Abstand(p2,s)<epsilon or Abstand(p3,s)<epsilon:
                    return s
                else:
                    p1s=Normieren(p1-s)
                    p2s=Normieren(p2-s)
                    p3s=Normieren(p3-s)

                    winkel1=arccos(sp(p1s,p2s))
                    winkel2=arccos(sp(p3s,p2s))
                    winkel3=arccos(sp(p1s,p3s))

                    winkel_total=winkel1+winkel2+winkel3-2*math.pi

                    if abs(winkel_total)<epsilon:
                        return a+t*v
                    else:
                        return Fernpunkt

            else:
                return Fernpunkt
    
    def Normalenvektor(self,p):
        return Normieren(self.normale)
