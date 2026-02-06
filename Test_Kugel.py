from Klasse_Vektor3 import *
from Klasse_Objekte import *
from RTBefehle import*

# Augpunkt A
# "Pixelpunkt" P1 bis P3
A = Vektor3(0,-1,2)

P1 = Vektor3(0,0,1.8)
v1 = P1 - A

P2 = Vektor3(0,0,1.5)
v2 = P2 - A

P3 = Vektor3(2,0,1.5)
v3 = P3 - A

# Kugel
m1 = Vektor3(0,3,2)
r1 = 2
Kugel1 = Kugel(m1, r1, [])

S1 = Kugel1.Schnittpunkt(A, v1)
#PrintV3(S1)
# Korrekt ist: S1 = [0, 1.042, 1.592]


S2 = Kugel1.Schnittpunkt(A, v2)
#PrintV3(S2)
# Korrekt ist: S2 = [0, 1.4, 0.8]


S3 = Kugel1.Schnittpunkt(A, v3)
#PrintV3(S3)
# Korrekt ist: S3 = [weit, weit, weit]

N1=Kugel1.Normalenvektor(v1)
#PrintV3(N1)

K1 = Kugel(Vektor3(0,4,2.5),2.5,[np.array([1.00,0.85,0.3]),1,0,0,0])
K2 = Kugel(Vektor3(-0.7,1,0.9),0.9,[np.array([0.10,0.33,0.70]),1,0,0,0])
K3 = Kugel(Vektor3(1.0,1.5,0.7),0.7,[np.array([0.70,0.20,0.20]),1,0,0,0])

Szene = [K1,K2,K3]

sichtbares_objekt, spunkt, dist = SichtbaresObjekt(A,v1,Szene)
