class Departement:
    def __init__(self, id, nom, budget_annuel) -> None:
        self.id = id
        self.nom = nom
        self.budget_annuel = budget_annuel


    @classmethod
    def from_string(cls, )