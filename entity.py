class Entity:
    def __init__(self, name, hp, max_hp, attack, defense):
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.attack = attack
        self.defense = defense

    def is_alive(self):
        return self.hp > 0
    
    def attack(self, entity):
        damage = max(0, self.attack - entity.defense)
        entity.hp -= damage
        print(f"{self.name} attacks {entity.name} for {damage} damage!")

    def take_damage(self, damage):
        self.hp -= damage
        print(f"{self.name} takes {damage} damage!")

    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)
        print(f"{self.name} heals for {amount} HP!")

    def play_turn(self, entity):
        if self.is_alive():
            self.attack(entity)
        else:
            print(f"{self.name} is defeated and cannot attack.")