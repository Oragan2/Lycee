import pyxel

class App():
    def __init__(self):
        # Initialisation des variables globales
        pyxel.init(128, 128, title="Déplacement avec gravité")
        self.x = 60
        self.y = 116  
        self.vy = 0   # Vitesse verticale initiale
        self.on_ground = False  # Indique si le joueur est sur une plateforme
        self.PLATFORMS = [(0, 124, 128, 4),(20, 90, 40, 4),(70, 70, 40, 4),(20, 40, 40, 4),(70, 20, 40, 4)]
        self.EXIT = (100, 12, 8, 8)
        self.game_won = False
        pyxel.run(self.update, self.draw)

    def deplacement(self):
        """Gère le déplacement du joueur et les collisions."""
        # Déplacement horizontal
        if pyxel.btn(pyxel.KEY_RIGHT) and self.x < 120:
            self.x += 2
        if pyxel.btn(pyxel.KEY_LEFT) and self.x > 0:
            self.x -= 2
        
        # Appliquer la gravité
        self.vy += 0.5  # Gravité constante
        self.y += self.vy
        
        # Vérifier les collisions avec les plateformes
        self.on_ground = False  # On réinitialise l'état au début de chaque frame
        for p in self.PLATFORMS:
            if (self.x < p[0] + p[2] and  # Joueur à gauche de la plateforme
                self.x + 8 > p[0] and     # Joueur à droite de la plateforme
                self.y + 8 >= p[1] and     # Joueur touche le dessus de la plateforme
                self.y + 8 <= p[1] + p[3] + self.vy):  # Collision dans la frame actuelle
                
                # Collision par le haut (atterrissage sur une plateforme)
                if self.vy > 0 :
                    self.y = p[1] - 8  # Aligner le joueur sur la plateforme
                    self.vy = 0  # Réinitialiser la vitesse verticale
                    self.on_ground = True
            elif (self.x < p[0] + p[2] and  # Joueur à gauche de la plateforme
                self.x + 8 > p[0] and     # Joueur à droite de la plateforme
                self.y <= p[1] + p[3] and     # Joueur touche le dessus de la plateforme
                self.y >= p[1] + p[3] + self.vy):  # Collision dans la frame actuelle
                
                # Collision par le haut (atterrissage sur une plateforme)
                if self.vy < 0 :
                    self.y = p[1] + p[3]  # Aligner le joueur sur la plateforme
                    self.vy = 0  # Réinitialiser la vitesse verticale
                    
        # Gestion du saut
        if self.on_ground and pyxel.btnp(pyxel.KEY_SPACE):
            self.vy = -7  # Appliquer une impulsion vers le haut
            self.on_ground = False
                
    def update(self):
        """Met à jour les variables du jeu."""
        if not self.game_won: 
            self.deplacement()
            # Vérifier si le joueur atteint la porte
            if (self.x + 8 > self.EXIT[0] and self.x < self.EXIT[0] + self.EXIT[2] and
                    self.y + 8 > self.EXIT[1] and self.y < self.EXIT[1] + self.EXIT[3]):
                self.game_won = True  # Le joueur a gagné

    def draw(self):
        """Dessine les éléments du jeu."""
        pyxel.cls(6)  # Efface l'écran avec une couleur bleu clair
        
        # Dessine le joueur
        pyxel.rect(self.x, self.y, 8, 8, 1)
        
        # Dessine les plateformes
        for p in self.PLATFORMS:
            pyxel.rect(p[0], p[1], p[2], p[3], 13)
        
        # Dessine la sortie
        pyxel.rect(self.EXIT[0], self.EXIT[1], self.EXIT[2], self.EXIT[3], 4)
        
        # Affiche un message "Gagné" si le joueur atteint la sortie
        if self.game_won:
            pyxel.text(50, 60, "GAGNE !!!", 0)

App()