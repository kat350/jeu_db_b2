class Player():
    def __init__(self, name, score, team, inventory):
        self.name = name
        self.score = score
        self.team = team if team is not None else []
        self.inventory = inventory if inventory is not None else []

    def create_team(self, characters):
        while len(self.team) < 3:
            self.team.append(characters.pop())
        return self.team

    def pick_character(self, character):
        if character not in self.team:
            self.team.append(character)

    def is_team_alive(self):
        return any(character.is_alive() for character in self.team)

    def check_inventory(self):
        for _ in self.inventory:
            #afficher l'item_name et ses stats
            pass

    