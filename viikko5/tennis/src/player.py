SCORE_INIT = 0


class Player:
    def __init__(self, name):
        self.name = name
        self.score = SCORE_INIT

    def increment_score(self):
        self.score += 1

    def __repr__(self):
        return self.name

    def __lt__(self, other):
        return self.score < other.score
