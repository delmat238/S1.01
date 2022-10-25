import getpass
from programme.utile.saisieNombre import saisieInt


def tourDeJeu(joueurChoisit, joueurCherche, borne: int) -> int:
    borne: int = 0
    comptJoueur: int = 0
    nbATrouver: int = 0
    choix: int = 0

    while nbATrouver <= 0 or nbATrouver >= borne:
        try:
            nbATrouver = int(getpass.getpass("Entrez le nombre que " + joueurCherche.pseudo + " doit trouver entre 0 et " + str(borne) + " : "))
            break
        except ValueError:
            print("Erreur de saisie")

    while choix != 3:
        proposition = saisieInt(joueurCherche.pseudo + " devine le nombre : ", "Erreur de saisie")
        comptJoueur += 1

        print(joueurChoisit.pseudo, "à vous de jouer")
        print(proposition, "est :")
        print("1. Plus grand")
        print("2. Plus petit")
        print("3. Egal")

        choix = saisieInt(joueurChoisit.pseudo + " faites votre choix : ", "Erreur de saisie")

        if choix == 1 and proposition < nbATrouver:
            print(joueurChoisit.pseudo, "n'essaye pas de tricher")
        if choix == 2 and proposition > nbATrouver:
            print(joueurChoisit.pseudo, "n'essaye pas de tricher")
        if choix != 3 and proposition == nbATrouver:
            print(joueurChoisit.pseudo, "n'essaye pas de tricher")
            choix = 3
        if choix == 3 and proposition != nbATrouver:
            print("Fait attention", joueurChoisit.pseudo)

    print("Bien joué", joueurCherche.pseudo, "vous avez trouvé le nombre en", comptJoueur, "coups")

    return comptJoueur
