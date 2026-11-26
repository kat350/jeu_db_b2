from entity import Entity

class Character(Entity):
    
    def __init__(self, name, hp, attack, defense, equipment=None):
        super().__init__(name, hp, attack, defense)
        self.equipment = equipment
        if self.equipment is None:
            self.equipment = []
        else:
            self.equipment = list(equipment)

    @property
    def attack(self):
        self._attack = super().attack
        if self.equipment:
            for item in self.equipment:
                self._attack += item.attack
        return self._attack

    @property
    def defense(self):
        self._defense = super().defense
        if self.equipment:
            for item in self.equipment:
                self._defense += item.defense
        return self._defense
    
    def is_slot_available(self, slot):
        for item in self.equipment:
            if item.slot == slot:
                return False
        return True

    def get_equipment(self, slot=None):
        if slot is None:
            return None
        for item in self.equipment:
            if item.slot == slot:
                return item
        return None

    def equip_item(self, item):
        if not self.is_slot_available(item.slot):
            to_remove = self.get_equipment(item.slot)
            if to_remove:
                self.unequip_item(to_remove)
        else:
            self.equipment.append(item)

    def unequip_item(self, item):
        if item in self.equipment:
            self.equipment.remove(item)
            print(f"{self.name} unequips {item.name}!")
        else:
            print(f"{self.name} does not have {item.name} equipped.")

    def play_turn(self, entity):
        # ouvrir inventaire
        self.attack(entity)

    
    
