#Tehee

print('yaya')


class Character():
    def __init__(self, name, type):
        self.name = name
        self.type = type

        self.health = 100
        self.ult = 0
        # health and other attributes such as mana and agility are predetermined, 
        # cannot ask user for imput bc they would obvi pick an overpowerd stats

    def creation(self):
        print(f'Character {self.name} has joined us, being a {self.type}.')

    def shield(self):
        print(f'{self.name} used shields')

class Rogue(Character):
    def __init__(self, name, type, agility):
        super().__init__(name, type)
        self.agility = agility

    def add(self): # to test if the ult system works
        self.ult += 10
        print(f'ult points now are {self.ult}')

    def L_ATK(self):
        print(f'{self.name} used a light attack')
    def M_ATK():
        pass
    def H_ATK():
        pass
    def special(self):
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
    def __init__(self, name, type,  strength):
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
    def __init__(self):
        self.yaya = 0
    def choice(self, person):
        yaya = int(input('0. for shield, 1. for L, 2. for M, 3. for H and 4. for ult'))
        self.yaya = yaya
        if yaya == 0:
            person.shield()
        if yaya == 1:
            person.L_ATK()
        if yaya == 2:
            pass
        if yaya == 3:
            pass
        if yaya == 4:
            pass



new = Character('Michelle', 'Spectator')
silly = Rogue('two dolla', 'rogue', 20)
new.creation()
silly.add()
silly.add()

place = Arena()

place.choice(silly)
place.choice(new)