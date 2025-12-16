# INI-03_Ex-sup.py
# Author: Balog Alexandru
# Date: 01.10.2025

# Exercice 1

def age():

    age = int(input("Entrez votre age :"))
    if age <= 12 :
        print("Ton billet cost 5fr")
    elif age <= 18 :
        print("Ton billet cost 8fr")
    elif age >= 18 :
        print("Ton billet cost 12fr")

# Exercice 2

poids = int(input("Entre poids en kg : "))
taille = int(input("Entre taille en cm: "))

def IMC(poids,taille):
    IMC = poids / (taille * taille) * 10000
    return IMC
print(IMC(poids,taille))

if IMC(poids,taille) <= 18.5 :
    print("insuffisance pondérale")
elif IMC(poids,taille) <= 18.5-25 :
     print("normal")
elif IMC(poids,taille) >= 25-30 :
    print("surpoids")
elif IMC(poids,taille) >= 30 :
    print("obésité")

#age()

