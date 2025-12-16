# INI-03_Ex-sup2.py
# Author: Balog Alexandru
# Date: 01.10.2025

# Exercice 3

def did():

    nb = int(input("Entrez votre nombre :"))
    print(nb)

    if nb > 0 :
        print("positif ")
    elif nb < 0 :
        print("negatif ")
    elif nb == 0 :
        print("nul")

#did()

# Exercice 4

def pop():
    try:
       while True:
           chiffre = int(input("Entrez un nombre entre 1 et 10 :"))
           if chiffre > 0 and chiffre <= 10 :
                return chiffre
    except:
        print("Entrez un nombre")
#pop()

# Exercice 5

def pto():
    prix = float(input("Entrez un prix :"))
    reduction = float(input("Entrez la reduction :"))

    nouveau_prix = prix - (prix) * (reduction / 100)
    print(nouveau_prix , "CHF")

#pto()

# Exercice 6

def eurotax():
    euro = float(input("Entrez un montant en euro :"))
    taux = (0.95)

    chf = euro * taux
    print(chf , "CHF")

#def eurotax()


# Execrice 7
def majeur():
    try:
        while True:
            age = int(input("Entrez votre age :"))
            if age <= 18 :
                print("mineur")
            elif age >= 18 :
                print("majeur")
            if age < 0 :
                return age
    except:print("Entrez votre age")


majeur()