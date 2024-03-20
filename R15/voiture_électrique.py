class Voiture:
    def __init__(self, marque, modele, annee, kilométrag, couleur, prix, etat = "neuf") -> None:
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilométrag = kilométrag
        self.couleur = couleur
        self.prix = prix
        self.etat = etat

    def imprimer_info(self):
        print(self.__dict__)



class Voiture_electrique(Voiture):
    def __init__(self, marque, modele, annee, kilométrag, couleur, prix, etat="neuf", autonomie_max, autonomie_actuelle, type_recharge) -> None:
        super().__init__(marque, modele, annee, kilométrag, couleur, prix, etat)
        self.autonomie_max = autonomie_max
        self.autonomie_actuelle = autonomie_actuelle
        self.type_recharge= type_recharge

    def recharger(self):
        

voiture= Voiture("toyota", "Tercel", "1972", "rouge", "12888888", "123", "superbe")

voiture.imprimer_info()