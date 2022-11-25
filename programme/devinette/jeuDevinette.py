from programme.devinette.tourDeJeu import tourDeJeu
from programme.joueur.joueur import Joueur
from programme.utile.ConfirmRetour import confirmRetour
from programme.utile.mrPropre import mrPropre
from programme.utile.saisieNombre import saisieInt
from programme.utile.score import incrementScore
from programme.utile.colorfull import *


def jeuDevinette(joueur1: Joueur, joueur2: Joueur):
    """
    Fonction principal du jeu Devinette
    :param joueur1:
    :param joueur2:
    :return:
    """
    comptJ1: int
    comptJ2: int
    borne: int = 0

    mrPropre()

    while borne <= 0:
        borne = saisieInt(joueur1.pseudo + " entrez la borne superieure à 0 : ",
                          "Erreur de saisie\n Le nombre doit etre superieur à 0.")

    mrPropre()
    print(textform.BOLD + "Bienvenue dans le jeu de la devinette\n" + textform.DEFAULT)

    comptJ2 = tourDeJeu(joueur1, joueur2, borne)

    print("\n" + joueur1.pseudo + ", à vous de deviner le nombre que",
          joueur2.pseudo, "a choisi\n")

    comptJ1 = tourDeJeu(joueur2, joueur1, borne)

    if comptJ1 < comptJ2:
        print("\n" + joueur1.pseudo + ", vous avez gagné !")
        incrementScore(joueur1, "devinette")
    elif comptJ1 > comptJ2:
        print("\n" + joueur2.pseudo + ", vous avez gagné !")
        incrementScore(joueur2, "devinette")
    else:
        print("\nMatch nul")

    confirmRetour()
