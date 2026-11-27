from entity import Entity

class Vague():
    def __init__(self, vague_actuelle, monsters, team):
        self.vague_actuelle = vague_actuelle
        self.monsters = monsters
        self.team = team

    @classmethod
    def is_alive(cls,entities):
        return any(entity.is_alive() for entity in entities)

    def pick_enemies(self):
        TODO


    def play_vague(self):
        while Vague.is_alive(self.monsters) and Vague.is_alive(self.team):
            for monster in self.monsters:
                if monster.is_alive():
                    monster.play_turn(self.team)
                    if not Vague.is_alive(self.team):
                        break
            for character in self.team:
                if character.is_alive():
                    choix = Affichage.display(vue_choix_action(character))
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

    def get_difficulty(self):
        # lap = vague_actuelle // end_number le plus grand
        vagues = db['VagueList']
        max_vague = vagues.sort()[-1]
        lap = self.vague_actuelle // max_vague
        return lap


        
    