import requests
from player import Player


class PlayerReader:
    def __init__(self, url):
        self.url = url
        self.players = []
        self.get_json_data()

    def get_json_data(self):
        self.response = requests.get(self.url).json()

    def get_players(self):
        return [Player(player_dict) for player_dict in self.response]


class PlayerStats:
    def __init__(self, players: PlayerReader):
        self.players = players.get_players()

    def top_scorers_by_nationality(self, nationality):
        players = [
            player for player in self.players if player.nationality == nationality]
        return sorted(players, key=lambda pl: (pl.points(), pl.goals), reverse=True)


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)


if __name__ == "__main__":
    main()
