# RAPPEL
# groupe = "1020"    
# print(dir(groupe))  #montre toutes les méthodes disponibles pour la variable groupe#
# #help#
# print(help(str)) #montre ce que fait chacune des méthodes de la classe str#
# print(help(str.find)) #montre ce que fait la méthode find de la classe str# 

# Q1                                                                                                            #
# créez une liste de 4 à 5 sports  et imprimez la liste                                                         #
print(f"Q1{u'_'*60}")
sports = ["Patin", "Tennis", "Badminton", "Ski","Soccer"]
print(f" Voici la liste : {sports}")
print()

# Q2                                                                                                             #
# affichez le premier sport de votre liste                                                                       #
print(f"Q2{u'_'*60}")
print(f"Voici la liste: {sports[0]}")
print()



# Q3                                                                                                             #
# ajoutez un item à la fin de la liste avec append                                                               #
# et affichez le dernier sport que vous avez dans la liste                                                       #
print(f"Q3{u'_'*60}")
sports.append("Hockey")
print(f"Dernier sport de la liste, récement ajouté : {sports[-1]}")



# Q4 ajoutez un item après le 1er sport de votre liste avec insert                                                  #
#    créez une liste d'autres sports que vous n'avez jamais fait                                                    #
#    imprimez la liste telle qu'elle est rendue                                                                     # 
#    ajoutez votre autre liste de sports à la première liste avec extend                                            #
#    imprimez la liste telle qu'elle est rendue                                                                     # 
print(f"Q4{u'_'*60}")

sports.insert(1,"Golf")
print(f"la liste aprè insert: {sports[1]}")
sport_nerver_done = ("Easport", "F1", "Natation", "bowling")
sports.extend(sport_nerver_done)
print(f"La liste après extend : {sports}")


#  Q5                                                                                                               #
#  Imprimez le nom d'un sport que vous enleverez ensuite de la liste                                                #
#  Enlevez un sport de la liste avec remove                                                                         #
#  Imprimez la liste et voyez que le sport que vous avez enlevé avec remove est bel et bien enlevé                  #
#  Enlever le dernier sport de la liste avec pop. Le sport enlevé est retourné par pop Affichez-le                  #
#  Imprimez la liste en spécifiant le sport enlevé et utilisant f-string                                            #
print(f"Q5{u'_'*60}")
print(f"Sport que je compte enlever: {sports[1]}")
sports.remove("Golf")
print(sports)

print(f"Derner sport enlevé de la liste : {sports.pop(-1)}")
print(sports)




# Q6                                                                                                             #
# Utilisez une boucle for pour passer à travers chaque sport dans la liste avec une boucle for                   #
# et affichez le sport sur différentes lignes                                                                    #
print(f"Q6{u'_'*60}")

for sport in sports:
    print(sport)



 
  
# Q7                                                                                                             #
# Ordonner la liste en ordre croissant avec la méthode sort et imprimez-la                                       #
print(f"Q7{u'_'*60}")
sports.sort()
print(sports)





# Q8                                                                                                                 #
# Créez un noveau str contenant toutes les valeurs dans la liste séparée par une virgule. Affichez ce str                                            #
print(f"Q8{u'_'*60}")

liste_sport_propre = ", ".join(sports)
print(f"La liste devenue en str: {liste_sport_propre}")




# Q9                                                                                                                 #
# Imprimez une sous-liste des deux premiers sports, en utilisant le slicing                                          #
print(f"Q9{u'_'*60}")

print(sports[0:2])




