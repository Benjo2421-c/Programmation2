# demo de boucles


liste_os_supporter = ["Win 10", "WinXp", "WinVista", "macOS", 
                      "iOS", "Android", "Chrome Os","Win7", 
                      "Ubuntu 22.02", "Linux Mint","Win 8.1"]

___ = [None] # deux variables vides qui devront être remplacer.

print("\nListe des os avec boucle while : ")

print("\nListe des os avec boucle for : ")
for  os  in liste_os_supporter : # completer la boucle for pour imprimer chaque os dans la lise
    print(os, end =" | ")
print()

print("\nListe des os windows avec boucle for : ")
for  os  in liste_os_supporter : # ajouter une condition pour que seul les os commencant par "Win sont imprimer"
    if"Win" in os :
        print (os, end = " | ")
