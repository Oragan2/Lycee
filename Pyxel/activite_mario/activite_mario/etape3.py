# on importe la bibliothèque pyxel
import pyxel

### Initialisation des variables globales
player_x = 60
player_y = 116

GROUND = (0, 124, 128, 4)
### Fin del'initialisation des variables globales

def deplacement(x, y):
    """ renvoie les nouvelles coordonnées du personnage après appuie sur les 
        touches directionnelles """
    if pyxel.btn(...) and x < 120: # appuie sur la flèche droite
        x = x + 2
    if ... and ... x > 0 : # appuie sur la flèche gauche
            ...
    return x, y

def update():
    """ met à jour les variables (30 fois par seconde) """
    pass

def draw():
    """ crée les objets (30 fois par seconde) """
    pyxel.cls(6)  # Efface l'écran avec une couleur bleu clair
    
    # représentation du personnage
    pyxel.rect(player_x, player_y, 8 , 8, 1)
    
    # représentation du sol
    pyxel.rect(GROUND[0], GROUND[1], GROUND[2], GROUND[3], 13)

# on initialise de la taille de la fenêtre 128x128 pixels
pyxel.init(128, 128, title="Déplacement avec gravité")
# on lance l'exécution du jeu
pyxel.run(update, draw)