class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.team = dict['team']
        self.nationality = dict['nationality']

    def points(self):
        return self.goals + self.assists

    def __str__(self):
        return f"{self.name:25} {self.team:3} {self.goals:2} + {self.assists:2} = {self.points()}"
