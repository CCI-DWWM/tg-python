"""
Exercice :
Écrivez une fonction qui compte le nombre d'occurrences de chaque élément
dans une liste et retourne un dictionnaire avec ces comptages.
ex :
maliste=[5,2,4,8,65,6,8,7,1,3,9,8,5,2,2,6,54,2,4,85,4,5,54,8,5,5,1,58,8]
"""

myList = [5,2,4,8,65,6,8,7,1,3,9,8,5,2,2,6,54,2,4,85,4,5,54,8,5,5,1,58,8]

myDict = {}

for i in myList:
    myDict[i] = myList.count(i)
print(myDict)
