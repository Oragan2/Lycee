import pyxel

### Initialisation des variables globales
player_x = 60
player_y = 116  

GROUND = (0, 124, 128, 4)
### Fin de l'initialisation des variables globales

def deplacement(x, y, vy):
    """ renvoie les nouvelles coordonnées du personnage après appuie sur les 
        touches directionnelles """    
    # Déplacement horizontal
    if pyxel.btn(pyxel.KEY_RIGHT) and x < 120:  # Appuie sur la flèche droite
        x += 2
    if pyxel.btn(pyxel.KEY_LEFT) and x > 0:  # Appuie sur la flèche gauche
        x -= 2
    # Appliquer la gravité
    if y >= GROUND[1] - 8 :  # Vérifier la collision avec le sol
        y = GROUND[1] - 8
        vy = 0  # Réinitialiser la vitesse verticale
        ### Gestion du saut- A modifier
        ...
        ### Fin de la partie à modifier
    vy += 0.5  #  Augmenter la vitesse verticale pour simuler la gravité
    y += vy     # Mettre à jour la position verticale en fonction de la vitesse
    
    return x, y, vy


def update():
    """ met à jour les variables (30 fois par seconde) """
    global player_x, player_y, player_vy
    player_x, player_y, player_vy = deplacement(player_x, player_y, player_vy)


def draw():
    """ crée les objets (30 fois par seconde) """
    pyxel.cls(6)  # Efface l'écran avec une couleur bleu clair
    # Représentation du personnage
    pyxel.rect(player_x, player_y, 8, 8, 1)
    # Représentation du sol
    pyxel.rect(GROUND[0], GROUND[1], GROUND[2], GROUND[3], 13)

# On initialise la taille de la fenêtre 128x128 pixels
pyxel.init(128, 128, title="Déplacement avec gravité")
# On lance l'exécution du jeu
pyxel.run(update, draw)