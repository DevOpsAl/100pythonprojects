print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
#imports
import sys

print("Welcome to Treasure Island.")


def game():
    print()
    
    print("""Plenty of riches await you, if only you can survive the perilous path ahead. 
If you so choose to be brave enough to continue, do so at your own risk. 
I wish you the best! 
          
~Treasure Master
""")
    player1 = input("""Do you wish to continue? (y/n)
    """)
    
    if player1 == "y" or player1 == "Y":
        print("""You have landed on treasure island. Your group is deciding whether to make camp on the beach or scout the
    area for food, water, and predators.\n""")
        
        player1 = input("""As the expedition leader, you get to make the final decision. What will you do? 
[C]amp or [S]cout the area. (c/s)
    """)
        
        if player1 == "c" or player1 == "C":
            print("""
    Your camp is attacked by a bank of Komodo Dragons, destroying your supplies and killing several of your team. 
    Your expedition has been cancelled, and the ship has been called back to rescue the remaining survivors.
                                            GAME OVER!!!
    """)
            restart = input("Play Again? (y/n)")
            if restart == "y" or restart == "Y":
                print("Starting New Game!")
                game()
            elif restart == "n" or restart == "N":
                sys.exit(0)
        
        elif player1 == "s" or player1 == "S":
            print("""After leaving the beach area, you notice a large bank of Komodo Dragons scavenging the beach you just left. 
    You're greatful to have avoided meeting them. You take a look at the treasure map and push forward into the forest. 
    After following the trail for a few hours, one of your spotters finds a cave that resembles the drawing on the map. You want 
    to explore the cave, but a faint grumbling gives you the small idea that there might be something waiting in the cave.
    Another spotter finds a watering hole just past the cave. She says that there are no animals there and plenty of water. 
    You now have to choose.             
    """)
            
            player1 = input("Will you [e]xplore the cave, set a [t]rap for any animal that may be lingering in the cave, or [c]ontinue\nto the watering hole? (e/t/c)")
            
            if player1 == "e" or player1 == "E":
                print("""
    After headed into the cave, the coast appears to be clear. No sign of any predators. Everyone begins to unload themsleves when 
    three giant black bears appear from a recess in the cave. Frightened by your presence in their cave, the bears begin to maul your 
    entire expetition crew, destroying your supplies and killing several of your team. Your expedition has been cancelled, and the ship 
    has been called back to rescue the remaining survivors.
                                            GAME OVER!!!
    """)
                restart = input("Play Again? (y/n)")
                if restart == "y" or restart == "Y":
                    print("Starting New Game!")
                    game()
                elif restart == "n" or restart == "N":
                    sys.exit(0)
      
            elif player1 == "t" or player1 == "T":
                print("""A few of your crew begin to set predator bait at the mouth of the cave while the rest of the crew trains their
    weapons on the dark opening. After what seemed to be an hour wait, a large roar comes from the cave. Then shortly after three large black bears 
    appear from the cave and begin to eat the bait. A few quick shots take out the trio giving the crew plenty of food and ownership over the cave. 
    
    Everyone finally begins to relax and feel a sense of security after the eventful day. You however are still restless. Looking over and over the map.
    you can't make why this cave seems to be a dead end on the map. You decide to visit the deeper parts of the cave, looking for any clue that could explain 
    the dead end. Finally, you find a rock formation that seems to be out of place. Thinking quickly, you call for the resident puzzle master. After some 
    examination, it becomes apparent that each stone fits into a pattern of small cutouts on an obscure wall a little deeper in the cave. The puzzle master 
    places the stones intheir repsective slots. Suddenly, the ground shakes and three large rock doors open from the ground up. Overcome with joy, you call out
    to the entire crew to get up and help decide which path to take. Before the dicussion begins, a small scroll pops out from hidden compartment and rolls to 
    your feet. You pick it up and read it.
    
                            "I am box without hinges, key or lid,
                            Yet golden treasure inside is hid.
                            What am I?"
    """)
                player1 = input("""The path to treasure is the same as my identity (a/b/c) 
    a. a book
    b. the mind
    c. an egg
""")
                if player1 == "a" or player1 == "A":
                    print("""Your crew takes the first path. As everyone enters the narrow space, the last team members notices the door abruptly 
slam closed behind them. Suddenly, one wall of the narrow passage opens up to the blinding light of what seemed to be a small sun. Immediately, the 
entire crew in incenerated, and their shadows etched into the walls like ancient cave paiting. Your crew is lost. Your expedition has failed.
                                    GAME OVER!!!
""")
                    restart = input("Play Again? (y/n)")
                    if restart == "y" or restart == "Y":
                        print("Starting New Game!")
                        game()
                    elif restart == "n" or restart == "N":
                        sys.exit(0)
                elif player1 == "b" or player1 == "B":
                    print("""Taking the second path, everyone piles into a narrow hall like structure that opens up into a great hall. The sight of
the great hall send a jolt of energy through everyone. With the quickness that elation was blasted away as the wall of the great hall begin to close in 
on themselves and the chamber rapidly fills with a strange gas. As the team breathes in more of the gas, panic, joy, laughter, fear, and a host of other 
emotions take over as everyone has heavy psychedelic trips. Realizing that the answer you the crew chose was the mind, you desparately try to regain control
and break the trip as the wall close in. You slap yourself to no availe. Two members of your team who seem to be less affected by the gas are using crowbars 
to try to pry open another door looking structure. You look around the hall and notice a mask on the wall smiling at you. You believe it is out of place in 
the hall, but don't know if you are hallucinating or not. 
""")
                    player1 = input("Should you [h]elp your team or [i]nvestigate the mask? (h/i)")
                    if player1 == "i" or player1 == "I":
                        print("""As you feel around the back of the mask, your hand trips a lever that opens a trap door. Overtaken by relief, you stubble 
through, and the rest of your team follows you. There is a long path to follow. After two hours, the effects of the gas wear off. A spotter ahead sees the opening 
of the cavern a relays back. Upon arriving at the opening, you are astounded! You've done it!!! You have led the expedition to discover the greatest treasure known 
to man. 
""")
                        restart = input("Play Again? (y/n)")
                        if restart == "y" or restart == "Y":
                            print("Starting New Game!")
                            game()
                        elif restart == "n" or restart == "N":
                            sys.exit(0)
                    elif player1 == "h" or player1 == "H":
                        print("""The door never budges. The walls close in faster, and the gas begins to take over. Everyone passes out or is crushed by the walls.
Your expedition has failed. Your crew is lost.
                                    GAME OVER!!!
""")
                        restart = input("Play Again? (y/n)")
                        if restart == "y" or restart == "Y":
                            print("Starting New Game!")
                            game()
                        elif restart == "n" or restart == "N":
                            sys.exit(0)
                elif player1 == "c" or player1 == "C":
                    print("""After walking through the third door, your entire team is encased in what looks like a transparent egg. This "egg" transports you above.
several perils where you notice the area littered with the bones of failed explorers. After passing over and through what seem like impossible obstacles, the egg gently
sets down in the middle of a beautiful field. Are rush of emotions takes over as your eyes see it! You've done it!!! You have led the expedition to discover the greatest treasure known 
to man. 
""""")
                    restart = input("Play Again? (y/n)")
                    if restart == "y" or restart == "Y":
                        print("Starting New Game!")
                        game()
                    elif restart == "n" or restart == "N":
                        sys.exit(0)     
            elif player1 == "c" or player1 == "C":
                print("""As the team moves on towards the watering hole, someone notices bear dropping and partially eaten fish. Half the team 
is not affected by the possibility of predators, but the other half cautions that the watering hole is a frequent roaming ground for predators. 
They suggest turning back to the cave and figuring out how it fits the treasure map. You arrive at the watering hole to absolute calm and beauty. 
There is plenty of food and shade. A small waterfall feed the gathering place. The overall atmosphere is positive and inviting. 
""")
                player1 = input("Will you [s]tay and relax at the watering hole or [r]eturn to the cave? (s/r)")
                if player1 == "s" or player1 == "S":
                    print("""
While relaxing and frolicking at the watering hole, your expedition is attacked by three black bears. The bears were inside the cave and followed 
your team to the watering hole. Angry and hungry, each bear lashed out at the crew, destroying your supplies and killing several 
of your team. Your expedition has been cancelled, and the ship has been called back to rescue the remaining survivors.
                                            GAME OVER!!!
""")
                    restart = input("Play Again? (y/n)")
                    if restart == "y" or restart == "Y":
                        print("Starting New Game!")
                        game()
                    elif restart == "n" or restart == "N":
                        sys.exit(0)
                elif player1 == "r" or player1 == "R":
                    print("""It was wise to decide to return to the cave. Soon after leaving, several large wild cats began hunging small rodents 
drinking at the hole. With a sense of urgency since seeing the wild cats, the team picks up speed back towards the cave. Left with the original 
two options.          
""")
                    player1 = input("Will you [e]xplore the cave or set a [t]rap for any animals? (e/t) ")
                    if player1 == "e" or player1 == "E":
                        print("""
After headed into the cave, the coast appears to be clear. No sign of any predators. Everyone begins to unload themsleves when 
three giant black bears appear from a recess in the cave. Frightened by your presence in their cave, the bears begin to maul your 
entire expetition crew, destroying your supplies and killing several of your team. Your expedition has been cancelled, and the ship 
has been called back to rescue the remaining survivors.
                                                GAME OVER!!!
""")
                        restart = input("Play Again? (y/n)")
                        if restart == "y" or restart == "Y":
                            print("Starting New Game!")
                            game()
                        elif restart == "n" or restart == "N":
                            sys.exit(0)
                    elif player1 == "t" or player1 == "T":
                        print("""A few of your crew begin to set predator bait at the mouth of the cave while the rest of the crew trains their
weapons on the dark opening. After what seemed to be an hour wait, a large roar comes from the cave. Then shortly after three large black bears 
appear from the cave and begin to eat the bait. A few quick shots take out the trio giving the crew plenty of food and ownership over the cave. 
    
Everyone finally begins to relax and feel a sense of security after the eventful day. You however are still restless. Looking over and over the map.
you can't make why this cave seems to be a dead end on the map. You decide to visit the deeper parts of the cave, looking for any clue that could explain 
the dead end. Finally, you find a rock formation that seems to be out of place. Thinking quickly, you call for the resident puzzle master. After some 
examination, it becomes apparent that each stone fits into a pattern of small cutouts on an obscure wall a little deeper in the cave. The puzzle master 
places the stones intheir repsective slots. Suddenly, the ground shakes and three large rock doors open from the ground up. Overcome with joy, you call out
to the entire crew to get up and help decide which path to take. Before the dicussion begins, a small scroll pops out from hidden compartment and rolls to 
your feet. You pick it up and read it.
    
                            "I am box without hinges, key or lid,
                            Yet golden treasure inside is hid.
                            What am I?"
""")
                        player1 = input("""The path to treasure is the same as my identity (a/b/c) 
    a. a book
    b. the mind
    c. an egg
""")
                        if player1 == "a" or player1 == "A":
                            print("""Your crew takes the first path. As everyone enters the narrow space, the last team members notices the door abruptly 
slam closed behind them. Suddenly, one wall of the narrow passage opens up to the blinding light of what seemed to be a small sun. Immediately, the 
entire crew in incenerated, and their shadows etched into the walls like ancient cave paiting. Your crew is lost. Your expedition has failed.
                                    GAME OVER!!!
""")
                            restart = input("Play Again? (y/n)")
                            if restart == "y" or restart == "Y":
                                print("Starting New Game!")
                                game()
                            elif restart == "n" or restart == "N":
                                sys.exit(0)
                        elif player1 == "b" or player1 == "B":
                            print("""Taking the second path, everyone piles into a narrow hall like structure that opens up into a great hall. The sight of
the great hall send a jolt of energy through everyone. With the quickness that elation was blasted away as the wall of the great hall begin to close in 
on themselves and the chamber rapidly fills with a strange gas. As the team breathes in more of the gas, panic, joy, laughter, fear, and a host of other 
emotions take over as everyone has heavy psychedelic trips. Realizing that the answer you the crew chose was the mind, you desparately try to regain control
and break the trip as the wall close in. You slap yourself to no availe. Two members of your team who seem to be less affected by the gas are using crowbars 
to try to pry open another door looking structure. You look around the hall and notice a mask on the wall smiling at you. You believe it is out of place in 
the hall, but don't know if you are hallucinating or not. 
""")
                            player1 = input("Should you [h]elp your team or [i]nvestigate the mask? (h/i)")
                            if player1 == "i" or player1 == "I":
                                print("""As you feel around the back of the mask, your hand trips a lever that opens a trap door. Overtaken by relief, you stubble 
through, and the rest of your team follows you. There is a long path to follow. After two hours, the effects of the gas wear off. A spotter ahead sees the opening 
of the cavern a relays back. Upon arriving at the opening, you are astounded! You've done it!!! You have led the expedition to discover the greatest treasure known 
to man. 
""")
                                restart = input("Play Again? (y/n)")
                                if restart == "y" or restart == "Y":
                                    print("Starting New Game!")
                                    game()
                                elif restart == "n" or restart == "N":
                                    sys.exit(0)
                            elif player1 == "h" or player1 == "H":
                                print("""The door never budges. The walls close in faster, and the gas begins to take over. Everyone passes out or is crushed by the walls.
Your expedition has failed. Your crew is lost.
                                    GAME OVER!!!
""")
                                restart = input("Play Again? (y/n)")
                                if restart == "y" or restart == "Y":
                                    print("Starting New Game!")
                                    game()
                                elif restart == "n" or restart == "N":
                                    sys.exit(0)
                elif player1 == "c" or player1 == "C":
                    print("""After walking through the third door, your entire team is encased in what looks like a transparent egg. This "egg" transports you above.
several perils where you notice the area littered with the bones of failed explorers. After passing over and through what seem like impossible obstacles, the egg gently
sets down in the middle of a beautiful field. Are rush of emotions takes over as your eyes see it! You've done it!!! You have led the expedition to discover the greatest treasure known 
to man. 
""""")
                    restart = input("Play Again? (y/n)")
                    if restart == "y" or restart == "Y":
                        print("Starting New Game!")
                        game()
                    elif restart == "n" or restart == "N":
                        sys.exit(0)                        
                    
    elif player1 == "n" or player1 == "N":
        player1 = input("Are you sure you want to abandon the quest to find the greatest lost treasure man has known? (y/n)")
        if player1 == "n" or player1 == "N":
                print("""You have landed on treasure island. Your group is deciding whether to make camp on the beach or scout the
area for food, water, and predators.\n""")
                player1 = input("""As the expedition leader, you get to make the final decision. What will you do? 
[C]amp or [S]cout the area. (c/s)
    """)
                if player1 == "c" or player1 == "C":
                    print("""
Your camp is attacked by a bank of Komodo Dragons, destroying your supplies and killing several of your team. 
Your expedition has been cancelled, and the ship has been called back to rescue the remaining survivors.
                                                GAME OVER!!!
""")
                    restart = input("Play Again? (y/n)")
                    if restart == "y" or restart == "Y":
                        print("Starting New Game!")
                        game()
                    elif restart == "n" or restart == "N":
                        sys.exit(0)
        
                elif player1 == "s" or player1 == "S":
                    print("""After leaving the beach area, you notice a large bank of Komodo Dragons scavenging the beach you just left. 
You're greatful to have avoided meeting them. You take a look at the treasure map and push forward into the forest. 
After following the trail for a few hours, one of your spotters finds a cave that resembles the drawing on the map. You want 
to explore the cave, but a faint grumbling gives you the small idea that there might be something waiting in the cave.
Another spotter finds a watering hole just past the cave. She says that there are no animals there and plenty of water. 
You now have to choose.             
""")
                    player1 = input("Will you [e]xplore the cave, set a [t]rap for any animal that may be lingering in the cave, or [c]ontinue\nto the watering hole? (e/t/c)")
                    if player1 == "e" or player1 == "E":
                        print("""
    After headed into the cave, the coast appears to be clear. No sign of any predators. Everyone begins to unload themsleves when 
    three giant black bears appear from a recess in the cave. Frightened by your presence in their cave, the bears begin to maul your 
    entire expetition crew, destroying your supplies and killing several of your team. Your expedition has been cancelled, and the ship 
    has been called back to rescue the remaining survivors.
                                            GAME OVER!!!
    """)
                        restart = input("Play Again? (y/n)")
                        if restart == "y" or restart == "Y":
                            print("Starting New Game!")
                            game()
                        elif restart == "n" or restart == "N":
                            sys.exit(0)
      
                    elif player1 == "t" or player1 == "T":
                        print("""A few of your crew begin to set predator bait at the mouth of the cave while the rest of the crew trains their
weapons on the dark opening. After what seemed to be an hour wait, a large roar comes from the cave. Then shortly after three large black bears 
appear from the cave and begin to eat the bait. A few quick shots take out the trio giving the crew plenty of food and ownership over the cave. 
        
Everyone finally begins to relax and feel a sense of security after the eventful day. You however are still restless. Looking over and over the map.
you can't make why this cave seems to be a dead end on the map. You decide to visit the deeper parts of the cave, looking for any clue that could explain 
the dead end. Finally, you find a rock formation that seems to be out of place. Thinking quickly, you call for the resident puzzle master. After some 
examination, it becomes apparent that each stone fits into a pattern of small cutouts on an obscure wall a little deeper in the cave. The puzzle master 
places the stones intheir repsective slots. Suddenly, the ground shakes and three large rock doors open from the ground up. Overcome with joy, you call out
to the entire crew to get up and help decide which path to take. Before the dicussion begins, a small scroll pops out from hidden compartment and rolls to 
your feet. You pick it up and read it.
        
                                "I am box without hinges, key or lid,
                                Yet golden treasure inside is hid.
                                What am I?"
        """)
                        player1 = input("""The path to treasure is the same as my identity (a/b/c) 
            a. a book
            b. the mind
            c. an egg
""")
                        if player1 == "a" or player1 == "A":
                            print("""Your crew takes the first path. As everyone enters the narrow space, the last team members notices the door abruptly 
slam closed behind them. Suddenly, one wall of the narrow passage opens up to the blinding light of what seemed to be a small sun. Immediately, the 
entire crew in incenerated, and their shadows etched into the walls like ancient cave paiting. Your crew is lost. Your expedition has failed.
                                            GAME OVER!!!
        """)
                            restart = input("Play Again? (y/n)")
                            if restart == "y" or restart == "Y":
                                print("Starting New Game!")
                                game()
                            elif restart == "n" or restart == "N":
                                sys.exit(0)
                        elif player1 == "b" or player1 == "B":
                            print("""Taking the second path, everyone piles into a narrow hall like structure that opens up into a great hall. The sight of
the great hall send a jolt of energy through everyone. With the quickness that elation was blasted away as the wall of the great hall begin to close in 
on themselves and the chamber rapidly fills with a strange gas. As the team breathes in more of the gas, panic, joy, laughter, fear, and a host of other 
emotions take over as everyone has heavy psychedelic trips. Realizing that the answer you the crew chose was the mind, you desparately try to regain control
and break the trip as the wall close in. You slap yourself to no availe. Two members of your team who seem to be less affected by the gas are using crowbars 
to try to pry open another door looking structure. You look around the hall and notice a mask on the wall smiling at you. You believe it is out of place in 
the hall, but don't know if you are hallucinating or not. 
""")
                            player1 = input("Should you [h]elp your team or [i]nvestigate the mask? (h/i)")
                            if player1 == "i" or player1 == "I":
                                print("""As you feel around the back of the mask, your hand trips a lever that opens a trap door. Overtaken by relief, you stubble 
through, and the rest of your team follows you. There is a long path to follow. After two hours, the effects of the gas wear off. A spotter ahead sees the opening 
of the cavern a relays back. Upon arriving at the opening, you are astounded! You've done it!!! You have led the expedition to discover the greatest treasure known 
to man. 
""")
                                restart = input("Play Again? (y/n)")
                                if restart == "y" or restart == "Y":
                                    print("Starting New Game!")
                                    game()
                                elif restart == "n" or restart == "N":
                                    sys.exit(0)
                            elif player1 == "h" or player1 == "H":
                                print("""The door never budges. The walls close in faster, and the gas begins to take over. Everyone passes out or is crushed by the walls.
Your expedition has failed. Your crew is lost.
                                            GAME OVER!!!
        """)
                                restart = input("Play Again? (y/n)")
                                if restart == "y" or restart == "Y":
                                    print("Starting New Game!")
                                    game()
                                elif restart == "n" or restart == "N":
                                    sys.exit(0)
                        elif player1 == "c" or player1 == "C":
                            print("""After walking through the third door, your entire team is encased in what looks like a transparent egg. This "egg" transports you above.
several perils where you notice the area littered with the bones of failed explorers. After passing over and through what seem like impossible obstacles, the egg gently
sets down in the middle of a beautiful field. Are rush of emotions takes over as your eyes see it! You've done it!!! You have led the expedition to discover the greatest treasure known 
to man. 
""""")
                            restart = input("Play Again? (y/n)")
                            if restart == "y" or restart == "Y":
                                print("Starting New Game!")
                                game()
                            elif restart == "n" or restart == "N":
                                sys.exit(0)    
                                 
                    elif player1 == "c" or player1 == "C":
                        print("""As the team moves on towards the watering hole, someone notices bear dropping and partially eaten fish. Half the team 
is not affected by the possibility of predators, but the other half cautions that the watering hole is a frequent roaming ground for predators. 
They suggest turning back to the cave and figuring out how it fits the treasure map. You arrive at the watering hole to absolute calm and beauty. 
There is plenty of food and shade. A small waterfall feed the gathering place. The overall atmosphere is positive and inviting. 
""")
                        player1 = input("Will you [s]tay and relax at the watering hole or [r]eturn to the cave? (s/r)")
                        if player1 == "s" or player1 == "S":
                            print("""
While relaxing and frolicking at the watering hole, your expedition is attacked by three black bears. The bears were inside the cave and followed 
your team to the watering hole. Angry and hungry, each bear lashed out at the crew, destroying your supplies and killing several 
of your team. Your expedition has been cancelled, and the ship has been called back to rescue the remaining survivors.
                                                    GAME OVER!!!
""")
                            restart = input("Play Again? (y/n)")
                            if restart == "y" or restart == "Y":
                                print("Starting New Game!")
                                game()
                            elif restart == "n" or restart == "N":
                                sys.exit(0)
                        elif player1 == "r" or player1 == "R":
                            print("""It was wise to decide to return to the cave. Soon after leaving, several large wild cats began hunging small rodents 
drinking at the hole. With a sense of urgency since seeing the wild cats, the team picks up speed back towards the cave. Left with the original 
two options.          
""")
                            player1 = input("Will you [e]xplore the cave or set a [t]rap for any animals? (e/t) ")
                            if player1 == "e" or player1 == "E":
                                print("""
After headed into the cave, the coast appears to be clear. No sign of any predators. Everyone begins to unload themsleves when 
three giant black bears appear from a recess in the cave. Frightened by your presence in their cave, the bears begin to maul your 
entire expetition crew, destroying your supplies and killing several of your team. Your expedition has been cancelled, and the ship 
has been called back to rescue the remaining survivors.
                                                        GAME OVER!!!
""")
                                restart = input("Play Again? (y/n)")
                                if restart == "y" or restart == "Y":
                                    print("Starting New Game!")
                                    game()
                                elif restart == "n" or restart == "N":
                                    sys.exit(0)
                            elif player1 == "t" or player1 == "T":
                                print("""A few of your crew begin to set predator bait at the mouth of the cave while the rest of the crew trains their
weapons on the dark opening. After what seemed to be an hour wait, a large roar comes from the cave. Then shortly after three large black bears 
appear from the cave and begin to eat the bait. A few quick shots take out the trio giving the crew plenty of food and ownership over the cave. 
            
Everyone finally begins to relax and feel a sense of security after the eventful day. You however are still restless. Looking over and over the map.
you can't make why this cave seems to be a dead end on the map. You decide to visit the deeper parts of the cave, looking for any clue that could explain 
the dead end. Finally, you find a rock formation that seems to be out of place. Thinking quickly, you call for the resident puzzle master. After some 
examination, it becomes apparent that each stone fits into a pattern of small cutouts on an obscure wall a little deeper in the cave. The puzzle master 
places the stones intheir repsective slots. Suddenly, the ground shakes and three large rock doors open from the ground up. Overcome with joy, you call out
to the entire crew to get up and help decide which path to take. Before the dicussion begins, a small scroll pops out from hidden compartment and rolls to 
your feet. You pick it up and read it.
            
                                    "I am box without hinges, key or lid,
                                    Yet golden treasure inside is hid.
                                    What am I?"
""")
                                player1 = input("""The path to treasure is the same as my identity (a/b/c) 
    a. a book
    b. the mind
    c. an egg
""")
                                if player1 == "a" or player1 == "A":
                                    print("""Your crew takes the first path. As everyone enters the narrow space, the last team members notices the door abruptly 
slam closed behind them. Suddenly, one wall of the narrow passage opens up to the blinding light of what seemed to be a small sun. Immediately, the 
entire crew in incenerated, and their shadows etched into the walls like ancient cave paiting. Your crew is lost. Your expedition has failed.
                                            GAME OVER!!!
""")
                                    restart = input("Play Again? (y/n)")
                                    if restart == "y" or restart == "Y":
                                        print("Starting New Game!")
                                        game()
                                    elif restart == "n" or restart == "N":
                                        sys.exit(0)
                                elif player1 == "b" or player1 == "B":
                                    print("""Taking the second path, everyone piles into a narrow hall like structure that opens up into a great hall. The sight of
the great hall send a jolt of energy through everyone. With the quickness that elation was blasted away as the wall of the great hall begin to close in 
on themselves and the chamber rapidly fills with a strange gas. As the team breathes in more of the gas, panic, joy, laughter, fear, and a host of other 
emotions take over as everyone has heavy psychedelic trips. Realizing that the answer you the crew chose was the mind, you desparately try to regain control
and break the trip as the wall close in. You slap yourself to no availe. Two members of your team who seem to be less affected by the gas are using crowbars 
to try to pry open another door looking structure. You look around the hall and notice a mask on the wall smiling at you. You believe it is out of place in 
the hall, but don't know if you are hallucinating or not. 
""")
                                    player1 = input("Should you [h]elp your team or [i]nvestigate the mask? (h/i)")
                                    if player1 == "i" or player1 == "I":
                                        print("""As you feel around the back of the mask, your hand trips a lever that opens a trap door. Overtaken by relief, you stubble 
through, and the rest of your team follows you. There is a long path to follow. After two hours, the effects of the gas wear off. A spotter ahead sees the opening 
of the cavern a relays back. Upon arriving at the opening, you are astounded! You've done it!!! You have led the expedition to discover the greatest treasure known 
to man. 
""")
                                        restart = input("Play Again? (y/n)")
                                        if restart == "y" or restart == "Y":
                                            print("Starting New Game!")
                                            game()
                                        elif restart == "n" or restart == "N":
                                            sys.exit(0)
                                    elif player1 == "h" or player1 == "H":
                                        print("""The door never budges. The walls close in faster, and the gas begins to take over. Everyone passes out or is crushed by the walls.
Your expedition has failed. Your crew is lost.
                                            GAME OVER!!!
""")
                                        restart = input("Play Again? (y/n)")
                                        if restart == "y" or restart == "Y":
                                            print("Starting New Game!")
                                            game()
                                        elif restart == "n" or restart == "N":
                                            sys.exit(0)
                        elif player1 == "c" or player1 == "C":
                            print("""After walking through the third door, your entire team is encased in what looks like a transparent egg. This "egg" transports you above.
several perils where you notice the area littered with the bones of failed explorers. After passing over and through what seem like impossible obstacles, the egg gently
sets down in the middle of a beautiful field. Are rush of emotions takes over as your eyes see it! You've done it!!! You have led the expedition to discover the greatest treasure known 
to man. 
""")
                            restart = input("Play Again? (y/n)")
                            if restart == "y" or restart == "Y":
                                print("Starting New Game!")
                                game()
                            elif restart == "n" or restart == "N":
                                sys.exit(0)                        

        elif player1 == "y" or player1 == "Y":
            print("""As long as the treasure remains lost, you will be welcomed to join the quest. See you soon.""")
            
            
game()
