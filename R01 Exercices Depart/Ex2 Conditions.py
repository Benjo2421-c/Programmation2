# RAPPEL12
# groupe = "1020"    
# print(dir(groupe))  #montre toutes les méthodes disponibles pour la variable groupe#
# #help#
# print(help(str)) #montre ce que fait chacune des méthodes de la classe str#
# print(help(str.find)) #montre ce que fait la méthode find de la classe str# 



# 
# Q1 Demandez à l'usager d'entrer un nombre entre 1 à 10 #
#    Faites une structure de code conditionnelle pour vérifier si le nombre entré est entre 1 et 10
#    Si oui, affichez "Exellent vous avez entré un nombre entre 1 et 10"
#    Sinon, affichez "Erreur, vous n'avez pas entré un nombre entre 1 et 10"
#    
print(f"\nQ1{'_'*60}")

nombre = int(input('Donner un nombre entre 1 et 10 : '))
if (nombre >=1 or nombre <=10 ):
    print ("Excellent vous avez entré un nombre entre 1 et 10")
else:
    print ("Erreur, vous n'avez pas entré un nombre entre 1 et 10")




# Q2 Demandez à l'usager d'entrer un mot#
#    Faites un test pour vérifier si la longueur du mot entré est plus petit ou égal à 5
#    Si oui, affichez "Bien vous avez utilisé un mot de vocabulaire court"
#    Sinon, faites un autre test pour vérifier si la longueur du mot entré est entre 6 et 10
#          , affichez "Très bien, vous avez utilisé un mot de vocabulaire élaboré"
#    Sinon, (pas besoin de test mais dans ce cas la longueur du mot sera supérieure à 10)
#            affichez "Excellent, vous avez un vocabulaire très élaboré"
print(f"\nQ2{'_'*60}")
mot = input('Donner un mot ')

if (len (mot)) <=5 :
    print("bien vous avez utiliser un mot de vocabulaire court")
elif (len (mot))>=6 and len(mot)<=10:
    print("Très bien, vous avez utilisé un mot de vocabulaire élaboré")
elif (len(mot)) >=10 :
    print("Excellent, vous avez un vocabulaire très élaboré")

    
# Q3 Comme dans l'exercice précédent mais dans le message incluez le mot entré et la longueur du mot
# par exemple: si le mot entré est patato, le message affiché sera 
# "Bien, vous avez entré le mot 'patato', soit un mot de 6 lettres. \n Vous avez utilisé un mot de vocabulaire plus élaboré"
print(f"\nQ3{'_'*60}")


