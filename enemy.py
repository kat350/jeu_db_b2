from entity import Entity
import random

class Enemy(Entity):
    def __init__(self, name, hp, attack, defense, dropable_items=None):
        super().__init__(name, hp, attack, defense)
        self.dropable_items = dropable_items if dropable_items is not None else []

    def drop_items(self, dropable_items):
        dropped_items = []
        for item in dropable_items:
            if random.random() < item.drop_rate:
                dropped_items.append(item)
        return dropped_items
    
    def play_turn(self, entity):
        self.attack(entity)