# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!IMPORTANT!!!!!!!!!!! !!!!!!!!!!MUST READ BEFORE PLAYING THE GAME!!!!!!!!!!!!!!!!!!!!
# This is under development so don't expect much 
# At night, monsters might come out (you don't want to be out in the dark)
# Use your coins wisely.
# If you dodge an attack, you take damage based off of your flexibility (which is less than what you would take if you defended), but you get stunned. If you get stunned, you cannot attack the monster the next round.
# Hunger is serious. If you get too hungry, you could pass out and die. So, it is smart to eat if you are hungry.
# Strength determines how much damage you do in combat
# Defense determines how much defense you are capable of.
# Intelligence determines what you would do under certain circumstances:
# Ex. William has 10 intelligence. Jake has 70 intelligence. If both of them see guards, for example, William might just walk without care, but Jake might try avoiding them.
# Also, your characters powers(ex. Jack has lightning powers) will start unlocking as the story goes on.


character = input("Select your character: Jack, Emily, Michael, Sarah ")

if character == 'Jack':
    print("Stats:\nStrength:30\nDefense:25\nFlexibility:20\nIntelligence:80")
    question = input("Are you sure you want to select Jack? ")
    if question == 'Yes' or 'yes' or 'y' or 'Y':
        from Jack import Jack
    else: 
        print("Restart the console to play again")
elif character == 'Emily':
    print("Stats:\nStrength:15\nDefense:40\nFlexibility:60\nIntelligence:80")
    question = input("Are you sure you want to select Emily? ")
    if question == 'Yes' or 'yes' or 'y' or 'Y':
        from Emily import Emily 
    else: 
        print("Restart the console to play again")
elif character == 'Michael':
    print("Stats:\nStrength:70\nDefense:40\nFlexibility:10\nIntelligence:30")
    question = input("Are you sure you want to select Michael")
    if question == "Yes" or 'yes' or 'y' or 'Y':
        pass
    else: 
        print("Restart the console to play again")
elif character == 'Sarah':
    print("Stats:\nStrength:40\nDefense:70\nFlexibility:85\nIntelligence:20")
    question = input("Are you sure you want to be Sarah")
    if question == "Yes" or 'yes' or 'y' or 'Y':
        pass
    else: 
        print("Restart the console to play again")
else:
    print("Character not recognized. Please select a valid character.")
    




