# Fantasy Character Creator

## About
Fantasy Character Creator is a command-line Python application that allows users to create a custom fantasy character by choosing a name, race, class, and elemental affinity.

Each choice affects the final character. Classes determine base stats, races provide stat bonuses, and elements provide unique abilities, effects, resistance and weaknesses.

The fnished character can also be saved to a text file.

## Features

- Create a custom character name
- Choose from the five races:
    - Human
    - Elf
    - Dragonborn
    - Angel
    - Hybrid
- Choose from four classes:
    - Mage
    - Warrior
    - Archer
    - Healer
- Choose from six elements: 
    - Water
    - Fire
    - Light
    - Shadow
    - Earth
    - Wind
- Class-based character stats
- Race-specific stat bonuses
- Elemental abilities, effects, resistance, and weaknesses
- Input validation for character selections
- Option to save the complete character to a `.txt` file

## Python Concepts Practiced

This project was created to practice and combine several core Python concepts: 

- Variable and user input
- Conditional statements (`if`, `elif`, `else`)
- `While` loops
- Lists and memebership operators
- Functions and parameters
- Return values
- Classes and objects
- The `__init__()` method
- Object attributes
- String formatting with f-strings
- File handling
- Input validation

## How to Run

1. Make sure Python is installed.
2. Clone or download this repository.
3. Open the project folder in a terminal
4. Run:
    Python main.py

5. Follow the prompts to create your character.

## Example

A generated characater may look like:

Name: Solien
Race: Hybrid
Class: Mage
Element: Water
    Ability: Tidal Strike
    Resistance: Fire
    Effect: Soaked
    Weakness: Earth

Health: 105
Strength: 45
Magic: 85
Defense: 45
Dexterity: 55
Healing: 35

## Future Improvements

Possible future additons inlcude:

- Character combat
- Enemies
- Leveling and eperience
- Additonal races, classes and elements
- Loading previously saved character