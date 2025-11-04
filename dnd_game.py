#Tehee
import random

print(random.randint(1,10))

print('yaya')




rogue_buff = False
mage_buff = False
warrior_buff = False


# Main class for the characters
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

    def shields(self):
        self.shield = True
        print(f'{self.name} used shields \n')

    def skip_turn(self):
        print(f'{self.name} has skipped their turn \n')

    def check_stats(self):
        if self.shield == True:
            print(f'{self.name}, has {self.health} hp left, {self.ult} ult points.')
            print('Shields are active! \n')
        else:
            print(f'{self.name}, has {self.health} hp left, {self.ult} ult points \n')

    def is_alive(self):
        if self.health <= 0:
            self.health = 0
            self.alive = False


    def got_hit(self, damage):
        
        if self.shield == True:
            damage = int(damage*0.75)
            self.health -= damage
            self.shield = False
            print(f"{self.name} has sheilds active! And only took {damage} damange instead, their health is now {self.health} \n")
        else:
            self.health -= damage
            print(f"{self.name} took {damage} damange, their health is now {self.health} \n")
        self.is_alive()


    






        

    


# three subclasses for each type of character
class Rogue(Character):
    def __init__(self, name):
        super().__init__(name)
        self.stamina = 3
        self.health += 10
        self.enough = 5

        self.specific = 'stamina'


        self.needed = {
            'L' : 10,
            'M' : 0,
            'H' : 0,
            'S' : 0,

        }
        self.got_it = False
        #self.neededL = 0
        #self.neededM = 0
        #self.neededH = 0
        #self.neededS = 0


        

    def add(self): # to test if the ult system works
        self.ult += 10
        print(f'ult points now are {self.ult}')

    def check(self, what):
        if self.stamina >= self.needed[what]:
            self.got_it = True
        else:
            self.got_it = False

    def L_ATK(self, victim):
        damage = 3
        if rogue_buff == True:
            int(damage *1.5)
        else:
            pass

        self.ult += 4
        
        #print(f'{self.name} used a light attack')
        print(f"{self.name} attacks {victim.name} with a light attack. \n")
        print(f'{self.stamina} stamina points left!')

        victim.got_hit(damage)
        if victim.alive == False:
            print(f'{self.name} won!')
            place.character_death()

    def M_ATK(self, victim):
        damage = 5
        if rogue_buff == True:
            int(damage *1.5)
        else:
            pass

        self.stamina -= damage
        self.ult += 1

        print(f"{self.name} attacks {victim.name} with a medium attack. \n")
        print(f'{self.stamina} stamina points left!')

        victim.got_hit(damage)
        if victim.alive == False:
            print(f'{self.name} won!')
            place.character_death()
    
    def H_ATK(self, victim):
        damage = 10
        if rogue_buff == True:
            int(damage *1.5)
        else:
            pass

        self.stamina -= damage
        self.ult += 1
        
        print(f"{self.name} attacks {victim.name} with a heavy attack. \n")
        print(f'{self.stamina} stamina points left!')

        victim.got_hit(damage)
        if victim.alive == False:
            print(f'{self.name} won!')
            place.character_death()
    
    
    def special(self, victim):
        damage = 20
        if rogue_buff == True:
            int(damage *1.5)
        else:
            pass

        self.stamina -= damage
        self.ult -= self.enough
        
        print(f"{self.name} attacks {victim.name} with a light attack. \n")
        print(f'{self.stamina} stamina points left! and {self.ult} ult points left!')
        

        victim.got_hit(damage)
        if victim.alive == False:
            print(f'{self.name} won!')
            place.character_death()


    def check_stats(self):
        super().check_stats()
        print(f'And {self.stamina} stamina points left. \n')




class Mage(Character):
    def __init__(self, name):
        super().__init__(name)
        self.mana = 2
        self.health -= 20
        self.enough = 20

        self.specific = 'mana'

        self.needed = {
            'L' : 3,
            'M' : 0,
            'H' : 0,
            'S' : 0,

        }
        self.got_it = False

    def check(self, what):
        if self.mana >= self.needed[what]:
            self.got_it = True
        else:
            self.got_it = False


    def L_ATK(self, victim):
        damage = 5
        if mage_buff == True:
            int(damage *1.5)
        else:
            pass

        self.mana -= damage
        self.ult += 1
        
        print(f"{self.name} attacks {victim.name} with a medium attack. \n")
        print(f'{self.mana} mana points left!')

        victim.got_hit(damage)
        if victim.alive == False:
            print(f'{self.name} won!')
            place.character_death()
    
    
    def M_ATK(self, victim):
        damage = 8
        if mage_buff == True:
            int(damage *1.5)
        else:
            pass

        self.mana -= damage
        self.ult += 1
        
        print(f"{self.name} attacks {victim.name} with a medium attack. \n")
        print(f'{self.mana} mana points left!')

        victim.got_hit(damage)
        if victim.alive == False:
            print(f'{self.name} won!')
            place.character_death()
    
    
    def H_ATK(self, victim):
        damage = 12
        if mage_buff == True:
            int(damage *1.5)
        else:
            pass

        self.mana -= damage
        self.ult += 1
        
        print(f"{self.name} attacks {victim.name} with a medium attack. \n")
        print(f'{self.mana} mana points left!')

        victim.got_hit(damage)
        if victim.alive == False:
            print(f'{self.name} won!')
            place.character_death()
   
   
   
    def special(self, victim):
        damage = 5
        if mage_buff == True:
            int(damage *1.5)
        else:
            pass

        self.mana -= damage
        self.ult -= self.enough
        
        print(f"{self.name} attacks {victim.name} with a medium attack. \n")
        print(f'{self.mana} mana points left! and {self.ult} ult points left!')
        

        victim.got_hit(damage)
        if victim.alive == False:
            print(f'{self.name} won!')
            place.character_death()



    def check_stats(self):
        super().check_stats()
        print(f'And {self.mana} mana points left.')




class Warrior(Character):
    def __init__(self, name):
        super().__init__(name)
        self.strength = 100
        self.health += 30
        self.enough = 20

        self.specific = 'strength'

        self.needed = {
            'L' : 0,
            'M' : 0,
            'H' : 0,
            'S' : 0,

        }
        self.got_it = False
    

    def check(self, what):
        if self.strength >= self.needed[what]:
            self.got_it = True
        else:
            self.got_it = False

    def L_ATK(self, victim):
        damage = 5
        if warrior_buff == True:
            int(damage *1.5)
        else:
            pass

        self.strength -= damage
        self.ult += 1
        
        print(f"{self.name} attacks {victim.name} with a medium attack. \n")
        print(f'{self.strength} strength points left!')

        victim.got_hit(damage)
        if victim.alive == False:
            print(f'{self.name} won!')
            place.character_death()
    
    def M_ATK(self, victim):
        damage = 5
        if warrior_buff == True:
            int(damage *1.5)
        else:
            pass

        self.strength -= damage
        self.ult += 1
        
        print(f"{self.name} attacks {victim.name} with a medium attack. \n")
        print(f'{self.strength} strength points left!')

        victim.got_hit(damage)
        if victim.alive == False:
            print(f'{self.name} won!')
            place.character_death()
    
    def H_ATK(self, victim):
        damage = 5
        if warrior_buff == True:
            int(damage *1.5)
        else:
            pass

        self.strength -= damage
        self.ult += 1
        
        print(f"{self.name} attacks {victim.name} with a medium attack. \n")
        print(f'{self.strength} strength points left!')

        victim.got_hit(damage)
        if victim.alive == False:
            print(f'{self.name} won!')
            place.character_death()
    
    
    def special(self, victim):
        damage = 5
        if warrior_buff == True:
            int(damage *1.5)
        else:
            pass
        
        self.strength -= damage
        self.ult -= self.enough
        
        print(f"{self.name} attacks {victim.name} with a medium attack. \n")
        print(f'{self.strength} strength points left! and {self.ult} ult points left!')
        

        victim.got_hit(damage)
        if victim.alive == False:
            print(f'{self.name} won!')
            place.character_death()
    


    def check_stats(self):
        super().check_stats()
        print(f'And {self.strength} strength points left.')


####################################








# Class for the arena itself where the game also takes place in
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
        choice_type = int(input('1. for rogue, 2. for mage and 3. for warrior \n'))
        choice_name = input('Insert name for character: \n')
        if choice_type == 1:
            type = Rogue
        elif choice_type == 2:
            type = Mage
        elif choice_type == 3:
            type = Warrior
        else:
            print('oj')



    def choice(self, person, victim):
        #self.yaya = yaya
        making_choice = True
        while making_choice == True:
            yaya = int(input('0. for shield, 1. for L, 2. for M, 3. for H and 4. for ult, 9. to check stats \n'))
            if yaya == 0:
                person.shields()
                making_choice = False
            elif yaya == 1:
                person.check('L')
                if person.got_it == True:
                    person.L_ATK(victim)
                    making_choice = False
                else:
                    print(f'Sorry but {person.name} does not have enoygh {person.specific} points')

            elif yaya == 2:
                person.check('M')
                if person.got_it == True:
                    person.M_ATK(victim)
                    making_choice = False
                else:
                    print(f'Sorry but {person.name} does not have enoygh {person.specific} points')

            elif yaya == 3:
                person.check('H')
                if person.got_it == True:
                    person.H_ATK(victim)
                    making_choice = False
                else:
                    print(f'Sorry but {person.name} does not have enoygh {person.specific} points')
                    
            elif yaya == 4:
                if person.ult >= person.enough:
                    person.check('S')
                    if person.got_it == True:
                        person.special(victim)
                        making_choice = False
                    else:
                        print(f'Sorry but {person.name} does not have enoygh {person.specific} points')    
                else:
                    print(f'Sorry but {person.name} does not have enough ult points')

            elif yaya == 9:
                person.check_stats()
            elif yaya == 10:
                person.skip_turn()
                making_choice = False
            else:
                print('uh oh')
    

    def arena_type(self):
        print('there are three and bla bla ba')
        what_arena = int(input('1. for _, 2. for __, 3. for ___.'))
        global rogue_buff
        global mage_buff
        global warrior_buff
        if what_arena == 1:
            rogue_buff = True
            mage_buff = True
            print('rog and mag buffed!')
        elif what_arena == 2:
            mage_buff = True
            warrior_buff = True
            print('mag and war buffed!')
        elif what_arena == 3:
            rogue_buff = True
            warrior_buff = True
            print('rog and war buffed!')
        else:
            print('uhoh')
        


    def character_death(self):
        self.running = False
        self.dead_character = True
        #print('done')





    def game(self):
        self.running = True
        round = 1
        while self.running == True:
            print("Round", round, "has begun. \n")
            
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
            print("Round", round, "has ended. \n")
            round += 1

    
        
        
            
            
        






# might remove later ngl
class diffArena(Arena):
    def __init__(self):
        super().__init__()

    def arenas(self, diff):
        if diff == 1:
            pass


################################33





#old code <3

#new = Character('Michelle')
#silly = Rogue('two dolla', 20)
#new.creation()
#silly.add()
#silly.add()





########################################################

instructions = "  Each player gets to pick a fighter and an arena to fight in. \n  On each turn you have three attack options, and a special attack once you have enough ult points. \n  You could even use shields or skip your turn entirely! \n  But beware, you get one move only, so think wisely!\n"

# Choice for the game to start, introduces the game etc
beginning = True


print('Welcome and hello! This game is a turn based dnd inspired game! \nAnd the instructions are:')
print(instructions)


while beginning == True:
    start = int(input('To start the game press 1, press 2 for instructions again or 3 to quit.'))
    if start == 1:
        pass
        beginning = False
    elif start == 2:
        print(instructions)
    elif start == 3:
        print("Sad to see you go, but hope you'd be up for a game coon :)")
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
player_1 = type(choice_name)
#print(player_1)
#print(silly)

place.character_choice(player_2)
player_2 = type(choice_name)
#print(player_2)



place.arena_type()

#print(rogue_buff)
#print(mage_buff)
#print(warrior_buff)


#place.choice(player_1)
#place.choice(player_2)



place.game()

#done = int(input('done? 1. for done, 2. for no'))

#if done == 1:
#    del player_1
#else:
#    print('oj')



# all thats left now is to special arenas, and finsih all the types of attacks and ults
#WHERED BY COMMENT ABOUT, oh. didn¨t commit it?!?! buruhhhhhhhh