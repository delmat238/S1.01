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
            data = json.loads(decrytion("programme/joueur/scores.dat"))
        except FileNotFoundError:
            print("\n"+textform.WARNING+"Fichier de sauvegarde absent, un nouveau sera généré."+textform.DEFAULT)
            repair()
            data = json.loads(decrytion("programme/joueur/scores.dat"))
        with open("programme/joueur/scores.json", "w") as w_score_file:
            if not pseudo in data['players']:
                data['players'][pseudo] = {
                    "allumette": 0,
                    "devinette": 0,
                    "morpion": 0,
                    "puissance 4": 0
                }
            json.dump(data, w_score_file, indent=4)
        self.scoreDevinette = data['players'][pseudo]["devinette"]
        self.scoreAllumette = data['players'][pseudo]["allumette"]
        self.scoreMorpion = data['players'][pseudo]["morpion"]
        self.scoreP4 = data['players'][pseudo]["puissance 4"]
        self.reloadScore()

    def reloadScore(self):
        """Recharge le score du joueur dans le fichier chiffré
        """

        pseudo = self.pseudo
        with open("programme/joueur/scores.json", "r") as r_score_file:
            data = json.load(r_score_file)
            self.scoreDevinette = data['players'][pseudo]["devinette"]
            self.scoreAllumette = data['players'][pseudo]["allumette"]
            self.scoreMorpion = data['players'][pseudo]["morpion"]
            self.scoreP4 = data['players'][pseudo]["puissance 4"]
        encryption("programme/joueur/scores.json")

    def afficherScore(self):
        print(textcolor.PINK+"Scores du joueur "+self.pseudo+":"+textcolor.DEFAULT)
        self.afficherScoreDevinette()
        self.afficherScoreAllumette()
        self.afficherScoreMorpion()

    def afficherScoreDevinette(self):
        print("Score Devinette : ", self.scoreDevinette)

    def afficherScoreAllumette(self):
        print("Score Allumette : ", self.scoreAllumette)

    def afficherScoreMorpion(self):
        print("Score Morpion : ", self.scoreMorpion)
