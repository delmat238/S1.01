from programme.joueur.joueur import Joueur
from programme.utile.ConfirmRetour import confirmRetour
from programme.utile.colorfull import textcolor
from programme.utile.mrPropre import mrPropre
from programme.utile.saisieNombre import saisieInt
from programme.utile.score import incrementScore


def afficherPlateau(plateau: list[list[str]]):
    """Affiche le plateau de jeu du Puissance 4

    Args:
        plateau (list[list[str]]): Plateau de Jeu
    """
    print(" 1 2 3 4 5 6 7")
    for ligne in plateau:
        print("|", end="")
        for case in ligne:
            print(case, end="|")
        print()
    print()


def saisirColonne() -> int:
    """
Saisie d'une colonne

    Returns:
        int: Colonne saisie
    """
    colonne: int = saisieInt("Choisissez une colonne : ")
    while colonne < 1 or colonne > 7:
        print("Colonne invalide")
        colonne = saisieInt("Choisissez une colonne : ")
    return colonne - 1


def placerPion(plateau: list[list[str]], pion: str):
    """Place un pion dans la colonne donnée

    Args:
        plateau (list[list[str]]): Plateau
        pion (str): Chaine affichée en tant que pion
    """
    i: int = 5
    colonne: int = saisirColonne()

    while plateau[i][colonne] != " ":  # Tant que la case est occupée
        i -= 1
        if i == -1:
            print("Colonne pleine")
            colonne = saisirColonne()
            i = 5
        if colonne < 0 or colonne > 6:
            print("Colonne invalide")
            colonne = saisirColonne()
            i = 5

    plateau[i][colonne] = pion


def pionAligne(plateau: list[list[str]], pion: str) -> bool:
    """Vérifie si un pion est aligné

    Args:
        plateau (list[list[str]]): Plateau de Jeu
        pion (str): Chaine affichée en tant que pion

    Returns:
        bool: Vrai si le pion est aligné
    """
    # Vérification horizontale
    for ligne in plateau:
        for i in range(4):
            if ligne[i] == pion and ligne[i + 1] == pion and ligne[i + 2] == pion and ligne[i + 3] == pion:
                return True

    # Vérification verticale
    for j in range(7):
        for i in range(3):
            if plateau[i][j] == pion and plateau[i + 1][j] == pion and plateau[i + 2][j] == pion \
                    and plateau[i + 3][j] == pion:
                return True

    # Vérifications diagonales
    for i in range(3):
        for j in range(4):
            if plateau[i][j] == pion and plateau[i + 1][j + 1] == pion and plateau[i + 2][j + 2] == pion and \
                    plateau[i + 3][j + 3] == pion:
                return True

    for i in range(3):
        for j in range(3, 7):
            if plateau[i][j] == pion and plateau[i + 1][j - 1] == pion and plateau[i + 2][j - 2] == pion and \
                    plateau[i + 3][j - 3] == pion:
                return True

    return False


def plateauPlein(plateau: list[list[str]]) -> bool:
    """Vérifie si le plateau est plein

    Args:
        plateau (list[list[str]]): Plateau de jeu

    Returns:
        bool: Vrai si le plateau est plein
    """
    for ligne in plateau:
        for case in ligne:
            if case == " ":
                return False
    return True


def tourPuissance4(joueur1: Joueur, joueur2: Joueur):
    """Joue une partie de puissance 4 entre deux joueurs

    Args:
        joueur1 (Joueur): Joueur 1
        joueur2 (Joueur): Joueur 2
    """

    plateau: list[list[str]] = [[" " for _ in range(7)] for _ in range(6)] #Taille de 7*6 
    pionJ: str = textcolor.YELLOW + 'O' + textcolor.DEFAULT
    pionR: str = textcolor.RED + 'O' + textcolor.DEFAULT
    aligne: bool = False

    mrPropre()
    print(joueur1.pseudo, "joueur avec les", pionJ) #On indique à chaue joueur ses pions
    print(joueur2.pseudo, "joueur avec les", pionR)

    afficherPlateau(plateau)

    while not aligne and not plateauPlein(plateau): #On joue tant qu'il n'y a ni égalité ni victoire
        print(joueur1.pseudo + ", joue !")
        placerPion(plateau, pionJ)
        mrPropre()
        afficherPlateau(plateau)
        aligne = pionAligne(plateau, pionJ)
        if aligne:
            print(textcolor.GREEN + "Le joueur " +
                  joueur1.pseudo + " a gagné !" + textcolor.DEFAULT + "\n")
            incrementScore(joueur1, "puissance 4")
        if plateauPlein(plateau) or aligne:
            break

        print(joueur2.pseudo + ", joue !")
        placerPion(plateau, pionR)
        mrPropre()
        afficherPlateau(plateau)
        aligne = pionAligne(plateau, pionR)
        if aligne:
            print(textcolor.GREEN + "Le joueur " +
                  joueur2.pseudo + " a gagné !" + textcolor.DEFAULT + "\n")
            incrementScore(joueur2, "puissance 4")

    if plateauPlein(plateau):
        print(textcolor.CYAN + "Match nul !" + textcolor.DEFAULT + "\n")

    confirmRetour()
