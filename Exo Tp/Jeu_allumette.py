<<<<<<< HEAD
import random as ran

def gbaton(allumettes: int) -> str:
    """Fais l'affichage des baton"""
    baton = ""
    nb = round(allumettes/3, 1)
    print(nb)
    if (nb - int(nb) == 0.3) or (nb - int(nb) == 0.2999999999999998):
        baton += "|"
    elif (nb - int(nb) == 0.7) or (nb - int(nb) == 0.7000000000000002):
        baton += "||"
    while int(nb) > 0:
        baton = "||| " + baton
        nb -= 1
    print(nb)
    return baton
    

def IA_enemy(j: int) -> int:
    """Calcule les choix de l'ennemy pour devenir le rendre imbatable"""
    if j == 3:
        return 1
    elif j == 2:
        return 2
    else:
        return 3

allumettes = 21

while allumettes > 0:
    baton = gbaton(allumettes)
    print(f"Il y a {allumettes} sur la table : {baton}")
    j = int(input("Combien en prenez-vous ? "))
    while j > 3 or j <= 0 or j > allumettes:
        print("Vous avez trop allumettes ou pas assez")
        j = int(input("Combien en prenez-vous ? "))
    allumettes -= j
    if allumettes <= 0:
        print("Vous avez perdus !")
        break
    o = IA_enemy(j)
    print(f"Je prend {o} allumette.\n")
    allumettes -= o
    if allumettes <= 0:
        print("Vous avez gagné !")
        break
=======
import random as ran

def gbaton(allumettes: int) -> str:
    """Fais l'affichage des baton"""
    baton = ""
    nb = round(allumettes/3, 1)
    print(nb)
    if (nb - int(nb) == 0.3) or (nb - int(nb) == 0.2999999999999998):
        baton += "|"
    elif (nb - int(nb) == 0.7) or (nb - int(nb) == 0.7000000000000002):
        baton += "||"
    while int(nb) > 0:
        baton = "||| " + baton
        nb -= 1
    print(nb)
    return baton
    

def IA_enemy(j: int) -> int:
    """Calcule les choix de l'ennemy pour devenir le rendre imbatable"""
    if j == 3:
        return 1
    elif j == 2:
        return 2
    else:
        return 3

allumettes = 21

while allumettes > 0:
    baton = gbaton(allumettes)
    print(f"Il y a {allumettes} sur la table : {baton}")
    j = int(input("Combien en prenez-vous ? "))
    while j > 3 or j <= 0 or j > allumettes:
        print("Vous avez trop allumettes ou pas assez")
        j = int(input("Combien en prenez-vous ? "))
    allumettes -= j
    if allumettes <= 0:
        print("Vous avez perdus !")
        break
    o = IA_enemy(j)
    print(f"Je prend {o} allumette.\n")
    allumettes -= o
    if allumettes <= 0:
        print("Vous avez gagné !")
        break
>>>>>>> fc9acc5024275baf41e857549168f97a380f1a0b
