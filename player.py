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
        choix = Affichage.display(vue_selection_equipe(self.team, list_characters))
        return list_characters[choix]
        
    def is_team_alive(self):
        return any(character.is_alive() for character in self.team)

    def check_inventory(self):
        item = Affichage.display(vue_inventaire(self.inventory))
        if item in self.inventory:
            return item

    def use_item(self, item, character):
        if item.consumable:
            item.effect(character)
            self.inventory.remove(item)
        else:
            character.equip_item(item)
            self.inventory.remove(item)


    