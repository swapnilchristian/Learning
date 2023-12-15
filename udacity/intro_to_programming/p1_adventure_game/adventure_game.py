'''
Program: Introduction to Programming Nano Degree
Project: Adventure Game
Author: Swapnil Christian
'''

from time import sleep
from random import choice
import sys


def print_pause(console_msg):
    print(console_msg)
    sleep(0)


def intro_msg(enemy):
    return ["You find yourself standing in an open field, filled with grass and yellow wildflowers.",
            f"Rumor has it that a {enemy} is somewhere around here, and has been terrifying the nearby village.",
            "In front of  you is a house.",
            "To your right is a dark cave.",
            "In your hand you hold your trust (but not very effective) dagger.\n"]


def display_intro_msg(intro_list):
    for phrase in intro_list:
        print_pause(phrase)


def player_input_msg():
    return ["Enter 1 to knock on the door of the house.",
            "Enter 2 to peer into the cave",
            "What would you like to do?"]


def display_player_input_msg(input_msg):
    for phrase in input_msg:
        print_pause(phrase)


def handle_incorrect_input(user_val, exp_val_1, exp_val_2, func_to_call):
    '''
    This function takes 4 argruments.
    user_val --> This is the input from user
    exp_val_1 --> Expected user input 1 for e.g. yes (y)
    exp_val_2 --> Expected user input 2 for e.g. no (n)
    func_to_call --> Get user input if value does not match exp_val_1 or exp_val_2
    '''
    if user_val in exp_val_1:
        return exp_val_1
    elif user_val in exp_val_2:
        return exp_val_2
    else:
        func_to_call


def get_player_input():
    player_input = input("(Please enter 1 or 2.)\n")
    if '1' in player_input:
        return '1'
    elif '2' in player_input:
        return '2'
    else:
        get_player_input()


def get_defence_input():
    defence = input("Would you like to (1) fight or (2) run away?")
    if defence == '1':
        return '1'
    elif defence == '2':
        return '2'
    else:
        play_again()


def play_again():
    continue_play = input("Would you like to play again? (y/n)")
    if continue_play == 'y':
        print_pause("Excellent! Restarting the game ...")
        return 'y'
    elif continue_play == 'n':
        print_pause("Thanks for playing! See you next time.")
        return 'n'
    else:
        play_again()


def win(enemy):
    print_pause(f"You have rid the town of the {enemy}. You are victorious!")

def main():
    enemy_type = ['dragon', 'gorgon', 'wicked fairie', 'troll']
    enemy = choice(enemy_type)
    weapon = 'Trusty Dagger'

    display_intro_msg(intro_msg(enemy))
    display_player_input_msg(player_input_msg())
    area_to_explore = get_player_input()
    while True:
        if area_to_explore == '1':
            print_pause("You approach the door of the house.")
            print_pause(f"You are about to knock when the door opens and out steps a {enemy}.")
            print_pause(f"Eep! This is the {enemy}'s house!")
            print_pause(f"The {enemy} attacks you!")
            if 'sword' not in weapon.lower():
                print_pause("You feel a bit under-prepared for this, what with only having a tiny dagger.")
                defend = get_defence_input()
                print("my input was ---> ", defend)
                if defend == '1':
                    print_pause("You do your best...")
                    print_pause(f"but your dagger is no match for the {enemy}.")
                    print_pause("You have been defeated!")
                    play_again()
                else:
                    print_pause("You run back into the field. Luckily, you don't seem to have been followed.\n")
                    display_player_input_msg(player_input_msg())
                    area_to_explore = get_player_input()
            else:
                defend = get_defence_input()
                if defend == '1':
                    print_pause(f"As the {enemy} moves to attack, you unsheath your new sword.")
                    print_pause(f"The {weapon} shines brightly in your hand as you brace yourself for the attack.")
                    print_pause(f"But the {enemy} takes on look at your shiny new toy and runs away!")
                    win(enemy)
                    play_again()
                else:
                    print_pause("You run back into the field. Luckily, you don't seem to have been followed.")
                    display_player_input_msg(player_input_msg())
                    area_to_explore = get_player_input()

        else:
            print_pause("You peer cautiously into the cave.")
            if 'sword' in weapon.lower():
                print_pause("You've been here before, and gotten all the good stuff. It's just an empty cave now.")
                print_pause("You walk back out to the field.\n")
            else:
                print_pause("It turns out to be only a very small cave.")
                print_pause("Your eye catches a glint of metal behind a rock.")
                print_pause("You have found the magical Sword of Ogoroth!")
                print_pause("You discard your silly old dagger and take the sword with you.")
                weapon = 'Sword of Ogoroth'
                print_pause("You walk back out to the field.\n")
            display_player_input_msg(player_input_msg())
            area_to_explore = get_player_input()


if __name__ == "__main__":
    main()