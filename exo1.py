"""
Exercice :
Demandez à l’utilisateur de saisir son PRENOM, puis son NOM, et enfin,
son année de naissance
Afficher « Bonjour PRENOM NOM, vous avez XX ans »
Note : vérifier que l'année est un nombre
"""

surname = input('Entrez votre prénom : ')
name = (input('Entrez votre nom : '))
dateOfBirth = int(input('Entrez votre année de naissance : '))
age = 2025 - dateOfBirth

print(f"Bonjour {surname.upper()} {name.upper()}, vous avez {age} ans")
