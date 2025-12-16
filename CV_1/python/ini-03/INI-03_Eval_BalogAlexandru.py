# INI-03_Eval_BalogAlexandru.py
# Author: Balog Alexandru
# Date: 30.10.2025

print("=== MINI CAISSE AUTOMATIQUE ===")
print("")


int(input("Combien d'articles?: "))
article = int(input("Quels articles avez-vous et?: "))

article1 = int(input("Article 1 : Pomme - 1.20 CHF: "));
article2 = int(input("Article 2 : Pain - 2.50 CHF: "));
article3 = int(input("Article 3 : Lait - 1.90 CHF: "));

mon_tuple = (article1, article2, article3)

total = 1.20 + 2.50 + 1.90
if total <= 50:
    print(total)
elif total >= 50:
    total = (total / 100) * total
    print(total)







