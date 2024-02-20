# RAPPEL
# groupe = "1020"    
# print(dir(groupe))  #montre toutes les méthodes disponibles pour la variable groupe#
# #help#
# print(help(str)) #montre ce que fait chacune des méthodes de la classe str#
# print(help(str.find)) #montre ce que fait la méthode find de la classe str# 

# Pour chaque question ci-dessous, faites le code demandé puis imprimez toujours 80*'_' de séparer les questions.      #
# Imprimez le résultat en utilisant f-string pour afficher le numéro de la question et les infos demandées             # 


# Q1                                                                                                                   #
# Créez une liste de 3 barrettes de RAM parmis les suivantes:                                                          #
#          G.SKILL Trident Z5, CORSAIR Dominator, CORSAIR Vengeance, G.SKILL Ripjaws V, G.SKILL Ripjaws X              #
# imprimez la liste                                                                                                    #
print(f"Q1{u'_'*60}")
liste_de_rams = ["CORSAIR Vengeance", "G.SKILL Trident Z5", "CORSAIR Dominator,"]
print(liste_de_rams)





# Q2                                                                                                                   #
# Ajoutez un item à la fin de la liste avec append                                                                     #
# et affichez la dernière barrette RAM que vous avez dans la liste                                                     #
print(f"Q2{u'_'*60}")
liste_de_rams.append("G.SKILL Ripjaws V")
print(liste_de_rams[-1])






#  Q3                                                                                                               #
#  Observez quelle est la deuxième barrette de RAM de votre liste                                                   #
#  Enlevez-la de la liste avec remove                                                                               #
#  Imprimez la liste en spécifiant la barrette de RAM enlevée                                                       #
print(f"Q3{u'_'*60}")

liste_de_rams.remove("G.SKILL Trident Z5")
print(f"La ram G.SKILL Trident Z5 a été enlever : {liste_de_rams}")





# Q4                                                                                                             #
# Ordonner la liste en ordre croissant avec la méthode sort et imprimez-la                                       #
print(f"Q4{u'_'*60}")
liste_de_rams.sort()
print(liste_de_rams)





# Q5                                                                                                             #
# Ordonner la liste en ordre décroissant avec la fonction sorted (qui crée une nouvelle liste)                    #
# et imprimez-la                                                                                                 
print(f"Q5{u'_'*60}")
liste_de_rams.sort(reverse=True)

print(liste_de_rams)




# Q6                                                                                                                 #
# Imprimez le nombre d'éléments qu'il y a dans votre liste présentement                                              #
print(f"Q6{u'_'*60}")
print(len(liste_de_rams))





# Q7                                                                                                                 #
# Imprimez une sous-liste des deux dernières barrettes RAMS de votre liste, en utilisant le slicing                  #
print(f"Q7{u'_'*60}")
print(liste_de_rams)
print(liste_de_rams[-2:])





