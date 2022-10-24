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
