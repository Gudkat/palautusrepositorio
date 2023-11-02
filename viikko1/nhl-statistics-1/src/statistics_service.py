from player_reader import PlayerReader
from enum import Enum


class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3


def sort_by_points(player, goals=False, assists=False):
    points = 0
    if goals:
        points += player.goals
    if assists:
        points += player.assists
    return points


class StatisticsService:
    def __init__(self, player_reader: PlayerReader):
        reader = player_reader
        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, sort_by=SortBy.POINTS):
        if sort_by == SortBy.GOALS:
            assists, goals = False, True
        elif sort_by == SortBy.ASSISTS:
            assists, goals = True, False
        elif sort_by == SortBy.POINTS:
            assists, goals = True, True
        else:
            return None

        sorted_players = sorted(
            self._players,
            reverse=True,
            key=lambda player: sort_by_points(
                player, goals=goals, assists=assists)
        )

        result = []
        i = 0
        while i < how_many:
            result.append(sorted_players[i])
            i += 1

        return result
