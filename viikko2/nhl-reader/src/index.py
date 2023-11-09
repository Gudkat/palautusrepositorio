import requests
from player import Player


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url).json()

    # Kommentoitu JSON printit pois. Oletan ettei niitä kukaan halua lukea.
    # print("JSON-muotoinen vastaus:")
    # print(response)

    players = []

    for player_dict in response:
        if player_dict['nationality'] == "FIN":
            player = Player(player_dict)
            players.append(player)

    print("Players from FIN:\n")

    for player in sorted(players, key=lambda pl: (pl.points(), pl.goals), reverse=True):
        print(player)


if __name__ == "__main__":
    main()
