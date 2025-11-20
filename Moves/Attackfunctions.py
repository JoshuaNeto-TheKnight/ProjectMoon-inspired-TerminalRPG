import random
import time

class Attackpower:
    def __init__(self, base, power, count):
        self.__base = base
        self.__power = power
        self.__count = count

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

#ADD CLASHING YOU DUMMY!!!!!!!!!!!!!!!!!

Tanglecleaver = Attackpower(6, 4, 3)
SelfDestructivePurge = Attackpower(30, -12, 3)
Tanglecleaver.rolls(30)
SelfDestructivePurge.rolls(-30)
LordLuS2 = Attackpower(3,3,4)
LordLuS2.rolls(1)

