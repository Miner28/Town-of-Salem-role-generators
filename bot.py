import discord
from discord.ext import commands
import random
import requests
import sys, os
from dotenv import load_dotenv
import gspread, gspread.utils
import datetime

client = commands.Bot(command_prefix='!')
load_dotenv()
secret = os.getenv("secret")
gclient = gspread.service_account(filename="client_secret.json")
role_sheet = gclient.open("roleGenerator").sheet1
curColumn = 1


async def AltTest(townNumbers, GameMode, ctx):
    GameMode -= 1
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
        "Consigliere", \
        "Consort", \
        "Blackmailer", \
        "Janitor", \
        "Ambusher", \
        "Disquiser", \
        "Framer", \
        "Hypnotist", \
        "Serial Killer", \
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
        "Coven leader", \
        "Medusa", \
        "Necromancer", \
        "Hex Master", \
        "Potion Master", \

    MafiaReturns = \
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, \
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, \
        1, 1, 1, 1, 1, 1, 1, 1, 0, 1, \
        1, 1, 1, 1, 1, 0, 0, 0, 0, 0, \
        0, 0, \

    Classic = 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, \
              0, 0, 1, 1, 1, 1, 0, 1, 1, 1, \
              1, 0, 1, 1, 0, 1, 1, 1, 1, 1, \
              0, 1, 1, 0, 1, 0, 1, 0, 0, 0, \
              0, 0, \

    Coven = 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, \
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, \
            1, 1, 1, 1, 1, 1, 0, 0, 0, 1, \
            1, 1, 1, 1, 1, 0, 1, 1, 1, 1, \
            1, 1, \

    TownList = []

    MafiaList = []

    NeuList = []

    CovenList = []

    FinalePrint = []

    combindedList = MafiaReturns, Classic, Coven

    if townNumbers == 7:
        mafiaCount = 2
        neuCount = 1
        townCount = 4
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
        townCount = 7
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

    # MAFIA RETURNS SYLE
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
    return FinalePrint


def sendembed(title, name, value):
    if name.upper() == "ERROR:":
        color = 0xFF0000
    elif name.upper() == "INFO:":
        color = 0x00FFFF
    elif name.upper() == "WARNING":
        color = 0xFF4500
    else:
        color = 0xFFFF00
    embed = discord.Embed(title=title, color=color)
    embed.add_field(name=name, value=value, inline=True)
    return embed


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord! In {len(client.guilds)} servers')


@client.command(name="makeroles", aliases=["makelist", "generateroles", "makerolelist"])
async def makeroles(ctx):
    global curColumn
    print(ctx.author)

    def check(m):
        return m.channel == ctx.channel and ctx.author.id != client.user.id and ctx.author.id == m.author.id

    def rcheck(react, u):
        return str(react) in ["1️⃣", "2️⃣", "3️⃣", "✅", "❌"] and u.id == ctx.message.author.id

    async def send_list():
        global curColumn
        final_list = await AltTest(int(players), int(gamemode), ctx)
        prints = []
        for each in [final_list]:
            cur_print = ""
            num = 1
            for item in each:
                cur_print = cur_print + f"**[{num}] - " + item + "**\n"
                num += 1
            prints.append(cur_print)
        final_print = prints[0]
        await ctx.send(embed=sendembed("Shuffled full list", f"number: {len(final_list)}", final_print))
        msg = await ctx.send(embed=sendembed("", "INFO:", "Would you like to upload the list to connected spreadsheet\nhttps://docs.google.com/spreadsheets/d/1aVvqZUqJRfarE7mMZENH_b9IKnEKa1DZPzBT91OlRZk"))
        await msg.add_reaction("✅")
        await msg.add_reaction("❌")
        reaction, user = await client.wait_for('reaction_add', check=rcheck, timeout=20)
        if str(reaction) == "✅":
            await ctx.send(embed=sendembed("", "Uploading..", f"This can take upto 10 seconds (Usually instant)\nYour roles will be on column - {curColumn}"))
            row = 0
            role_sheet.update_cell(1, curColumn, str(datetime.datetime.now()))
            start = gspread.utils.rowcol_to_a1(3, curColumn)
            end = gspread.utils.rowcol_to_a1(17, curColumn)
            cell_list = role_sheet.range(f'{start}:{end}')
            for cell in cell_list:
                cell.value = ""
            for x in final_list:
                cell_list[row].value = x
                row += 1
            role_sheet.update_cells(cell_list)
            curColumn += 1
        await ctx.send(embed=sendembed("", "INFO:", "Do you want to generate new list with the same parameters ? y/n"))
        answer = await client.wait_for('message', check=check, timeout=20)
        if answer.content == "y":
            await send_list()
        else:
            return

    await ctx.send(embed=sendembed("", "INFO:",
                                   "Thank you for using Town of Salem's role list generator made by KingOfNova and reworked into discord version by Miner28_3\n\nNow please write number of players 6-15"))
    playersmsg = await client.wait_for('message', check=check, timeout=120)
    players = playersmsg.content
    gamemodemsg = await ctx.send(embed=sendembed("", "INFO:", "Please choose a gamemode.\n"
                                                              "1. Mafia Returns\n"
                                                              "2. Classic\n"
                                                              "3. Coven"))
    await gamemodemsg.add_reaction("1️⃣")
    await gamemodemsg.add_reaction("2️⃣")
    await gamemodemsg.add_reaction("3️⃣")

    reaction, user = await client.wait_for('reaction_add', check=rcheck, timeout=120)
    gamemodes = {"1️⃣": 1, "2️⃣": 2, "3️⃣": 3}
    gamemode = gamemodes[str(reaction)]

    await send_list()


@client.command(name="update", hidden=True)
async def update(ctx):
    if ctx.author.id != 231025351051051010:
        return
    await ctx.send(embed=sendembed("", "INFO:", "Please send bot.py!"))

    def check(m):
        return m.channel == ctx.channel and ctx.author == m.author

    try:
        msg = await client.wait_for('message', timeout=20, check=check)
        url = msg.attachments[0].url
        img_data = requests.get(url).content
        with open('bot.py', 'wb') as handler:
            handler.write(img_data)
    except TimeoutError:
        await ctx.send(embed=sendembed("", "INFO:", "Sorry too late"))
        return
    except:
        await ctx.send(embed=sendembed("", "INFO:", "This is not bot.py"))
        return
    sys.exit()


client.run(secret)
