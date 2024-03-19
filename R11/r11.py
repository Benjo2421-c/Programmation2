import datetime
import random


class Inscription:
    def __init__(self, alias, role) -> None:
        self.date_inscription = datetime.date.today()
        self.alias= alias
        self.role = role
        self.cout = 45
        self.no_confirmation = 0

    def confirmer(self):
        self.no_confirmation= random.randint(1,1000)
        print(f"Nous avons bien confirmer votre inscription {self.alias}, voici votre numéro d'inscription : {self.no_confirmation}")
    
    def canceller(self):
        
        print(f"nous avons bien canceller votre inscription {self.no_confirmation}")
        self.no_confirmation =0 

Gandalf = Inscription("Gandalf le magnifique", "Magicien’")

Thormal = Inscription("Thornal le ténébreux", "Guerrier")


Gandalf.confirmer()
Thormal.confirmer()
Thormal.canceller()