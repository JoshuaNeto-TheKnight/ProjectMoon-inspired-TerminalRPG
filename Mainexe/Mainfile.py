import Events.Rawfunctions as Rawfunctions
import random
import Moves.Attackfunctions as Attack
import Moves.Defensefunctions as Defensefunctions
import os
import Events.Enemylists as Enem
Rawfunctions.clear_screen()
print("/You find yourself in a void so dark, it burns your eyes, then, almost in an instant, a spark starts talking to you.../")
print("I will be your guiding light, even in your lowest of lows, I shall shelter you.")
print("Do you understand?")
while True:
    print("/Answer the prompts with any highlighted letters/", "[Y]es", "[N]o")
    Choice = input()
    Rawfunctions.clear_screen()
    if Choice == "Y":
        print("Good... Now... Tell about yourself:")
        break
    elif Choice == "N":
        print("Good to know... Now, to your preferences...")
        break
    else:
        print("Hm? Sorry, be clearer next time, speaking of which...")
    
Stats = []
ChoiceFinale = "N"
Choice = 0
while ChoiceFinale == "N":
    pity = 0
    while True:
        print("Tell me, do you often find yourself as a strong-willed person with a thick skinned tolerance?")
        print("[Y]es [N]o")
        HP = 0
        Choice = input()
        if Choice == "Y":
            HP = 60
            break
        elif Choice == "N":
            HP = 50
            pity += 1
            break
        print("Let us try this again.")
    
    while True:
        print("Are you a brave person that will soldier on regardless of your weaknesses?")
        print("[Y]es [N]o")
        DEF = 0
        Choice = input()
        if Choice == "Y":
            DEF = 2
            break
        elif Choice == "N":
            DEF = 1
            pity += 1
            break
        else:
            print("Let us try this again.")
    while True:
        print("Do you find yourself as a righteous one?")
        print("[Y]es [N]o")
        PWR = 0
        Choice = input()
        if Choice == "Y":
            PWR = 5
            break
        elif Choice == "N":
            PWR = 3
            pity += 1
            break
        print("Let us try this again.")
    while True:        
        print("Are you a resilient person? Being more stubborn than you can backup with?")
        print("[Y]es [N]o")
        DEF = 0
        Choice = input()
        if Choice == "Y":
            DEF = 2
            break
        elif Choice == "N":
            DEF = 1
            pity += 1
            break
        print("Let us try this again.")
        print('Let me ask again...')
    defensive = 0
    while True:
        print('What type of action fits with your person?')
        print('[P]assive [N]eutral [A]ctive')
        Choice = input()
        if Choice == 'P':
            defensive = Defensefunctions.Guard
            break
        elif Choice == 'N':
            defensive = Defensefunctions.Counter
            break
        elif Choice == 'A':
            defensive = Defensefunctions.Evade
            break
        print('Please, answer with the options in mind.')
    print("Now, for an odd question...")
    while True:
        print("Which of these dinning utensils is your go-to?")
        print("[S]poon [F]ork [K]nife")
        Choice = input()
        if Choice == "S":
            movelist = [Attack.Bash]
            blunt = 0.5
            while True:
                print('Now for a follow up... Which of these two you fear the most?')
                print('[G]un [C]hainsaw')
                Choice = input()
                if Choice == 'G':
                    pierce, slash = 2.0,1.0
                    weaknesses = [blunt,pierce,slash]
                    break
                elif Choice == 'C':
                    pierce,slash = 1.0,2.0
                    weaknesses = [blunt,pierce,slash]
                    break
                else:
                    print('Retry again...')
            break
        elif Choice == 'F':
            movelist = [Attack.Stab]
            pierce = 0.5
            while True:
                print('Now for a follow up... Which of these two you fear the most?')
                print('[S]ledgehammer [C]hainsaw')
                Choice = input()
                if Choice == 'S':
                    blunt, slash = 2.0,1.0
                    weaknesses = [blunt,pierce,slash]
                    break
                elif Choice == 'C':
                    blunt, slash = 1.0,2.0
                    weaknesses = [blunt,pierce,slash]
                    break
                else:
                    print('Retry again...')
            break
        elif Choice == 'K':
            movelist = [Attack.Cut]
            slash = 0.5
            while True:
                print('Now for a follow up... Which of these two you fear the most?')
                print('[S]ledgehammer [G]un')
                Choice = input()
                if Choice == 'S':
                    blunt, pierce = 2.0,1.0
                    weaknesses = [blunt,pierce,slash]
                    break
                elif Choice == 'G':
                    blunt,pierce = 1.0,2.0
                    weaknesses = [blunt,pierce,slash]
                    break
                else:
                    print('Retry again...')
            break
    break
        
print('Your form takes a new shape ...')

Stats = [HP, DEF, PWR, movelist,defensive,weaknesses]

print(Stats)

print("Welcome to The City...")
print("Where you Face The Fear, and Build The Future...?")
print("Argh, thats unimportant. Now, what's your name, fresh blood?")
name = input("Insert your nickname: ")
print("Ah, right... you seem familiar with these streets, right?")
print("[Y]es.", "[N]o.")
while True:
    Choice = input()
    if Choice == "Y":
        print("Alright then, good luck out there, ya will need it...")
        break
    elif Choice == "N":
        print("You have a screw loose? Heh, well...")
        print("Here, take this then.")
        break
    else:
        print("Speak with your brain, not ya tounge!")
print(f'As a last advice: death will be your only sweet release, {name}...')
Stats.append(name)


def fight(EnemyStats,Stats):
    print("/Battle Start!/")
    #this will get the stats for the player and the enemy you fight
    #this is good as a function since it will be a the main feature
    HP,DEF,PWR,TYPEBLU,TYPEPIE,TYPESLA,NAME = Stats[0], Stats[1], Stats[2], Stats[5][0], Stats[5][1],Stats[5][2],Stats[6]
    EHP, EDEF, EPWR, ENTYPEBLU, ENTYPEPIE, ENTYPESLA,EMNAME = EnemyStats[0], EnemyStats[1], EnemyStats[2], EnemyStats[3][0], EnemyStats[3][1],EnemyStats[3][2],EnemyStats[4]
    while EHP > 0 or HP <= 0:
        
        while EHP > 0 or HP > 0:
            while True:
                print(EMNAME,"health:",EHP)
                print(f'Your stats: HP:{HP}, PWR:{PWR}, DEF:{DEF}')
                print(f"/How should {NAME} engage?/")
                print('[A]ttack [D]efense')
                action = input()
                if action == "A":
                    while True:
                        for i in range(len(Stats[3])):
                            print(f'{i+1}.{Stats[3][i]}')
                        print('/Input 0 if you want to cancel the action/')
                        action = input('/Type a number for the attack you wish to use/')
                        if action == 0: 
                            break
                        if action.isdigit() == True:
                            action = int(action)
                            action -= 1
                            if action < len(Stats[3]):
                                action = Stats[3][action]
                                DMG = action(Stats,EnemyStats)
                                Combatstart = True
                                Offense = True
                                Defense = False
                                break
                        else:
                            print('/Incorrect input/')
                elif action =='D':
                    print('WIP')   
                if Combatstart == True:
                    Combatstart = False
                    break
            Rawfunctions.clear_screen()
            if Offense == True:
                print(f'{name} attacked {EMNAME}')
                print(f'{name} dealt {DMG}!')
                EHP = EHP - DMG
            if EHP > 0:
                enemychoice = random.randrange(1,3)
                if enemychoice == 1:
                    print("He produces a knife from his pocket and swings at you!")
                    EnemyDMG = Attack.Cut(EPWR,Stats[5][3])
                    print(f'Took {EnemyDMG} damage!')
                    HP = HP - EnemyDMG
                elif enemychoice == 2:
                    print("The thug rests for a bit")
                    Recover = int(EnemyStats[0] / EDEF)
                    print(f'The enemy restored {Recover} HP')
                    EHP = EHP + Recover
                elif enemychoice == 3:
                    print("The thug continues to glare at you")
            
    if HP > 0:
        print("You won!")
        return HP
    elif HP <= 0:
        print('You lost...')
wheel = random.randint(1,2)
if wheel == 1:
    Enemy =  Enem.ToughThug
else:
    Enemy = Enem.Ratofthestreets
Stats[0] = fight(Enemy,Stats)