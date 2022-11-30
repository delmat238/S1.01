from programme.devinette.tourDeJeu import tourDeJeu
from programme.joueur.joueur import Joueur
from programme.utile.ConfirmRetour import confirmRetour
from programme.utile.mrPropre import mrPropre
from programme.utile.saisieNombre import saisieInt
from programme.utile.score import incrementScore
from programme.utile.colorfull import *


def jeuDevinette(joueur1: Joueur, joueur2: Joueur):
    """Procédure gérant le jeu Devinette

    Args:
        joueur1 (Joueur): _description_
        joueur2 (Joueur): _description_
    """
    comptJ1: int
    comptJ2: int
    borne: int = 0

    mrPropre()

    while borne <= 1: #Saisie et vérification de la borne
        borne = saisieInt(joueur1.pseudo + " entrez la borne superieure à 1 : ",
                          "Erreur de saisie\n Le nombre doit etre superieur à 1.")

    mrPropre()
    print(textform.BOLD + "Bienvenue dans le jeu de la devinette\n" + textform.DEFAULT)

    comptJ2 = tourDeJeu(joueur1, joueur2, borne)

    print("\n" + joueur1.pseudo + ", à vous de deviner le nombre que",
          joueur2.pseudo, "a choisi\n")

    comptJ1 = tourDeJeu(joueur2, joueur1, borne)

    if comptJ1 < comptJ2:
        print("\n" +textcolor.GREEN+ joueur1.pseudo + ", vous avez gagné !"+textcolor.DEFAULT+"\n")
        incrementScore(joueur1, "devinette") #Ajout d'un point
    elif comptJ1 > comptJ2:
        print("\n" +textcolor.GREEN+ joueur2.pseudo + ", vous avez gagné !"+textcolor.DEFAULT+"\n")
        incrementScore(joueur2, "devinette") #Ajout d'un point
    else:
        print("\n"+textcolor.YELLOW + "Match nul"+textcolor.DEFAULT+"\n")

    confirmRetour()
