
import csv
import os
os.chdir(os.path.dirname(__file__))

# Q3
# Ouvrez le ficher en lecture
# Utilisez le module csv pour lire le contenu du fichier
# Sautez la première ligne contenant les en-têtes
# Ajoutez chaque ligne à la variable list_client
# Finalement, imprimer la variable list_client

nom_fichier = "fichier_a_lire.csv"
list_client = []

with open(nom_fichier, "r") as ficier_lu:
    csv_reader = csv.reader(ficier_lu)
    next(csv_reader)

    for ligne in csv_reader:
        list_client.append(ligne)

print (list_client)
