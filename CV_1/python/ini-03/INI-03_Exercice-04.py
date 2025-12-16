#nom INI-03_Exercice-04.py
#auteur Alexandru Balog
#date 27.08.2025

def arrondis_simple(nombre):
    arrondi_inf = int(nombre)

    arrondi_sup = arrondi_inf + 1

    print("Arrondi inférieur :", arrondi_inf)
    print("Arrondi supérieur :", arrondi_sup)

n = float(input("Entrez un nombre réel : "))
arrondis_simple(n)
