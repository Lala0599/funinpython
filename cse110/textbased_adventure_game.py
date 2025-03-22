"""
Text-Based Adventure Game
Aurthor: Laone Tsheole
Description: This is a text based game with 3 levels of choices. It includes
a hidden path and a trick question for added creativity.
"""

#Welcome message
print("Welcome to the Text-Based Adventure Game ^.^!")
print("\nYou find yourself in a mysterious forest. Your choice will determine your fate. Let's get started!\n")

#initial choice
print("You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you pick up?\n")

choice_1 = input("Type MATCH or FLASHLIGHT: ").strip().lower()

#consequences of the first choice
if choice_1 == "match":
    print("\nYou pick up the match and strike it. For an instant, the forest around you is illuminated.")
    print("You see a large scary mythical creature ready to pounce, then the match burns out. Do you want to RUN or HIDE behind a tree?\n")
    
    choice_2 = input("Type RUN or HIDE: ").strip().lower()
    
    #consequence of the second choice(match path)
    if choice_2 == "run":
        print("\nYou start to run as fast as you can. The creature closes in, but luckily you manage to escape!\n")
        print("You find yourself at a river. Do you want to SWIM across or FOLLOW the riverbank?\n")
        
        choice_3 = input("Type SWIM or FOLLOW: ").strip().lower()
        
        #cosequnces of choice 3 (run path)
        if choice_3 == "swim":
            print("\nYou dive into the river and swim across. Youu reach the other side safely and find a hidden treasure chest!\n")
            print("Congratulations, you made it out safely. You win!")
            
        elif choice_3 == "follow":
            print("\nYou follow the riverbank and stumble upon a friendly village, the villagers offer you food and shelter.\n")
            print("You live happily ever after; Congratulations!")
            
        else:
            print("\nInvalid choice. You stand still, and the creature catches up to you. It devours you, Game Over!")
        
    elif choice_2 == "hide":
        print("\nYou hide behind a tree. The creature sniffs around but does not see you.")
        print("After the creature leaves, you find a secret path. Do you want to EXPLORE the path or RETURN to the forest?\n")
        
        choice_3 = input("Type EXPLORE or RETURN: ").strip().lower()
        
        #cosequences of choice 3 (hide path)
        if choice_3 == "explore":
            print("\nYou will follow the secret path and discover a magical portal. You go through it and find yourself in a paradise!")
            print("\nCongratulations. You win !!")
            
        elif choice_3 == "return":
            print("\nYou return to the forest and get lost. You wander forever. Game Over!")
            
        else:
            print("\nInvalid choice. The creature finds and devours you, Game Over!")
    else:
        print("\nInvalid choice. The creature finds and attacks, Game Over!")
        
elif choice_1 == "flashlight":
    print("\nYou pick up the flashlight and turn it on. You see a oathway lit up in front of you.")
    print("You thought you also heard something off to the side. Do you want to Follow the path ir LOOK in the trees?")
    
    choice_2 = input("Type FOLLOW or LOOK: ").strip().lower()
    
    #consequences of the second choice(flash path)
    if choice_2 == "follow":
        print("\nYou follow the path and come across a bridge. Do you want to CROSS the bridge or TURN back?")
        
        choice_3 = input("\nType CROSS or TURN").strip().lower()
        
        #consequences of third choice
        if choice_3 == "cross":
            print("\nYou cross the bridge and find a hidden cave filled with gold and jewels!")
            print("Congratulations, You Win!!")
            
        elif choice_3 == "turn":
            print("\nYou turn nack and get lost in the forest. Game Over!")
            
        else:
            print("\nInvalid choice. You hesitate and fall off the bridge. Game over!")
    elif choice_2 == "look":
        print("\nYou look in the trees and see a pair of glowing eyes. Do you APPROACH or IGNORE it?\n")
        
        choice_3 = input("Type APPROACH or IGNORE: ").strip().lower()
        
        if choice_3 == "approach":
            print("\nYou approach the glowing eyes and find a friendly owl. It leads you to safety!")
            print("Congratulations, you win!")
            
        elif choice_3 == "ignore":
            print("\nYou ignore the glowing eyes and continue walking. You fall into a trap. Gave Over!!")
        else:
            print("\nInvalid choice. The glowing eyes attack you. Game Over!")
    else:
        print("\nInvalid choice. You stand still, and the forest consumes you. Game Over!!")
else:
    print("\nInvalid choice. You stand still and the forest consumes you. Game Over!!")
        
            
        
    
        
        
            
            
        
    
