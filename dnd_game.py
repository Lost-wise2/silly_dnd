#Tehee
import random
import time
print(random.randint(1,2))

rogue_debuff = False
mage_debuff = False
warrior_debuff = False

want_game = True

dodging = False

invalid_input = True
invalid_number = True

# Main class for the characters
class Character():
    def __init__(self, name):
        self.name = name

        self._health = 100 ##
        self._ult = 0 ##

        self.alive = True
        self.shield = False

        
        
        

        # health and other attributes such as mana and agility are predetermined, 
        # cannot ask user for imput bc they would obvi pick an overpowerd stats


    def shields(self):
        self.shield = True
        print(f'{self.name} used shields \n')

    def check_stats(self):
        if self.shield == True:
            print(f'{self.name}, has {self._health} hp left, {self._ult} ult points.')
            print('Shields are active! \n')
        else:
            print(f'{self.name}, has {self._health} hp left, {self._ult} ult points currently, you need {self._enough} for your next ult.\n')

    def is_alive(self):
        if self._health <= 0:
            self._health = 0
            self.alive = False


    def got_hit(self, damage):
        global dodging

        if dodging == True:
            damage = 0
            dodging = False
            print(f'{self.name} had dodged the attack! They got no damage!')        
        if self.shield == True:
            damage = int(damage*0.75)
            self._health -= damage
            self.shield = False
            print(f"{self.name} has sheilds active! And only took {damage} damange instead, their health is now {self._health} \n")
        else:
            self._health -= damage
            print(f"{self.name} took {damage} damange, their health is now {self._health} \n")
        self.is_alive()


    






        

    


# three subclasses for each type of character
class Rogue(Character):
    def __init__(self, name):
        super().__init__(name)
        self._stamina = 40 ##
        self._health += 10
        self._enough = 10 ##

        self.specific = 'stamina'

        
        


        self.needed = {
            'L' : 0,
            'M' : 6,
            'H' : 15,
            'S' : 20,

        }
        self.got_it = False


    def shields(self):
        super().shields()
        self._stamina += 8


    def check(self, what):
        if self._stamina >= self.needed[what]:
            self.got_it = True
        else:
            self.got_it = False

    def L_ATK(self, victim):
        damage = 7
        if rogue_debuff == True:
            int(damage//1.5)
        else:
            pass
        
        self._stamina -= self.needed['L']
        self._ult += 1
        
        print(f"{self.name} attacks {victim.name} with a light punch! \n")
        print(f'{self._stamina} stamina points left!')

        victim.got_hit(damage)
        if victim.alive == False:
            print(f'{self.name} won!')
            place.character_death()

    def M_ATK(self, victim):
        damage = 15
        if rogue_debuff == True:
            int(damage//1.5)
        else:
            pass

        self._stamina -= self.needed['M']
        self._ult += 2

        print(f"{self.name} attacks {victim.name} with a spin kick!. \n")
        print(f'{self._stamina} stamina points left!')

        victim.got_hit(damage)
        if victim.alive == False:
            print(f'{self.name} won!')
            place.character_death()
    
    def H_ATK(self, victim):
        damage = 20
        if rogue_debuff == True:
            int(damage//1.5)
        else:
            pass

        self._stamina -= self.needed['H']
        self._ult += 3
        
        print(f"{self.name} attacks {victim.name} with an arrow shot! \n")
        print(f'{self._stamina} stamina points left!')

        victim.got_hit(damage)
        if victim.alive == False:
            print(f'{self.name} won!')
            place.character_death()
    
    
    def special(self, victim):
        global dodging
        dodging = True

        damage = 20
        if rogue_debuff == True:
            int(damage//1.5)
        else:
            pass

        self._stamina -= self.needed['S']
        self._ult -= self._enough
        
        print(f"{self.name} teleports behind {victim.name} and stabs them in the back!! \n")
        print(f'{self._stamina} stamina points left! and {self._ult} ult points left!')
        

        victim.got_hit(damage)
        if victim.alive == False:
            print(f'With their sharp mind and quick action {self.name} won!')
            place.character_death()


    def check_stats(self):
        super().check_stats()
        print(f'And {self._stamina} stamina points left. \n')




class Mage(Character):
    def __init__(self, name):
        super().__init__(name)
        self._mana = 70 ##
        self._health -= 20
        self._enough = 25 ##

        self.specific = 'mana'

        self.needed = {
            'L' : 5,
            'M' : 12,
            'H' : 20,
            'S' : 30,

        }

        self.got_it = False

    def shields(self):
        super().shields()
        self._mana += 10


    def check(self, what):
        if self._mana >= self.needed[what]:
            self.got_it = True
        else:
            self.got_it = False


    def L_ATK(self, victim):
        damage = 10
        if mage_debuff == True:
            int(damage//1.5)
        else:
            pass

        self._mana -= self.needed['L']
        self._ult += 3
        
        print(f"{self.name} attacks {victim.name} with a small water shot! \n")
        print(f'{self._mana} mana points left!')

        victim.got_hit(damage)
        if victim.alive == False:
            print(f'{self.name} won!')
            place.character_death()
    
    
    def M_ATK(self, victim):
        damage = 18
        if mage_debuff == True:
            int(damage//1.5)
        else:
            pass

        self._mana -= self.needed['M']
        self._ult += 4
        
        print(f"{self.name} attacks {victim.name} with an electric zap! \n")
        print(f'{self._mana} mana points left!')

        victim.got_hit(damage)
        if victim.alive == False:
            print(f'{self.name} won!')
            place.character_death()
    
    
    def H_ATK(self, victim):
        damage = 22
        if mage_debuff == True:
            int(damage//1.5)
        else:
            pass

        self._mana -= self.needed['H']
        self._ult += 5
        
        print(f"{self.name} attacks {victim.name} with a fire ball! \n")
        print(f'{self._mana} mana points left!')

        victim.got_hit(damage)
        if victim.alive == False:
            print(f'{self.name} won!')
            place.character_death()
   
   
   
    def special(self, victim):
        damage = 16
        self._health += 16
        if mage_debuff == True:
            int(damage//1.5)
        else:
            pass

        self._mana -= self.needed['S']
        self._ult -= self._enough
        
        print(f"{self.name} absorbs {victim.name}'s health and heals themselves with it!! \n")
        print(f'{self._mana} mana points left! and {self._ult} ult points left!')
        

        victim.got_hit(damage)
        if victim.alive == False:
            print(f'With their gift of magic and creativity {self.name} won!')
            place.character_death()



    def check_stats(self):
        super().check_stats()
        print(f'And {self._mana} mana points left.')




class Warrior(Character):
    def __init__(self, name):
        super().__init__(name)
        self._strength = 50 ##
        self._health += 30
        self._enough = 20 ##

        self.specific = 'strength'

        self.needed = {
            'L' : 10,
            'M' : 15,
            'H' : 20,
            'S' : 25,

        }

        self.got_it = False
    

    def shields(self):
        super().shields()
        self._strength += 12


    def check(self, what):
        if self._strength >= self.needed[what]:
            self.got_it = True
        else:
            self.got_it = False

    def L_ATK(self, victim):
        damage = 8
        if warrior_debuff == True:
            int(damage//1.5)
        else:
            pass

        self._strength -= self.needed['L']
        self._ult += 4
        
        print(f"{self.name} attacks {victim.name} with a punch to the stomach! \n")
        print(f'{self._strength} strength points left!')

        victim.got_hit(damage)
        if victim.alive == False:
            print(f'{self.name} won!')
            place.character_death()
    
    def M_ATK(self, victim):
        damage = 20
        if warrior_debuff == True:
            int(damage//1.5)
        else:
            pass

        self._strength -= self.needed['M']
        self._ult += 5
        
        print(f"{self.name} attacks {victim.name} with a war mace! \n")
        print(f'{self._strength} strength points left!')

        victim.got_hit(damage)
        if victim.alive == False:
            print(f'{self.name} won!')
            place.character_death()
    
    def H_ATK(self, victim):
        damage = 26
        if warrior_debuff == True:
            int(damage//1.5)
        else:
            pass

        self._strength -= self.needed['H']
        self._ult += 6
        
        print(f"{self.name} attacks {victim.name} with a giant heavy sword! \n")
        print(f'{self._strength} strength points left!')

        victim.got_hit(damage)
        if victim.alive == False:
            print(f'{self.name} won!')
            place.character_death()
    
    
    def special(self, victim):
        damage = 28
        self_buff = self._health//7
        self._health -= self_buff
        damage += self_buff
        if warrior_debuff == True:
            int(damage//1.5)
        else:
            pass
        
        self._strength -= self.needed['S']
        self._ult -= self._enough
        
        print(f"{self.name} uses their own life force to attack {victim.name} with a cursed battleaxe!! \n")
        print(f'{self._strength} strength points left! and {self._ult} ult points left!')
        

        victim.got_hit(damage)
        if victim.alive == False:
            print(f'With their sheer strength and bravery {self.name} won!')
            place.character_death()
    


    def check_stats(self):
        super().check_stats()
        print(f'And {self._strength} strength points left.')


####################################








# Class for the arena itself where the game also takes place in
class Arena():
    def __init__(self):
        self.yaya = 0
        self.dead_character = False
        


    def error_handling(self, to_check, range):
        #self.to_check = to_check
        global invalid_input
        global invalid_number
        

        if to_check.isnumeric() == True:
            to_check = int(to_check) 
            #print(to_check)           
            invalid_input = False
            if to_check <= range and to_check > 0:
                invalid_number = False
            else:
                print("Please input a valid number!")
        else:
            print("Please input a valid number!")

        #try:
            #to_check = int(to_check)
            #invalid_input = False
        #except ValueError:
            #print("Please input a valid number!")
        


    def character_choice(self, player):
        global choice_name
        global type
        global invalid_input
        global invalid_number

        self.player = player
        print(f'\n{self.player} select your style:')

        invalid_input = True
        invalid_number = True
        while invalid_input == True or invalid_number == True:
            choice_type = input('1. for rogue, 2. for mage and 3. for warrior \n')
            place.error_handling(choice_type, 3)
        choice_type = int(choice_type)

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
        global invalid_input
        global invalid_number

        making_choice = True
        while making_choice == True:

            invalid_input = True
            invalid_number = True
            while invalid_input == True or invalid_number == True:
                yaya = input(f"It is now {person.name}'s turn! press the following: \n  1. for shield that regenerates your {person.specific},\n  2. For a light attack,\n  3. For a medium attack,\n  4. For a heavy attack,\n  5. For a ultimate attack,\n  6. To check stats \n")
                place.error_handling(yaya, 6)
            yaya = int(yaya)

            if yaya == 1:
                person.shields()
                making_choice = False
            elif yaya == 2:
                person.check('L')
                if person.got_it == True:
                    person.L_ATK(victim)
                    making_choice = False
                else:
                    print(f'Sorry but {person.name} does not have enoygh {person.specific} points')

            elif yaya == 3:
                person.check('M')
                if person.got_it == True:
                    person.M_ATK(victim)
                    making_choice = False
                else:
                    print(f'Sorry but {person.name} does not have enoygh {person.specific} points')

            elif yaya == 4:
                person.check('H')
                if person.got_it == True:
                    person.H_ATK(victim)
                    making_choice = False
                else:
                    print(f'Sorry but {person.name} does not have enoygh {person.specific} points')
                    
            elif yaya == 5:
                if person._ult >= person._enough:
                    person.check('S')
                    if person.got_it == True:
                        person.special(victim)
                        making_choice = False
                    else:
                        print(f'Sorry but {person.name} does not have enoygh {person.specific} points')    
                else:
                    print(f'Sorry but {person.name} does not have enough ult points')

            elif yaya == 6:
                person.check_stats()
                time.sleep(2)
            else:
                print('uh oh')
                quit()
    



    def arena_type(self):
        global rogue_debuff
        global mage_debuff
        global warrior_debuff

        global invalid_input
        global invalid_number

        options = []

        print('There are 3 are three different fightings arenas to pick from, each one having different effects on each character. \n  The first arena takes place in a mirrored dimension where the gravitational pull is much stronger. \n  The second arena takes place in an abandoned testing ground for machines, many strong magnets were left behind. \n  The third and last arena takes place in a corrupt forrest, the soil absorbing all magic from the area leaving it dry and lifeless. \n')
        print('To make it fair, both players will pick an arena and both options will be randomly picked from.')

        invalid_input = True
        invalid_number = True
        while invalid_input == True or invalid_number == True:
            what_arena1 = input('\nPlayer 1, please pick your arena. \n1. for the first arena, 2. for the second one or 3. for the last one.')
            place.error_handling(what_arena1, 3)
        what_arena1 = int(what_arena1)

        invalid_input = True
        invalid_number = True
        while invalid_input == True or invalid_number == True:
            what_arena2 = input('\nPlayer 2, please pick your arena. \n1. for the first arena, 2. for the second one or 3. for the last one.')
            place.error_handling(what_arena2, 3)
        what_arena2 = int(what_arena2)

        options.append(what_arena1)
        options.append(what_arena2)
        

        what_arena = random.choice(options)
        options.clear()

        if what_arena == 1: #More gravity
            rogue_debuff = True

            print('Arena 1 has been selected!')
            time.sleep(1)
            print('Due to the increased gravity in the area, any rogue characters will have a harder time moving!')
            time.sleep(2)
        elif what_arena == 2: #Strong magnets
            warrior_debuff = True

            print('Arena 2 has been selected!')
            time.sleep(1)
            print('Due to the strong magnets in the area, any warrior characters will have a harder time using their weapons!')
            time.sleep(2)
        elif what_arena == 3: #The ground consumes magic
            mage_debuff = True

            print('Arena 3 has been selected!')
            time.sleep(1)
            print('Due to the corrupted soil in the area, any mage characters will have a harder time casting spells!')
            time.sleep(2)
        else:
            print('none picked??')
            quit()
        


    def character_death(self):
        self.running = False
        self.dead_character = True
 





    def game(self):
        self.running = True
        round = 1
        while self.running == True:
            print("Round", round, "has begun. \n")
            time.sleep(1)
            
            place.choice(player_1, player_2)
            time.sleep(2)
            
            
            if self.dead_character == True:
                self.dead_character = False
                break
            


            place.choice(player_2, player_1)
            time.sleep(2)

            if self.dead_character == True:
                self.dead_character = False
                break
            
            

            print("Round", round, "has ended. \n")
            round += 1
            time.sleep(2)




    def game_run(self):
        global player_1
        global player_2

        global invalid_input
        global invalid_number

        instructions = "  Each player gets to pick a fighter and an arena to fight in. \n  On each turn you have three attack options, and a special attack once you have enough ult points. \n  You could even use shields to take less damage and regenerate your special stat like mana! \n  But beware, you get one move only, so think wisely!\n"
        instructions2 ="  The rogue is a cunning thief, using their agility and fast action to dodge attacks and catch their prey by surprise and strike them down where they least expected it. \n  The mage is born with the gift of magic, using their power to call the forces of nature to aid them in battle from afar and heal themselves when needed. \n  The warrior is a brave soldier driven by their strong sense of justice cursed with axe that draws from their lifeforce to deal extra damage to whoever stands in their way.\n"
        beginning = True


        print('Welcome and hello! This game is a turn based dnd inspired game! \nAnd the instructions are:')
        print(instructions)
        print(instructions2)

        while beginning == True:

            invalid_input = True
            invalid_number = True
            while invalid_input == True or invalid_number == True:
                start = input('To start the game press 1, press 2 for instructions again or 3 to quit.')
                place.error_handling(start, 3)
            start = int(start)

            if start == 1:
                pass
                beginning = False
            elif start == 2:
                print(instructions)
                print(instructions2)
            elif start == 3:
                print("Sad to see you go, but hope you'd be up for a game coon :)")
                quit()
            else:
                print('what the-')
                quit()
        


        while want_game == True:
            player_1 = 'player_1'
            player_2 = 'player_2'


            place.character_choice(player_1)
            player_1 = type(choice_name)
            print(f'Hello {player_1.name}!')

            place.character_choice(player_2)
            player_2 = type(choice_name)
            print(f'Hello {player_2.name}!')


            place.arena_type()

            place.game()

            invalid_input = True
            invalid_number = True
            while invalid_input == True or invalid_number == True:
                keep = input('Want to play again? \n1. for yes. \n2. for no.')
                place.error_handling(keep, 2)
            keep = int(keep)

            if keep == 1:
                del player_1
                del player_2

                beginning = True
                while beginning == True:
                    invalid_input = True
                    invalid_number = True
                    while invalid_input == True or invalid_number == True:
                        start = input('if you want instructions again, press 1, otherwise press 2.')
                        place.error_handling(start, 2)
                    if start == 1:
                        print(instructions)
                        
                    elif start == 2:
                        beginning = False
                    else:
                        print('what the-')
                        quit()

                
            elif keep == 2:
                print('ty for playing')
                break
            else:
                print('huh?')
                quit()



place = Arena()
place.game_run()
