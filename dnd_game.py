#Tehee
import time

rogue_buff = False
mage_buff = False
warrior_buff = False

want_game = True


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

    def skip_turn(self):
        print(f'{self.name} has skipped their turn \n')

    def check_stats(self):
        if self.shield == True:
            print(f'{self.name}, has {self._health} hp left, {self._ult} ult points.')
            print('Shields are active! \n')
        else:
            print(f'{self.name}, has {self._health} hp left, {self._ult} ult points \n')

    def is_alive(self):
        if self._health <= 0:
            self._health = 0
            self.alive = False


    def got_hit(self, damage):
        
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
        self._stamina = 80 ##
        self._health += 10
        self._enough = 10 ##

        self.specific = 'stamina'


        self.needed = {
            'L' : 0,
            'M' : 5,
            'H' : 10,
            'S' : 0,

        }
        self.got_it = False


    def shields(self):
        super().shields()
        self._stamina += 9


    def check(self, what):
        if self._stamina >= self.needed[what]:
            self.got_it = True
        else:
            self.got_it = False

    def L_ATK(self, victim):
        damage = 3
        if rogue_buff == True:
            int(damage *1.5)
        else:
            pass

        self._ult += 4
        
        print(f"{self.name} attacks {victim.name} with a light attack. \n")
        print(f'{self._stamina} stamina points left!')

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

        self._stamina -= self.needed['M']
        self._ult += 1

        print(f"{self.name} attacks {victim.name} with a medium attack. \n")
        print(f'{self._stamina} stamina points left!')

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

        self._stamina -= self.needed['H']
        self._ult += 1
        
        print(f"{self.name} attacks {victim.name} with a heavy attack. \n")
        print(f'{self._stamina} stamina points left!')

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

        self._stamina -= self.needed['S']
        self._ult -= self._enough
        
        print(f"{self.name} attacks {victim.name} with a light attack. \n")
        print(f'{self._stamina} stamina points left! and {self._ult} ult points left!')
        

        victim.got_hit(damage)
        if victim.alive == False:
            print(f'{self.name} won!')
            place.character_death()


    def check_stats(self):
        super().check_stats()
        print(f'And {self._stamina} stamina points left. \n')




class Mage(Character):
    def __init__(self, name):
        super().__init__(name)
        self._mana = 2 ##
        self._health -= 20
        self._enough = 20 ##

        self.specific = 'mana'

        self.needed = {
            'L' : 3,
            'M' : 0,
            'H' : 0,
            'S' : 0,

        }

        self.got_it = False

    def shields(self):
        super().shields()
        self._mana += 9


    def check(self, what):
        if self._mana >= self.needed[what]:
            self.got_it = True
        else:
            self.got_it = False


    def L_ATK(self, victim):
        damage = 5
        if mage_buff == True:
            int(damage *1.5)
        else:
            pass

        self._mana -= self.needed['L']
        self._ult += 1
        
        print(f"{self.name} attacks {victim.name} with a medium attack. \n")
        print(f'{self._mana} mana points left!')

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

        self._mana -= self.needed['M']
        self._ult += 1
        
        print(f"{self.name} attacks {victim.name} with a medium attack. \n")
        print(f'{self._mana} mana points left!')

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

        self._mana -= self.needed['H']
        self._ult += 1
        
        print(f"{self.name} attacks {victim.name} with a medium attack. \n")
        print(f'{self._mana} mana points left!')

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

        self._mana -= self.needed['S']
        self._ult -= self._enough
        
        print(f"{self.name} attacks {victim.name} with a medium attack. \n")
        print(f'{self._mana} mana points left! and {self._ult} ult points left!')
        

        victim.got_hit(damage)
        if victim.alive == False:
            print(f'{self.name} won!')
            place.character_death()



    def check_stats(self):
        super().check_stats()
        print(f'And {self._mana} mana points left.')




class Warrior(Character):
    def __init__(self, name):
        super().__init__(name)
        self._strength = 100 ##
        self._health += 30
        self._enough = 15 ##

        self.specific = 'strength'

        self.needed = {
            'L' : 0,
            'M' : 0,
            'H' : 0,
            'S' : 0,

        }

        self.got_it = False
    

    def shields(self):
        super().shields()
        self._strength += 9


    def check(self, what):
        if self._strength >= self.needed[what]:
            self.got_it = True
        else:
            self.got_it = False

    def L_ATK(self, victim):
        damage = 5
        if warrior_buff == True:
            int(damage *1.5)
        else:
            pass

        self._strength -= self.needed['L']
        self._ult += 1
        
        print(f"{self.name} attacks {victim.name} with a medium attack. \n")
        print(f'{self._strength} strength points left!')

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

        self._strength -= self.needed['M']
        self._ult += 1
        
        print(f"{self.name} attacks {victim.name} with a medium attack. \n")
        print(f'{self._strength} strength points left!')

        victim.got_hit(damage)
        if victim.alive == False:
            print(f'{self.name} won!')
            place.character_death()
    
    def H_ATK(self, victim):
        damage = 60
        if warrior_buff == True:
            int(damage *1.5)
        else:
            pass

        self._strength -= self.needed['H']
        self._ult += 1
        
        print(f"{self.name} attacks {victim.name} with a medium attack. \n")
        print(f'{self._strength} strength points left!')

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
        
        self._strength -= self.needed['S']
        self._ult -= self._enough
        
        print(f"{self.name} attacks {victim.name} with a medium attack. \n")
        print(f'{self._strength} strength points left! and {self._ult} ult points left!')
        

        victim.got_hit(damage)
        if victim.alive == False:
            print(f'{self.name} won!')
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
                if person._ult >= person._enough:
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

        instructions = "  Each player gets to pick a fighter and an arena to fight in. \n  On each turn you have three attack options, and a special attack once you have enough ult points. \n  You could even use shields or skip your turn entirely! \n  But beware, you get one move only, so think wisely!\n"

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
                quit()
            else:
                pass
        


        while want_game == True:
            player_1 = 'player_1'
            player_2 = 'player_2'


            place.character_choice(player_1)
            player_1 = type(choice_name)

            place.character_choice(player_2)
            player_2 = type(choice_name)


            place.arena_type()

            place.game()

            keep = int(input('Want to play again? \n1. for yes. \n2. for no.'))
            if keep == 1:
                del player_1
                del player_2

                beginning = True
                while beginning == True:
                    start = int(input('if you want instructions again, press 1, otherwise press 2.'))
                    if start == 1:
                        print(instructions)
                        
                    elif start == 2:
                        beginning = False
                    else:
                        pass

                
            elif keep == 2:
                print('ty for playing')
                break
            else:
                print('huh?')



place = Arena()
place.game_run()
