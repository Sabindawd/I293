# nom INI-03 tuple_exe.py
# auteur Alexandru Balog
# date 03.09.2025

while True:
    nombre1 = input("Combien d'articles? : ")
    if nombre1.isdigit():
        break

# Demande un deuxième nombre entier à l'utilisateur et valide le nombre
# entré, avec utilisation d'une variable pour sortir de la boucle
pas_entier = True
while pas_entier:
    nombre2 = input("Quels articles avez-vous? "
                    + "premier (" + nombre1 + ") : ")
    if nombre2.isdigit():
        pas_entier = False

# Affiche tous les chiffres entre les deux nombres entiers
for chiffre in range(int(nombre1), int(nombre2)+1):
    print (chiffre)