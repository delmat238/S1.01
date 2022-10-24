from programme.joueur.joueur import Joueur
from programme.utile.mrPropre import mrPropre
from programme.utile.saisieNombre import saisieInt
import getpass


def jeuDevinette(joueur1: Joueur, joueur2: Joueur):
    comptJ1: int = 0
    comptJ2: int = 0
    born: int = 0
    nbATrouver: int = 0
    proposition: int

    choix: int = 0

    mrPropre()

    print("Bienvenue dans le jeu de la devinette")

    while born <= 0:
        born = saisieInt(joueur1.pseudo + " entrez la borne superieure à 0 : ", "Erreur de saisie\n Le nombre doit etre superieur à 0.")

    while nbATrouver <= 0 or nbATrouver >= born:
        try:
            nbATrouver = int(getpass.getpass("Entrez le nombre que " + joueur2.pseudo + " doit trouver entre 0 et " + str(born) + " : "))
            break
        except ValueError:
            print("Erreur de saisie")

    while choix != 3:
        proposition = saisieInt(joueur2.pseudo + " devine le nombre : ", "Erreur de saisie")
        comptJ1 += 1

        print(joueur1.pseudo, "à vous de jouer")
        print(proposition, "est :")
        print("1. Plus grand")
        print("2. Plus petit")
        print("3. Egal")

        choix = saisieInt(joueur1.pseudo + " faites votre choix : ", "Erreur de saisie")

        if choix == 1 and proposition < nbATrouver:
            print(joueur1.pseudo, "n'essaye pas de tricher")
        if choix == 2 and proposition > nbATrouver:
            print(joueur1.pseudo, "n'essaye pas de tricher")
        if choix != 3 and proposition == nbATrouver:
            print(joueur1.pseudo, "n'essaye pas de tricher")
            choix = 3
        if choix == 3 and proposition != nbATrouver:
            print("Fait attention", joueur1.pseudo)

    print("Bien joué", joueur1.pseudo, "vous avez gagné en", comptJ1, "coups")

    print(joueur1.pseudo, "à vous de deviner le nombre que", joueur2.pseudo, "a choisi")

    while nbATrouver <= 0 or nbATrouver >= born:
        try:
            nbATrouver = int(getpass.getpass("Entrez le nombre que " + joueur1.pseudo + " doit trouver entre 0 et " + str(born) + " : "))
            break
        except ValueError:
            print("Erreur de saisie")

    choix = 0
    while choix != 3:
        proposition = saisieInt(joueur1.pseudo + " devine le nombre : ", "Erreur de saisie")
        comptJ1 += 1

        print(joueur2.pseudo, "à vous de jouer")
        print(proposition, "est :")
        print("1. Plus grand")
        print("2. Plus petit")
        print("3. Egal")

        choix = saisieInt(joueur2.pseudo + " faites votre choix : ", "Erreur de saisie")

        if choix == 1 and proposition < nbATrouver:
            print(joueur2.pseudo, "n'essaye pas de tricher")
        if choix == 2 and proposition > nbATrouver:
            print(joueur2.pseudo, "n'essaye pas de tricher")
        if choix != 3 and proposition == nbATrouver:
            print(joueur2.pseudo, "n'essaye pas de tricher")
            choix = 3
        if choix == 3 and proposition != nbATrouver:
            print("Fait attention", joueur1.pseudo)









