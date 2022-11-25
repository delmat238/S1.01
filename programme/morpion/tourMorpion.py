from programme.joueur.joueur import Joueur
from programme.morpion.fonctionMorpion import pionAligne, affichePlateau, saisieX, saisieY, plateauPlein
from programme.utile.ConfirmRetour import confirmRetour
from programme.utile.score import incrementScore


def tourMorpion(joueur1: Joueur, joueur2: Joueur):
    """Procédure gérant un tour de morpion

    Args:
        joueur1 (Joueur): Joueur 1
        joueur2 (Joueur): Joueur 2
    """
    plateau: list[list[str]] = [
        ["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
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

    if pion == "X":
        print(joueur1.pseudo + " a gagné !")
        incrementScore(joueur1, "morpion")
    elif pion == "O":
        print(joueur2.pseudo + " a gagné !")
        incrementScore(joueur2, "morpion")
    elif plein:
        print("Match nul !")

    confirmRetour()
