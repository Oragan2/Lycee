import random as ran

def jeu():
    choixIA = ran.ranint(1,3)
    print("1 : Pierre ; 2 : Feuille ; 3 : Ciseaux")
    choixJ = int(input("Quel est votre choix "))
    
def victoire(IA, J):
    if IA == J:
        pass
    if IA == 1:
        if J == 2:
            scoreJ += 1
        if J == 3:
            scoreAI += 1
    if IA == 2:
        if J == 1:
            scoreAI += 1
        if J == 3:
            scoreJ += 1
            
    