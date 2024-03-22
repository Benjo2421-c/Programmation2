class Personne :
    def __init__(self, nom, prenom, date_de_naissance) -> None:
        self.nom = nom
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance

class Employe(Personne):
    def __init__(self, nom, prenom, date_de_naissance, NAS, poste, salaire) -> None:
        super().__init__(nom, prenom, date_de_naissance)
        self.NAS = NAS
        self.poste = poste
        self.salaire = salaire

class Realisateur(Employe):
    def __init__(self, nom, prenom, date_de_naissance, NAS, salaire, bonus) -> None:
        super().__init__(nom, prenom, date_de_naissance, NAS, "Réalisateur", salaire)
        self.bonus = bonus
class Acteur(Employe):
    def __init__(self, nom, prenom, date_de_naissance, NAS,  salaire, role) -> None:
        super().__init__(nom, prenom, date_de_naissance, NAS, "Acteur", salaire)
        self.role = role


class film:
    def __init__(self, nom , date_sortie, liste_employes: list[Employe]=[]) -> None:
        self.nom = nom
        self.liste_employes = liste_employes
        self.date_sortie = date_sortie



James = Realisateur("Cameroun", "James", "né le 16 août 1954", any, 15000, 5000)


Elise = Acteur("Maroune", "Elise", "2 aout 1999", any, 50000, "principaux")
Guy = Acteur("Marmadout", "Guy", "2 aout 1999", any, 50000, "principaux")


titanic = film("Titanic", "19 décembre 1997", [James, Elise])
Abyss = film("Abyss", "9 août 1989")
Avatar= film("Avatar", "18 décembre 2009")