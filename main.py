#import lol
import random

#ai/player class
class person():
    def __init__(self,name):
        name=self.name

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
    
    There are 2 phases, day and night. During day, someone is chosen to be voted out. 
    During night, the special powers of the role come in.
    
    The game ends when the good team elimantes the evil, or the good team fails to do so.
    """)

c=person("jane")
print(c)