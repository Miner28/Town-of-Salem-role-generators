import random
import gspread

# __________________________________________________________
# Created by George Shea
# Edited by Miner28_3
# 15/6/2020
# 15/6/2020
# Version 2.0
#
# Automatically gives out roles for the town of salem game
# __________________________________________________________

# Put you're link below
link = "https://docs.google.com/spreadsheets/d/1Ni3F9nH0BRdcZh3P5tOzbxDPK2MsQAP59GHR8JvcqZo/edit?usp=sharing"
# Put your link above


# Googlespreadsheet initialization
gclient = gspread.service_account(filename="client_secret.json")
game_sheet = gclient.open_by_url(link).sheet1


def main():
    # NEUTRAL
    # For games of lower then 11
    neu_low = "Serial Killer", "Jester", "Executioner", "Witch", "Pirate"
    # Inclue lowNue for games over 11
    neu_high = "Amnesiac", "Arsonist", "Guardian Angel", "Werewolf", "Plaguebearer", "Vampire"

    # MAFIA
    mafia_low = "Consigliere", "Consort", "Hypnotist", "Blackmailer", "Janitor", "Ambusher",
    mafia_high = "Disquiser", "Framer"

    # TOWN
    town_low = "Bodyguard", "Investigator", "Doctor", "Lookout", "Escort", "Vigilante", "Veteran", "Sheriff", "Mayor", \
               "Tracker", "Trapper"

    town_high = "Psychic", "Crusader", "Retrobutionist", "Transporter", "Spy", "Jailer"

    mafia_list = list()
    town_list = list()

    print("Welcome To The Town Of Salem Role Picker Console App\n"
          "______________________________________________________\n"
          "Created by KingOfNova\n"
          "Edited by Miner28_3\n"
          "Please follow the prompts\n")
    town_numbers = input("Please enter players present above 6\n")
    try:
        town_numbers = int(town_numbers)
        if town_numbers <= 6 or town_numbers >= 16:
            print("\n\n\n\n")
            main()
    except:
        print("\n\n\n\n")
        main()
    print("You will be prompted to have certain roles in your game")
    print("This does not guarantee that the roles will generate")
    print("Simply answer y for yes or n for no")
    medium_choice = input("Do you wish to have a medium || y/n ||\n").lower()
    forger_choice = input("Do you wish to have a Forger || y/n ||\n").lower()

    if town_numbers == 7:
        mafia_count = 2
        neu_count = 1
        town_count = 4
    elif town_numbers == 8:
        mafia_count = 2
        neu_count = 1
        town_count = 5
    elif town_numbers == 9:
        mafia_count = 2
        neu_count = 1
        town_count = 6
    elif town_numbers == 10:
        mafia_count = 3
        neu_count = 1
        town_count = 6
    # Big Game cut off
    elif town_numbers == 11:
        mafia_count = 3
        neu_count = 1
        town_count = 7
    elif town_numbers == 12:
        mafia_count = 3
        neu_count = 2
        town_count = 7
    elif town_numbers == 13:
        mafia_count = 3
        neu_count = 2
        town_count = 8
    elif town_numbers == 14:
        mafia_count = 4
        neu_count = 2
        town_count = 8
    elif town_numbers == 15:
        mafia_count = 4
        neu_count = 3
        town_count = 8
    else:
        mafia_count = 0
        neu_count = 0
        town_count = 0

    town_print = []
    mafia_print = []
    neu_print = []

    # MafiaGeneration
    if town_numbers >= 10:
        mafia_list = mafia_low + mafia_high
    elif town_numbers < 10:
        mafia_list = mafia_list.append(mafia_low)

    if forger_choice == "y":
        forger = "Forger", "Forger"
        mafia_list = mafia_list + forger

    print("\n\n\n")
    print("Mafia Roles")
    print("_____________________________________")

    mafia_print.append("Godfather")
    mafia_print.append("Mofioso")
    if mafia_count > 2:
        while len(mafia_print) < mafia_count:
            generate = mafia_list[random.randrange(0, len(mafia_list))]
            if generate not in mafia_print:
                mafia_print.append(generate)
    if mafia_count > 3:
        while len(mafia_print) < mafia_count:
            generate = mafia_list[random.randrange(0, len(mafia_list))]
            if generate not in mafia_print:
                mafia_print.append(generate)

    for x in range(len(mafia_print)):
        print(mafia_print[x])

    # Town Generation
    if town_count >= 10:
        town_list = town_low + town_high
    elif town_count < 10:
        town_list = town_low

    if medium_choice == "y":
        medium = "Medium", "Medium"
        town_list = town_list + medium

    print("\n")
    print("Town Roles")
    print("_____________________________________")

    while len(town_print) < town_count:
        generate = town_list[random.randrange(0, len(town_list))]
        if generate not in town_print:
            town_print.append(generate)

    for x in range(len(town_print)):
        print(town_print[x])

    # Neu Generation
    if town_numbers > 10:
        neu_list = neu_low + neu_high
    else:
        neu_list = neu_low

    print("\n")
    print("Neutral Roles")
    print("_____________________________________")

    while len(neu_print) < neu_count:
        generate = neu_list[random.randrange(0, len(neu_list))]
        if generate not in neu_print:
            neu_print.append(generate)

    for x in range(len(neu_print)):
        print(neu_print[x])

    final_print = neu_print + mafia_print + town_print
    random.shuffle(final_print)
    print("\n\n\n")
    print("Houses")
    print("_____________________________________")
    for x in range(len(final_print)):
        print([x + 1], " ", final_print[x])
    print("_____________________________________\n")
    if "y" == input("Do you want to upload results to linked spreadsheet ? || y/n\n"):
        for x in range(len(final_print)):
            game_sheet.update_cell(11+x, 7, final_print[x])
        print("Spreadsheet updated successfully!")
    reroll = input("Re-roll || y/n").lower()
    if reroll == "y":
        main()


main()
