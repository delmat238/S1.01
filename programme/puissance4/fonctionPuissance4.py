from programme.utile.saisieNombre import saisieInt


def afficherPlateau(plateau: list[list[str]]) -> None:
    """
    Affiche le plateau de jeu
    :param plateau: le plateau de jeu
    :return: None
    """
    print(" 0 1 2 3 4 5 6")
    for ligne in plateau:
        print("|", end="")
        for case in ligne:
            print(case, end="|")
        print()
    print("---------------")


def placerPion(plateau: list[list[str]], pion: str) -> None:
    """
    Place un pion dans la colonne donnée
    :param plateau: le plateau de jeu
    :param pion: le pion à placer
    :return: None
    """
    i: int = 5
    colonne: int = saisieInt("Choisissez une colonne : ")

    while plateau[i][colonne] != " ":  # Tant que la case est occupée
        i -= 1
        if i == -1:
            print("Colonne pleine")
            colonne = saisieInt("Choisissez une colonne : ")
            i = 5

    plateau[i][colonne] = pion


def pionAligne(plateau: list[list[str]], pion: str) -> bool:
    """
    Vérifie si un pion est aligné
    :param plateau: le plateau de jeu
    :param pion: le pion à vérifier
    :return: True si le pion est aligné, False sinon
    """
    # Vérification horizontale
    for ligne in plateau:
        for i in range(4):
            if ligne[i] == pion and ligne[i+1] == pion and ligne[i+2] == pion and ligne[i+3] == pion:
                return True

    # Vérification verticale
    for j in range(7):
        for i in range(3):
            if plateau[i][j] == pion and plateau[i+1][j] == pion and plateau[i+2][j] == pion and plateau[i+3][j] == pion:
                return True

    # Vérification diagonale
    for i in range(3):
        for j in range(4):
            if plateau[i][j] == pion and plateau[i+1][j+1] == pion and plateau[i+2][j+2] == pion and plateau[i+3][j+3] == pion:
                return True

    for i in range(3):
        for j in range(3, 7):
            if plateau[i][j] == pion and plateau[i+1][j-1] == pion and plateau[i+2][j-2] == pion and plateau[i+3][j-3] == pion:
                return True

    return False


