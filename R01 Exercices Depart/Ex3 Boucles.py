# RAPPEL
# groupe = "1020"    
# print(dir(groupe))  #montre toutes les méthodes disponibles pour la variable groupe#
# #help#
# print(help(str)) #montre ce que fait chacune des méthodes de la classe str#
# print(help(str.find)) #montre ce que fait la méthode find de la classe str# 




salutation = "Bonjour"
# Q1 Imprimez chacun des caractères de la variable salutation en utilisant for #
print(f"Q1{'_'*60}")
for lettre in salutation:
    print(lettre)

# Q2 Imprimez chacun des caractères de la variable salutation SUR UNE MÊME LIGNE#
#       Vous devez passé une valeur de paramètre supplémentaire à la fonction "print()"
print(f"Q2{'_'*60}")
for lettre in salutation:
    print(lettre, end='')
print()

# Q3 Demandez à l'usager d'entrer un chiffre pair en boucle
# Si le chiffre entré est pair, affichez "Merci vous avez entré le chiffre X, soit un chiffre pair."  où X est le chiffre entré
# Si l'usager entre un chiffre impair vous sortez de la boucle et affichez "Non, vous avez entré le chiffre X, et ce n'est pas un chiffre pair." #
#   RAPPEL : Vous pouvez utilisé la l'opérateur module ( % ) pour déterminer si un nombre est pair ou impair.
print(f"Q3{'_'*60}")

nombre = int(input("donner un nombre entier"))

while nombre %2 ==0:
    print(f"Merci vous avez entré le chiffre {nombre}, soit un chiffre pair.")
    nombre = int(input("donner un nombre entier"))
else: print (f"Non, vous avez entré le chiffre {nombre}, et ce n'est pas un chiffre pair.")











