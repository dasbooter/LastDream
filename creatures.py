class Creature:
    def __init__(self, name, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.name = name
        self.attributes = {
            'strength': strength,
            'dexterity': dexterity,
            'constitution': constitution,
            'intelligence': intelligence,
            'wisdom': wisdom,
            'charisma': charisma
        }
        self.health = 0