from statistics import Statistics
from player_reader import PlayerReader
from matchers import *
from query_builder import QueryBuilder


def main():
    url = "https://studies.cs.helsinki.fi//nhlstats/2022-23/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()

    matcher = (
        query
        .oneOf(
            query.playsIn("PHI")
            .hasAtLeast(5, "assists")
            .hasFewerThan(5, "goals")
            .build(),
            query.playsIn("EDM")
            .hasAtLeast(5, "points")
            .build()
        )
        .build()
    )

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
