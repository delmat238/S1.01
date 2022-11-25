from programme.joueur.joueur import Joueur
from programme.utile.mrPropre import mrPropre
from programme.utile.saisieNombre import *
from programme.utile.score import incrementScore
from programme.utile.colorfull import *


def jeuAllumette(joueur1: Joueur, joueur2: Joueur):
    """Procédure gérant le jeu des allumettes

    Args:
        joueur1 (Joueur): Premier Joueur
        joueur2 (Joueur): Second Joueur
    """

    nallum: int = 20
    nret: int
    nrest: int
    cp: Joueur = joueur1

    mrPropre()

    print(textcolor.CYAN+"\nBienvenue dans le jeu des allumettes\n"+textcolor.DEFAULT)

    nrest = nallum
    print(affichageAllumette(nallum, nrest))

    while nrest > 0:
        while True:
            nret = saisieInt(
                cp.pseudo + ", retirez entre 1 et 3 allumettes : ", "Erreur de saisie")
            if nret > 0 and nret < 4:
                break
            else:
                print(
                    textform.WARNING+"Nombre invalide, il doit être compris entre 1 et 3 inclus"+textform.DEFAULT)
        nrest = nrest - nret
        mrPropre()
        print(affichageAllumette(nallum, nrest))
        if cp == joueur1:
            cp = joueur2
        else:
            cp = joueur1

    print(textcolor.GREEN+cp.pseudo + " gagne la partie !"+textcolor.DEFAULT)
    incrementScore(cp, "allumette")


def affichageAllumette(nallum: int, nrest: int) -> str:
    """Génère l'affichage des allumettes

    Args:
        nallum (int): Nombre d'allumettes en début de partie
        nrest (int): Nombre d'allumettes restantes

    Returns:
        str: Chaîne correspondant à l'affichage des allumettes actuellement en jeu
    """

    show: str = ""

    for i in range(0, nallum):
        if i < nrest:
            show = show + " |"
        else:
            show = show + " ."

    show = "\n"+show+"\n"
    return show