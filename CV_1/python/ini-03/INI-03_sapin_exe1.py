# nom: INI-03_sapin_exe1.py
# auteur: Alexandru Balog
# date: 03.09.2025

def sapin(n):
    k = 0
    for y in range(1, n + 1):
        for x in range(1, (n -y) + 1):
            print(end="  ")

        while k != (2 * y - 1):
            print("* ", end="")
            k += 1

        k = 0
        print()


sapin(int(input("Entrer total ligne: ")))