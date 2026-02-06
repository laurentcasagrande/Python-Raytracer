import numpy as np
import time
from Klasse_Vektor3 import *
from Klasse_Licht import *
from Klasse_Objekte import *
from RTBefehle import *
from RTDefinitionenFarbenMaterial5 import *
from Bild_DarstellenSpeichern import *

#Hintergrundfarbe
Hintergrundfarbe = schwarz

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
u0, v0 = -3, 2
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
Iamb = 0.8
AmbientesLicht = Ambientes_Licht(Famb, Iamb)


## Definiere später eine Liste von Lichtquellen
Lichterliste = []
## Komponiere später eine Szene

K1 = Kugel(Vektor3(0,4,2.5),2.5,[np.array([1.00,0.85,0.3]),1,0,0,0])
K2 = Kugel(Vektor3(-0.7,1,0.9),0.9,[np.array([0.10,0.33,0.70]),1,0,0,0])
K3 = Kugel(Vektor3(1.0,1.5,0.7),0.7,[np.array([0.70,0.20,0.20]),1,0,0,0])

Szene = [K1,K2,K3]


#Bild speichern. Als png oder auch als eps-Datei möglich.
Speichern = False
Dateiname = "Testbild01.png"
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
        frb = BerechneFarbe(Auge, vrichtung, Auge, Szene,
                            Hintergrundfarbe, AmbientesLicht, Lichterliste)
        bild_matrix[i,j] = np.clip(frb, 0, 1)
print("Zeitdauer für die Berechnung: ", time.time() - t0)
Bild_DarstellenSpeichern(bild_matrix, hor, ver, Dotspi, Speichern, Dateiname)
