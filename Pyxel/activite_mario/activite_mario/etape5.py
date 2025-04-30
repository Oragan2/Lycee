import pyxel

# Initialisation des variables globales
player_x = 60
player_y = 116  
player_vy = 0   # Vitesse verticale initiale
on_ground = False  # Indique si le joueur est sur une plateforme

PLATFORMS = [
    (0, 124, 128, 4),  # Sol
    (20, 90, 40, 4),
    (70, 70, 40, 4),
    (20, 40, 40, 4),
    (70, 20, 40, 4)]

EXIT = (100, 12, 8, 8)


def deplacement(x, y, vy):
    """ renvoie les nouvelles coordonnées du personnage après appuie sur les 
        touches directionnelles """    
    # Déplacement horizontal
    if pyxel.btn(pyxel.KEY_RIGHT) and x < 120:  # Appuie sur la flèche droite
        x += 2
    if pyxel.btn(pyxel.KEY_LEFT) and x > 0:  # Appuie sur la flèche gauche
        x -= 2
    # Appliquer la gravité
    if y >= PLATFORMS[0][1] - 8 :  # Vérifier la collision avec le sol
        y = PLATFORMS[0][1] - 8
        vy = 0  # Réinitialiser la vitesse verticale
        # Gestion du saut  
        if pyxel.btnp(pyxel.KEY_SPACE):
            vy = -7  # Saut
    vy += 0.5  #  Augmenter la vitesse verticale pour simuler la gravité
    y += vy  # Mettre à jour la position verticale en fonction de la vitesse
    
    return x, y, vy


def update():
    """Met à jour les variables du jeu."""
    global player_x, player_y, player_vy
    player_x, player_y, player_vy = deplacement(player_x, player_y, player_vy)
        

def draw():
    """Dessine les éléments du jeu."""
    pyxel.cls(6)  # Efface l'écran avec une couleur bleu clair
    
    # Dessine le joueur
    pyxel.rect(player_x, player_y, 8, 8, 1)
    
    # Dessine les plateformes
    for p in ...:
        pyxel.rect(..., ..., ..., ..., 13)
    
    # Dessine la sortie
    ...


# Initialisation de Pyxel
pyxel.init(128, 128, title="Déplacement avec gravité")
pyxel.run(update, draw)