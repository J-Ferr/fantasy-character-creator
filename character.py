# Creating the actual character
class Character:
    def __init__(self, character_name, character_race, character_class, character_element):
        self.name = character_name
        self.race = character_race
        self.character_class = character_class
        self.element = character_element
        self.health = 100
        self.strength = 50
        self.magic = 50
        self.defense = 50
        self.dexterity = 50
        self.healing = 20
        self.ability = ""
        self.resistance = ""
        self.effect = ""
        self.weakness = ""
            
        ## character class stats
        if self.character_class == "Mage":
            self.strength = 40
            self.magic = 80
            self.defense = 40
            self.dexterity = 50
            self.healing = 30
        elif self.character_class == "Warrior":
            self.strength = 80
            self.magic = 30
            self.defense = 80
            self.dexterity = 40
            self.healing = 20
        elif self.character_class == "Archer":
            self.strength = 60
            self.magic = 40
            self.defense = 60
            self.dexterity = 85
            self.healing = 20
        elif self.character_class == "Healer":
            self.strength = 40
            self.magic = 80
            self.defense = 30
            self.dexterity = 45
            self.healing = 90
            
        # character race bonus 
        if self.race == "Human":
            self.health += 10
        elif self.race == "Elf":
            self.dexterity += 10
        elif self.race == "Dragonborn":
            self.strength += 10
        elif self.race == "Angel":
            self.healing += 10
        elif self.race == "Hybrid":
            self.magic += 5
            self.strength += 5
            self.defense += 5
            self.dexterity += 5
            self.healing += 5
            self.health += 5

        # character element ability
        if self.element == "Water":
            self.ability = "Tidal Strike"
            self.resistance = "Fire"
            self.effect = "Soaked"
            self.weakness = "Earth"
        elif self.element == "Fire":
            self.ability = "Flame Burst"
            self.resistance = "Light"
            self.effect = "Burn"
            self.weakness = "Water"
        elif self.element == "Light":
            self.ability = "Solar Beam"
            self.resistance = "Water"
            self.effect = "Blessed"
            self.weakness = "Earth"
        elif self.element == "Shadow":
            self.ability = "Shadow Jump"
            self.resistance = "Water"
            self.effect = "Blinded"
            self.weakness = "Light"
        elif self.element == "Earth":
            self.ability = "Stone Barrier"
            self.resistance = "Wind"
            self.effect = "Staggered"
            self.weakness = "Fire"
        elif self.element == "Wind":
            self.ability = "Wind Cutter"
            self.resistance = "Earth"
            self.effect = "Speed Boost"
            self.weakness = "Shadow"