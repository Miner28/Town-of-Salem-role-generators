import random

#__________________________________________________________
#Created by George Shea     ßeta
# 15/6/2020
# 28/6/2020
# Version 2.0
# Massive upgrade to include maffia returns coven and classic
# no bugs yet
# automaticly gives out roles for the town of salem game
#__________________________________________________________

def AltTest():

    AllRoles = \
        "Bodygaurd", \
        "Investigator", \
        "Doctor", \
        "Lookout", \
        "Escort", \
        "Vigilante", \
        "Veteran", \
        "Sheriff", \
        "Mayor", \
        "Tracker", \
        "Psychic", \
        "Crusader", \
        "Retributionist", \
        "Transporter", \
        "Spy", \
        "Jailor", \
        "Trapper", \
        "Medium", \
        "Consigliere",                  \
        "Consort", \
        "Blackmailer", \
        "Jainitor", \
        "Ambusher", \
        "Disquiser", \
        "Framer", \
        "Hypnotist", \
        "Serial Killer",                \
        "Jester", \
        "Executioner", \
        "Witch", \
        "Pirate", \
        "Amnesiac", \
        "Arsonist", \
        "Guardian Angle", \
        "Werewolf", \
        "Plaguebearer", \
        "Vampire", \
        "Coven leader" ,                 \
        "Medua", \
        "Necromancer", \
        "Hex Master", \
        "Potion Master", \

    MafiaReturns = 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , \
               1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , \
               1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 0 , 1 , \
               1 , 1 , 1 , 1 , 1 , 0 , 0 , 0 , 0 , 0 , \
               0 , 0 ,\

    Classic = 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , \
               0 , 0 , 0 , 1 , 1 , 1 , 1 , 0 , 1 , 1 , \
               1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 0 , 1 , \
               1 , 0 , 1 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , \
               0 , 0 ,\

    Coven = 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , \
               1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , \
               1 , 1 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , \
               1 , 1 , 1 , 1 , 1 , 0 , 1 , 1 , 1 , 1 , \
               1 , 1 ,\


    TownList = []

    MafiaList = []

    NeuList = []

    CovenList = []

    FinalePrint = []

    combindedList = MafiaReturns , Classic , Coven

    print("________________________________________________________")
    print("Welcome to the town of salem role picker")
    print("Built by KingOfNova")
    print("GameMode")
    print("____________________")
    print("1 Maffia Returns")
    print("2 Classic")
    print("3 Coven ")
    print("____________________")
    GameMode = int(input("Please enter number of gamemode you wish to play \n")) - 1
    print("________________________________________________________")
    townNumbers = int(input("Please enter players present above  6 \n"))

    if townNumbers == 7:
        mafiaCount = 2
        neuCount = 1
        townCount =4
        covenCount = 2
    elif townNumbers == 8:
        mafiaCount = 2
        neuCount = 1
        townCount = 5
        covenCount = 2
    elif townNumbers == 9:
        mafiaCount = 2
        neuCount = 1
        townCount = 6
        covenCount = 2
    elif townNumbers == 10:
        mafiaCount = 2
        neuCount = 1
        townCount = 6
        covenCount = 2
    elif townNumbers == 11:
        mafiaCount = 3
        neuCount = 1
        townCount = 7
        covenCount = 3
    elif townNumbers == 12:
        mafiaCount = 3
        neuCount = 2
        townCount = 7
        covenCount = 3
    elif townNumbers == 13:
        mafiaCount = 3
        neuCount = 2
        townCount = 8
        covenCount = 3
    elif townNumbers == 14:
        mafiaCount = 4
        neuCount = 2
        townCount = 8
        covenCount = 4
    elif townNumbers == 15:
        mafiaCount = 4
        neuCount = 3
        townCount = 8
        covenCount = 4

    #MAFIA RETURNS SYLE
    count = 0
    # TOWN ___________________________________________________
    for x in combindedList[GameMode]:
        if combindedList[GameMode][count] == 1 and count >= 0 and count <= 17:
            TownList.append(AllRoles[count])

        if combindedList[GameMode][26] == 1:
            if combindedList[GameMode][count] == 1 and count >= 18 and count <= 25:
                MafiaList.append(AllRoles[count])

        if combindedList[GameMode][count] == 1 and count >= 26 and count <= 36:
            NeuList.append(AllRoles[count])

        if combindedList[GameMode][37] == 1:
            if combindedList[GameMode][count] == 1 and count >= 37 and count <= 42:
                CovenList.append(AllRoles[count])

        count = count + 1

    count = 1
    countSecond = 1

    while count <= townCount:
        generate = random.choice(TownList)
        if generate not in TownList: TownList.append(generate)
        FinalePrint.append(TownList[count])

        countSecond = countSecond + 1
        count = count + 1

    count = 1

    while count <= neuCount:
        generate = random.choice(NeuList)
        if generate not in NeuList: NeuList.append(generate)
        FinalePrint.append(NeuList[count])

        count = count + 1
        countSecond = countSecond + 1

    count = 1

    if combindedList[GameMode][26] == 1:
        FinalePrint.append("Godfather")
        FinalePrint.append("Moffisio")
        while count <= mafiaCount - 2:
            generate = random.choice(MafiaList)
            if generate not in MafiaList: MafiaList.append(generate)
            FinalePrint.append(MafiaList[count])

            countSecond = countSecond + 1
            count = count + 1

    count = 1

    # dont forget coven leader
    if combindedList[GameMode][37] == 1:
        FinalePrint.append("Coven Leader")
        while count <= covenCount - 1:
            generate = random.choice(CovenList)
            if generate not in CovenList: CovenList.append(generate)
            FinalePrint.append(CovenList[count])

            countSecond = countSecond + 1
            count = count + 1


    random.shuffle(FinalePrint)

    count = 0
    for x in FinalePrint:
        print("[",  count + 1, "]        ", FinalePrint[count])
        count = count + 1

    reroll = input("Do you wish to reroll y/n \n")
    if reroll == "y":
        AltTest()
    else:
        exit()
AltTest()