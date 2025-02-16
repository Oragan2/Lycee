from cellule import Cellule

class Liste:
    """Une liste chainée"""
    def __init__(self,t=None):
        """Créer une liste vide"""
        self.tete = t
    
    def affiche(self):
        L = Liste(self.tete.suivant)
        if L.est_vide():
            return f"{self.tete.valeur}"
        else:
            return f"{self.tete.valeur}," + L.affiche()
    
    def get_tete(self) -> Cellule:
        return self.tete.valeur
    
    def mod_tete(self,t):
        self.tete = t
    
    def est_vide(self) -> bool:
        if self.tete == None:
            return True
        return False
    
    def ajoute(self,x):
        self.tete = Cellule(x,self.tete)
    
    def longueur(self) -> int:
        L = Liste(self.tete.suivant)
        if L.est_vide():
            return 1
        else:
            return 1 + L.longueur()
    
    def n_ieme_element(self,n) -> Cellule:
        L = Liste(self.tete.suivant)
        if n == 0:
            return self.tete.valeur
        else:
            return L.n_ieme_element(n-1)
        
    def concatener(self,L):
        L3 = Liste()
        for i in range(L.longueur()):
            L3.ajoute(L.n_ieme_element(i))
        for i in range(self.longueur()):
            L3.ajoute(self.n_ieme_element(i))
        return L3
    
    def renverser(self):
        L = Liste(self.tete)
        L2 = Liste()
        for i in range(self.longueur()): 
            L2.ajoute(self.tete.valeur)
            self.tete = self.tete.suivant
        self = Liste(L.tete)
        return L2
    
    def inserer(self, element, i):
        L = Liste(self.tete)
        L2 = Liste()
        for i in range(i):
            L2.ajoute(L.get_tete)
            L.tete = L.tete.suivant
        L.ajoute(element)
        L.concatener(L2.renverser())
        return L

        
        

L = Liste()
L2 = Liste()
L.ajoute(7)
L.ajoute(8)
L.ajoute(9)
L2.ajoute(4)
L2.ajoute(5)
L2.ajoute(6)
print(L.inserer(6,3).affiche())