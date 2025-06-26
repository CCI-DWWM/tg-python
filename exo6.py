"""
Exercice :
Vérification de nombres premiers : Écrivez une fonction en Python qui
vérifie si un nombre donné est premier ou non.
Un nombre entier naturel (supérieur ou égal à 2) est un nombre premier s'il
admet exactement 2 diviseurs : 1 et lui-même. Exemple : 2, 3, 5, 7, 11, 13, 17,
19 … sont des nombres premiers. Il en existe une infinité
"""

n = input('Entrez votre nombre : ')

if n.isdigit() :
    if int(n) <= 1 :
        print("il n'est pas premier")
    else :
        for i in range(2, (int(n)-1), 1):
            if (int(n)) % i == 0 :
                print("il n'est pas premier")
                break
        else:
            print("il est premier")
else :
    print("Ce n'est pas un nombre")