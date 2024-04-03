class Game:
    """
    Class representing a basketball game
    Atributes: team - dict: containing infromation about teams:
               keys: 'command1', 'command2'
               values: points
    Methods: ball_thrown() - adds the number of points
             get_score() - return the current scores
             get_winner()- return the name of the winning team
    """
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


game = Game({'command1': 'EF', 'command2': 'MMF'})
game.ball_thrown('EF', 3)
game.ball_thrown('MMF', 4)
game.ball_thrown('EF', 2)
print(game.get_score())
print(game.get_winner())
