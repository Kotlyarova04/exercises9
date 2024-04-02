class Game:
    def __init__(self, teams):
        self.teams = {teams['command1']: 0, teams['command2']:0}

    def ball_thrown(self, command, points):
        self.teams[command] += points

    def get_score(self):
        return list(self.teams.values())

    def get_winner(self):
        max_result = max(self.teams.values())
        if list(self.teams.values())[0] == list(self.teams.values())[1]:
            return 'Ничья'
        else:
            for team, res in self.teams.items():
                if res == max_result:
                    return team

game = Game({'command1': 'A', 'command2': 'B'})
game.ball_thrown('A', 2)
game.ball_thrown('B', 4)
game.ball_thrown('A', 2)
print(game.get_score())
print(game.get_winner())