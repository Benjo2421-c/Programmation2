import datetime

class Personne:
    def __init__(self, nom, prenom, date_naissance) -> None:
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
    

class Joueur(Personne):
    def __init__(self, nom, prenom, date_naissance, no_chandail, position) -> None:
        super().__init__(nom, prenom, date_naissance)
        self.no_chandail = no_chandail
        self.position = position



class attaquant(Joueur):
    def __init__(self, nom, prenom, date_naissance, no_chandail, position) -> None:
        super().__init__(nom, prenom, date_naissance, no_chandail, position)
        self.nb_tirs_au_but = 0
        self.nb_assistance = 0
    
    def Compter_but(self):
        self.nb_tirs_au_but +=1

class Défenseur(Joueur):
    def __init__(self, nom, prenom, date_naissance, no_chandail, position) -> None:
         super().__init__(nom, prenom, date_naissance, no_chandail, position)
         self.nb_interceptions = 0
         self.nb_passes = 0


class Gardien(Joueur):
    def __init__(self, nom, prenom, date_naissance, no_chandail, position, nb_arrêts, nb_tirs_esssuyes) -> None:
        super().__init__(nom, prenom, date_naissance, no_chandail, position)
        self.nb_arrêts = nb_arrêts
        self.nb_tirs_esssuyes = nb_tirs_esssuyes


Goaler = Gardien("Ketterer", "Logan", "9 novembre 1993", "1", "Gardien", "128", "208")
Defense= Défenseur("")