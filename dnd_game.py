#Tehee

print('yaya')


class Character():
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def creation(self):
        print(f'Character {self.name} has joined us, being a {self.type}.')

    def shield():
        pass

class Rogue(Character):
    def __init__(self, name, type, agility):
        super().__init__(name, type)
        self.agility = agility

    def L_ATK():
        pass
    def M_ATK():
        pass
    def H_ATK():
        pass
    def special():
        pass


class Mage(Character):
    def __init__(self, name, type, mana):
        super().__init__(name, type)
        self.mana = mana

    def L_ATK():
        pass
    def M_ATK():
        pass
    def H_ATK():
        pass
    def special():
        pass


class Warrior(Character):
    def __init__(self, name, type, strength):
        super().__init__(name, type)
        self.strength = strength
    

    def L_ATK():
        pass
    def M_ATK():
        pass
    def H_ATK():
        pass
    def special():
        pass


class Arena():
    pass