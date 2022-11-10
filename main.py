from programme.allumette.jeuAllumette import jeuAllumette
from programme.joueur.joueur import Joueur
from programme.morpion.jeuMopion import jeuMopion
from programme.devinette.jeuDevinette import jeuDevinette
from programme.utile.score import menuScore
from programme.utile.mrPropre import mrPropre
from programme.utile.colorfull import *

if __name__ == '__main__':
    choix: str = ""
    joueur1: Joueur
    joueur2: Joueur

    mrPropre()
    pseudo = input("Entrez le pseudo du joueur 1 : ")
    joueur1 = Joueur(pseudo)
    pseudo = input("Entrez le pseudo du joueur 2 : ")
    joueur2 = Joueur(pseudo)

    mrPropre()
    print("\n"+textcolor.BLUE+"Menu principal"+textcolor.DEFAULT)

    while choix != "5":
        print("""
    1. Devinette
    2. Allumette
    3. Morpion
    4. Scores
    5. Quitter
        """)

        choix = input("Faites votre choix : ")

        match choix:
            case '1': jeuDevinette(joueur1, joueur2)
            case '2': jeuAllumette(joueur1, joueur2)
            case '3': jeuMopion(joueur1, joueur2)
            case '4': menuScore(joueur1, joueur2)
            case '5': print("Au revoir\n")
