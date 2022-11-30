import json

from programme.joueur.joueur import Joueur
from programme.utile.chiffrement import *
from programme.utile.mrPropre import mrPropre
from programme.utile.colorfull import *
from programme.utile.ConfirmRetour import confirmRetour


def incrementScore(joueur: Joueur, nomjeu: str):
    """Permet d'incrémenter de 1 le score d'un joueur pour un jeu

    Args:
        joueur (Joueur): joueur dont le score est augmenté
        nomjeu (str): nom du jeu pour lequel le score est augmenté
    """
    data = json.loads(decrytion("programme/joueur/scores.dat")
                      )  # On charge les scores actuels dans le json
    with open("programme/joueur/scores.json", "w") as w_score_file:
        if joueur.pseudo in data['players']:
            data['players'][joueur.pseudo][nomjeu] = int(
                data['players'][joueur.pseudo][nomjeu])+1  # On incrémente les scores dans la sauvegarde
        else:
            data['players'][joueur.pseudo] = {
                "allumette": 0,
                "devinette": 0,
                "morpion": 0,
                "puissance 4": 0
            }
            data['players'][joueur.pseudo][nomjeu] = 1
        json.dump(data, w_score_file, indent=4)
    joueur.reloadScore()  # On demande une synchronisation


def classementJeu(nomjeu: str):
    listejoueurs: list = []
    scoresjoueurs: list = []
    classement: list[tuple] = []
    data = json.loads(decrytion("programme/joueur/scores.dat"))

    for joueur in data['players']:  # Récupération de la liste des joueurs
        listejoueurs.append(joueur)

    # Récupération des scores des joueurs
    for i in range(0, len(data['players'])):
        scoresjoueurs.append(data['players'][listejoueurs[i]][nomjeu])

    # Association des scores et des joueurs
    classement = sorted(zip(scoresjoueurs, listejoueurs), reverse=True)
    print(textform.BOLD+textcolor.PINK+"Classement "+nomjeu+textform.DEFAULT)

    for i in range(0, len(classement)):  # Affichage des scores pour le jeu donné
        print(textform.BOLD+str(i+1)+" : "+textform.DEFAULT +
              classement[i][1]+" - "+str(classement[i][0]))
    print()


def printClassement():
    """Affiche le classement des meilleurs joueurs
    """
    jeu: str
    mrPropre()
    for jeu in {'allumette', 'devinette', 'morpion', 'puissance 4'}: #On affiche pour chaque jeu présent dan le set
        classementJeu(jeu)
    confirmRetour()


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
    3. Retour
        """)

        choix = input("Faites votre choix : ")

        match choix:
            case '1': mrPropre(), joueur1.afficherScore(), print(), joueur2.afficherScore(), print(), confirmRetour()
            case '2': printClassement()
            case '3': mrPropre()
            case _: mrPropre()
