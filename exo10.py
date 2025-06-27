"""
Créer une fonction qui permette d'afficher lun nom encadré :
┌──────────┐
│ Emmanuel │
└──────────┘
"""
from colorama import Fore, Back, Style

def encadre(name):
    nb_chars = len(name) + 2
    line = "─" * nb_chars
    red_name = Fore.RED + name + Style.RESET_ALL

    print(f"┌{line}┐\n│ {red_name} │\n└{line}┘")

encadre("Thibaut")
encadre("Coucou")
