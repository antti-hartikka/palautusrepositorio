class PlayerStats:

    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        return sorted(
            filter(lambda p: p.nationality == nationality, self.players),
            key=lambda p: p.goals + p.assists,
            reverse=True
        )
