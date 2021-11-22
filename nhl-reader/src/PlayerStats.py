class PlayerStats:
    def __init__(self,reader):
        self.reader = reader
        self.players = self.reader.get_players()
    
    def top_scorers_by_nationality(self, nationality):
        if nationality in self.players:
            result = self.players[nationality]
            for i in range(len(result)):
                for j in range(len(result)-i-1,0,-1): 
                    n = len(result)-1-i-j
                    s = n+1
                    if(result[s] > result[n]):
                        t = result[n]
                        result[n] = result[s]
                        result[s] = t
            return result
        else:
            print("Nationality does not exist among the player group")
            return []