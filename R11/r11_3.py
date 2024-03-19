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
       
voiture= Voiture("toyota", "Tercel", "1972", "rouge", "12888888", "123", "superbe")

voiture.imprimer_info()