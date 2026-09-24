################################
# Character blueprint
################################
def main():
    print("=======================================")
    print("        FANTASY CHARACTER CREATOR      ")
    print("=======================================")

    # CHARACTER NAME
    character_name = input("What is your character's name? ")

    # welcome character greeting
    print(f"\nWelcome, {character_name}!")

    # Character Race
    def choose_race():
        character_race = input(
            "\nChoose your race:\n"
            "1. Human\n"
            "2. Elf\n"
            "3. Dragonborn\n"
            "4. Angel\n"
            "5. Hybrid\n"
            "> "
        )

        while character_race not in ["1", "2", "3", "4", "5"]:
            print("Invalid choice. Please try again.")

            character_race = input("> ")


        if character_race == "1":
            character_race = "Human"
        elif character_race == "2":
            character_race = "Elf"
        elif character_race == "3":
            character_race = "Dragonborn"
        elif character_race == "4":
            character_race = "Angel"
        elif character_race == "5":
            character_race = "Hybrid"

        return character_race

    character_race = choose_race()

    # Print character chosen
    print(f"\nYou have chosen {character_race}!")

    # Character class
    def choose_class():
        character_class = input(
            "\nChoose your class:\n"
            "1. Mage\n"
            "2. Warrior\n"
            "3. Archer\n"
            "4. Healer\n"
            "> "
        )
        while character_class not in ["1", "2", "3", "4"]:
            print("Invalid Choice. Please try again.")

            character_class = input("> ")

        if character_class == "1":
            character_class = "Mage"
        elif character_class == "2":
            character_class = "Warrior"
        elif character_class == "3":
            character_class = "Archer"
        elif character_class == "4":
            character_class = "Healer"
        return character_class

    character_class = choose_class()

    # print class chosen
    print(f"\nYou have chosen {character_class}!")

    # Assign Elemental properties
    def choose_element():
        character_element = input(
            "\nChoose your element:\n"
            "1. Water\n"
            "2. Fire\n"
            "3. Light\n"
            "4. Shadow\n"
            "5. Earth\n"
            "6. Wind\n"
            "> "
        )

        while character_element not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid choice. Please try again.")

            character_element = input("> ")

        if character_element == "1":
            character_element = "Water"
        elif character_element == "2":
            character_element = "Fire"
        elif character_element == "3":
            character_element = "Light"
        elif character_element == "4":
            character_element = "Shadow"
        elif character_element == "5":
            character_element = "Earth"
        elif character_element == "6":
            character_element = "Wind"

        return character_element

    character_element = choose_element()

    print(f"\nYou have chosen {character_element}!")

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

    # Save Function
    def save_character(player):
        filename = f"{player.name}.txt"

        with open(filename, "w") as file:
            file.write(f"Name: {player.name}\n")
            file.write(f"Race: {player.race}\n")
            file.write(f"Class: {player.character_class}\n")
            file.write(f"Element: {player.element}\n")
            file.write(f"    Ability: {player.ability}\n")
            file.write(f"    Resistance: {player.resistance}\n")
            file.write(f"    Effect: {player.effect}\n")
            file.write(f"    Weakness: {player.weakness}\n")
            file.write("\n")

            file.write(f"Health: {player.health}\n")
            file.write(f"Strength: {player.strength}\n")
            file.write(f"Magic: {player.magic}\n")
            file.write(f"Defense: {player.defense}\n")
            file.write(f"Dexterity: {player.dexterity}\n")
            file.write(f"Healing: {player.healing}\n")

        print(f"\nCharacter saved to {filename}!")

    player = Character(
        character_name,
        character_race,
        character_class,
        character_element
    )

    # print your actual character

    print("=========================")
    print("      Your Character     ")
    print("=========================")
    print(f"Name: {player.name}")
    print(f"Race: {player.race}")
    print(f"Class: {player.character_class}")
    print(f"Element: {player.element}")
    print(f"    Ability: {player.ability}")
    print(f"    Resistance: {player.resistance}")
    print(f"    Effect: {player.effect}")
    print(f"    Weakness: {player.weakness}")

    print(f"\nHealth: {player.health}")
    print(f"Strength: {player.strength}")
    print(f"Magic: {player.magic}")
    print(f"Defense: {player.defense}")
    print(f"Dexterity: {player.dexterity}")
    print(f"Healing: {player.healing}")
    print("=========================")

    save_choice = input("Do you want to save your character? (yes/no): ").lower()
    while save_choice not in ["yes", "no"]:
        save_choice = input("Please enter 'yes' or 'no': ").lower()

    if save_choice == "yes":
        save_character(player)
    else:
        print("Character not saved.")

if __name__ == "__main__":
    main()