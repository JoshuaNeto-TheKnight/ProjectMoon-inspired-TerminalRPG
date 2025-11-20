import random
import time

class Attackpower:
    def __init__(self, base, power, count, offensive, name):
        self.__base = base
        self.__power = power
        self.__count = count
        self.__off = offensive
        self.__name = name

    @property
    def base(self):
        return self.__base
    @base.setter
    def base(self, new):
        self.__base = new

    @property
    def power(self):
        return self.__power
    @power.setter
    def power(self, new):
        self.__power = new

    @property
    def count(self):
        return self.__count
    @count.setter
    def count(self, new):
        self.__count = new
    
    @property
    def off(self):
        return self.__off
    @off.setter
    def off(self, new):
        self.__off = new

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new):
        self.__name = new

    def rolls(self, sanity): #here we obtain the base, coin power and coin count on the self, and also obtain the sanity number
        FinalpowerReady = False #here is a conditional so the function runs until said
        usedcoins = 1 #setting the coins to 1 so we can further use it down the line
        while FinalpowerReady == False: #this piece of code will run all the lines below it if they arent on the same level as it until conditionals meet 
            Finalpower = self.base #extracts the base power from the variable, setting the base for the power
            while usedcoins <= self.count: #will run until the coin count is equal or above
                flipresult = random.randint(1, 100) #still am thinking about it
                print(flipresult) #prints the roll for testing
                if flipresult <= (sanity+50): #supposed to do checks on the results, incrementing when heads (prints the resulting face)
                    Finalpower += self.power
                    print('Heads!')
                else:
                    print('Tails!')
                time.sleep(1.5) #these just delay the result printed
                usedcoins += 1
            if Finalpower < 0: #if the final power is below zero, sets the power to 0 instead
                Finalpower = 0
            FinalpowerReady = True #finally, exits out of the 'while' we set up, signaling the power is ready
            time.sleep(1.5)
        print(f'Final power obtained: {Finalpower}') #prints out the final result
        return Finalpower

    def clashing(self, target, selfsanity, targetsanity):
        #coins are saved here
        selfcoinamount = self.count
        targetcoinamount = target.count
        while True: #rolls until one of them have no coins available to use
            if self.count == 0 or target.count == 0:
                break
            YourRolls = self.rolls(selfsanity)
            TheirRolls = target.rolls(targetsanity)
            print(f' You rolled {YourRolls}!')
            print(f' Target rolled {TheirRolls}!') 
            time.sleep(2)
            if YourRolls > TheirRolls:
                target.count -= 1
                print(f'you have {self.count} coins left and the target has {target.count} left!')
                time.sleep(0.5)            
            elif TheirRolls > YourRolls: 
                self.count -= 1
                print(f'you have {self.count} coins left and the target has {target.count} left!')
                time.sleep(0.5)            
            else:
                print("clash tie!")
                time.sleep(2)
            clashcount += 1 #not really useful right now
            print(f'Clash {clashcount}!')
        if self.count == 0:
            print("Clash lost...")
            self.count = selfcoinamount
            target.count = targetcoinamount 
            return target.name
        elif target.count == 0:
            print("Clash won!!!")
            self.count = selfcoinamount
            target.count = targetcoinamount 
            return self.name
#Testing
LordLuS2 = Attackpower(3,3,4,2, 'Serious slashes')
Tanglecleaver = Attackpower(6, 4, 3, 5, 'Lets dance.')
SelfDestructivePurge = Attackpower(30, -12, 3, 2, 'I AM WASHED')
winner = Tanglecleaver.clashing(SelfDestructivePurge, 20, -20 )
print(winner)
winner = Tanglecleaver.clashing(LordLuS2, 20, 20)
print(f'{winner} won!')


