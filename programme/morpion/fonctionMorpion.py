from programme.joueur.joueur import Joueur
from programme.utile.saisieNombre import saisieInt


def affichePlateau(plateau: list[list[str]]) -> None:
    """ Affiche le plateau de jeu
    """
    print("  0 1 2")
    for i in range(3):
        print(i, end=" ")
        for j in range(3):
            print(plateau[i][j], end=" ")
        print()


def saisieX(joueur: Joueur) -> int:
    """ Saisie de la ligne
    """
    while True:
        x = saisieInt(joueur.pseudo + " entrez la ligne : ", "Erreur de saisie")
        if x >= 0 and x <= 2:
            break
    return x


def saisieY(joueur: Joueur) -> int:
    """ Saisie de la colonne
    """
    while True:
        y = saisieInt(joueur.pseudo + " entrez la colonne : ", "Erreur de saisie")
        if y >= 0 and y <= 2:
            break
    return y



