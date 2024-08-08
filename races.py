from creatures import Creature

class Race(Creature):
    def __init__(self, name, strength, dexterity, constitution, intelligence, wisdom, charisma, race_type):
        super().__init__(name, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.race_type = race_type
        self.apply_race_modifiers()

    def apply_race_modifiers(self):
        if self.race_type == "Human":
            for key in self.attributes:
                self.attributes[key] += 1
        elif self.race_type == "Dragonborn":
            self.attributes["strength"] += 2
            self.attributes["charisma"] += 1
        elif self.race_type == "Dwarf":
            self.attributes['constitution'] += 2
            #self.feats["Darkvision"]
        elif self.race_type == "Elf":
            self.attributes['dexterity'] += 2
        elif self.race_type == "Gnome":
            self.attributes["intelligence"] += 2
        elif self.race_type == "Half-Elf":
            self.attributes["charisma"] += 2
            #self.attributes +1 to Two others
        elif self.race_type == "Halfling":
            self.attributes["dexterity"] += 2
        elif self.race_type == "Half-Orc":
            self.attributes["strength"] += 2
            self.attributes["constitution"] += 1
        elif self.race_type == "Tiefling":
            self.attributes["charisma"] += 2
            self.attributes["intelligence"] += 1
        else:
            raise Exception("Not a valid Race")
