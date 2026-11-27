from abstract import ABC, abstractmethod

class Entity(ABC):
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense

    def __str__(self):
        return f"{self.name} (HP: {self.hp}/{self.max_hp}, Attack: {self.attack}, Defense: {self.defense})"

    def is_alive(self):
        return self.hp > 0

    def attaquer(self, entity):
        damage = max(1, self.attack - entity.defense)
        entity.take_damage(damage)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)

    @abstractmethod
    def play_turn(self, entity):
        pass