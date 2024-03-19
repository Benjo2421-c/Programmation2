class Compte:
    def __init__(self, no_compte, type_compte, nip_client) -> None:
        self.no_compte = no_compte
        self.typecompte = type_compte
        self.nip_client = nip_client
        self.solde = 0

    def deposer(self, montant ):
        self.solde += montant
    
    def retirer(self, retirer):
        if self.solde < retirer:
            print(f"Votre solde est de {self.solde} ce qui est inférieur au montant {retirer} que vous voulez retirer")
        else:
            self.solde -= retirer

    def __repr__(self) -> str:
        return f"{self.no_compte} {self.typecompte} {self.nip_client}"


client1 = Compte(12345678,"chèque", 888888888)
client2 = Compte(23456789,"épargne", 888888888)

print(client1.solde)
client1.retirer(100)
client1.deposer(1000)
print(client1.solde)
client1.deposer(2000)
print(client1.solde)
client2.deposer(5000)
print(client2.solde)