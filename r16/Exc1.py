import csv

class Departement:
    def __init__(self, id, nom, budget_annuel) -> None:
        self.id = id
        self.nom = nom
        self.budget_annuel = budget_annuel


        
class Achat:
    def __init__(self, id, montant_total_achat, est_paye, equipements) -> None:
        self.id = id
        self.montant_total_achat = montant_total_achat
        self.est_paye= est_paye
        self.equipement = equipements
    
    def calculer_total_estimer():
        pass
    def payer():
        pass


class Equipement:
    def __init__(self, id, nom_equipement, cie, modele, qty, prix) -> None:
        self.id = id
        self.nom_equipement = nom_equipement
        self.cie = cie
        self.modele = modele
        self.qty = qty
        self.prix = prix


equipements = []
with open ("r16/AchatsDepartement2023.csv", "r") as fichier_lu:
        csv_reader = csv.reader(fichier_lu, delimiter=";")
        next (csv_reader)
        for line in csv_reader:
            eq = Equipement(line[0],line[1], line[2], line[3], line[4], line[5])
            
