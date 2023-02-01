import random

safiyeliste = [1, "5", "merhaba", ["a", "b", "c", "d", "e", "f"]]
stringlist = ["safiye", "ayşe", "ekrem", "ismail"]
integerlist = [3, 5, 1, 14, 99, 54]
shufflelist = [1, 2, 3, 4, 5, 6, 7]

uzunluk = len(safiyeliste) # montrer le nombre d'éléments d'une liste
safiyeliste.append("ekrem") # ajouter un élément à la liste à la fin
x = safiyeliste.pop(2) # prendre le deuxième élément de la liste, et supprimer de la liste

stringlist.sort() # ranger les éléments en fonction de la rang alphabétique ou numérique
integerlist.sort()
random.shuffle(shufflelist) # ranger les éléments dans un ordre aléatoire
s = random.choice(integerlist)
integerlist.append(stringlist) # ajouter une liste dans une liste
eleman = integerlist.index(5)

print(safiyeliste[-1]) # prendre le dernier élément
print(safiyeliste)
print(x)
print(stringlist)
print(integerlist)
print(shufflelist)
print(uzunluk)
print(safiyeliste[len(safiyeliste)-1])
print(eleman)

"""
une classe de 12 élèves
une fonction pour ajouter un nouvel élève et on peut ajouter le nom de ce nouveau élève
une fontion pour enlever un élève
ranger les élèves dans un ordre alphabétique
shuffle les élèves
choisir un élève d'une façon aléatoire
une fonction qui donne le nombre d'élèves qui sont présents
une fonction qui donne le rang d'un élève qui a été écrit par l'utilisateur
"""