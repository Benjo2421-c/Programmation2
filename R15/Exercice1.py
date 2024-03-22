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
    def __repr__(self) -> str:
        return (f"{self.nom}, {self.prenom}")



class attaquant(Joueur):
    def __init__(self, nom, prenom, date_naissance, no_chandail, position, nb_tirs_au_but, nb_assistance) -> None:
        super().__init__(nom, prenom, date_naissance, no_chandail, position)
        self.nb_tirs_au_but = nb_tirs_au_but
        self.nb_assistance = nb_assistance
    
    def Compter_but(self):
        self.nb_tirs_au_but +=1

class Défenseur(Joueur):
    def __init__(self, nom, prenom, date_naissance, no_chandail, position, nb_interceptions, nb_passes) -> None:
         super().__init__(nom, prenom, date_naissance, no_chandail, position)
         self.nb_interceptions = nb_interceptions
         self.nb_passes = nb_passes


class Gardien(Joueur):
    def __init__(self, nom, prenom, date_naissance, no_chandail, position, nb_arrêts, nb_tirs_esssuyes) -> None:
        super().__init__(nom, prenom, date_naissance, no_chandail, position)
        self.nb_arrêts = nb_arrêts
        self.nb_tirs_esssuyes = nb_tirs_esssuyes


Goaler = Gardien("Ketterer", "Logan", "9 novembre 1993", "1", "Gardien", "128", "208")
Defense= Défenseur("Brault-Guillard", "Zachary", "5 mars 1991", "15", "Défenseur", "32", "44")
attaque = attaquant("Ibrahim", "Sunusi", "1 octobre 2002", "14", "Attaquant", "23", "44")




print(Goaler.date_naissance, Defense.date_naissance, attaque.date_naissance)
print(Goaler.no_chandail, Defense.no_chandail, attaque.no_chandail)
print(Goaler.position, Defense.position, attaque.position)

class Équipe:
    nbr_joueur_dans_ligue=0
    def __init__(self, nom, liste_joueur=[]) -> None:
        self.nom = nom
        self.liste_joueur= liste_joueur
        Équipe.nbr_joueur_dans_ligue += len(liste_joueur)
    
    def engager_joueur(self,joueur):
        self.liste_joueur.append(joueur)
        Équipe.nbr_joueur_dans_ligue +=1
    
    def éjecter_joueur(self,joueur):
        self.liste_joueur.remove(joueur)
        Équipe.nbr_joueur_dans_ligue -=1


equipe_CF_Montreal = Équipe("CF Montréal", [Goaler, Defense])
equipe_CF_Montreal.engager_joueur([attaque])

print(equipe_CF_Montreal.liste_joueur)