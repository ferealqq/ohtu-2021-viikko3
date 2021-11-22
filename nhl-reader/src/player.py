class Player:
    def __init__(self, name,team, nationality,goals, assists, penalties, games):
        self.name = name
        self.team = team
        self.nationality = nationality
        self.goals = goals
        self.assists = assists
        self.penalties = penalties
        self.games = games
    
    def __str__(self):
        return f"{self.name:20} {self.team:3} {self.goals:2}+{self.assists:2}={self.goals+self.assists:3}"

    def __lt__(self,other):
        return self.__qt__(other) != True
    
    def __qt__(self,other):
        return (self.goals+self.assists)>(other.goals+other.assists)

