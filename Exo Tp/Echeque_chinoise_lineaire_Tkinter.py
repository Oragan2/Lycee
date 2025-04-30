#Import
import tkinter as tk

#Variable
player = 1
plateau = [1,1,1,1,0,0,0,2,2,2,2]
victoire = True
#Tk
main = tk.Tk()
main.title("Echeque chinoise linéaire")
main.geometry("1124x626")

tk_plateau_v = tk.StringVar()
tk_player_txt = tk.StringVar()
tk_player_rep = tk.StringVar()


tk_jouer_bt = tk.Button(main,
                        text = "Jouer",
                        #command = jouer
                        )

tk_plateau = tk.Label(main,
                      textvariable = tk_plateau_v,
                      font = ("Ubuntu", "52")
                      )

tk_jouer_txt = tk.Label(main,
                        textvariable = tk_player_txt,
                        font = ("Ubuntu", "18"))

tk_jouer = tk.Entry(main,
                    textvariable = tk_player_rep,
                    font = ("Ubuntu", "24")
                    )

tk_plateau.grid(row = 0, column = 0, padx = 133, pady = 266)
tk_jouer.focus_set()
tk_jouer.grid(row = 0, column = 0, sticky= 's')
tk_jouer_txt.grid(row= 0, column = 0, sticky= 'sw')
tk_jouer_bt.grid(row = 0, column = 0, sticky= 'se')

def quitter():
    main.quit()
    main.destroy()

#fonction
def mouvement_pion(plateau:list, pion:int, joueur:int) -> list:
    """Fais bouger le pion donné a la prochaine case vide"""
    count = 4
    for i in range(len(plateau)):
        if (count == pion) and (plateau[i] == joueur):
            case_vide = trouver_case_vide(plateau, i, joueur)
            if case_vide == 404:
                break
            plateau[i] = 0
            plateau[case_vide] = joueur            
            plateau = verifier(plateau, i, joueur)
            count -= 1
        if plateau[i] == joueur:
            count -= 1
    return plateau

def trouver_case_vide(p:list, index_p:int, joueur:int) -> int:
    """Trouve la première case vide devant le pion qui vas jouez"""
    Passe = False
    Passe2 = True
    for i in range(index_p, len(p)):
        if p[i] == 0:
            return i
    for car in plateau:
        if car == joueur:
            Passe = True
        if car == 0 and Passe:
            Passe2 = False
    if Passe and Passe2:
        print("Vous ne pouvais pas jouez, a l'autre.")
        return 404
    jouer()
    return 404

def victoire_s(plateau:list) -> bool:
    """Verifie si un joueur gagne"""
    if plateau[0:4] == [2,2,2,2]:
        return False
    if plateau[7:11] == [1,1,1,1]:
        return False
    return True

def verifier(plateau:list, i:int, joueur:int):
    """Verifie que le plateau n'as pas de problème"""
    if plateau.count(joueur) == 5:
        plateau[i] = 0
    if plateau.count(3-joueur) == 3:
        plateau[i] = 3-joueur
    return plateau

def jouer() -> int:
    """Permet au joueur de jouée au jeu"""
    pion = input(f"Joueur{player} - Choisiser votre pion: ")
    tk_player_txt.set(f"Joueur{player} - Choisiser votre pion: ")
    while pion == "":
        pion = int(input("Quelle pion voulez vous jouez?(entre 1 et 4) "))
        tk_player_txt.set("Quelle pion voulez vous jouez?(entre 1 et 4) ")
    pion = int(pion)
    if pion <= 0 or pion > 4:
        while pion <= 0 or pion > 4:
            pion = int(input("Quelle pion voulez vous jouez?(entre 1 et 4) "))
            tk_player_txt.set("Quelle pion voulez vous jouez?(entre 1 et 4) ")
    return pion

while victoire:
    tk_plateau_v.set(f"{plateau}")
    tk_player_txt.set(f"Joueur{player} - Choisiser votre pion: ")
    pion = jouer()
    if player == 1:
        mouvement_pion(plateau, pion, player)
    else:
        plateau.reverse()
        mouvement_pion(plateau, pion, player)
        plateau.reverse()
    victoire = victoire_s(plateau)
    player = 3 - player

print(plateau)
print(f"Bravo Joueur {3-player}, vous avez gagnée")

#truc Tk
main.mainloop()