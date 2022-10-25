from programme.joueur.joueur import Joueur
from programme.utile.mrPropre import mrPropre


def jeuAllumette(joueur1: Joueur, joueur2: Joueur):

    amax: int = 20  # Détermine un nombre max d'allumettes possible
    nallum: int = 0  # Nombre d'allumettes fixé par l'utilisateur

    mrPropre()

    print("Bienvenue dans le jeu des allumettes")

    while nallum >= 5 and nallum >= amax:
        try: 
            int(input("Sélectionnez le nombre d'allumettes")) 
            break
        except ValueError:
            print("Merci de choisir un nombre valide")
    
    #WIP