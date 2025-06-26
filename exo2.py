"""
Exercice 2 :
Même chose que le 1 mais on rajoute une condition si on rentre pas un nombre
pour l'année !
"""

surname = input('Entrez votre prénom : ')
name = (input('Entrez votre nom : '))
dateOfBirth = input('Entrez votre année de naissance : ')

if dateOfBirth.isdigit() :
    age = 2025 - int(dateOfBirth)
    print(f"Bonjour {surname.upper()} {name.upper()}, vous avez {age} ans")
else :
    print(f'''"{dateOfBirth}" n'est pas un nombre !''')