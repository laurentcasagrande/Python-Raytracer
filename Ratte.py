import numpy as np
from Klasse_Vektor3 import *
from Klasse_Licht import *
from Klasse_Objekte import *
from RTBefehle import *
from RTDefinitionenFarbenMaterial5 import*
m_Ratte = Vektor3(0,3,3)
material_Ratte=[braun,0.3,0.7,0.6,10]
Grösse=1

Fuss1=(Dreieck((m_Ratte+Grösse*Vektor3(-1,-0.5,-0.25)),(m_Ratte+Grösse*Vektor3(-0.975,-0.5,-0.45)),(m_Ratte+Grösse*Vektor3(-0.95,-0.5,-0.25)),material_Ratte))
Fuss2=(Dreieck((m_Ratte+Grösse*Vektor3(1,-0.5,-0.25)),(m_Ratte+Grösse*Vektor3(0.975,-0.5,-0.45)),(m_Ratte+Grösse*Vektor3(0.95,-0.5,-0.25)),material_Ratte))
Fuss3=(Dreieck((m_Ratte+Grösse*Vektor3(-1,0.5,-0.25)),(m_Ratte+Grösse*Vektor3(-0.975,0.5,-0.45)),(m_Ratte+Grösse*Vektor3(-0.95,0.5,-0.25)),material_Ratte))
Fuss4=(Dreieck((m_Ratte+Grösse*Vektor3(1,0.5,-0.25)),(m_Ratte+Grösse*Vektor3(0.975,0.5,-0.45)),(m_Ratte+Grösse*Vektor3(0.95,0.5,-0.25)),material_Ratte))

Körper1=(Dreieck((m_Ratte+Grösse*Vektor3(-1,-0.5,-0.25)),(m_Ratte+Grösse*Vektor3(1,-0.5,-0.25)),(m_Ratte+Grösse*Vektor3(1,-0.5,0.25)),material_Ratte))
Körper2=(Dreieck((m_Ratte+Grösse*Vektor3(-1,-0.5,-0.25)),(m_Ratte+Grösse*Vektor3(1,-0.5,0.25)),(m_Ratte+Grösse*Vektor3(-1,-0.5,0.25)),material_Ratte))
Körper3=(Dreieck((m_Ratte+Grösse*Vektor3(-1,-0.5,0.25)),(m_Ratte+Grösse*Vektor3(1,-0.5,0.25)),(m_Ratte+Grösse*Vektor3(1,0.5,0.25)),material_Ratte))
Körper4=(Dreieck((m_Ratte+Grösse*Vektor3(-1,-0.5,0.25)),(m_Ratte+Grösse*Vektor3(1,0.5,0.25)),(m_Ratte+Grösse*Vektor3(-1,0.5,0.25)),material_Ratte))
#Körper5=(Dreieck((m_Ratte+Grösse*Vektor3(-1,-0.5,-0.25)),(m_Ratte+Grösse*Vektor3(-1,0.5,-0.25)),(m_Ratte+Grösse*Vektor3(1,0.5,-0.25)),material_Ratte))
#Körper6=(Dreieck((m_Ratte+Grösse*Vektor3(-1,-0.5,-0.25)),(m_Ratte+Grösse*Vektor3(1,0.5,-0.25)),(m_Ratte+Grösse*Vektor3(1,-0.5,-0.25)),material_Ratte))
Körper7=(Dreieck((m_Ratte+Grösse*Vektor3(1,0.5,-0.25)),(m_Ratte+Grösse*Vektor3(-1,0.5,0.25)),(m_Ratte+Grösse*Vektor3(1,0.5,0.25)),material_Ratte))
Körper8=(Dreieck((m_Ratte+Grösse*Vektor3(1,0.5,-0.25)),(m_Ratte+Grösse*Vektor3(-1,0.5,-0.25)),(m_Ratte+Grösse*Vektor3(-1,0.5,0.25)),material_Ratte))
Körper9=(Dreieck((m_Ratte+Grösse*Vektor3(1,-0.5,-0.25)),(m_Ratte+Grösse*Vektor3(-1,0.5,0.25)),(m_Ratte+Grösse*Vektor3(-1,-0.5,0.25)),material_Ratte))
Körper10=(Dreieck((m_Ratte+Grösse*Vektor3(-1,-0.5,-0.25)),(m_Ratte+Grösse*Vektor3(-1,0.5,0.25)),(m_Ratte+Grösse*Vektor3(-1,-0.5,0.25)),material_Ratte))
Schwanz1=(Dreieck((m_Ratte+Grösse*Vektor3(-1,0.05,0)),(m_Ratte+Grösse*Vektor3(-2.5,0,0)),(m_Ratte+Grösse*Vektor3(-1,-0.05,0)),material_Ratte))
Schwanz2=(Dreieck((m_Ratte+Grösse*Vektor3(-1,0,0.05)),(m_Ratte+Grösse*Vektor3(-2.5,0,0)),(m_Ratte+Grösse*Vektor3(-1,0,-0.05)),material_Ratte))
NaseSeite1=(Dreieck((m_Ratte+Grösse*Vektor3(1.95,-0.5,-0.25)),(m_Ratte+Grösse*Vektor3(1,-0.5,-0.25)),(m_Ratte+Grösse*Vektor3(1,-0.5,0.25)),material_Ratte))
NaseSeite2=(Dreieck((m_Ratte+Grösse*Vektor3(1.95,0.5,-0.25)),(m_Ratte+Grösse*Vektor3(1,0.5,-0.25)),(m_Ratte+Grösse*Vektor3(1,0.5,0.25)),material_Ratte))
NaseOben1=(Dreieck((m_Ratte+Grösse*Vektor3(1.95,-0.5,-0.25)),(m_Ratte+Grösse*Vektor3(1,-0.5,0.25)),(m_Ratte+Grösse*Vektor3(1.95,0.5,-0.25)),material_Ratte))
NaseOben2=(Dreieck((m_Ratte+Grösse*Vektor3(1.95,0.5,-0.25)),(m_Ratte+Grösse*Vektor3(1,-0.5,0.25)),(m_Ratte+Grösse*Vektor3(1,0.5,0.25)),material_Ratte))
Unten1=(Dreieck((m_Ratte+Grösse*Vektor3(-1,-0.5,-0.25)),(m_Ratte+Grösse*Vektor3(1.95,-0.5,-0.25)),(m_Ratte+Grösse*Vektor3(1.95,0.5,-0.25)),material_Ratte))
Unten2=(Dreieck((m_Ratte+Grösse*Vektor3(-1,0.5,-0.25)),(m_Ratte+Grösse*Vektor3(-1,-0.5,-0.25)),(m_Ratte+Grösse*Vektor3(1.95,0.5,-0.25)),material_Ratte))
Ratte=[Fuss1,Fuss2,Fuss3,Fuss4,Körper1,Körper2,Körper3,Körper4,Körper7,Körper8,Körper9,Körper10,Schwanz1,Schwanz2, NaseSeite1, NaseSeite2, NaseOben1, NaseOben2]