import requests
from player import Player

class PlayerReader: 
    def __init__(self,url):
        self.url = url
    
    def get_json(self):
        return requests.get(self.url).json()

    def get_players(self):
        players = {}
        
        for player in self.get_json():
            if(player["nationality"] in players):
                players[player["nationality"]].append(Player(**player))
            else:
                players[player["nationality"]] = [Player(**player)]

        return players
