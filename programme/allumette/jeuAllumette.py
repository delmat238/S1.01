from programme.joueur.joueur import Joueur
from programme.utile.mrPropre import mrPropre
from programme.utile.saisieNombre import *


def jeuAllumette(joueur1: Joueur, joueur2: Joueur):

    amax: int = 20  # Détermine un nombre max d'allumettes possible
    nallum: int = 0  # Nombre d'allumettes fixé par l'utilisateur
    nret: int  # Nombre d'allumettes retirées
    nrest: int  # Nombre d'allumettes restantes
    cp: Joueur = joueur1  # Joueur actuel

    mrPropre()

    print("Bienvenue dans le jeu des allumettes")

    while True:
        try:
            nallum = int(input("Sélectionnez le nombre d'allumettes : "))
            if nallum >= 6 and nallum <= amax:
                break
            else:
                print("Merci de choisir un nombre valide (min:6 / max:"+str(amax)+")")
        except ValueError:
            print("Erreur de saisie")

    nrest = nallum
    print(affichageAllumette(nallum, nrest))

    while nrest > 0:
        while True:
            nret = saisieInt(
                cp.pseudo + ", retirez entre 1 et 3 allumettes : ", "Erreur de saisie")
            if nret > 0 and nret < 4:
                break
            else:
                print("Nombre invalide, il doit être compris entre 1 et 3 inclus")
        nrest = nrest - nret
        mrPropre()
        print(affichageAllumette(nallum, nrest))
        if cp == joueur1:
            cp = joueur2
        else:
            cp = joueur1

    print(cp.pseudo + " gagne la partie !\n")


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

    return show
