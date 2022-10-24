from programme.joueur.joueur import Joueur
from programme.utile.mrPropre import mrPropre
from programme.utile.saisieNombre import *


def jeuDevinette(joueur1: Joueur, joueur2: Joueur):
    comptJ1: int = 0
    comptJ2: int = 0
    born: int
    nbATrouver: int
    proposition: int

    choix: int

    mrPropre()

    print("Bienvenue dans le jeu de la devinette")

    born = saisieInt(joueur1.pseudo, "Entrez un nombre entier positif : ", "Erreur de saisie")
    nbATrouver = saisieInt(joueur1.pseudo, "Entrez un nombre entier positif à deviner", "Erreur de saisie")

    while choix != 3:
        proposition = saisieInt(joueur1.pseudo, "Entrez un nombre entier positif : ", "Erreur de saisie")
        comptJ1 += 1

        print("Joueur 2 à vous de jouer")
        print(proposition, "est :")
        print("1. Plus grand")
        print("2. Plus petit")
        print("3. Egal")

        choix = saisieInt(joueur2.pseudo, "Faites votre choix : ", "Erreur de saisie")











