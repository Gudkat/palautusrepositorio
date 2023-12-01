class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def won_point(self):
        self.score += 1
        return self.score


class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)

    def won_point(self, player_name):
        if player_name == self.player1.name:
            player = self.player1
        else:
            player = self.player2
        return player.won_point()

    def check_tie(self):
        if self.player1.score == self.player2.score:
            return True

    def translate_score(self, score):
        match score:
            case 0:
                return "Love"
            case 1:
                return "Fifteen"
            case 2:
                return "Thirty"
            case 3:
                return "Forty"

    def check_advantage(self):
        if self.player1.score == self.player2.score + 1:
            return "Advantage " + self.player1.name
        elif self.player1.score + 1 == self.player2.score:
            return "Advantage " + self.player2.name
        return None

    def check_win(self):
        if self.player1.score > 3 and self.player1.score - self.player2.score >= 2:
            return "Win for " + self.player1.name
        elif self.player2.score > 3 and self.player2.score - self.player1.score >= 2:
            return "Win for " + self.player2.name
        return None

    def get_score(self):
        if self.player1.score >= 3 and self.player2.score >= 3:
            if advantage := self.check_advantage():
                return advantage
            if self.player1.score == self.player2.score:
                return "Deuce"
        if winner := self.check_win():
            return winner
        if self.check_tie():
            return self.translate_score(self.player1.score) + "-All"
        return self.translate_score(self.player1.score) + "-" + self.translate_score(self.player2.score)
