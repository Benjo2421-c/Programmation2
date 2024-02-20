cours = ['Programmation 1', 'Math', 'Bureautique', 'Réseau 1','Math']
print(f"Liste au début : {cours}" end="\n\n")

#ajouter le cours "Math" à la fin avec append()



#Afficher le nombre de fois que le cours "Math" apparait


#ajouter les cours "AI", "Systèmes" à la liste avec extend()
cours_extra = ["AI", "Systèmes"]

#trouver l'index du cours "Bureautique" en utilisant index()
index = cour.index("Bureautique")

#Ajouter un cours "BD2" après "Bureautique" en utilisant insert() avec l'index que nous venons de découvrir.


#Enlever le cours "AI" de la liste avec remove()


#Enlever le dernier item de la liste avec pop(). L'item enlevé est retourné par pop#
dernier_element = cours.pop(2)
print(cours)
print(dernier_element)
print()

#Metter la lise de cours en ordre croissant avec sort()
#Puis metter la liste en ordre décroissant
cour.sort()

print(f"Liste Final : {cours}")