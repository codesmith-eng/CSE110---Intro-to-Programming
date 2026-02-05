# Text Adventure game
# all the towns in the game are all nested if statements
# i welcome the player
print(' Hey! Hello Welcome to this Text Adventure Game')
# i used print('\n') and print() to create space in this program
print('\n')
# this is the narration
print('NARRATION: You are on a journey to find the stolen crown that will restore peace, joy and stability in the town of SHEKINAH and the crown has been stolen and kept in the treasure house of one of these 3 towns, KEDRACH, PATHOS and OREGON. The first town KEDRACH are mainly drunkards, while the second town PATHOS are religious people, and the third town OREGON is full of cunning people. You are to choose any of the town and that will lead you to where the crown is, lets go.')   


print('\n')

# i informed the player the options he is to type
print ('NOTE: Only the option you are to type in the game are in CAPITAL LETTERS.')

print('\n')    

# i prompt the user to enter the town they wanted to go and search for the crown    
town = input('You get to the road that leads to the three town, which town did you want to head to:  ')


print('\n')

# the nested if for kedrach town
if town.lower() == 'kedrach':
    gate_kedrach = input('You entered into the town gate and you saw men that are drinking wines and they are enticing you to DRINK with them.You are to neither drink with them or ask for the direction to the treasure house or go your own way seeking for the treasure house yourself, what is your choice? DRINK WITH THEM or ASK FOR DIRECTION or GO MY WAY?    ') 
    
    if gate_kedrach.lower() == 'drink with them':
        drink_town = input('You sat down and drank with them to till you slept off and wake the next day, you are to neither continue drinking or go back home or continue your journey, what is your choice? CONTINUE DRINKING or GO BACK HOME or CONTINUE YOUR JOURNEY?  ') 
 
        if drink_town.lower() == 'continue drinking': 
            print('You drank to stupor again and from there you become a drunkard forgetting your mission. GAME OVER')
        elif drink_town.lower() == 'go back home':
           print('You went back home without fulfilling your mission. GAME OVER')
        elif drink_town.lower() == 'continue your journey':
           print('You continue your journey but you lost your way and couldnt get the crown. MISSION FAILED. GAME OVER')
        else:
            print('You type the wrong word, please restart the game and enter the right word')


    elif gate_kedrach.lower() == 'ask for direction':
        ask_town = input('You ask the drunkards to show you the way to the treasure house, one of them invited you to drink with them, another one told you to go northeast saying that is where the treasure house is, and another one told you to go home. what is your choice? DRINK WITH THEM or GO NORTHEAST or GO HOME?  ')
        if ask_town.lower() == 'drink with them':
            print('You drink with them to stupor and you slept off and woke up the next day stripped naked. You could not continue your journey and you went home ashamed. MISSION FAILED. GAME OVER')
        elif ask_town.lower() == 'go northeast':
            print('You go northeast searching for the treasure house, you got tired, thirsty, hungry and you died. MISSION FAILED. GAME OVER')
        elif ask_town.lower() == 'go home':
            print('You went home without achieving your aim. MISSON FAILED. GAME OVER')
        else:
            print('You type the wrong word, please restart the game and enter the right word')
   
                        
    elif gate_kedrach.lower() == 'go my way':
        go_town = input('You brought out a map and on the map you see that there are two roads to the treasure house, the northeast or southeast road, which path did you want to follow, GO NORTHEAST or GO SOUTHEAST or GO HOME?' )
        if go_town.lower() == 'go northeast':
            print('You followed the map and arrived in kedrach treasure house but you could not find it there. MISSION FAILED.  GAME OVER')
        elif go_town.lower() == 'go southeast':
            print('You went southeast but the journey was too long for you, you died on the way. MISSION FAILED. GAME OVER')
        elif go_town.lower() == 'go home':
            print('You followed the map and went back home without achieving your aim. MISSION FAILED. GAME OVER')
        else:
            print('You type the wrong word, please restart the game and enter the right word')
    else:
        print('You type the wrong word, please restart the game and enter the right word')
        
        
# the nested if for pathos town
elif town.lower() == 'pathos':
    gate_pathos = input('You entered into town gate and you saw gentle and quiet people starring at you and you wandered, can this people stole the crown. You are to either wait in the town for some days to find out some information or ask for direction to the treasure house or go your own way seeking for the treasure house yourself, what is your choice? ASK FOR DIRECTION or GO YOUR WAY or WAIT IN THE TOWN?  ')

    if gate_pathos.lower() == 'ask for direction':
        pathos_town = input('You entered into the town and you walk to some gentle looking men and ask for the direction to the treasure house and he told you to go southward, another one is telling you about there religion, you are to go southward or exit the town gate since you are doubting if they could be the thief or wait and listen to  the man telling you about there religion. what is your choice? GO SOUTHWARDS or LISTEN or EXIT?  ')
        if pathos_town.lower() == 'go southwards':
                print('You go southwards and discoverd the treasure house but what you found was only religious books, and not the crown. MISSION FAILED. GAME OVER')
        elif pathos_town.lower() == 'listen':
            print('You listen to the religious preaching and you became converted to there religion and you forget your mission. MISSION FAILED. GAME OVER')
        elif pathos_town.lower() == 'exit':
            print('You left the town and head back home doubting if they could be the thief because they are religious. MISSION ABORLISHED. GAME OVER')
        else:
            print('You type the wrong word, please restart the game and enter the right word')
        

        
    elif gate_pathos.lower() == 'go your way':
        pathos_town = input('You brought a map and you see in the map that there are three channels that leads to the treasure house, the first channel pass through the temple the second one goes through the king palace and the third one you have to swim across the town river what is your choice? PASS THROUGH THE TEMPLE or PASS THROUGH THE KING PALACE or SWIM ACROSS THE RIVER?  ')
        if pathos_town.lower() == 'pass through the temple':
            print('You pass through the temple and you are caught  by the temple guards. MISSION FAILED. GAME OVER')
        elif pathos_town.lower() == 'pass through the king palace':
            print('You pass through the king palace and you are caught by the palace guards. MISSION FAILED. GAME OVER')
        elif pathos_town.lower() == 'swim across the river':
            print('You jump into pathos river and you got drown. MISSION FAILED. GAME OVER')
        else:
            print('You type the wrong word, please restart the game and enter the right word')
    
        
    elif gate_pathos.lower() == 'wait in the town':
        pathos_town = input('You meet one of the town men and you ask for help on where to stay for some days, and he told you there are only 3 places you can stay, his house or the kings visitors place or the inn.  What is your choice, HIS HOUSE or THE KINGS VISITORS PLACE or THE INN?  ')
        if pathos_town.lower() == 'his house':
            print('You followed him to his house and you got all the information you need but you later find out the crown is not in pathos. You  left for home dissappointed. MISSION FAILED. GAME OVER')
        elif pathos_town.lower() == 'the kings visitors place':
            print('You went to kings visitors place and you stayed there for days and later find out the crown is not in pathos. You left for home dissappointed. MISSION FAILED. GAME OVER')
        elif pathos_town.lower() == 'the inn':
            print('You stayed in the inn for days and later find out the crown is not in pathos. You left for home dissappointed. MISSON FAILED. GAME OVER')
        else:
            print('You type the wrong word, please restart the game and enter the right word')
    else:
        print('You type the wrong word, please restart the game and enter the right word')
        
        
# the nested if for town oregon
elif town.lower() == 'oregon':
    gate_oregon = input('You entered into town gate and you see men smilling and laughing at you mockingly. A brothel on the left and half naked women enticing you to come and take a relax from your long journey. You are to either enter the brothel or ask for the direction to the treasure house or go your own way seeking for the treasure house yourself, what is your choice? ENTER THE BROTHEL or ASK FOR DIRECTION or GO MY WAY? ')
    
    if gate_oregon.lower() == 'enter the brothel':
        town_oregon = input('You enter the brothel to relax and you slept with two prostitute, you slept off and you spent two days there. You are to neither  SPEND MORE DAYS RELAXING or COME OUT OF THE BROTHEL or LIVE IN THE BROTHEL?    ')
        if town_oregon.lower() == 'spend more days relaxing':
            print('You spent days in the brothel enjoying and having fun with the prostitutes and you later abandoned your mission. MISSON FAILED. GAME OVER')
        elif town_oregon.lower() == 'come out of the brothel':
            print('You came out of the brothel but you are mislead by one the prostitute who gave you a wrong direction that leads to your doom. MISSION FAILED. GAME OVER')
        elif town_oregon.lower() == 'live in the brothel':
            print('You abandoned your mission and choose to live with prostitute because of sex. MISSION FAILED. GAME OVER')
        else:
            print('You type the wrong word, please restart the game and enter the right word')
        
        
    elif gate_oregon.lower() == 'ask for direction':
        town_oregon = input('You ask one of the town men the road to the treasure house and he answered you cunningly, he said there are three ways to the treasure house, the first way is to use your wisdom to navigate to the place or ask as you go on the town main road or you should stay with him for two days and after two days he is also going there and he will take you along, what is your choice, USE MY WISDOM or ASK I GO or STAY WITH HIM?   ')
        if town_oregon.lower() == 'use my wisdom':
            print('You use your wisdom to navigate the treasure house but you failed to get to there. You got tired, hungry and thirsty and died. MISSION FAILED. GAME OVER')
        elif town_oregon.lower() == 'ask i go':
            print('You were asking as you go, people gave you the right direction. You even met one of shekinah men in oregon who told you the crown is in oregon treasure house and how you can get it. You get to the treasure house, you get the crown, and you headed home. MISSION ACCOMPLISHED.')
            
        elif town_oregon.lower() == 'stay with him':
            print('You stayed with him, he locked you up, starved you till you died. MISSION FAILED. GAME OVER')
        else:
            print('You type the wrong word, please restart the game and enter the right word')
        
    elif gate_oregon.lower() == 'go my way':
        town_oregon = input('You brought a map and you see that three treasure house are in the town of oregon, the first treasure house is named the main treasure house, the second one is named eastern treasure the third one is named western treasure, which one will you go to, THE MAIN TREASURE or WESTERN TREASURE or EASTERN TREASURE?  ')
        if town_oregon.lower() == 'the main treasure':
            print('You followed the map to the main treasure but you could not find the crown there. MISSION FAILED. GAME OVER')
        elif town_oregon.lower() == 'western treasure':
            print('You followed the map to the western treasure, but when you get there you discover that it was an old abandoned treasure house. the crown is not there. MISSION FAILED. GAME OVER')
        elif town_oregon.lower() == 'eastern treasure':
            print('You followed the map to the eastern treasure, but when you get there you discover that it was an old abandoned treasure house. the crown is not there. MISSION FAILED. GAME OVER')
        else: 
            print('You type the wrong word, please restart the game and enter the right word')
    else:
        print('You type the wrong word, please restart the game and enter the right word')
else:
    print('You type the wrong word, please restart the game and enter the right word')









