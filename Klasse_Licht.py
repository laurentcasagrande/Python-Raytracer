from Klasse_Vektor3 import *

class Ambientes_Licht:
    def __init__(self, farbe, grundintensitaet):
        self.frb = farbe
        self.gint = grundintensitaet

class Punktlichtquelle:
    def __init__(self, position, farbe, grundintensitaet, abnahmekoeffizienten):
        #Ist vom Typ Vektor3
        self.pos = position
        #Die Farbe wird als rgb-Tripel angegeben
        self.frb = farbe
        #Intensität als Zahl in (0,1)
        self.gint = grundintensitaet
        self.abk = abnahmekoeffizienten

    def Intensitaet(self, punkt):
        i0, i1, i2 = self.abk
        d = Abstand(self.pos, punkt)
        return self.gint / (i0 + i1 * d + i2 * d ** 2)

print