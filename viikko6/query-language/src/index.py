from statistics import Statistics
from player_reader import PlayerReader
from matchers import *


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(20, "assists"),
        PlaysIn("PHI")
    )
    matcher2 = And(
        Not(HasAtLeast(2, "goals")),
        PlaysIn("NYR")
    )

    matcher3 = And(
        HasFewerThan(2, "goals"),
        PlaysIn("NYR")
    )

    assert (stats.matches(matcher2) == stats.matches(matcher3))

    for player in stats.matches(matcher2):
        print(player)

    filtered_with_all = stats.matches(All())
    assert (len(filtered_with_all) == 1058)

    matcher = And(
        HasAtLeast(70, "points"),
        Or(
            PlaysIn("NYR"),
            PlaysIn("FLA"),
            PlaysIn("BOS")
        )
    )


    print("\nOR matcher:")
    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
