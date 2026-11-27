from entity import Entity
import random
from game import db
from vue import VueTourJoueur
from affichage import Affichage

class Vague():
    def __init__(self, vague_actuelle, monsters, team):
        self.vague_actuelle = vague_actuelle
        self.team = team
        self.monsters = monsters

    @classmethod
    def is_alive(cls,entities):
        return any(entity.is_alive() for entity in entities)

    def pick_enemies(self,db):
        max_vague = self.get_max_vague(db)

        vague_bornee = self.vague_actuelle % max_vague
        # chercher labonne vague
        find_vague = db['vagues'].find_one({"start_number": {"$lte": vague_bornee}, "end_number": {"$gte": vague_bornee}})
        # recuperer les monstres de la vague
        self.monsters = find_vague['monsters']
        # choisi une equipe de 3 monstres aleatoirement² 
        enemies = random.sample(self.monsters, min(len(self.monsters), 3))
        return enemies


    def play_vague(self):

        # boucle de jeu
        while Vague.is_alive(self.monsters) and Vague.is_alive(self.team):
            for monster in self.monsters:
                if monster.is_alive():
                    monster.play_turn(self.team)
                    if not Vague.is_alive(self.team):
                        break
            for character in self.team:
                if character.is_alive():
                    choix = Affichage.display(VueTourJoueur(self.team, character, self.monsters))
                    if choix == 0:  # Attack
                        character.play_turn(self.monsters)
                    elif choix == 1:  # Use Item
                        character.use_item()
                    else:  # Flee
                        return_code = -1
                        break
        if not Vague.is_alive(self.team):
            return_code = 0  # Team defeated
        elif not Vague.is_alive(self.monsters):
            return_code = 1  # Monsters defeated
            self.vague_actuelle += 1
        return return_code

    def get_difficulty(self,db):
        # lap = vague_actuelle // end_number le plus grand
        max_vague = self.get_max_vague(db)
        lap = self.vague_actuelle // max_vague
        return lap

    def get_max_vague(self,db):
        find_max_vague = db['vagues'].find_one(sort=[("end_number", -1)])
        max_vague = find_max_vague['end_number']
        return max_vague
        
    