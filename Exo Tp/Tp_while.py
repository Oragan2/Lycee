import random as ran
import time

def jeu() -> tuple:
    types = ran.randint(1, 4)
    n1 = ran.randint(2, max)
    n2 = ran.randint(2, max)
    if types == 1:
        question = f"{n1} + {n2} = "
        reponse = int(input(question))
        resultat = n1 + n2
        return reponse, resultat, question
    elif types == 2:
        question = f"{n1} - {n2} = "
        reponse = int(input(question))
        resultat = n1 - n2
        return reponse, resultat, question
    elif types == 3:
        question = f"{n1} * {n2} = "
        reponse = int(input(question))
        resultat = n1 * n2
        return reponse, resultat, question
    else:
        question = f"Premier entier de {n1} / {n2} = "
        reponse = int(input(question))
        resultat = n1 // n2
        return reponse, resultat, question

max = int(input("Quelle est le chiffre max: "))
point = 0
prenom = input("Quelle est votre nom: ")
erreurs = 0
reponse, resultat, question = jeu()
temps = time.time()


while point <= 10:
    reponse, resultat, question = jeu()
    if resultat == reponse:
        point += 1
    else:
        while resultat != reponse:
            erreurs += 1
            print("Faux ! Réessayez !")
            reponse = int(input(question))
            if resultat == reponse:
                 break

duree = time.time() - temps
if erreurs == 1 or erreurs == 0:
    print(f"{prenom} ! Ton temps est de {round(duree, 1)} seconds et tu as fait {erreurs} erreur")
else:
    print(f"{prenom} !Ton temps est de {round(duree, 1)} seconds et tu as fait {erreurs} erreurs")