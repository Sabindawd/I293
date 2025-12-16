#nom INI-03_Exercice-05.py
#auteur Alexandru Balog
#date 27.08.2025

text = "apcpedagogie"
long = len(text)
pos = 0

while pos < long:
    if text[pos] == "p":
        print("Le caractere 'p' se trouve a la position :", pos,"dans la chaine ch")
    pos += 1