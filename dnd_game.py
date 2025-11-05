#Tehee
import random
import time

print(random.randint(1,10))


print('yaya')






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
        self.stamina = 100
        self.health += 10

    def add(self): # to test if the ult system works
        self.ult += 10
        print(f'ult points now are {self.ult}')



    def L_ATK(self, victim):
        damage = 3
        #print(f'{self.name} used a light attack')
        print(f"{self.name} attacks {victim.name} with a light attack. \n")
        print(f'{self.stamina} stamina points left!')

        victim.got_hit(damage)
        if victim.alive == False:
            print(f'{self.name} won!')
            place.character_death()

    def M_ATK(self, victim):
        damage = 5
        self.stamina -= damage

        print(f"{self.name} attacks {victim.name} with a medium attack. \n")
        print(f'{self.stamina} stamina points left!')

        victim.got_hit(damage)
        if victim.alive == False:
            print(f'{self.name} won!')
            place.character_death()
    
    def H_ATK(self, victim):
        damage = 10
        self.stamina -= damage
        
        print(f"{self.name} attacks {victim.name} with a heavy attack. \n")
        print(f'{self.stamina} stamina points left!')

        victim.got_hit(damage)
        if victim.alive == False:
            print(f'{self.name} won!')
            place.character_death()
    
    
    def special(self, victim):
        damage = 20
        self.stamina -= damage
        
        print(f"{self.name} attacks {victim.name} with a light attack. \n")
        print(f'{self.stamina} stamina points left!')

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
        self.mana = 100
        self.health -= 20



    def L_ATK(self, victim):
        damage = 5
        self.mana -= damage
        
        print(f"{self.name} attacks {victim.name} with a medium attack. \n")
        print(f'{self.mana} mana points left!')

        victim.got_hit(damage)
        if victim.alive == False:
            print(f'{self.name} won!')
            place.character_death()
    
    
    def M_ATK(self, victim):
        damage = 8
        self.mana -= damage
        
        print(f"{self.name} attacks {victim.name} with a medium attack. \n")
        print(f'{self.mana} mana points left!')

        victim.got_hit(damage)
        if victim.alive == False:
            print(f'{self.name} won!')
            place.character_death()
    
    
    def H_ATK(self, victim):
        damage = 12
        self.mana -= damage
        
        print(f"{self.name} attacks {victim.name} with a medium attack. \n")
        print(f'{self.mana} mana points left!')

        victim.got_hit(damage)
        if victim.alive == False:
            print(f'{self.name} won!')
            place.character_death()
   
   
   
    def special(self, victim):
        damage = 5
        self.mana -= damage
        
        print(f"{self.name} attacks {victim.name} with a medium attack. \n")
        print(f'{self.mana} mana points left!')

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
    

    def L_ATK(self, victim):
        damage = 5
        self.strength -= damage
        
        print(f"{self.name} attacks {victim.name} with a medium attack. \n")
        print(f'{self.strength} strength points left!')

        victim.got_hit(damage)
        if victim.alive == False:
            print(f'{self.name} won!')
            place.character_death()
    
    def M_ATK(self, victim):
        damage = 5
        self.strength -= damage
        
        print(f"{self.name} attacks {victim.name} with a medium attack. \n")
        print(f'{self.strength} strength points left!')

        victim.got_hit(damage)
        if victim.alive == False:
            print(f'{self.name} won!')
            place.character_death()
    
    def H_ATK(self, victim):
        damage = 5
        self.strength -= damage
        
        print(f"{self.name} attacks {victim.name} with a medium attack. \n")
        print(f'{self.strength} strength points left!')

        victim.got_hit(damage)
        if victim.alive == False:
            print(f'{self.name} won!')
            place.character_death()
    
    
    def special(self, victim):
        damage = 5
        self.strength -= damage
        
        print(f"{self.name} attacks {victim.name} with a medium attack. \n")
        print(f'{self.strength} strength points left!')

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
        print(f'\n{self.player} select your style:')
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
                person.L_ATK(victim)
                making_choice = False
            elif yaya == 2:
                person.M_ATK(victim)
                making_choice = False
            elif yaya == 3:
                person.H_ATK(victim)
                making_choice = False
            elif yaya == 4:
                pass
            elif yaya == 9:
                person.check_stats()
            elif yaya == 10:
                person.skip_turn()
                making_choice = False
            else:
                print('uh oh')
    




    def character_death(self):
        self.running = False
        self.dead_character = True
        #print('done')





    def game(self):
        self.running = True
        round = 1
        while self.running == True:
            print("Round", round, "has begun. \n")
            time.sleep(1)
            
            place.choice(player_1, player_2)
            time.sleep(2)
            #player_2.is_alive()
            #if player_2.alive == False:
                #print('Round ended, Player 2 won!')
            #    running = False
            #else:
            #    pass
            
            if self.dead_character == True:
                break
            
            place.choice(player_2, player_1)
            time.sleep(2)
            #player_1.is_alive()
            #if player_1.alive == False:
                #print('Round ended, Player 1 won!')
            #    running = False
            #else:
            #    pass
            print("Round", round, "has ended. \n")
            round += 1
            time.sleep(2)

    
        
        
            
            
        






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







#place.choice(player_1)
#place.choice(player_2)



place.game()

#done = int(input('done? 1. for done, 2. for no'))

#if done == 1:
#    del player_1
#else:
#    print('oj')



# all thats left now is to special arenas, and finsih all the types of attacks and ults
#and private variables