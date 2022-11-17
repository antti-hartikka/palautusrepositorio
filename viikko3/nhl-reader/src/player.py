class Player:
    def __init__(self, player):
        self.name = player["name"]
        self.nationality = player["nationality"]
        self.assists = player["assists"]
        self.goals = player["goals"]
        self.penalties = player["penalties"]
        self.team = player["team"]
        self.games = player["games"]
    
    def __str__(self):
        return f"{self.name:20} {self.team} {self.goals:2} + {self.assists:2} = {(self.goals + self.assists):3}"
