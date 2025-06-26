name = (input('Entrez votre nom : '))
surname = input('Entrez votre prénom : ')
dateOfBirth = int(input('Entrez votre année de naissance : '))
age = 2025 - dateOfBirth

print('Bonjour', surname.upper(), name.upper(), 'vous avez', age, 'ans')
