# nom: INI-03_ma_liste_exe2.py
# auteur: Alexandru Balog
# date: 03.09.2025
import os

date_list = [11,12,2011,1111]

while True:
    os.system("cls")
    print("Bonjour qu'est ce que vous voulais faire ?")
    print("[1] Afficher la liste")
    print("[2] Changer le jour")
    print("[3] Changer le mois")
    print("[4] Changer l'année")
    choix = int(input("@-> "))

    if choix == 1:
        print("liste:", date_list)
        input()
        pass
    elif choix == 2:
        date_list[0] = int(input("entrer le jour: "))
        pass
    elif choix == 3:
        date_list[1] = int(input("entrer le mois: "))
        pass
    elif choix == 4:
        date_list[2] = int(input("entrer l'année: "))
        pass