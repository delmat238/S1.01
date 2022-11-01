def affichePlateau(plateau: list[list[str]]) -> None:
    """ Affiche le plateau de jeu
    """
    print("  0 1 2")
    for i in range(3):
        print(i, end=" ")
        for j in range(3):
            print(plateau[i][j], end=" ")
        print()