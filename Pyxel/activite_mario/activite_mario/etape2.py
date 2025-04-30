# on importe la bibliothèque pyxel
import pyxel

### Initialisation des variables globales

### Fin del'initialisation des variables globales

def update():
    """ met à jour les variables (30 fois par seconde) """
    pass

def draw():
    """ crée les objets (30 fois par seconde) """
    pyxel.cls(6)  # Efface l'écran avec une couleur bleu clair    

# on initialise de la taille de la fenêtre 128x128 pixels
pyxel.init(128, 128, title="Déplacement avec gravité")
# on lance l'exécution du jeu
pyxel.run(update, draw)