import getpass

from programme.joueur.joueur import Joueur
from programme.utile.mrPropre import mrPropre
from programme.utile.saisieNombre import saisieInt


def tourDeJeu(joueurChoisit: Joueur, joueurCherche: Joueur, borne: int) -> int:
    """Procédure gérant un tour du jeu Devinette

    Args:
        joueurChoisit (Joueur): Joueur qui choisit la borne
        joueurCherche (Joueur): Joueur qui joue en 2e
        borne (int): Borne définie par le premier joueur

    Returns:
        int: Nombre de coups pour trouver le nombre
    """

    comptJoueur: int = 0
    nbATrouver: int = 0
    choix: int = 0
    proposition: int

    while nbATrouver <= 0 or nbATrouver >= borne: #Entrée du nombre caché
        try:
            nbATrouver = int(getpass.getpass("Entrez le nombre que " +
                             joueurCherche.pseudo + " doit trouver entre 0 et " + str(borne) + " : "))
            break
        except ValueError:
            print("Erreur de saisie")

    while choix != 3:
        proposition = saisieInt( #proposition par le joueur
            "\n"+joueurCherche.pseudo + " devine le nombre : ", "Erreur de saisie")
        comptJoueur += 1

        print("\n"+joueurChoisit.pseudo, "à vous de jouer") #Réponse
        print(proposition, "est :")
        print("1. Plus grand")
        print("2. Plus petit")
        print("3. Egal")

        choix = saisieInt(joueurChoisit.pseudo +
                          " faites votre choix : ", "Erreur de saisie")

        match choix:
            case 1: print(proposition, "est plus grand")
            case 2: print(proposition, "est plus petit")

        if choix == 1 and proposition < nbATrouver:
            print(joueurChoisit.pseudo, "n'essaye pas de tricher !")
            print(proposition, "est plus petit")
        if choix == 2 and proposition > nbATrouver:
            print(joueurChoisit.pseudo, "n'essaye pas de tricher !")
            print(proposition, "est plus grand")
        if choix != 3 and proposition == nbATrouver:
            print(joueurChoisit.pseudo, "n'essaye pas de tricher !")
            choix = 3
        if choix == 3 and proposition != nbATrouver:
            print("Fait attention", joueurChoisit.pseudo)

    mrPropre()
    print("Bien joué", joueurCherche.pseudo,
          "vous avez trouvé le nombre en", comptJoueur, "coups")

    return comptJoueur
