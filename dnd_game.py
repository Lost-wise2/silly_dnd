#Tehee
import random

print(random.randint(1,10))

print('yaya')







class Character():
    def __init__(self, name):
        self.name = name

        self.health = 100
        self.ult = 0
        self.alive = True
        self.shield = False
        
        

        # health and other attributes such as mana and agility are predetermined, 
        # cannot ask user for imput bc they would obvi pick an overpowerd stats

    #def creation(self):
        #print(f'Character {self.name} has joined us, being a {self.type}.')

    def shield(self):
        self.shield = True
        print(f'{self.name} used shields')

    def skip_turn(self):
        print(f'{self.name} has skipped their turn')

    def check_stats(self):
        print(f'{self.name}, has {self.health} hp left, {self.ult} ult points')

    def is_alive(self):
        if self.health <= 0:
            self.health = 0
            self.alive = False


    def got_hit(self, damage):
        
        self.health -= damage

        print(f"{self.name} took {damage} damange, their health is now {self.health}")
        self.is_alive()


    






        

    



class Rogue(Character):
    def __init__(self, name, stamina):
        super().__init__(name)
        self.stamina = stamina
        self.health += 10

    def add(self): # to test if the ult system works
        self.ult += 10
        print(f'ult points now are {self.ult}')

    def L_ATK(self, victim):
        damage = 50
        print(f'{self.name} used a light attack')
        print(f"{self.name} attacks {victim.name}.")

        victim.got_hit(damage)
        if victim.alive == False:
            print(f'{self.name} won!')
            place.character_death()

    def M_ATK():
        pass
    def H_ATK():
        pass
    def special(self):
        pass


    def check_stats(self):
        super().check_stats()
        print(f'And {self.stamina} stamina points left.')




class Mage(Character):
    def __init__(self, name, mana):
        super().__init__(name)
        self.mana = mana
        self.health -= 20

    def L_ATK():
        pass
    def M_ATK(self):
        print(f'{self.name} used a medium attack')
    def H_ATK():
        pass
    def special():
        pass

    def check_stats(self):
        super().check_stats()
        print(f'And {self.mana} mana points left.')




class Warrior(Character):
    def __init__(self, name,  strength):
        super().__init__(name)
        self.strength = strength
        self.health += 30
    

    def L_ATK():
        pass
    def M_ATK():
        pass
    def H_ATK():
        pass
    def special():
        pass
    

    def check_stats(self):
        super().check_stats()
        print(f'And {self.strength} strength points left.')


####################################









class Arena():
    def __init__(self):
        self.yaya = 0
        self.dead_character = False
        #self.running = True


    #def how_many(self):
    #    global player_count
    #    how_player_count = int(input('how many?'))
    #    x = 0
    #    player_count = []
    #    while x < how_player_count:
    #        x += 1
    #        player_count.append(x)



    def character_choice(self, player):
        global choice_name
        global type
        self.player = player
        print(f'{self.player} select your style:')
        choice_type = int(input('1. for rogue, 2. for mage and 3. for warrior'))
        choice_name = input('Insert name for character:')
        if choice_type == 1:
            type = Rogue
        elif choice_type == 2:
            type = Mage
        elif choice_type == 3:
            type = Warrior
        else:
            print('oj')



    def choice(self, person, victim):
        yaya = int(input('0. for shield, 1. for L, 2. for M, 3. for H and 4. for ult, 9. to check stats'))
        self.yaya = yaya
        if yaya == 0:
            person.shield()
        elif yaya == 1:
            person.L_ATK(victim)
        elif yaya == 2:
            person.M_ATK(victim)
        elif yaya == 3:
            pass
        elif yaya == 4:
            pass
        elif yaya == 9:
            person.check_stats()
        elif yaya == 10:
            person.skip_turn()
        else:
            print('uh oh')
    




    def character_death(self):
        self.running = False
        self.dead_character = True
        print('done')





    def game(self):
        self.running = True
        round = 1
        while self.running == True:
            print("Round", round, "has begun.")
            
            place.choice(player_1, player_2)
            #player_2.is_alive()
            #if player_2.alive == False:
                #print('Round ended, Player 2 won!')
            #    running = False
            #else:
            #    pass
            
            if self.dead_character == True:
                break
            
            place.choice(player_2, player_1)
            #player_1.is_alive()
            #if player_1.alive == False:
                #print('Round ended, Player 1 won!')
            #    running = False
            #else:
            #    pass
            print("Round", round, "has ended.")
            round += 1

    
        
        
            
            
        







class diffArena(Arena):
    def __init__(self):
        super().__init__()

    def arenas(self, diff):
        if diff == 1:
            pass


################################33






new = Character('Michelle')
silly = Rogue('two dolla', 20)
#new.creation()
silly.add()
silly.add()





########################################################




beginning = True


print('Welcome and hello! This game is a turn based dnd inspired game!')
start = int(input('To start the game press 1, press 2 for instructions again or 3 to quit.'))
while beginning == True:
    if start == 1:
        pass
        beginning = False
    elif start == 2:
        pass
    elif start == 3:
        pass
        quit
    else:
        pass








place = Arena()

#place.choice(silly)
#place.choice(new)

#place.how_many()

#for player in player_count:
#    place.character_choice(player)

player_1 = 'player_1'
player_2 = 'player_2'

place.character_choice(player_1)
player_1 = type(choice_name, 20)
#print(player_1)
#print(silly)

place.character_choice(player_2)
player_2 = type(choice_name, 10)
#print(player_2)







#place.choice(player_1)
#place.choice(player_2)



place.game()

#done = int(input('done? 1. for done, 2. for no'))

#if done == 1:
#    del player_1
#else:
#    print('oj')



# all thats left now is to special arenas, and finsih all the types of attacks and ults