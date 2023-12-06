player_name = ""

def get_player_name():
        player_name = input("Enter your name: ")
        return player_name

class Dialogues:
    @staticmethod
    def start_menu():
        print("""
888    d8P                    888                                     888       888       888                          d8b                  
888   d8P                     888                                     888       888   o   888                          Y8P                  
888  d8P                      888                                     888       888  d8b  888                                               
888d88K      .d88b.  888  888 88888b.   .d88b.   8888b.  888d888  .d88888       888 d888b 888  8888b.  888d888 888d888 888  .d88b.  888d888 
8888888b    d8P  Y8b 888  888 888 "88b d88""88b     "88b 888P"   d88" 888       888d88888b888     "88b 888P"   888P"   888 d88""88b 888P"   
888  Y88b   88888888 888  888 888  888 888  888 .d888888 888     888  888       88888P Y88888 .d888888 888     888     888 888  888 888     
888   Y88b  Y8b.     Y88b 888 888 d88P Y88..88P 888  888 888     Y88b 888       8888P   Y8888 888  888 888     888     888 Y88..88P 888     
888    Y88b  "Y8888   "Y88888 88888P"   "Y88P"  "Y888888 888      "Y88888       888P     Y888 "Y888888 888     888     888  "Y88P"  888     
                          888                                                                                                               
                     Y8b d88P                                                                                                               
                      "Y88P"                                                                                                                                                                                                                             
""")
        print("1. Start")
        print("2. Credits")
        print("3. Exit")

    @staticmethod
    def player_stats(player_stats):
        print("Player Stats:")
        print(f"Health: {player_stats['health']}")
        print(f"Attack: {player_stats['attack']}")
        print(f"Defense: {player_stats['defense']}")

    @staticmethod
    def enemy_stats(enemy_stats):
        print("Enemy Stats:")
        print(f"Health: {enemy_stats['health']}")
        print(f"Attack: {enemy_stats['attack']}")
        print(f"Defense: {enemy_stats['defense']}")

    @staticmethod
    def enemy_encounter():
        print("You've encountered an enemy!")

    @staticmethod
    def checkpoint_reached():
        print("You've met an old friend")
        print("""
⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆ 
⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿ 
⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀ 
⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠛⠉                                                                                                                                                                                                                     
""")

    @staticmethod
    def victory():
        print("You defeated the enemy!")

    @staticmethod
    def credits():
        print("Game created by 404 Gatekeepers")

    @staticmethod
    def dialogue_0():
        global player_name
        print(f"""\nnWith your passion for the legend of the keyboard, you venture to the desert to acquire the lost remaining symbol relics that will complete the keyboard. The symbols !,$,&,* and ~.

Your companion, Jebrael, helped you to get to the location because only you {player_name} were the last person in your bloodline who has the capabilities to take hold of them and place them to the right location.

On the last leg, you finally acquire the “~” symbol. However the whole place started shaking.
""")

    @staticmethod
    def dialogue_1():
        global player_name
        print(f"""\nJebrael: Welcome back, <player name> you passed out after collecting the relics of the keyboard symbols !,$,&,*,~. Get up, we need to get out of this place
	{player_name}: W-What happened?
	Jebrael: Oh no, perhaps this is the effect of acquiring all the symbol relics. You have to get it together! Tell me what you remember.
	{player_name}: We went to the desert to finish acquiring the letters of the keyboard.
	Jebrael: Skip to the part where we went in the underground, will ya!
	{player_name}: I don’t know! We got the 4th symbol and I don't remember how we got here! Stop shouting at me!
	Jebrael: Well we have to hurry up or we’re gonna get buried. We have the symbol relics, now we just have to defeat all enemies on our way out, come on lad!
""")
    
    @staticmethod
    def dialogue_2():
        global player_name
        print(f"""\nFrom the distance you hear someone whisper your name, telling you which way is the right way out.

	{player_name}: Here? No… Here! Let’s go here!
	Jebrael: Are you sure lad? You just woke up from passing out. Are you sure you’re not imagining things?
	{player_name}: No Just trust me. Trust me on this
""")
    
    @staticmethod
    def dialogue_3():
        print("""\nYou start feeling lightheaded, feeling the absorption of energy that helped you gain strength.

You watch as an enemy approaches and you lunge to a forceful attack

""")
        
    @staticmethod
    def dialogue_4():
        global player_name
        print(f"""\nYou start feeling lightheaded, feeling the absorption of energy that helped you gain strength.

You watch as an enemy approaches and you lunge to a forceful attack

{player_name}: The symbol strike, keyboard smash! AAAAAHHHHHHH
""")
        
    @staticmethod
    def dialogue_5():
        print("""\nYou defeated the enemy and a bright green light appears before you, floating like a fog. 

You seem to notice its behavior and that it’s trying to show you the way

You and Jabreal follow through...
""")
        
    @staticmethod
    def dialogue_6():
        global player_name
        print(f"""\nYou’re near the exit and saw the light outside of the door

As you run with the relics, you hear Jebreal let out a painful scream.

You turn around only to see him be devoured by the location’s guardian, slowly chewing him limb by limb.

Suddenly, your memories with Jebrael on the whole adventure flashes before your eyes. 

You hear him say “Run for your life {player_name}! Go without me!”

However, with no hesitation you run forward and attacked the enemy

Little by little. The relics on your possession start lighting on different colors and you feel its power being absorbed in your body
""")
    
def dialogue_7():
        global player_name
        print(f"""\nYou defeated the enemy, however, on the corner of your eyes, you see Jebreal, stiff, cold…and lifeless

You can’t help but cry, despite knowing you’ve only known each other for a short moment

You notice that he was gripping something on his bloody hand…it seemed like…a photograph?
Slowly and gently, you take it from his hands and unfold it to reveal an image

An image of a family with smiles on their faces. A familiar woman and an oh-so-familiar child playing with the keyboard relics.

Confused, you try to see if there are any other images attached, but to no avail, that was the only one.

You catch a glimpse of the back and notice a somehow long message written, surprisingly, addressed to you
              
{player_name},

I know I’ve had my share of not being there for the both of you. But I know that there is a reason why the dessert always calls me to explore. This is selfish, I know, but son. I pass down this blessing to you, in hopes that one day we get to venture the world together, discovering the world and its true beauty. I hope you can one day forgive me for leaving you and your mother. I had promised our ancestors that I would help keep and guide the relics of the keyboard. And you will one day have to reclaim them. I hope that one day you will understand everything that I did for you and your mom. I love you always.

Dad
""")
