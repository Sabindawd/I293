#nom INI-03_Exercice-01.py
#auteur Alexandru Balog
#date 20.08.2025

from datetime import datetime

annee_naissance = int(input("Entrez votre annee de naissance : "))

annee_actuelle = datetime.now().year
age = annee_actuelle - annee_naissance

print("Vous avez environ :")
print(age, "annees")
print(age * 12, "mois")
print(age * 52, "semaines")
print(age * 52 * 7, "jours")
print(age * 52 * 7 * 24, "heures")
print(age * 52 * 7 * 24 * 60, "minutes")
print(age * 52 * 7 * 24 * 60 * 60, "secondes")
