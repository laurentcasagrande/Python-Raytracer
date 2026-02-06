class Vektor3:
    def __init__(self, x, y, z):
        """Damit lassen sich die einzelnen Komponenten auslesen."""
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        """Additionsoperator + wird überladen."""
        return Vektor3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        """Subtraktionsoperator - wird überladen."""
        return Vektor3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, t):
        """Multiplikationsoperator * wird überladen (von rechts): v * t"""
        return Vektor3(self.x * t, self.y * t, self.z * t)

    def __rmul__(self, t):
        """Multiplikationsoperator * wird überladen (von links): t * v"""
        return self.__mul__(t)

    def Komponentenliste(self):
        """Liefert eine Liste der Komponenten des Vektors."""
        return [self.x, self.y, self.z]
    


def PrintV3(v):
    """
    Gibt die Komponenten eines Vektor3 auf die Konsole aus.
    """
    print("Die Komponenten lauten: ", v.Komponentenliste())

def sp(v, w):
    """Skalarprodukt von v und w wird berechnet."""
    return(v.x * w.x + v.y * w.y + v.z * w.z)

def vp(v,w):
    return Vektor3(v.y*w.z-v.z*w.y,v.z*w.x-v.x*w.z,v.x*w.y-v.y*w.x)

def Betrag(v):
    """Gibt den Betrag des Vektors v zurück."""
    return((v.x**2+v.y**2+v.z**2)**0.5)

def Abstand(v, w):
    """Berechnet den Abstand der (Orts--)Vektoren v und w. """
    return(((v.x-w.x)**2+(v.y-w.y)**2+(v.z-w.z)**2)**0.5)

def Normieren(v):
    """Gibt den auf Länge 1 normierten Vektor zurück."""
    b = Betrag(v)
    if b == 0:
        raise ValueError('Nullvektor kann nicht normiert werden.')
    else:
        v=v*(1/b)
        #return[v.x,v.y,v.z]         #für print()
        return (v)                  #für PrintV3()
