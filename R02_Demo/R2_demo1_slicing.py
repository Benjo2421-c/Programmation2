#utilisation de l'index pour les listes
cours = ['Programmation 1', 'Math', 'Bureautique', 'Réseau 1','Math',"Programmation 2", "Programmation 3", "Pogrammation Web"]

#imprimer le premier cours
print([0])
#imprimer les 6 premiers cours
print(cours[0:6])
for cour in cours [0:6] :
    print(f"{cours}")
#imprimer le dernier cours
print(cours[-1])
#imprimer les 3 derniers cours
print(cours[-4:-1])
#imprimer la liste tronqué d'une valeur
print(cours[1:-1])

cours_retirer = cours.pop()