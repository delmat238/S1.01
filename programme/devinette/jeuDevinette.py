from programme.devinette.tourDeJeu import tourDeJeu
from programme.joueur.joueur import Joueur
from programme.utile.mrPropre import mrPropre
from programme.utile.saisieNombre import saisieInt


def jeuDevinette(joueur1: Joueur, joueur2: Joueur):
    comptJ1: int = 0
    comptJ2: int = 0
    borne: int = 0

    while borne <= 0:
        borne = saisieInt(joueur1.pseudo + " entrez la borne superieure à 0 : ", "Erreur de saisie\n Le nombre doit etre superieur à 0.")

    mrPropre()

    print("Bienvenue dans le jeu de la devinette")

    comptJ1 = tourDeJeu(joueur1, joueur2)

    print(joueur1.pseudo, "à vous de deviner le nombre que", joueur2.pseudo, "a choisi")

    comptJ2 = tourDeJeu(joueur2, joueur1)

    if comptJ1 < comptJ2:
        print(joueur1.pseudo, "vous avez gagné !")
        joueur1.scoreDevinette += 1
    elif comptJ1 > comptJ2:
        print(joueur2.pseudo, "vous avez gagné !")
        joueur2.scoreDevinette += 1
    else:
        print("Match nul")







