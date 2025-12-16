dictionnaire_morse = {
    'A': ".-",
    'B': "-...",
    'C': "-.-.",
    'D': "-..",
    'E': ".",
    'F': "..-.",
    'G': "--.",
    'H': "....",
    'I': "..",
    'J': ".---",
    'K': "-.-",
    'L': ".-..",
    'M': "--",
    'N': "-.",
    'O': "---",
    'P': ".--.",
    'Q': "--.-",
    'R': ".-.",
    'S': "...",
    'T': "-",
    'U': "..-",
    'V': "...-",
    'W': ".--",
    'X': "-..-",
    'Y': "-.--",
    'Z': "--..",
}

print("1) Lettre vers morse")
print("2) Morse vers lettre")
choice = int(input("Choisissez entre les deux traductions : "))

dictionnaire_ascii = {v: k for k, v in dictionnaire_morse.items()}


def choices():
    if choice == 1:
        print(ascii_morse(inp))
    elif choice == 2:
        print(morse_ascii(inp))
    else:
        print("Veuillez choisir entre le choix 1 et le choix 2")


def ascii_morse(inp):
    try:
        lettres_final = ""
        for v in inp:
            v_maj = v.upper()
            if v_maj in dictionnaire_morse:
                lettres_final = f"{lettres_final} {dictionnaire_morse[v_maj]}"

        return lettres_final
    except:
        print("Veuilez mettre des lettres")


inp = input("Mettez un mot en lettres ou en morse : ")


def morse_ascii(inp):
    final_letters = ""
    words = inp.strip().split(" / ")
    for word in words:
        letters = word.split(" ")
        for code in letters:
            if code in dictionnaire_ascii:
                final_letters = f"{final_letters}{dictionnaire_ascii[code]}"
        final_letters = f"{final_letters}"
    return final_letters.strip()

