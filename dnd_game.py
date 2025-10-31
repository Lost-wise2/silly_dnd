#Tehee

print('yaya')


class Character():
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def creation(self):
        print(f'Character {self.name} has joined us, being a {self.type}.')

class Rogue(Character):
    def __init__(self, name, type, agility):
        super().__init__(name, type)
        self.agility = agility


class Mage(Character):
    def __init__(self, name, type, mana):
        super().__init__(name, type)
        self.mana = mana


class Warrior(Character):
    def __init__(self, name, type, strength):
        super().__init__(name, type)
        self.strength = strength