from programme.joueur.joueur import Joueur
from programme.puissance4.fonctionPuissance4 import afficherPlateau, placerPion
from programme.utile.colorfull import textcolor


def jeuPuissance4(joueur1: Joueur, joueur2: Joueur,) -> tuple[Joueur, Joueur]:
    """
    Joue une partie de puissance 4 entre deux joueurs
    :param joueur1: le premier joueur
    :param joueur2: le deuxième joueur
    :return: le joueur gagnant et le joueur perdant
    """

    plateau: list[list[str]] = [[" " for _ in range(7)] for _ in range(6)]
    pionJ: str = textcolor.YELLOW+'O'+textcolor.DEFAULT
    pionR: str = textcolor.RED+'O'+textcolor.DEFAULT

    print(textcolor.CYAN+"Jeu Puissance 4"+textcolor.DEFAULT)

    afficherPlateau(plateau)
    placerPion(plateau, pionJ)
    afficherPlateau(plateau)

