import matplotlib.pyplot as plt

## Bild ausgeben und allenfalls speichern:
## Nicht verändern:

def Bild_DarstellenSpeichern(Bild_Matrix, hor, ver, Dotspi, Speichern, Dateiname):
    """
    Die Einträge von Bild_Matrix werden als Bild der Breite hor und Höhe ver interpretiert.
    Dotspi ist die Auflösung: dots per inch.
    Speichern ist True oder False.
    Das Bild wird unter dem Dateinamen abgelegt und auf dem Bildschirm dargestellt.
    """
    fig = plt.figure(frameon = False)
    fig.set_size_inches(hor / Dotspi, ver / Dotspi)
    ax = plt.Axes(fig, [0, 0, 1, 1])
    ax.set_axis_off()
    fig.add_axes(ax)
    ax.imshow(Bild_Matrix, aspect = "equal")
    if Speichern == True:
        fig.savefig(Dateiname, dpi = Dotspi)
    plt.show()
