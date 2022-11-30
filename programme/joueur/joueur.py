import json
from programme.utile.chiffrement import *


class Joueur:
    pseudo: str
    scoreDevinette: int
    scoreAllumette: int
    scoreMorpion: int
    scoreP4: int

    def __init__(self, pseudo: str):
        self.pseudo = pseudo
        try:
            data = json.loads(decrytion("programme/joueur/scores.dat")) #On cherche à récupérer le joueur dans la sauvegarde
        except FileNotFoundError:
            print("\n" + textform.WARNING +
                  "Fichier de sauvegarde absent, un nouveau sera généré." + textform.DEFAULT)
            repair()
            data = json.loads(decrytion("programme/joueur/scores.dat"))
        with open("programme/joueur/scores.json", "w") as w_score_file:
            if not pseudo in data['players']: #On ajoute le joueur à la sauvegarde si il n'y est pas
                data['players'][pseudo] = {
                    "allumette": 0,
                    "devinette": 0,
                    "morpion": 0,
                    "puissance 4": 0
                }
            json.dump(data, w_score_file, indent=4)
        self.scoreDevinette = data['players'][pseudo]["devinette"] #On synchronise l'objet avec le contenu de la sauvegarde
        self.scoreAllumette = data['players'][pseudo]["allumette"]
        self.scoreMorpion = data['players'][pseudo]["morpion"]
        self.scoreP4 = data['players'][pseudo]["puissance 4"]
        self.reloadScore()

    def reloadScore(self):
        """Recharge le score du joueur dans le fichier chiffré
        """

        pseudo = self.pseudo
        with open("programme/joueur/scores.json", "r") as r_score_file: #Synchronise le score de la sauvegarde avec celui de la classe
            data = json.load(r_score_file)
            self.scoreDevinette = data['players'][pseudo]["devinette"]
            self.scoreAllumette = data['players'][pseudo]["allumette"]
            self.scoreMorpion = data['players'][pseudo]["morpion"]
            self.scoreP4 = data['players'][pseudo]["puissance 4"]
        encryption("programme/joueur/scores.json")

    def afficherScore(self):
        """Affiche la totalité des scores
        """
        print(textcolor.PINK + "Scores du joueur " +
              self.pseudo + ":" + textcolor.DEFAULT)
        self.afficherScoreDevinette()
        self.afficherScoreAllumette()
        self.afficherScoreMorpion()
        self.afficherScoreP4()

    def afficherScoreDevinette(self):
        """Affiche les scores de Devinette
        """
        print("Score Devinette : ", self.scoreDevinette)

    def afficherScoreAllumette(self):
        """Affiche les scores des Allumettes
        """
        print("Score Allumette : ", self.scoreAllumette)

    def afficherScoreMorpion(self):
        """Affiche les scores du Morpion
        """
        print("Score Morpion : ", self.scoreMorpion)

    def afficherScoreP4(self):
        """Affiche les scores du Puissance4
        """
        print("Score Puissance 4 : ", self.scoreP4)
