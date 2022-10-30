import json

from programme.joueur.joueur import Joueur


def setScore(score: int, joueur: Joueur, nomjeu: str):
    """Permet de définir le nouveau score d'un joueur

    Args:
        score (int): nouveau score du joueur
        joueur (Joueur): Joueur concerné
    """

    with open("programme/joueur/scores.json", "r") as r_score_file:
        data = json.load(r_score_file)
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
    with open("programme/joueur/scores.json", "r") as r_score_file:
        data = json.load(r_score_file)
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

def resetScore(joueur:Joueur):
    """Permet de remettre à 0 tous les cores d'un joueur

    Args:
        joueur (Joueur): Joueur dont les scores sont remis à 0
    """
    with open("programme/joueur/scores.json", "r") as r_score_file:
        data = json.load(r_score_file)
        with open("programme/joueur/scores.json", "w") as w_score_file:
            data['players'][joueur.pseudo] = {
                    "allumette": 0,
                    "devinette": 0,
                    "morpion": 0,
                    "puissance 4": 0
                }
            json.dump(data, w_score_file, indent=4)
    joueur.reloadScore()