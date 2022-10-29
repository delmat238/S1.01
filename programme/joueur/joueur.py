import json


class Joueur:
    pseudo: str
    scoreDevinette: int
    scoreAllumette: int
    scoreMorpion: int

    def __init__(self, pseudo: str):
        self.pseudo = pseudo
        with open("programme/joueur/scores.json", "r") as r_score_file:
            data = json.load(r_score_file) 
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

    def afficherScore(self):
        self.afficherScoreDevinette()
        self.afficherScoreAllumette()
        self.afficherScoreMorpion()

    def afficherScoreDevinette(self):
        print("Score Devinette : ", self.scoreDevinette)

    def afficherScoreAllumette(self):
        print("Score Allumette : ", self.scoreAllumette)

    def afficherScoreMorpion(self):
        print("Score Morpion : ", self.scoreMorpion)



