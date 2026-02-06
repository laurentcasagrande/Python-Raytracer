from Klasse_Vektor3 import *
import numpy as np

# Ein Fernpunkt wird festgelegt
weit = 10 ** 6
Fernpunkt = Vektor3(weit, weit, weit)

#Basis der uv-Ebene, hier Basis der Ebene y=0:
basisvektor1 = Vektor3(1, 0, 0)
basisvektor2 = Vektor3(0, 0, 1)

#######################
def IndicesZuPunkt(i, j, Zentrum, Einheit, b1, b2, u0, v0):
    """
    (i,j) sind die Indices der numpy-Bildmatrix.
    zentrum (die Bildmitte), Richtungsvektoren (Basis) b1, b2 der uv-Ebene.
    Zurückgegeben wird der entsprechende 3D-Punkt p.
    Der Punkt p ist das Zentrum desjenigen Punktes der Projektionsebene,
    durch welchen der (primäre) Sehstrahl gesendet wird.
    """
    p = Zentrum + (u0 + j * Einheit) * b1  + (v0 - i * Einheit) * b2
    return p
#########################


def SichtbaresObjekt(p, v, Szene):
    """
    Das gesuchte Objekt ist das zu p in Richtung v nächstgelegene Objekt der Szene.
    Gibt Objekt, Schnittpunkt, Abstand zurück: sichtbares_objekt, spunkt, dist
    Gibt es kein Objekt in jener Richtung wird [None, Fernpunkt, weit]
    zurückgegeben.
    """
    sichtbares_objekt = None
    spunkt = Fernpunkt
    dist = weit
    for objekt in Szene:
        schp = objekt.Schnittpunkt(p,v)
        if schp == Fernpunkt:
            continue
        elif Betrag(schp) < dist:
            dist = Betrag(schp)
            spunkt = schp
            sichtbares_objekt = objekt
    
    return sichtbares_objekt, spunkt, dist


def BerechneFarbeVer1(Startpunkt, Richtungsvektor, Auge, Szene,
                  Hintergrundfarbe, AmbientesLicht, Lichterliste):
    """
    Zu Testzwecken wird stets die Hintergrundfarbe zurückgegeben.
    """
    return Hintergrundfarbe


def BerechneFarbeVer2(p, v, Auge, Szene,
                  Hintergrundfarbe, AmbientesLicht, Lichterliste):
    """
    Berechnet den Farbanteil, der entlang des Strahls p+tv gesammelt wird.
    Gibt die Farbe als np.array (rgb-Tripel) zurück.
    In Version 1 wird nur der ambiente Farbanteil addiert.
    """
    objekt, spunkt, dist = SichtbaresObjekt(p,v,Szene)
    if objekt is not None:
        farbe = np.array([0.0,0.0,0.0])
        farbe += objekt.material[0]*objekt.material[1]*AmbientesLicht.frb*AmbientesLicht.gint

    else:
        farbe = Hintergrundfarbe
    return farbe


def BerechneFarbeVer4(p, v, Auge, Szene,
                      Hintergrundfarbe, AmbientesLicht, Lichterliste):
    """
    Berechnet den Farbanteil, der entlang des Strahls p+tv gesammelt wird.
    Gibt die Farbe als np.array (rgb-Tripel) zurück.
    In Version 2 werden der ambiente und der diffuse Farbanteil addiert.
    """
    objekt, spunkt, dist = SichtbaresObjekt(p,v,Szene)
    if objekt is not None:
        farbe = np.array([0.0,0.0,0.0])
        Famb = AmbientesLicht.frb
        Iamb = AmbientesLicht.gint
        Fobj = objekt.material[0]
        ka = objekt.material[1]    
        kd = objekt.material[2]
        kg = objekt.material[3]
        e = objekt.material[4]
        farbe += ka*Iamb*Fobj*Famb

        for L in Lichterliste:
            nvek = objekt.Normalenvektor(spunkt)
            l = Normieren(L.pos-spunkt)
            b = Normieren((-1)*v)
            h = Normieren(l+b)
            nh = sp(nvek,h)
            nl = sp(nvek,l)

            if nl > 0:
                farbe += Fobj*kd*nl*L.gint*L.frb
                if nh > 0:
                    farbe += kg*(nh**e)*L.gint*L.frb
    else:
        farbe = Hintergrundfarbe
    return farbe

def BerechneFarbeVer3(Startpunkt, Richtungsvektor, Auge,
                      Szene, Hintergrundfarbe, AmbientesLicht, Lichterliste):
    """
    Berechnet den Farbanteil, der entlang des Strahls p+tv gesammelt wird.
    Gibt die Farbe als np.array (rgb-Tripel) zurück.
    In Version 3 werden der ambiente und der diffuse Farbanteil,
    sowie Glanzpunkte addiert.
    """
    pass


def ImSchatten(Punkt, Lichtposition, Szene, delta = 0.01):
    """
    Gibt den Wert True oder False zurück, je nachdem,
    ob sich zwischen dem Punkt p und der Lichtposition ein Objekt
    aus der Szene befindet oder nicht.
    Der Startpunkt des Schattenstrahls wird leicht (mit delta) in Richtung
    der Lichtquelle verschoben.
    Wählt man delta = 0, so kann man starke Schatten-Akne beobachten!
    """
    # Vektor vlicht zum Licht hin.
    vlicht = Normieren( Lichtposition - Punkt )
    # Startpunkt leicht in Richtung Lichtquelle schieben,
    # um Schattenakne zu vermeiden.
    startp = Punkt + delta * vlicht
    distanz = Betrag( startp - Lichtposition )
    for objekt in Szene:
        spunkt = objekt.Schnittpunkt(startp,vlicht)
        if Betrag(spunkt-Punkt)<distanz:
            return True
    else:
        return False
    

def BerechneFarbe(p, v, Auge, Szene, Hintergrundfarbe, AmbientesLicht, Lichterliste):
    """
    Berechnet den Farbanteil, der entlang des Strahls p+tv gesammelt wird.
    Gibt die Farbe als np.array (rgb-Tripel) zurück.
    In dieser Version werden der ambiente und der diffuse Farbanteil addiert,
    Glanzpunkte gesetzt und Schatten berücksichtigt.
    """
    objekt, spunkt, dist = SichtbaresObjekt(p,v,Szene)
    if objekt is not None:
        farbe = np.array([0.0,0.0,0.0])
        Famb = AmbientesLicht.frb
        Iamb = AmbientesLicht.gint
        Fobj = objekt.material[0]
        ka = objekt.material[1]    
        kd = objekt.material[2]
        kg = objekt.material[3]
        e = objekt.material[4]
        farbe += ka*Iamb*Fobj*Famb

        for L in Lichterliste:
            if not ImSchatten(spunkt,L.pos,Szene):
                nvek = objekt.Normalenvektor(spunkt)
                l = Normieren(L.pos-spunkt)
                b = Normieren((-1)*v)
                h = Normieren(l+b)
                nh = sp(nvek,h)
                nl = sp(nvek,l)

                if nl > 0:
                    farbe += Fobj*kd*nl*L.gint*L.frb
                    if nh > 0:
                        farbe += kg*(nh**e)*L.gint*L.frb
    else:
        farbe = Hintergrundfarbe
    return farbe




