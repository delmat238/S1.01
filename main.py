from programme.allumette.jeuAllumette import jeuAllumette
from programme.joueur.joueur import Joueur
from programme.morpion.jeuMopion import jeuMorpion
from programme.devinette.jeuDevinette import jeuDevinette
from programme.puissance4.JeuPuissance4 import jeuPuissance4
from programme.utile.score import menuScore
from programme.utile.mrPropre import mrPropre
from programme.utile.colorfull import *

if __name__ == '__main__':
    choix: str = ""
    joueur1: Joueur
    joueur2: Joueur
    pseudo: str
    mrPropre()
    pseudo = input("Entrez le pseudo du joueur 1 : ")
    joueur1 = Joueur(pseudo)
    while pseudo == joueur1.pseudo:
        pseudo = input("Entrez le pseudo du joueur 2 : ")
        if pseudo == joueur1.pseudo:    #Le premier pseudo doit être différent du second
            print(textform.ERROR +
                  "Ce pseudo est déjà utilisé par le joueur 1"+textform.DEFAULT)
    joueur2 = Joueur(pseudo)

    mrPropre()

    while choix != "6":
        print("\n"+textcolor.PURPLE+maintexts.MP+textcolor.DEFAULT)
        print("""
    1. Devinette
    2. Allumette
    3. Morpion
    4. Puissance 4
    5. Scores
    6. Quitter
        """)

        choix = input("Faites votre choix : ")

        match choix:
            case '1': jeuDevinette(joueur1, joueur2)
            case '2': jeuAllumette(joueur1, joueur2)
            case '3': jeuMorpion(joueur1, joueur2)
            case '4': jeuPuissance4(joueur1, joueur2)
            case '5': menuScore(joueur1, joueur2)
            case '6': print("Au revoir\n")
            case _: mrPropre()
