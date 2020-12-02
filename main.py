#import lol
import random

#intro
inp=input("Welcome to Ace Mystery!\nSay \"help\" for help.\n\n> ")
#check if help needed
if inp=="help":
    print("""This is like mafia, there are 2 teams, with 3 roles each.
    Good team:
    
    Suvivor - limit: none - No special powers.
    Detective - limit: 2 - Gets hints and clues.
    Coyboy - limit: 4 - Can choose to keep someone safe.
    
    Evil team:
    
    Follower - limit: none - Other than being Evil, is a Suvivor.
    Murderer - limit: 1 - Chooses someone to die each night.
    Witch - limit: 1 - Can revive anyone.
    
    There are 2 phases, day and night. During day, 
    
    """)