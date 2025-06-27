"""
Créer une fonction qui permette d'afficher lun nom encadré :
┌──────────┐
│ Emmanuel │
└──────────┘
"""

def encadre(name):
    nb_chars = len(name) + 2
    line = "─" * nb_chars

    print(f"┌{line}┐\n│ {name} │\n└{line}┘")

encadre("Thibaut")
encadre("Coucou")
encadre("§MAR!!")
