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

game_won = False  # Indique si le joueur a gagné


def deplacement(x, y, vy):
    """Gère le déplacement du joueur et les collisions."""
    global on_ground
    
    # Déplacement horizontal
    if pyxel.btn(pyxel.KEY_RIGHT) and x < 120:
        x += 2
    if pyxel.btn(pyxel.KEY_LEFT) and x > 0:
        x -= 2
    
    # Appliquer la gravité
    vy += 0.5  # Gravité constante
    y += vy
    
    # Vérifier les collisions avec les plateformes
    on_ground = False  # On réinitialise l'état au début de chaque frame
    for p in PLATFORMS:
        if (x < p[0] + p[2] and          # Joueur à gauche de la plateforme
            x + 8 > p[0] and             # Joueur à droite de la plateforme
            y + 8 >= p[1] and            # Joueur touche le dessus de la plateforme
            y + 8 <= p[1] + p[3] + vy):  # Collision dans la frame actuelle
            
            # Collision par le haut (atterrissage sur une plateforme)
            if vy > 0 :
                y = p[1] - 8   # Aligner le joueur sur la plateforme
                vy = 0         # Réinitialiser la vitesse verticale
                on_ground = True
        elif (x < ... and            # Joueur à gauche de la plateforme
            x + 8 > ... and          # Joueur à droite de la plateforme
            y <= ... and     # Joueur touche le dessus de la plateforme
            y >= ... + vy):  # Collision dans la frame actuelle
            
            # Collision par le haut (atterrissage sur une plateforme)
            if vy < 0 :
                y = p[1] + p[3]  # Aligner le joueur sur la plateforme
                vy = 0           # Réinitialiser la vitesse verticale
                
    # Gestion du saut
    if on_ground and pyxel.btnp(pyxel.KEY_SPACE):
        vy = -7          # Appliquer une impulsion vers le haut
        on_ground = ...  # booléen indiquant si le joueur est au sol
    
    return x, y, vy


def update():
    """Met à jour les variables du jeu."""
    global player_x, player_y, player_vy, game_won
    if not game_won: 
        player_x, player_y, player_vy = deplacement(player_x, player_y, player_vy)
        # Vérifier si le joueur atteint la porte
        if (player_x + 8 > ... and player_x < ... and 
                player_y + 8 > ... and player_y < ...):
            game_won = ...  # Le joueur a gagné


def draw():
    """Dessine les éléments du jeu."""
    pyxel.cls(6)  # Efface l'écran avec une couleur bleu clair
    
    # Dessine le joueur
    pyxel.rect(player_x, player_y, 8, 8, 1)
    
    # Dessine les plateformes
    for p in PLATFORMS:
        pyxel.rect(p[0], p[1], p[2], p[3], 13)
    
    # Dessine la sortie
    pyxel.rect(EXIT[0], EXIT[1], EXIT[2], EXIT[3], 4)
    
    # Affiche un message "Gagné" si le joueur atteint la sortie
    if game_won:
        pyxel.text(50, 60, "GAGNE !!!", 0)


# Initialisation de Pyxel
pyxel.init(128, 128, title="Déplacement avec gravité")
pyxel.run(update, draw)
