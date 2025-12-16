
class Menu:
    def __init__(self):
        print("--- Gestionnaire de Budget ---")
        print("[1] Définir le budget initial")
        print("[2] Ajouter un article")
        print("[3] Afficher le total des dépenses")
        print("[4] Afficher le solde restant")
        print("[5] Appliquer une réduction")
        print("[6] Quitter")
        self.choix = int(input())
        if self.choix == 1:
            budget = int(input("Entrez le budget: "))
        elif self.choix == 2:
            article = input("Entrez votre article: ")

Menu()