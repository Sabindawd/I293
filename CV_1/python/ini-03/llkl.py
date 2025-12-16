ch = input("Saisissez une chaîne : ")
print("Nombre de caractères :", len(ch))

if len(ch) > 1:
    ch = ch[-1] + ch[1:-1] + ch[0]

print("Chaîne après permutation :", ch)

