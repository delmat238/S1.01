import json

from programme.joueur.joueur import Joueur
from programme.utile.chiffrement import *
from programme.utile.mrPropre import mrPropre
from programme.utile.colorfull import *


def setScore(score: int, joueur: Joueur, nomjeu: str):
    """Permet de définir le nouveau score d'un joueur

    Args:
        score (int): nouveau score du joueur
        joueur (Joueur): Joueur concerné
    """

    data = json.loads(decrytion("programme/joueur/scores.dat"))
    with open("programme/joueur/scores.json", "w") as w_score_file:
        if joueur.pseudo in data['players']:
            data['players'][joueur.pseudo][nomjeu] = score
        else:
            data['players'][joueur.pseudo] = {
                "allumette": 0,
                "devinette": 0,
                "morpion": 0,
                "puissance 4": 0
            }
            data['players'][joueur.pseudo][nomjeu] = score
        json.dump(data, w_score_file, indent=4)
    joueur.reloadScore()


def incrementScore(joueur: Joueur, nomjeu: str):
    """Permet d'incrémenter de 1 le score d'un joueur pour un jeu

    Args:
        joueur (Joueur): joueur dont le score est augmenté
        nomjeu (str): nom du jeu pour lequel le score est augmenté
    """
    data = json.loads(decrytion("programme/joueur/scores.dat"))
    with open("programme/joueur/scores.json", "w") as w_score_file:
        if joueur.pseudo in data['players']:
            data['players'][joueur.pseudo][nomjeu] = int(
                data['players'][joueur.pseudo][nomjeu])+1
        else:
            data['players'][joueur.pseudo] = {
                "allumette": 0,
                "devinette": 0,
                "morpion": 0,
                "puissance 4": 0
            }
            data['players'][joueur.pseudo][nomjeu] = 1
        json.dump(data, w_score_file, indent=4)
    joueur.reloadScore()


def resetScore(joueur: Joueur):
    """Permet de remettre à 0 tous les cores d'un joueur

    Args:
        joueur (Joueur): Joueur dont les scores sont remis à 0
    """
    data = json.loads(decrytion("programme/joueur/scores.dat"))
    with open("programme/joueur/scores.json", "w") as w_score_file:
        data['players'][joueur.pseudo] = {
            "allumette": 0,
            "devinette": 0,
            "morpion": 0,
            "puissance 4": 0
        }
        json.dump(data, w_score_file, indent=4)
    joueur.reloadScore()


def classementJeu(nomjeu: str):
    listejoueurs: list = []
    scoresjoueurs: list = []
    classement: list[tuple] = []
    data = json.loads(decrytion("programme/joueur/scores.dat"))

    for joueur in data['players']:                          #Récupération de la liste des joueurs
        listejoueurs.append(joueur)

    for i in range(0, len(data['players'])):                #Récupération des scores des joueurs
        scoresjoueurs.append(data['players'][listejoueurs[i]][nomjeu])

    classement = sorted(zip(scoresjoueurs, listejoueurs),reverse=True)   #Association des scores et des joueurs
    print(textform.BOLD+textcolor.PINK+"Classement "+nomjeu+textform.DEFAULT)

    for i in range(0, len(classement)):                     #Affichage des scores pour le jeu donné
        print(textform.BOLD+str(i+1)+" : "+textform.DEFAULT +
              classement[i][1]+" - "+str(classement[i][0]))
    print()


def printClassement():
    """Affiche le classement des meilleurs joueurs
    """
    jeu: str
    mrPropre()
    for jeu in {'allumette', 'devinette', 'morpion', 'puissance 4'}:
        classementJeu(jeu)


def menuScore(joueur1: Joueur, joueur2: Joueur):
    """Gère le menu des scores

    Args:
        joueur1 (Joueur): premier joueur renseigné sur le menu principal
        joueur2 (Joueur): second joueur renseigné sur le menu principal
    """

    choix: str = ""
    mrPropre()

    while choix != "3":
        print(textcolor.CYAN+maintexts.MS+textcolor.DEFAULT)
        print("""
    1. Score des Joueurs
    2. Classements
    3. Quitter
        """)

        choix = input("Faites votre choix : ")

        match choix:
            case '1': mrPropre(), joueur1.afficherScore(), print(), joueur2.afficherScore()
            case '2': printClassement()
            case '3': mrPropre()
            case _: mrPropre()
