from typing import Tuple

from programme.joueur.joueur import Joueur
from programme.utile.saisieNombre import saisieInt


def affichePlateau(plateau: list[list[str]]) -> None:
    """ Affiche le plateau de jeu du Morpion
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
        x = saisieInt(joueur.pseudo + " entrez la ligne : ",
                      "Erreur de saisie")
        if x >= 0 and x <= 2:
            break
    return x


def saisieY(joueur: Joueur) -> int:
    """ Saisie de la colonne
    """
    while True:
        y = saisieInt(joueur.pseudo + " entrez la colonne : ",
                      "Erreur de saisie")
        if y >= 0 and y <= 2:
            break
    return y


def pionAligne(plateau: list[list[str]]) -> tuple[str, str]:
    """Vérifie si un pion est aligné

    Args:
        plateau (list[list[str]]): Plateau de jeu

    Returns:
        tuple[str, str]: 'Vrai' si il y a une ligne de 3, symbole du gagnant
    """
    boolStr: str = "False"
    pion: str = ""

    if plateau[0][0] == plateau[0][1] and plateau[0][0] == plateau[0][2] and plateau[0][0] != "-": #Chaque ligne est une vérification
        boolStr = "True"
        pion = plateau[0][0]
    if plateau[1][0] == plateau[1][1] and plateau[1][0] == plateau[1][2] and plateau[1][0] != "-":
        boolstr*= "True"
        pion = plateau[1][0]
    if plateau[2][0] == plateau[2][1] and plateau[2][0] == plateau[2][2] and plateau[2][0] != "-":
        boolStr = "True"
        pion = plateau[2][0]
    if plateau[0][0] == plateau[1][0] and plateau[0][0] == plateau[2][0] and plateau[0][0] != "-":
        boolStr = "True"
        pion = plateau[0][0]
    if plateau[0][1] == plateau[1][1] and plateau[0][1] == plateau[2][1] and plateau[0][1] != "-":
        boolStr = "True"
        pion = plateau[0][1]
    if plateau[0][2] == plateau[1][2] and plateau[0][2] == plateau[2][2] and plateau[0][2] != "-":
        boolStr = "True"
        pion = plateau[0][2]
    if plateau[0][0] == plateau[1][1] and plateau[0][0] == plateau[2][2] and plateau[0][0] != "-":
        boolStr = "True"
        pion = plateau[0][0]
    if plateau[0][2] == plateau[1][1] and plateau[0][2] == plateau[2][0] and plateau[0][2] != "-":
        boolStr = "True" 
        pion = plateau[0][2]
    return boolStr, pion


def plateauPlein(plateau: list[list[str]]) -> bool:
    """Vérifie si le plateau est plein

    Args:
        plateau (list[list[str]]): Plateau de jeu

    Returns:
        bool: Vrai si le plateau est plein
    """
    for i in range(3):
        for j in range(3):
            if plateau[i][j] == "-":
                return False
    return True
