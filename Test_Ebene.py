from Klasse_Vektor3 import *
from Klasse_Objekte import *

# Augpunkt A
# "Pixelpunkt" P1 bis P2
A = Vektor3(0,-1,2)

P1 = Vektor3(0,0,1.8)
v1 = P1 - A

P2 = Vektor3(1,0,1.5)
v2 = P2 - A


# Ebene
punkt1 = Vektor3(0,5,0)
normale1= Vektor3(0,-1,1)
Ebene1 = Ebene(punkt1, normale1, [])


S1 = Ebene1.Schnittpunkt(A, v1)
PrintV3(S1)
# Korrekt ist: S1 = [0, 5.667, 0.667]

S2 = Ebene1.Schnittpunkt(A, v2)
PrintV3(S2)
# Korrekt ist: S2 = [5.333, 4.333, -0.667]

v3 = Vektor3(0,-0.9,0.8)
S3 = Ebene1.Schnittpunkt(A, v3)
PrintV3(S3)
# Korrekt ist: S3 = [weit, weit, weit]
