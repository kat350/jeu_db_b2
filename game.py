from pymongo import MongoClient

from player import Player
from vague import Vague

class Game:
    client = MongoClient(host='localhost', port=27017)
    db = client.game_db

    def __init__(self):
        self.player = Player()
        self.vague = Vague()

    def exist_in_db(self, player_name):
        return self.db['players'].find_one({"player.name": player_name})

    def save_game(self):

        save = {
            "player": self.player.__dict__(),
            "vague": self.vague.__dict__()
        }
        if not self.exist_in_db(self.player.name):
            self.db['players'].insert_one(save)

        else:
            self.db['players'].update_one(
                {"name": self.player.name},
                {"$set": save}
            )


    def load_game(self):
        save = self.db['saves'].find_one({"player.name": self.player.name})
        if save:
            self.player = Player(**save['player'])
            self.vague = Vague(**save['vague'])
            Vague.play_vague(self.vague)
        else:
            print("No saved game found for this player.")

    def launch_game(self):
        index_choix = Affichage.display(vue_ecran_titre())

        # Nouvelle partie
        if index_choix == 0:
            self.player.name = input("Entrez votre nom : ")
            self.player.create_team()
            while self.player.is_team_alive():
                self.vague.play_vague()
                self.save_game()
            

        
    