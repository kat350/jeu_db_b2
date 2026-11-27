from pymongo import MongoClient

from affichage import Affichage
from player import Player
from vague import Vague

class Game:
    client = MongoClient(host='localhost', port=27017)
    db = client.game_db

    def __init__(self):
        self.player = Player()
        self.vague = Vague()

    def exist_in_db(self, player_name):
        return self.db['players'].find_one({"player.name": player_name}) is not None

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
        # Load player data
        save = self.db['saves'].find_one({"player.name": self.player.name})
        
        # regarder mongo et aller chercher chaque data pour reconstruire l'environment de jeu

    def launch_game(self):
        index_choix = Affichage.display(VueEcranTitre())

        # Nouvelle partie
        if index_choix == 0:
            self.player.name = input("Entrez votre nom : ")
            self.player.create_team()
            while self.player.is_team_alive():
                self.vague.pick_enemies(self, self.db)
                return_code = self.vague.play_vague()
                if return_code == -1:
                    self.save_game()
                    break

            self.db['scores'].insert_one({"player.name": self.player.name, "score": self.player.score})
            Affichage.display(VueGameOver(self.player.score))

        # Load partie
        elif index_choix == 1:
            index_sauvegarde = Affichage.display(VueChargerSauvegarde())
            find_saves = self.db['saves'].find({"player.name": self.player.name})
            self.load_game(find_saves[index_sauvegarde])
            while self.player.is_team_alive():
                self.vague.pick_enemies()
                return_code = self.vague.play_vague()
                if return_code == -1:
                    self.save_game()
                    break
            self.db['saves'].delete_one({"player.name": self.player.name})
            self.db['scores'].insert_one({"player.name": self.player.name, "score": self.player.score})
            Affichage.display(VueGameOver(self.player.score))

        elif index_choix == 2:
            scores = self.db['scores'].find().sort("score", -1).limit(3)
            Affichage.display(VueLeaderboard(scores))

        elif index_choix == 3:
            Affichage.display(VueQuitter())
        
    