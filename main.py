from programme.allumette.jeuAllumette import jeuAllumette
from programme.joueur.joueur import Joueur
from programme.utile.mrPropre import mrPropre
from programme.devinette.jeuDevinette import jeuDevinette

if __name__ == '__main__':
    choix: str = ""
    joueur1: Joueur
    joueur2: Joueur

    pseudo = input("Entrez le pseudo du joueur 1 : ")
    joueur1 = Joueur(pseudo)
    pseudo = input("Entrez le pseudo du joueur 2 : ")
    joueur2 = Joueur(pseudo)

    while choix != "4":
        print("""
    1. Devinette
    2. Allumette
    3. Morpion
    4. Quitter   
        """)

        choix = input("Faites votre choix : ")

        match choix:
            case '1': jeuDevinette(joueur1, joueur2)
            case '2': jeuAllumette(joueur1, joueur2)
            case '4': print("Au revoir")
