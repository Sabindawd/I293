# nom INI-03_For_exe1.py
# auteur Alexandru Balog
# date 03.09.2025


étoiles = int(input("combien d'étoiles ? : "))
for i in range(étoiles):
    for y in range(i+1):
        print("* ", end="")
    print()
