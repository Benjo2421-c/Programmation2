# RAPPEL
# groupe = "1020"    
# print(dir(groupe))  #montre toutes les méthodes disponibles pour la variable groupe#
# #help#
# print(help(str)) #montre ce que fait chacune des méthodes de la classe str#
# print(help(str.find)) #montre ce que fait la méthode find de la classe str# 

# Pour chaque question ci-dessous, faites le code demandé puis imprimez toujours 80*'_' de séparer les questions.      #
# Imprimez le résultat en utilisant f-string pour afficher le numéro de la question et les infos demandées             #
# CHOISISSEZ LA MÉTHODE QUI VOUS SEMBLE LA MIEUX POUR FAIRE CE QUI EST DEMANDÉ                                         # 


# Q1                                                                                                                   #
# Créez une liste de 3 modèles de cartes graphiques. Voici une liste de cartes graphiques. Vous pouvez construire votre liste en choisissant parmi les suivantes:                                                          #
#          GeForce RTX 3090Ti, GeForce RTX 3080Ti, GeForce RTX 3070Ti, Radeon RX 6950 XT, Radeon RX 6900 XT, Radeon RX 6800 XT             
# Vous pouvez aussi mettre un autre modèle de carte graphique si vous voulez.#
# imprimez la liste                                                                                                    #
print(f"Q1{u'_'*60}")
liste_carte_graphic = ["GeForce RTX 3090Ti", "GeForce RTX 3080Ti", "GeForce RTX 3070Ti"]
print(liste_carte_graphic) 




#Q2                                                                                                                   #
#  Obtenez la carte graphique à l'index 1 de la liste de vos cartes graphiques                                        #
#  Enlevez-la de la liste                                                                                             #
#  Imprimez la liste en spécifiant l'item enlevé                                                                      #
print(f"Q2{u'_'*60}")
print(liste_carte_graphic[1])
liste_carte_graphic.remove("GeForce RTX 3080Ti")
print(f"j'enlève GeForce RXT 3080Ti : {liste_carte_graphic}")





# Q3                                                                                                                   #
# Ajoutez un nouvel item à la fin de la liste                                                                          #
# et affichez la dernière carte graphique que vous avez maintenant dans la liste                                       #
print(f"Q3{u'_'*60}")
liste_carte_graphic.append("Radeo6600 XT")
print(liste_carte_graphic[-1])





#  

# Q4                                                                                                                 #
# Inversez les items de votre liste                                                                                  #
print(f"Q4{u'_'*60}")
liste_carte_graphic.reverse()
print(liste_carte_graphic)



# Q5                                                                                                                 #
# Créez une petite liste de deux nouvelles cartes graphiques                                                         #
# Imprimez cette nouvelle petite liste                                                                               #
# Ajoutez cette nouvelle petite liste à la fin de votre première liste                                               #
# Imprimez votre liste initale telle qu'elle est rendue                                                              #
print(f"Q5{u'_'*60}")
liste_carte_graphic_new = ["Radeon RX 6900 XT", "Radeon RX 6800 XT"]
print(liste_carte_graphic_new)
liste_carte_graphic.extend(liste_carte_graphic_new)
print(liste_carte_graphic)




# Q6                                                                                                                  #
# Ordonnez la liste en ordre croissant de façon à créer une nouvelle liste                                            #
# et imprimez cette nouvelle liste                                                                                    #
print(f"Q6{u'_'*60}")
liste_orde_croissant= sorted(liste_carte_graphic)
print(liste_orde_croissant)





