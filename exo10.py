"""
Créer une fonction qui permette d'afficher lun nom encadré :
┌──────────┐
│ Emmanuel │
└──────────┘
"""
import sys
from colorama import Fore, Back, Style

def encadre(name, color):
    x = '─' * len(name)
    couleur = getattr(Fore, color.upper())
    print(f"""
┌─{x}─┐
│ {couleur}{name}{Style.RESET_ALL} │
└─{x}─┘""")

if __name__ == "__main__":
    print(f"=> {sys.argv[1]}")

    encadre(sys.argv[1], sys.argv[2])

# pour utiliser la fonction :
# CMD ==> py exo10.py Nom couleur