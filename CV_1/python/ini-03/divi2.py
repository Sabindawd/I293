
import os


def division(nombre1, nombre2):
    os.system('cls')
    try:
        nombre1 = float(nombre1)
        nombre2 = float(nombre2)
        return True,
    except:
        print("Erreur")
        nombre1_2 = input("Bonjour,donnez-moi un premier nombre entre 1 et 50 :")
        nombre2_2 = input("Bonjour,donnez-moi un second nombre entre 1 et 50 :")
        return division(nombre1_2, nombre2_2)


if __name__ == "__main__":
    nombre1 = input("Bonjour,donnez-moi un premier nombre entre 1 et 50 :")
    nombre2 = input("Bonjour,donnez-moi un second nombre entre 1 et 50 :")
    result = division(nombre1, nombre2)
    print("Donc j'ai compris, je vais travailler avec min", nombre1, "et max", nombre2)