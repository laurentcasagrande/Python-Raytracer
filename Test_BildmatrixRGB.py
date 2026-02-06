import matplotlib.pyplot as plt
import numpy as np

# --- Bildmatrix erzeugen ---
hor = 9
ver = 5
bild_matrix = np.zeros((ver, hor, 3))
# Hintergrundfarbe
hellblau = np.array([0.5, 0.82, 0.98])
# Die Einträge von bild_matrix werden überschrieben:
for i in range(ver):
    for j in range(hor):
        bild_matrix[i, j] = hellblau

# Beispielhafte Farben setzen
rot = np.array([1, 0, 0])
gruen = np.array([0, 1, 0])
blau = 0.5 * np.array([0, 0, 1])
gelb = rot + gruen
cyan = blau + gruen

bild_matrix[0, 0] = gruen
bild_matrix[0, 8] = gelb
bild_matrix[2, 4] = rot
bild_matrix[4, 0] = cyan
bild_matrix[4, 8] = blau
# Man kann auch mit negativen Indices arbeiten:
# bild_matrix[-1, -1] = blau

# Gewünschte Grösse in Pixeln
pixel_hor = 100 * hor
pixel_ver = 100 * ver
Dotspi = 100

# Speichern: True oder False
Speichern = False
# Dateiname
Dateiname = "Test01.png"

## Bild ausgeben und allenfalls speichern:
## Nicht verändern:
fig = plt.figure(frameon = False)
fig.set_size_inches(pixel_hor / Dotspi, pixel_ver / Dotspi)
ax = plt.Axes(fig, [0, 0, 1, 1])
ax.set_axis_off()
fig.add_axes(ax)
ax.imshow(bild_matrix, aspect = "equal")
if Speichern == True:
    fig.savefig(Dateiname, dpi = Dotspi)
plt.show()
