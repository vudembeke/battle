import os
import random
import time


def health():
    six = random.randint(1,7)
    twelve = random.randint(1,13)
    healthstat = ((six * twelve) / 2) + 10
    return healthstat

def strength():
    six = random.randint(1,7)
    twelve = random.randint(1,13)
    strengthstat = ((six * twelve) / 2 )+ 12
    return strengthstat

def character():
    dice = random.randint(1,7)
    return dice 
    
round = 1
winner = None
while True:
    time.sleep(1)
    os.system("clear")
    round = 1
    winner = None
    print("Character Builder")
    print()
    fname = input("Enter your character name:\n ")
    ctype = input("Enter your character type:\n ")
    c1health = health()
    c1strength = strength()
    print()
    print(fname, "the", ctype)
    print("Health :", c1health)
    print("Strength :", c1strength)
    print()
    f2name = input("Who are they battling?\n")
    c2type = input("Enter your character type:\n ")
    c2health = health()
    c2strength = strength()
    print()
    print(f2name, "the", c2type)
    print("Health :", c2health)
    print("Strength :", c2strength) 
    print()
    print("⚔️TIME TO BATTLE!⚔️")
    print()
    print("The battle begins!")    
    print()
    c1dice = character()
    c2dice = character()
    while True:
        if c1dice > c2dice:
            print(fname, "wins the first blow")
            diff = abs(c1strength - c2strength)+1
            c2health = c2health - diff
            print(f2name, "takes a hit with", diff, "damage")                        
        elif c2dice > c1dice:
            print(f2name, "wins the first blow")
            diff = abs(c1strength - c2strength)+1
            c1health = c1health - diff
            print(fname, "takes a hit with", diff, "damage")
        else:
            print("Their swords clash and they draw round", round)
        print()
        print(fname)
        print("Health :", c1health)
        print()
        print(f2name)
        print("Health :", c2health)
        print()
        if c1health <= 0:
            print(fname, "has died!")
            winner = f2name
            break
        elif c2health <= 0:
            print(f2name, "has died!")
            winner = fname
            break
        else:
            print("And they're both standing for the next round")
            round += 1
    
    time.sleep(1)
    os.system("clear")
    print()
    print(winner, "has won in", round, "rounds")
    break   
             
        
    
        
    




