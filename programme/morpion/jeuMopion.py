from programme.joueur.joueur import Joueur
from programme.morpion.fonctionMorpion import *
from programme.utile.saisieNombre import saisieInt


def jeuMopion(joueur1: Joueur, joueur2: Joueur) -> None:
    plateau: list[list[str]] = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    x: int
    y: int

    while not pionAligne(plateau):
        affichePlateau(plateau)
        while True:
            x = saisieX(joueur1)
            y = saisieY(joueur1)
            if plateau[x][y] == "-":
                break
            else:
                print("Case déjà prise")
        plateau[x][y] = "X"
        if pionAligne(plateau):
            break
        affichePlateau(plateau)
        while True:
            x = saisieX(joueur2)
            y = saisieY(joueur2)
            if plateau[x][y] == "-":
                break
            else:
                print("Case déjà prise")
        plateau[x][y] = "O"

    affichePlateau(plateau)
