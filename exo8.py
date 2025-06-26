"""
Exercice :
Créez un tuple de nombres aléatoires, puis trouvez le nombre le plus grand et
le plus petit dans le tuple.
"""

import random

myList = [random.randint(1,100) for i in range(50)]
max = myList[0]
min = myList[0]

for i in myList:
    if i > max:
        max = i
    if i < min:
        min = i

print(f"max = {max} et min = {min}")