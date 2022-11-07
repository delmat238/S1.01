from programme.joueur.joueur import Joueur
from programme.morpion.fonctionMorpion import *
from programme.morpion.tourMorpion import tourMorpion
from programme.utile.saisieNombre import saisieInt
from programme.utile.colorfull import *


def jeuMopion(joueur1: Joueur, joueur2: Joueur):
    pseudo: str = ""

    while pseudo != joueur1.pseudo and pseudo != joueur2.pseudo:
        pseudo = input("Entrez le pseudo du joueur qui commence : ")

        if pseudo != joueur1.pseudo and pseudo != joueur2.pseudo:
            print(textform.WARNING+"Pseudo inconnu"+textform.DEFAULT)

    if pseudo == joueur1.pseudo:
        joueur1, joueur2 = tourMorpion(joueur1, joueur2)
    else:
        joueur2, joueur1 = tourMorpion(joueur2, joueur1)




