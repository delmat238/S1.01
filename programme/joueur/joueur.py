class Joueur:
    pseudo: str
    scoreDevinette: int
    scoreAllumette: int
    scoreMorpion: int

    def __init__(self, pseudo: str):
        self.pseudo = pseudo
        self.scoreDevinette = 0
        self.scoreAllumette = 0
        self.scoreMorpion = 0

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



