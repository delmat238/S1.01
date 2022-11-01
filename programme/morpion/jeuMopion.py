from programme.joueur.joueur import Joueur
from programme.morpion.fonctionMorpion import affichePlateau


def jeuMopion(joueur1: Joueur, joueur2: Joueur) -> None:
    plateau: list[list[str]] = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    x: int
    y: int

    affichePlateau(plateau)



