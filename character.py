from affichage import Affichage
from entity import Entity
from vague import Vague

class Character(Entity):
    
    def __init__(self, name, hp, attack, defense, equipment=None):
        super().__init__(name, hp, attack, defense)
        self.equipment = equipment
        if self.equipment is None:
            self.equipment = []
        else:
            self.equipment = list(equipment)
        self._attack = super().attack
        self._defense = super().defense


    @property
    def attack(self):
        attaque_totale = self._attack
        if self.equipment:
            for item in self.equipment:
                attaque_totale += item.attack
        return attaque_totale

    @attack.setter
    def attack(self, value):
        self._attack = value

    @property
    def defense(self):
        defense_totale = self._defense
        if self.equipment:
            for item in self.equipment:
                defense_totale += item.defense
        return defense_totale

    @defense.setter
    def defense(self, value):
        self._defense = value
    
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
        existing_item = self.get_equipment(item.slot)
        if existing_item:
            self.unequip_item(existing_item)
        self.equipment.append(item)
        
    def unequip_item(self, item):
        if item in self.equipment:
            self.equipment.remove(item)

    def play_turn(self, monsters):
        index_cible = Affichage.display(vue_choix_cible(monsters))
        damage = self.attaquer(monsters[index_cible])
        return (monsters[index_cible], damage)  # Return the attacked monster and the damage dealt


    
