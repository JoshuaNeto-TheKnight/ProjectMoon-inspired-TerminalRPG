import random

#functions that define the defense type
#still doesnt meet my standards, will be updated

def Counter(HP: int, DEF: int,ENEMYDMG: int ):
    CurrentHP = HP - ENEMYDMG
    if CurrentHP == HP:
        print('Action failed.')
        return
    elif CurrentHP != HP:
        print('Counter!')
        DMG = int(DEF * (ENEMYDMG * 0.5))
        print(f'Dealt {DMG} damage!')
        return DMG
    """
    Counters you take damage but you deal a higher sum of damage back, will tweak the dmg value later
    """
def Guard(HP: int, DEF: int, ENEMYDMG: int):
    """
    Guards will make you generate artificial HP to tank some of the damage off, reducing the enemy dmg total
    """
    ReducedDMG = int((HP * 0.1) * DEF)
    print('Block value:', ReducedDMG)
    FinalDMG = ReducedDMG - ENEMYDMG
    if FinalDMG > 0:
        print('blocked!')
        return 0
    else:
        print('Took damage!')
        print('Damage:', FinalDMG)
        return FinalDMG
def Evade(HP, DEF, ENEMYDMG):
    """
    Evade is a all or nothing defense, you either take none or take it all
    """
    Evadevalue = round(((HP * 0.2) + (DEF * 0.5)), 0)
    print('Evade power:', Evadevalue)
    if Evadevalue >= ENEMYDMG:
        DMG = 0
        print('Dodged!')
        return DMG
    elif Evadevalue < ENEMYDMG:
        DMG = ENEMYDMG
        print('Failed.')
        return DMG
"""    
ENEMYDMG = random.randint(0,10)
MAXHP = 20
HP = 25
Attack = 5
DEF = 5
method = 0
print('test one')
while True:
    print('Counter, Guard, Evade')
    choice = input()
    if choice == 'Counter':
        method = [Counter(HP, ENEMYDMG, DEF), 1]
        break
    if choice == 'Guard':
        method = [Guard(MAXHP, DEF, ENEMYDMG), 2]
        break
    if choice == 'Evade':
        method = [Evade(HP, DEF, ENEMYDMG), 3]
        break


print('Enemy Damage:', ENEMYDMG)
if method[1] == 1:
    damagedealt = method
    totaldmg = ENEMYDMG
elif method[1] == 2 or method[1] == 3:
    totaldmg = method
print('Damage taken:', totaldmg)
if totaldmg > 0:
    HP = HP - totaldmg
    print('New HP:' , HP)
    """