from affichage import Affichage
from vue import VueSelectionEquipe


class Player():
    def __init__(self, name, score, team, inventory):
        self.name = name
        self.score = score
        self.team = team if team is not None else []
        self.inventory = inventory if inventory is not None else []

    def create_team(self, list_characters):
        list_characters = list_characters.copy()
        while len(self.team) < 3:
            character = self.pick_character(list_characters)
            self.team.append(character)
            list_characters.remove(character)
        return self.team

    def pick_character(self, list_characters):
        choix = Affichage.display(VueSelectionEquipe(self.team, list_characters))
        return list_characters[choix]
        
    def is_team_alive(self):
        return any(character.is_alive() for character in self.team)

    def check_inventory(self):
        while True:
            item = self.pick_item()
            if item is None:
                break
            character = self.pick_character(self.team)
            self.use_item(item, character)

    def use_item(self, item, character):
        if type(item) == Consumable:
            item.effect(character)
            self.inventory.remove(item)
        else:
            character.equip_item(item)
            self.inventory.remove(item)


    