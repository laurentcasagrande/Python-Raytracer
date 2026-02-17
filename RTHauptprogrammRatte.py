import numpy as np
import time
from Klasse_Vektor3 import *
from Klasse_Licht import *
from Klasse_Objekte import *
from RTBefehle import *
from RTDefinitionenFarbenMaterial5 import *
from Bild_DarstellenSpeichern import *
import Ratte

#Hintergrundfarbe
Hintergrundfarbe = np.array([26/255,24/255,27/255])

#Augpunkt sollte so gesetzt werden, dass auge-zentrum normal ist zur Bildebene.
#Und auch nicht zu nah an der Bildebene. yA = -6 ist eine gute Wahl.
#Ansonsten entstehen schnell Verzerrungen.
zA = 1.7
yA = -6
Auge = Vektor3(0, yA, zA)
## Zentrum der Blickrichtung
Zentrum = Vektor3(0, 0, zA)

#Wahl Bildausschnitt
#Linke obere Ecke p0 und rechte untere Ecke p1
#p0:=zentrum+u0*b1+v0*b2; p1:=zentrum+u1*b1+v1*b2;
u0, v0 = -3, 3
#Ist u1=-u0, so ist das zentrum in der Mitte des Bildes
u1, v1 = -u0, -zA
#Anzahl Pixel in der Horizontalen
hor = 600
#Einheit wird berechnet
Einheit = (u1 - u0) / hor
#Pixelanzahl ver wird berechnet:
ver = int( (v0 - v1) / Einheit )

## Ambientes Licht: weiss
Famb = weiss
## Intensität des ambienten Lichts
Iamb = 1
AmbientesLicht = Ambientes_Licht(Famb, Iamb)



L1=Punktlichtquelle(Vektor3(3,-0.5,5.1),weiss,1,[1,0.1,0.05])
## Definiere später eine Liste von Lichtquellen
Lichterliste = [L1]
## Komponiere später eine Szene

M1 = [np.array([0.1,0.1,1.0]),0.3,0.7,0.6,10]
M2 = [np.array([1,0.85,0.3]),0.4,0.6,0.3,5]
M3 = [np.array([1,1,1]),0.4,0.6,0,0]

K1 = Kugel(Vektor3(0,4,2.5),2.5,[np.array([1.00,0.85,0.3]),0.2,0.8,0,0])
K2 = Kugel(Vektor3(-0.7,1,0.9),0.9,[np.array([0.10,0.33,0.70]),0.3,0.7,0.6,10])
K3 = Kugel(Vektor3(1.0,1.5,0.7),0.7,[np.array([0.70,0.20,0.20]),0.4,0.6,0.3,5])


E1 = Ebene(Vektor3(0,0,0),Vektor3(0,0,1), M1)






Szene = [E1]





for ind in range(72):
    #.Rotiert(0, 4, i*10)

    theta = 5
    
    frameszene = []
    for obj in Szene:
        frameszene.append(obj)
    
    for face in Ratte.Ratte:
        frameszene.append(face.Rotiert(Ratte.m_Ratte.x, Ratte.m_Ratte.y, theta))
        
        

    
    #Bild speichern. Als png oder auch als eps-Datei möglich.
    Speichern = True
    Dateiname = f"Ratte/Ratte{ind}.png"
    Dotspi = 100
    ######## Ende der Eingabe ####################################
    
    ## Nicht verändern:
    t0 = time.time()
    #Die bild_matrix wird erzeugt und mit Einträgen [0,0,0] gefüllt.
    bild_matrix = np.zeros((ver, hor, 3))
    #Hauptschleifen über jeden Bildfensterpixel
    for i in range(ver):
        for j in range(hor):
            p = IndicesZuPunkt(i, j, Zentrum, Einheit, basisvektor1, basisvektor2, u0, v0)
            vrichtung = p - Auge
            frb = BerechneFarbe(Auge, vrichtung, Auge, frameszene,
                                Hintergrundfarbe, AmbientesLicht, Lichterliste)
            bild_matrix[i,j] = np.clip(frb, 0, 1)
    print(f"{ind+1}/72: Zeitdauer für die Berechnung: ", time.time() - t0)
    Bild_DarstellenSpeichern(bild_matrix, hor, ver, Dotspi, Speichern, Dateiname)
