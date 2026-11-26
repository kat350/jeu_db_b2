class Item:
    def __init__(self, name, description, drop_rate, item_type, rarity, effect, consumable):
        self.name = name
        self.description = description
        self.drop_rate = drop_rate
        self.item_type = item_type
        self.rarity = rarity
        self.effect = effect
        self.consumable = consumable

    def __dict__(self):
        return {
            "name": self.name,
            "description": self.description,
            "drop_rate": self.drop_rate,
            "item_type": self.item_type,
            "rarity": self.rarity,
            "effect": self.effect,
            "consumable": self.consumable
        }