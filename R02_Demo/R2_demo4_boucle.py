#boucle for


liste_cours = ['Programmation 1', 'Math', 
               'Bureautique', 'Réseau 1','Math']

#print chacun des cours dans la liste
for cours in liste_cours:
    pass


#print chacun des cours dans la liste ansi que leur ( index + )
for nbr, cours in enumerate(liste_cours):
    print(f"Cours {nbr+1}")
