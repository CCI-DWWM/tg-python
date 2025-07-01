"""
Exercice :
Faire une fonction qui donne le nom du département passé en entrée
Ex : 41 -> "Loir et Cher"
CSV : disponible ici : https://www.data.gouv.fr/fr/datasets/departements-de-france/
"""
import sqlite3
import sys

def get_dept(departement):
    con = sqlite3.connect('departements.sqlite')
    cur = con.cursor()

    res = cur.execute(f"SELECT nom_departement FROM "
                      f"'departements-france'WHERE code_departement="
                      f"'{departement}'")

    nom_dep = res.fetchone()[0]
    print(nom_dep)
    return nom_dep

if __name__ == "__main__":
    print(f"=> {sys.argv[1]}")

    get_dept(sys.argv[1])

