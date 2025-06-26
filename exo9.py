"""
Exercice :
Créer une fonction est_premier(N) qui retourne True si le nombre passé est
premier, False sinon
"""

def isPremier(n):
    if n <= 1 :
        return False
    else :
        for i in range(2, n-1, 1) :
            if n % i == 0 :
                return False
        else:
            return True

n = int(input("Entrez un nombre : "))
if isPremier(n):
    print(f"{n} est un nombre premier.")
else:
    print(f"{n} n'est pas un nombre premier.")