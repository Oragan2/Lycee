import random as ran

def tetraedre() -> int:
    """Lance un dé forme de Tétraèdre et lance un autre suivant le résultat du dé et ranvoie cette valeur"""
    dee = ran.randint(1,4)
    if dee == 1:
        resultat = ran.randint(1,6)
        return "Cube", resultat
    elif dee == 2:
        resultat = ran.randint(1,8)
        return "Octaèdre", resultat
    elif dee == 3:
        resultat = ran.randint(1,10)
        return "Dodécaèdre", resultat
    else:
        resultat = ran.randint(1,20)
        return "Icosaèdre", resultat

compteur = 0
moyenne = 0
while compteur < 100:
    dee, nombre = tetraedre()
    print(f"Le dé lancée est un {dee} et le résultat est {nombre}")
    compteur += 1
    moyenne = moyenne + nombre
moyenne = moyenne/100
print(f"La moyenne de tout les lancée arrondie est égale à {round(moyenne)}")
