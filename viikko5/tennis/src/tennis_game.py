from player import Player

POINT_NAMES = ["Love", "Fifteen", "Thirty", "Forty", "Deuce"]


def tie_score(points):
    score = POINT_NAMES[min(points, 4)]
    if points <= 3:
        score = score + "-All"
    return score


def standard_score(player1, player2):
    return f"{POINT_NAMES[player1.score]}-{POINT_NAMES[player2.score]}"


def there_is_winner(player1, player2):
    return abs(player1.score - player2.score) >= 2


class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)

    def won_point(self, player_name):
        if player_name == self.player1.name:
            self.player1.increment_score()
        elif player_name == self.player2.name:
            self.player2.increment_score()

    def get_score(self):
        player1 = self.player1
        player2 = self.player2
        score_difference = player1.score - player2.score

        if score_difference == 0:
            return tie_score(player1.score)

        if player1.score >= 4 or player2.score >= 4:
            leader = max(player1, player2)
            if there_is_winner(player1, player2):
                return f"Win for {leader}"
            else:
                return f"Advantage {leader}"

        return standard_score(player1, player2)
