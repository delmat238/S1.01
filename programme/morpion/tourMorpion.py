from programme.joueur.joueur import Joueur
from programme.morpion.fonctionMorpion import pionAligne, affichePlateau, saisieX, saisieY, plateauPlein
from programme.utile.ConfirmRetour import confirmRetour
from programme.utile.score import incrementScore
from programme.utile.mrPropre import mrPropre
from programme.utile.colorfull import *


def tourMorpion(joueur1: Joueur, joueur2: Joueur):
    """Procédure gérant un tour de morpion

    Args:
        joueur1 (Joueur): Joueur 1
        joueur2 (Joueur): Joueur 2
    """

    mrPropre()

    plateau: list[list[str]] = [ #Définition du plateau
        ["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    x: int
    y: int
    pion: str
    aligne: bool
    plein: bool
    Bool: str

    affichePlateau(plateau) #Premier affichage

    while True:
        while True: #On joue tant qu'il n'y a pas de victoire ou d'égalité
            x = saisieX(joueur1)
            y = saisieY(joueur1)
            if plateau[x][y] == "-":
                break
            else:
                print("Case déjà prise")
        plateau[x][y] = "X"
        Bool, pion = pionAligne(plateau)
        aligne = eval(Bool)
        plein = plateauPlein(plateau)
        affichePlateau(plateau)
        if aligne or plein:
            break
        while True:
            x = saisieX(joueur2)
            y = saisieY(joueur2)
            if plateau[x][y] == "-":
                break
            else:
                print(textform.WARNING+"Case déjà prise"+textform.DEFAULT)
        plateau[x][y] = "O"
        Bool, pion = pionAligne(plateau)
        aligne = eval(Bool)
        plein = plateauPlein(plateau)
        affichePlateau(plateau)
        if aligne or plein:
            break

    if pion == "X":
        print(textcolor.GREEN+"\n"+joueur1.pseudo +
              " a gagné !"+textcolor.DEFAULT+"\n")
        incrementScore(joueur1, "morpion")
    elif pion == "O":
        print(textcolor.GREEN+"\n"+joueur2.pseudo +
              " a gagné !"+textcolor.DEFAULT+"\n")
        incrementScore(joueur2, "morpion")
    elif plein:
        print("\n"+textcolor.YELLOW + "Match nul"+textcolor.DEFAULT+"\n")

    confirmRetour()
