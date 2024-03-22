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

    def __init__(self, marque, modele, annee, kilométrag, couleur, prix, autonomie_max, autonomie_actuelle, type_recharge, etat="neuf") -> None:
        super().__init__(marque, modele, annee, kilométrag, couleur, prix, etat)
        self.autonomie_max = autonomie_max
        self.autonomie_actuelle = autonomie_actuelle

        self.type_recharge= type_recharge

    def recharger(self, time):
        time = int(time)
        if self.type_recharge == "Niveau2":
            self.autonomie_actuelle += (time/120)*40

        elif self.type_recharge == "Rapide(100kw)":
            self.autonomie_actuelle += (time/8)*40

        else:
            self.autonomie_actuelle += (time/2)*40
        
        if self.autonomie_actuelle > self.autonomie_max:
            self.autonomie_actuelle = self.autonomie_max

    def imprimer_info(self):
        print(self.__dict__)



auto_Paul = Voiture_electrique("Audi", "Q8", "2021", "10", "Jaune", "68000$", 400 ,30, "Rapide(100kw)")
auto_Lucie = Voiture_electrique("Chevrolet", "Silverado", "2023", "10", "Argent", "86000$", 640, 30, "Rapide(300kw)")
auto_Paul.imprimer_info()
auto_Lucie. imprimer_info()
auto_Lucie.recharger(40)
auto_Paul.recharger(10)
print(f"{auto_Paul.autonomie_actuelle}, {auto_Lucie.autonomie_actuelle}")