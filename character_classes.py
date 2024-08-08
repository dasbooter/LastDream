from races import Race

class CharacterClass(Race):
    def __init__(self, name, strength, dexterity, constitution, intelligence, wisdom, charisma, race_type, character_class):
        super().__init__(name, strength, dexterity, constitution, intelligence, wisdom, charisma, race_type)
        self.character_class = character_class
        self.hit_die = self.get_hit_die()
        self.calculate_health()

    def apply_class_modifiers(self):
        if self.character_class == "Fighter":
            self.attributes['strength'] += 2
            self.health += 10
        elif self.character_class == "Wizard":
            self.attributes['intelligence'] += 2
            self.health += 4
        # Add more class modifiers here

    def calculate_health(self):
        constitution_modifier = (self.attributes['constitution'] - 10) // 2
        self.health = self.hit_die + constitution_modifier

    def get_hit_die(self):
        if self.character_class == "Fighter":
            return 10
        elif self.character_class == "Wizard":
            return 6
        elif self.character_class == "Cleric":
            return 8
        # Add more classes and their hit dice here
        else:
            return 6  # Default hit die for unspecified classes