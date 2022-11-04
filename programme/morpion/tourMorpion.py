from programme.joueur.joueur import Joueur
from programme.morpion.fonctionMorpion import pionAligne, affichePlateau, saisieX, saisieY, plateauPlein


def tourMorpion(joueur1: Joueur, joueur2: Joueur) -> tuple[Joueur, Joueur]:
    plateau: list[list[str]] = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    x: int
    y: int
    pion: str
    aligne: bool
    plein: bool
    Bool: str

    affichePlateau(plateau)

    while True:
        while True:
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
                print("Case déjà prise")
        plateau[x][y] = "O"
        Bool, pion = pionAligne(plateau)
        aligne = eval(Bool)
        plein = plateauPlein(plateau)
        affichePlateau(plateau)
        if aligne or plein:
            break

    if pion == "X" and not plein:
        print(joueur1.pseudo + " a gagné !")
        joueur1.scoreMorpion += 1
    elif pion == "O" and not plein:
        print(joueur2.pseudo + " a gagné !")
        joueur2.scoreMorpion += 1
    else:
        print("Match nul !")

    return joueur1, joueur2

