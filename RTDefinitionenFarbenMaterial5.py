import numpy as np

def rgbFarbe(r,g,b):
    """
    Angabe von r,g,b als jeweils ganze Zahl zwischen 0 und 255.
    Ausgabe als np.array mit Dezimalzahlen.
    """
    return np.array([r/255,g/255,b/255])

# Farben
schwarz = np.array([0.0, 0.0, 0.0])
grau = np.array([0.2, 0.2, 0.2])
rot = np.array([1.0, 0.0, 0.0])
gelb = np.array([1.0, 1.0, 0.0])
gruen = np.array([0.0, 1.0, 0.0])
blau = np.array([0.0, 0.0, 1.0])
magenta = np.array([1.0, 0.0, 1.0])
weiss = np.array([1.0, 1.0, 1.0])
cyan = np.array([0.0, 1.0, 1.0])
hellblau = np.array([0.5,0.82,0.98])
braun = np.array([0.647,0.165,0.165])
# Test rgbFarbe - Befehl
testfarbe=rgbFarbe(100,68,9)

## Material [F, ka, kd, kg, kexp]
## F: Farbe als np.array
## ka, kd: ambienter und diffuser Intensitätskoeffizient
## kg, kexp: Glanzpunkte


## Grundsätzlich:
## kleine Werte kg mit kleinen kexp; grosse kg mit grossen kexp

# Beispiele
# Stein
Stein = [np.array([0.53,0.68,0.7]), 0.2, 0.5, 0.3, 8]

# Rotes Plastik
rot1=np.array([0.8,0.1,0.1])
Plastik_rot=[rot1, 0.2, 0.6, 0.3, 20]

# Gold
Gold = [ np.array([1.0, 0.85, 0.3]), 0.1, 0.5, 0.9, 80 ]


