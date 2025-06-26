"""
Exercice:
Écrivez un programme qui demande à l'utilisateur de saisir une phrase
Puis compte et affiche le nombre de voyelles (a, e, i, o, u, y) et consonnes
dans la phrase.
"""

phrase = input("Entrez une phrase: ")
phraseToTest = ''.join(c for c in phrase.lower() if c.isalpha())

print(f"La phrase sans caractères spéciaux ni majuscules : {phraseToTest}")

vowels = ['a', 'e', 'i', 'o', 'u', 'y']
consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q',
             'r', 's', 't', 'v', 'w', 'x', 'z']
nbVowels = 0
nbConsonants = 0

for x in phraseToTest:
    if x in vowels:
        nbVowels += 1
    if x in consonant:
        nbConsonants += 1

print(f"Il y a {nbVowels} voyelles et {nbConsonants} consonnes dans votre "
      f"phrase !")