import random
import time
from enemy import A, B, C
from maze_generator import MazeGenerator, print_maze, move_player
from dialogues import Dialogues

player_stats = {'health': 100, 'attack': 10, 'defense': 5}

def karate_chop(enemy):
    damage = player_stats['attack'] + random.randint(1, 5)
    enemy.take_damage(damage)
    print(f"You used Karate Chop and dealt {damage} damage!")


def run_away():
    print("You ran away from the enemy.")
    return True  # Indicate that the player successfully ran away


def print_enemy_stats(enemy):
    if enemy.health > 0:
        print(f"Enemy Stats - Health: {enemy.health}, Attack: {enemy.attack}, Defense: {enemy.defense}")



def handle_enemy_encounter():
    enemy_type = random.choice([A(), B(), C()])
    Dialogues.enemy_encounter()

    print(f"You encountered {enemy_type.name}!")
    print_enemy_stats(enemy_type)

    while enemy_type.is_alive() and player_stats['health'] > 0:
        print(f"Your Health: {player_stats['health']}")
        print(f"{enemy_type.name}'s Health: {enemy_type.health}")
        print("Choose your move:")
        print("1. Attack")
        print("2. Karate Chop")
        print("3. Run Away")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            player_attack = max(0, player_stats['attack'] + random.randint(-2, 2))
            enemy_type.take_damage(player_attack)
            print(f"You attacked and dealt {player_attack} damage to {enemy_type.name}!")

        elif choice == "2":
            karate_chop(enemy_type)
        elif choice == "3":
            if run_away():
                break
        else:
            print("Invalid choice. You hesitated and the enemy took advantage!")
            enemy_attack = max(0, enemy_type.attack + random.randint(-2, 2))
            player_stats['health'] -= max(0, enemy_attack - player_stats['defense'])
            print(f"{enemy_type.name} attacked and dealt {enemy_attack} damage!")

        print_enemy_stats(enemy_type)  # Display enemy stats after the player's move

        if enemy_type.is_alive():
            enemy_attack = max(0, enemy_type.attack + random.randint(-2, 2))
            player_stats['health'] -= max(0, enemy_attack - player_stats['defense'])
            print(f"{enemy_type.name} attacked and dealt {enemy_attack} damage!")

    if player_stats['health'] <= 0:
        print("You were defeated. Game over.")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        return play_again == "yes"

    # Check if the enemy's health reached 0
    if not enemy_type.is_alive():
        print(f"You defeated {enemy_type.name}! The enemy is dead.")

    return True

def print_ending_dialogue():
    print("Congratulations! You reached the exit!")
    print("Thank you for playing. Exiting the game...")


def main():
    maze_size = 9

    # Opening dialogue
    Dialogues.start_menu()
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        print("Starting the game...")
        time.sleep(1)
        player_name = input("Enter your name: ")
        time.sleep(1)
        print(f"""\nWith your passion for the legend of the keyboard, you venture to the desert to acquire the lost remaining symbol relics that will complete the keyboard. The symbols !,$,&,* and ~.

Your companion, Jebrael, helped you to get to the location because only you {player_name} were the last person in your bloodline who has the capabilities to take hold of them and place them to the right location.

On the last leg, you finally acquire the “~” symbol. However the whole place started shaking.
""")
        time.sleep(5)
    elif choice == "2":
        Dialogues.credits()
        return
    elif choice == "3":
        print("Exiting the game...")
        return
    else:
        print("Invalid choice. Exiting the game...")
        return

    while True:
        maze_generator = MazeGenerator(maze_size, maze_size)
        maze_generator.generate_maze()
        current_position = maze_generator.get_start_position()
        checkpoint_positions = maze_generator.get_checkpoint_positions()
        player_stats = {'health': 100, 'attack': 10, 'defense': 5}

        while True:
            print_maze(current_position, maze_generator.get_maze())

            # Check if the current position is a checkpoint with the value 3
            if maze_generator.get_maze()[current_position[0]][current_position[1]] == 3:
                 Dialogues.checkpoint_reached()

            move = input("Enter move (W/A/S/D): ").lower()
            if move in {'w', 'a', 's', 'd'}:
                current_position = move_player(current_position, move, maze_generator.get_maze())

                # Check if the player reached a checkpoint
                if current_position in checkpoint_positions:
                    Dialogues.checkpoint_reached()

                # Check for a random enemy encounter
                if random.random() < 0.4:
                    if not handle_enemy_encounter():
                        continue  # If the player failed to run away, continue the loop

            else:
                print("Invalid move! Use W/A/S/D.")
                continue

            if maze_generator.get_maze()[current_position[0]][current_position[1]] == 1:
                print("Invalid move! You cannot move through walls.")
                continue

            if current_position == (maze_size - 1, maze_size - 1):
                print_ending_dialogue()
                return  # Exit the game when the player reaches the exit


if __name__ == "__main__":
    main()

def dialogue_7():
        print("""\nYou defeated the enemy, however, on the corner of your eyes, you see Jebreal, stiff, cold…and lifeless

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
