from time import sleep
from random import choice


def opening_greetings(enemy_type):
    # displays opening message to console
    greetings = ["You find yourself standing in an open field, filled with " +
                 "grass and yellow wildflowers.",
                 f"Rumor has it that a {enemy_type} is somewhere around " +
                 "here, and has been terifying the nearby village.",
                 "In front of you is as house.",
                 "To your right is a dark cave.",
                 "In your hand you hold your trusty (but not very effective)" +
                 " dagger.\n"]
    for sentence in greetings:
        print(sentence)
        sleep(2)


def set_enemy():
    # returns a random choice of enemy type
    return choice(['dragon', 'gorgon', 'wicked fairie', 'troll'])


def get_player_input():
    # request input from player until correct value is entered
    # and returns said value
    console_msg = ["Enter 1 to knock on the door of the house.",
                   "Enter 2 to peer into the cave",
                   "What would you like to do?"]

    for sentence in console_msg:
        print(sentence)
        sleep(2)

    user_input = input("(Please enter 1 or 2.)\n")
    while user_input not in ['1', '2']:
        user_input = input("(Please enter 1 or 2.)\n")

    return user_input


def approach_house_msg(weapon_type, enemy_type):
    # displays message onto console when the player approaches house
    console_msg = ["You approach the door of the house.",
                   "You are about to knock when the door opens and out " +
                   f"steps a {enemy_type}.",
                   f"Eep! This is the {enemy_type}'s house!",
                   f"The {enemy_type} attacks you!"]
    for sentence in console_msg:
        print(sentence)
        sleep(2)
    if weapon_type == 'dagger':
        print("You feel a bit under-prepared for this, what with only a tiny" +
              " dagger.")
        sleep(2)


def get_player_fight_input():
    # returns player input related to fight response
    return input("Would you like to (1) fight or (2) run away?")


def play_again_prompt():
    # returns player input for playing the game again
    play_again = input("Would you like to play again? (y/n)")
    if play_again not in ['y', 'n']:
        play_again_prompt()
    return play_again


def process_play_again_input(player_response):
    # control function to restart or quit game
    if player_response == 'y':
        print("Excellent! Restarting the game ...")
        sleep(2)
        return True
    else:
        print("Thanks for playing. See you next time.")
        return False


def defeat(enemy):
    # displays message to console when the player is defeated
    defeat_msg = ["You do your best...",
                  f"but your dagger is no match for the {enemy}",
                  "You have been defeated!"]
    for sentence in defeat_msg:
        print(sentence)
        sleep(2)


def go_back_to_field():
    # displays message to console when the player returns to field
    print("You run back into the field. Luckily, you don't seem to have been" +
          " followed.\n")


def approach_cave_msg(current_weapon):
    # displays message to console when the player enters cave
    if current_weapon != "sword":
        console_output = ["You peer cautiously into the cave.",
                          "It turns out to be only a very small cave.",
                          "Your eye catches a glint of metal behind a rock.",
                          "You have found the magical Sword of Ogoroth!",
                          "You discard your silly old dagger and take the " +
                          "sword with you.",
                          "You walk back out to the field.\n"]
    else:
        console_output = ["You peer cautiously into the cave.",
                          "You've been here before, and gotten all the good " +
                          "stuff. It's just an empty cave now.",
                          "You walk back out to the field\n"]

    for sentence in console_output:
        print(sentence)
        sleep(2)

    return "sword"


def win(enemy):
    # displays message to console when the player wins
    console_output = [f"As the {enemy} moves to attak, you unsheath your " +
                      "new sword.",
                      "The Sword of Ogoroth shines brightly in your hand as " +
                      "you brace yourself for the attack.",
                      f"But the {enemy} takes one look at your shiny new " +
                      "toy and runs away!",
                      f"You have rid the town of the {enemy}. " +
                      "You are victorious!"]

    for sentence in console_output:
        print(sentence)
        sleep(2)


def main():
    # set default values
    weapon = "dagger"
    enemy = set_enemy()
    is_playing = True

    # Opening message and get player choice to explore cave or approach house
    opening_greetings(enemy)

    while is_playing:
        player_input = get_player_input()
        # Conditional flow to take action based on user choice: appproach house
        # or explore cave
        if player_input == '1':
            # Player choose to approach house
            approach_house_msg(weapon, enemy)
            fight_response = get_player_fight_input()
            if fight_response == '1':
                if weapon == "dagger":
                    # you have been defeated
                    defeat(enemy)
                    # check to see if player wants to play again
                    is_playing = process_play_again_input(play_again_prompt())
                    # reset default values if starting a new game
                    if is_playing:
                        weapon = "dagger"
                        enemy = set_enemy()
                        opening_greetings(enemy)
                else:
                    # weapon is Sword of Ogoroth, display winning scenario.
                    win(enemy)
                    # check to see if player wants to play again
                    is_playing = process_play_again_input(play_again_prompt())
                    # reset defaut values if starting a new game
                    if is_playing:
                        weapon = "dagger"
                        enemy = set_enemy()
                        opening_greetings(enemy)

            elif fight_response == '2':
                # to-do: go back to the field and start at player_input
                go_back_to_field()
            else:
                is_playing = process_play_again_input(play_again_prompt())
                # reset default values and print opening greetings
                if is_playing:
                    weapon = "dagger"
                    enemy = set_enemy()
                    opening_greetings(enemy)
        else:
            # peer into cave
            weapon = approach_cave_msg(weapon)


if __name__ == "__main__":
    main()
