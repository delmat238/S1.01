from programme.joueur.joueur import Joueur
from programme.morpion.fonctionMorpion import *
from programme.utile.saisieNombre import saisieInt


def jeuMopion(joueur1: Joueur, joueur2: Joueur) -> None:
    plateau: list[list[str]] = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    x: int
    y: int

    affichePlateau(plateau)

    x = saisieX(joueur1)
    y = saisieY(joueur1)

    plateau[x][y] = "X"

    affichePlateau(plateau)