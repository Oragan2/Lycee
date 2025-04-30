import random as ran
import time

def texte_2_UTF(texte : str)->list:
    tab_codes_UTF = []
    for c in texte:
        tab_codes_UTF.append(ord(c))
    return tab_codes_UTF

def dec(text:str, cle:str) -> str:
    """Décode le text 'text' avec la cle 'cle' avec la methode xor"""
    message_chiffre = text.split()
    tab_cle_initial = texte_2_UTF(cle)
    tab_cle = []
    n,m = len(message_chiffre),len(tab_cle_initial)
    for i in range(n):
        tab_cle.append(tab_cle_initial[i%m])
    message_clair = [] 
    for i in range(n):
        message_clair.append(int(message_chiffre[i]) ^ tab_cle[i])
    texte_dechiffre = ''
    for c in message_clair:
        texte_dechiffre += chr(c)
    return texte_dechiffre

def decryptage(text:str, n:int) -> str:
    cle = ''
    for i in range(n):
        for lettre in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            test = dec(text, lettre)
            work = True
            for j in range(i,11,n):
                if test[j] != "identifiant"[j]:
                    work = False
            if work:
                cle += lettre
    return cle

start = time.time()
with open("D:\\Utilisateur\\Desktop\\Projet_NSI\\Decrypt\\[HACKED]fichier_cles_chiffre.txt","r",encoding="UTF-8") as fichier, open("D:\\Utilisateur\\Desktop\\Projet_NSI\\Decrypt\\[DECRYPT]fichier_cles_chiffre.txt","w",encoding="UTF-8") as fichier2:
    for ligne in fichier:
        fichier2.write(dec(ligne, decryptage(ligne,4))+"\n")
print(f"Le fichier a était décrypter en {round(time.time()-start, 2)} secondes") # 13.47 seconde
with open("D:\\Utilisateur\\Desktop\\Projet_NSI\\Decrypt\\[DECRYPT]fichier_cles_chiffre.txt","r",encoding="UTF-8") as fichier:
    for ligne in fichier:
        if "identifiant : 242158" in ligne:
            cle = ligne[29:45]
print(dec("97 26 119 71 143 4 27 88 40 65 119 214 125 19 37 14 74 9 54 91 2 17 84 71 46 65 36 66 52 48 42 14 94 14 37 21 10 21 84 64 50 65 123 22 49 120 49 64 68 13 50 71 21 84 17 66 123 72 50 22 47 58 55 90 72 91 50 70 18 84 64 4 117 46 1 89 52 60 45 14 65 30 119 71 143 7 1 91 178 4 51 67 125 51 45 88 95 30 119 18 42 17 84 81 46 77 51 83 125 59 49 14 91 20 46 84 1 17 1 68 123 67 54 90 60 60 48 71 92 14 50 18 70 16 17 22 31 75 34 81 49 62 55 14 108 31 54 88 21 90 126 117 52 73 58 83 51 43 100 73 76 9 51 80 20 84 0 89 46 80 119 69 50 49 100 72 65 30 48 88 3 84 5 67 58 74 51 22 50 49 100 79 93 11 37 80 8 16 84 82 58 74 36 22 49 62 100 67 199 22 50 21 12 27 1 68 53 205 50 22 103 127 53 91 72 91 36 84 70 25 21 95 40 75 57 22 43 62 100 196 89 9 50 21 7 22 21 66 47 81 50 22 57 62 42 93 13 23 54 21 11 29 26 67 47 65 119 70 50 42 54 14 65 26 62 70 21 17 6 22 43 72 54 85 56 127 164 14 88 21 50 21 2 157 2 95 58 80 62 89 51 127 32 9 76 14 35 90 20 27 1 66 62 4 108 22 44 42 33 14 65 26 119 97 3 6 6 83 123 82 54 22 183 43 54 75 13 31 190 65 20 1 29 66 62 4 51 17 52 60 45 14 73 30 34 77 70 25 29 88 46 80 50 69 113 127 55 75 13 15 37 90 19 2 21 88 47 8 119 85 50 176 42 77 68 31 50 91 5 17 84 91 58 72 63 83 40 45 33 91 94 30 123 21 21 1 6 22 55 65 119 66 47 62 39 199 13 31 112 64 8 17 84 80 46 80 34 68 56 127 50 65 68 30 119 80 30 4 6 83 40 87 119 95 51 43 33 92 74 26 59 84 5 0 29 71 46 65 119 13 125 46 49 75 13 8 56 91 70 25 17 95 55 72 50 67 47 127 37 67 68 87 119 86 3 6 0 83 40 4 51 223 49 54 39 71 72 14 36 80 11 17 26 66 123 64 190 85 60 51 173 2 13 30 36 65 70 17 26 22 61 69 62 66 125 42 42 14 76 8 35 71 9 7 0 89 43 84 50 67 47 127 42 79 89 18 49 21 2 17 84 116 178 80 50 90 58 58 49 93 72 87 119 80 18 84 7 17 58 84 39 68 183 43 33 14 205 91 33 90 19 7 84 83 53 80 37 87 179 49 33 92 13 26 34 77 70 23 27 88 61 77 57 69 125 59 33 14 65 26 119 82 7 24 21 78 50 65 119 9 87 15 37 93 13 31 50 21 22 21 26 95 42 81 50 22 124 127 78 109 76 9 119 116 20 0 28 67 41 4 19 83 51 43 104 14 88 21 119 116 8 19 24 87 50 87 119 83 37 43 54 79 66 9 51 92 8 21 29 68 62 73 50 88 41 127 41 65 84 30 57 25 70 4 27 67 41 86 54 22 62 48 41 94 89 30 37 21 21 1 6 22 55 65 119 80 60 61 49 66 72 14 47 21 33 1 29 82 62 4 51 67 125 41 43 87 76 28 50 64 20 84 19 87 55 69 52 66 52 46 49 75 13 11 56 64 20 84 24 17 58 71 52 89 48 47 37 73 67 30 37 21 2 21 26 69 123 87 50 69 125 58 60 90 95 26 56 71 2 29 26 87 50 86 50 69 125 59 173 92 76 11 54 82 3 7 84 69 43 69 35 95 60 42 60 14 64 20 46 80 8 26 17 91 62 74 35 22 62 48 42 90 95 143 59 220 21 90 126", cle))
