from programme.joueur.joueur import Joueur
from programme.puissance4.fonctionPuissance4 import tourPuissance4
from programme.utile.colorfull import textcolor


def jeuPuissance4(joueur1: Joueur, joueur2: Joueur, ) -> tuple[Joueur, Joueur]:
    """
    Joue une partie de puissance 4 entre deux joueurs
    :param joueur1: le premier joueur
    :param joueur2: le deuxième joueur
    :return: le joueur gagnant et le joueur perdant
    """

    pseudo: str = ''

    print(textcolor.CYAN + "Jeu Puissance 4" + textcolor.DEFAULT)

    while pseudo != joueur1.pseudo and pseudo != joueur2.pseudo:
        pseudo = input("Entrez le pseudo du joueur qui commence : ")

    if pseudo == joueur1.pseudo:
        joueur1, joueur2 = tourPuissance4(joueur1, joueur2)

    if pseudo == joueur2.pseudo:
        joueur2, joueur1 = tourPuissance4(joueur2, joueur1)

    return joueur1, joueur2
