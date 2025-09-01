import csv
import json
import pandas as pd
import time

dataset = pd.read_csv("dataset.csv")
corpus = dataset["text"]

with open("savefile.txt", encoding="utf-8") as savefile:
    save = json.load(savefile)

if save["first timer?"] == True:

    print("""
    You are about to play a game where your goal is to jump as high as possible.
    If you're confused on any of the rules at any point, just type \"help\".
      
      Note that the data from responding to the emoji prompts will be used by me, Fredrick, the creator of this project.
      That is the only data that will be collected. If your response to a prompt is invalid, and/or things you type in the shop,
      or in the game, etc. will not be collected.
      
      """)
    points = 0
    total_points = 0
    tickets = 0
    total_tickets = 0
    perma_upgrades = 0
    in_use = []
    items = []
    advanced_prompt_reached, standard_prompt_reached = 0, 0
    advanced_emoji_index, standard_emoji_index = 0, 0
    message_waittimes = 5

    implant_price = 10000
    bcdict = {"1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "", "10": ""}

else:
    print("Oh hey! You're back. If you forgot anything at all, type 'help'. Otherwise, just keep going!\n\n")
    offline_time_seconds = time.time() - save["toe"]
    items = save["it"]
    points = save["p"]
    total_points = save["tp"]
    tickets = save["t"]
    total_tickets = save["tt"]
    perma_upgrades = save["pu"]
    in_use = save["iu"]
    implant_price = save["ip"]
    bcdict = save["bcdict"]
    advanced_prompt_reached = save["advpr"]
    standard_prompt_reached = save["stdpr"]
    advanced_emoji_index = save["advei"]
    standard_emoji_index = save["stdei"]
    implant_price = save["ip"]
    message_waittimes = 0


index_to_item = {"1": "jump potion",
"2": "cocaine",
"3": "6 day gym membership",
"4": "jump rope",
"5": "feet implants",
"6": "usa health insurance",
"7": "good health insurance",
"8": "basketball hoop",
"9": "random training site",
"10": "passive income"}
index_to_price = {"1": 500,
"2": 1000,
"3": 800,
"4": 100,
"5": implant_price,
"6": 20000,
"7": 10,
"8": 500,
"9": 1000,
"10": 20000}
index_to_attribute = {"1": "six hours of 1.5x jump height",
"2": "three hours of 5x jump height",
"3": "an extra inch to jump height per day for 6 days",
"4": "+5 inches of jump height",
"5": "+1 inches of jump height",
"6": "makes feet implants cost 12000 tickets",
"7": "makes feet implants cost 9990 tickets",
"8": "does nothing, just makes you feel bad",
"9": "+2 inches of jump height",
"10": "+1 point for every 10 minutes offline"}
index_to_purchasability = {"1": "can stack",
"2": "can stack",
"3": "cannot stack",
"4": "are only once",
"5": "are only once",
"6": "are only once, but cost 100 points every offline hour, per purchase",
"7": "are a one-time lifetime subscription",
"8": "are only once",
"9": "are two total courses. You may buy it two times",
"10": "can stack"}

def shop():
    global implant_price, bcdict
    print(f"""You've entered the shop! You can buy any of these!
          Anything marked with a -- at the start cannot be bought anymore, as you've already gotten all purchases available of it.
          Anything marked with a - means that you've bought one purchase, and there is one remaining.
          
    {bcdict["1"]}1) Jump potion             500 tickets          Six hours of 1.5x jump height on use                      Can stack.
    {bcdict["2"]}2) Cocaine                 1000 tickets         Three hours of 5x jump height on use.                   Can stack.
    {bcdict["3"]}3) 6 Day Gym Membership    800 tickets          An extra inch to jump height per day for 6 days.       Cannot stack.
    {bcdict["4"]}4) Jump rope               100 tickets          +5 inches of jump height on one-time use.               Only once.
    {bcdict["5"]}5) Feet implants   {implant_price} tickets      +1 inches of jump height on one-time use.               Only once.
    {bcdict["6"]}6) USA Health Insurance    20000 tickets        Makes feet implants cost 12000 tickets.                 Costs 100 points every day (including offline) (DON'T BUY)
    {bcdict["7"]}7) Good Health Insurance   10 tickets           Makes feet implants cost 9990 tickets.                  Lifetime subscription.
    {bcdict["8"]}8) Basketball Hoop         500 tickets          Does nothing, just makes you feel bad.                  Only once.
    {bcdict["9"]}9) Random Training Site    1000 tickets         +2 inches of jump height.                               Three total courses.
    {bcdict["10"]}10) Passive Income         20000 tickets        +1 point for every 10 minutes offline.                  Can stack.
    
    """)
    
    buy_check = constrained_input("""Would you like to buy an item?

    You may respond with 1 or 0, or with one of the following commands: (if you are getting formatting errors)

    - checkname                 Checks the name of an item (given number).              
    - checkprice                Checks the price of an item (given number).
    - checkattribute            Checks the purpose, or what an item does (given number).
    - checkpurchasability       Checks how many purchases can be made of an item (given number).
                                  
    """, is_shopcommand_valid)
                
    print("Thanks for visiting the shop. Now go back to grinding for points.\n\n")

def buy_item(item):
    global items, tickets
    price = index_to_price[item]
    if tickets < price:
        print("You cannot afford this item right now.\n\n")
        return
    else:
        tickets -= price
        print(f"""You have successfully bought this item for {price} tickets.

You now have {tickets} tickets remaining.\n\n""")
        items.append(item)

def shopcommand(buy_check):
    if buy_check == "checkname":
        thing_to_check = constrained_input("What do you need to check the name of? (number 1-10)\n\n", is_shop_valid)
        print(f"That is the {index_to_item[thing_to_check]}.")
    if buy_check == "checkprice":
        thing_to_check = constrained_input("What do you need to check the price of? (number 1-10)\n\n", is_shop_valid)
        print(f"That item costs {index_to_price[thing_to_check]} tickets.")
    if buy_check == "checkattribute":
        thing_to_check = constrained_input("What do you need to know the purpose of? (number 1-10)\n\n", is_shop_valid)
        print(f"That item gives you {index_to_attribute[thing_to_check]}.")
    if buy_check == "checkpurchasability":
        thing_to_check = constrained_input("What do you need to know the purchasability of? (number 1-10)\n\n", is_shop_valid)
        if bcdict[thing_to_check] == "--":
            print("You have already acquired all purchases of this item.")
        print(f"That item's purchases {index_to_purchasability[thing_to_check]}.")
    
    while buy_check == "1":
        item = constrained_input("Type the number of the item you would like to buy.\n\n", is_shop_valid)
        if item in ["4", "5", "7", "8"]:
            if bcdict[item] == "":
                bcdict[item] = "--"
                buy_item(item)
            else:
                print("You have already purchased this one-time purchase item.\n\n")
        elif item == "6":
            areyousure = constrained_input("""This is a really, really stupid decision. This will do you nothing good.
                                           I promise this isn't a secret hack.
                                           This is non-refundable. Are you sure?\n\n""", is_std_valid)
            if areyousure == "0":
                continue
            else:
                buy_item(item)
        elif item == "9":
            if bcdict[item] == "--":
                print("You have run out of purchases for this two-time purchase item.\n\n")
            else:
                bcdict[item] += "-"
                buy_item(item)
        else:
            buy_item(item)
        
        buy_check = constrained_input("\n\nWould you like to try to get another item? (Respond with 1 or 0).\n\n", is_std_valid)
    if buy_check == "0":
        return

import random

def roulette():
    global tickets, total_tickets, points
    bet = int(constrained_input("How many points do you want to bet? Type '0' to exit the casino.\n\n", isvalidbet))
    if bet == 0:
        return
    points -= bet
    
    gametype = constrained_input(r"""

If you want to bet on a colour (converts 25% to tickets if you win, 5% if you lose), type '1'. Odds: 75% success.
If you want to bet on a number, (converts 100% to tickets if you win, 0% if you lose), type '0'. Odds: 10% success.

""", is_std_valid)

    if gametype == "1":
        color = constrained_input("Would you like to bet on red or black? Respond with '1' for red, and '0' for black.\n\n", is_std_valid)
        win = random.randint(1,4) <= 3
        if win:
            tickets += bet // 4
            total_tickets += bet // 4
            time.sleep(1)
            print("Spinning...")
            time.sleep(5)
            print(f"""Congratulations! You won the bet. Your {bet} points have been converted into {bet // 4} tickets.""")
        else:
            tickets += bet // 20
            total_tickets += bet // 20
            time.sleep(1)
            print("Spinning...")
            time.sleep(5)
            if color == "1":
                choice_arr = ["black"] * 10
                choice_arr.append("green")
                acc_color = random.choice(choice_arr)
            else:
                choice_arr = ["red"] * 10
                choice_arr.append("green")
                acc_color = random.choice(choice_arr)
            print(f"""Unfortunately, the wheel landed on {acc_color}.

Your {bet} points have been converted into {bet // 20} tickets.""")
            
    elif gametype == "0":
        number = constrained_input("What number do you pick (0-36)?\n\n", is_roulette_num)
        win = random.randint(1,10) == 1
        time.sleep(1)
        print("Spinning...")
        time.sleep(5)
        if win:
            tickets += bet
            total_tickets += bet
            print(f"""Congratulations! You won the bet. Your {bet} points have all been converted into tickets.""")
        else:
            num_options = list(range(37))
            num_options.remove(int(number))
            print(f"""Unfortunately, the wheel landed on {random.choice(num_options)}.

You have lost all of your bet points.""")

def blackjack():
    global tickets, total_tickets, points
    bet = int(constrained_input(r"""How many points do you want to bet? Type '0' to exit the casino.

If you win, 25% of your bet will be converted into tickets.
If you lose, 5% of your bet will be converted into tickets.
                                
""", isvalidbet))
    if bet == 0:
        return
    points -= bet
    dealer = 0
    player = random.randint(2, 11)
    decision = constrained_input(f"""\n\nYou currently have {player} in total.
                                         
If you want to hit, type 1. If you want to stay, type 0.\n\n""", is_std_valid)
    while decision == "1":
        if player < 20:
            player_hit = random.randint(2, 11)
        else:
            player_hit = random.randint(1, 10)
        player += player_hit
        print(f"""You hit and got a {player_hit}. You now have {player} in total.""")
        if player > 21:
            print(f"You busted. You lose. Your {bet} points have been converted into {bet // 20} tickets.")
            tickets += bet // 20
            total_tickets += bet // 20
            return
        decision = constrained_input(f"""\n\nYou currently have {player} as your total card count.
                                         
If you want to hit, type 1. If you want to stay, type 0.\n\n""", is_std_valid)
    
    print(f"You have stayed at {player}.\n\n")

    while dealer <= 16:
        print("The dealer hit.")
        dealer_hit = random.randint(2,11)
        dealer += dealer_hit
        print("Hitting...")
        time.sleep(message_waittimes)
        print(f"""He got a {dealer_hit}.

He now has a hand of {dealer}.""")
        if dealer > 21:
            print(f"The dealer busted. You win. Your {bet} points have been converted into {bet // 4} tickets.")
            tickets += bet // 4
            total_tickets += bet // 4
            return
    
    print(f"The dealer has stayed at {dealer}.")

    if dealer > player:
        print(f"The dealer wins. Your {bet} points have been converted into {bet // 20} tickets.")
        tickets += bet // 20
        total_tickets += bet // 20
    else:
        print(f"You win. Your {bet} points have been converted into {bet // 4} tickets.")
        tickets += bet // 4
        total_tickets += bet // 4
        

def gamble():
    game = constrained_input("""

Welcome to the casino!

Here, we have the option to play one of two games. 
    
    Type '1' for roulette, '2' for blackjack or '0' to exit the casino.\n\n""", is_gamble_valid)

    if game == "1":
        roulette()
    elif game == "2":
        blackjack()
    else:
        print("Thank you for visiting the casino!\n")
        return

def help():
    print("""
    You are playing a game where your goal is to have the highest possible vertical jump.
    To do this, you spend tickets in the shop to buy items.

    You can get points by responding to prompts regarding the possibility of emoji usage for a specific sentence.
    You can get tickets by gambling your points in the casino. Payouts are displayed in the games themselves.
          
    For more details regarding the way you should respond to prompts, type 'details' after any message, and rerun the program.
    
    WHEN QUITTING THE PROGRAM!
          
          - DO NOT EXIT BY CLOSING THE WINDOW. You will lose your saved progress, and potentially screw up data collection.
          - Instead, type 'exit', and the program will save your progress and quit by itself.
          - You may also press ctrl+C to forcibly stop the program, though it is much safer to use 'exit', as ctrl+C may wipe your progress.
          - ONLY THEN can you close the window.
    
    ALL COMMANDS MASTER LIST:
          
          - help        Displays this menu.
          - shop        Opens the shop, where you can buy items.
          - gamble      Opens the gambling menu, where you can play casino games (don't bet too much, please).
          - height      Shows your current vertical jump height. It could also have some fun facts for you :p, try it out!
          - details     Explains how you should respond to prompts.
          - balance     Tells you the number of points and tickets you have.
          - use         Allows you to use an item bought from the shop.
          - exit        Exits safely, and saves your current progress.
""")

def use_item():
    item = constrained_input("""Input the shop index of the item you would like to use.

If you don't remember or need to check, respond to this prompt with '0', and go check the shop.\n\n""", is_owned_item)
    if item == "0":
        return
    else:
        items.remove(item)
        in_use.append([item, time.time()])

        print(f"You have successfully used your {index_to_item[item]}.\n\n")


def effect_on_vert(vert, item_ts):
    global perma_upgrades, points, in_use, implant_price
    item, ts = item_ts

    if item == "1":
        if (time.time() - ts) >= 6*60*60:
            in_use.remove(item_ts)
            return vert
        else:
            return vert * 1.5
    elif item == "2":
        if (time.time() - ts) >= 3*60*60:
            in_use.remove(item_ts)
            return vert
        else:
            return vert * 5
    elif item == "3":
        gym_membership_effect = min(6, ((time.time() - ts) // (24*60*60)))
        if gym_membership_effect == 6:
            perma_upgrades += gym_membership_effect
            in_use.remove(item_ts)
        return vert + gym_membership_effect
    elif item == "4":
        perma_upgrades += 5
        in_use.remove(item_ts)
        return vert + 5
    elif item == "5":
        perma_upgrades += 1
        in_use.remove(item_ts)
        return vert + 1
    elif item == "6":
        days_since_buy = int((time.time() - ts) // (24*60*60))
        implant_price = 12000
        if days_since_buy > 0:
            points -= 100 * days_since_buy
            return (vert, [item, time.time()])
        else:
            return vert
    elif item == "7":
        implant_price = 9990
        return vert
    elif item == "8":
        return vert
    elif item == "9":
        perma_upgrades += 2
        in_use.remove(item_ts)
        return vert + 2
    elif item == "10":
        points += (time.time() - ts) // 600
        return (vert, [item, time.time()])

def current_vert():
    vert = 20 + perma_upgrades
    for item_ts in in_use[:]:  # copy so we can remove safely
        result = effect_on_vert(vert, item_ts)

        if isinstance(result, tuple):
            vert, new_item_ts = result
            in_use[in_use.index(item_ts)] = new_item_ts
        else:
            vert = result
    
    print(f"""Your current vertical jump height is {vert} inches!
""")

    time.sleep(message_waittimes)
    print(f"""You can currently jump over a {vert} inch ruler!\n\n""")

def point_count():
    print(f"""You currently have {points} points.
Over the course of this save, you have had {total_points} points in total.

You currently have {tickets} tickets.
Over the course of this save, you have had {total_tickets} tickets in total.""")
    
def details(advanced):

    if advanced == "1":
        print("""
        For the prompts, you will get a reddit message
        (note that they are unfiltered, and very much may be offensive).\n\n""")
        time.sleep(message_waittimes)

        print("""You will also get an emoji. You must respond with the likelihood of that emoji being accurate.
        (as a number between 0 and 1, with two decimal places, e.g. 0.45, 0.68, 0.12, 0.99, 0, 1, etc.).\n\n""")
        time.sleep(message_waittimes)

        print("""For example, you may see this prompt:
        \"I'm really happy right now\".
        With this emoji: 😍.

        A valid response would be 0.25, or 0.35, or something similar, as the hearts are not appropriate for the happiness.\n\n""")
        time.sleep(message_waittimes)

        print("""If you would like to be more optimistic, or more pessimistic, you will have to reflect that over ALL messages. For example:

        If "That's kinda cool" gets a 0.8 for 😂, then "That's kinda annoying" should get a 0.8 for 😠.
        And vice versa, if "That's kinda cool" gets a 0.2 for 😂, then "That's kinda annoying" should get a 0.2 for 😠.\n\n""")
        time.sleep(message_waittimes)

        print("""
            STAY CONSISTENT!\n""")
        time.sleep(message_waittimes)
        print("""
            Note that the point is not to find which emotion is accurate, it is to find which *emoji* is accurate.
              
            If a message isn't explicitly happy, but you believe that a laughing emoji is applicable, you may use it.
              
            This should only be in edge cases though. Generally, the emoji will match the emotion.\n\n""")
        time.sleep(message_waittimes)
        print("""

        Your results will be saved to a file and checked by me before being used,
        so please don't try to give bad answers just to buy items in the game.\n\n""")
        time.sleep(message_waittimes)

        print("""Since you are doing the survey on advanced mode, you will receive 10 points per question complete!
        To switch modes at any point, type 'switch' and follow the instructions.\n\n""")

    else:
        print("""
        For the prompts, you will get a reddit message
        (note that they are unfiltered, and very much may be offensive).""")
        time.sleep(message_waittimes)

        print("""You will also get an emoji. You must respond with if you believe that that emoji is accurate.
        Your response must be either '1' or '0'. '1' if the emoji is accurate, and '0' if it is not.""")
        time.sleep(message_waittimes)

        print("""For example, you may see this prompt:
        \"I'm really happy right now\".
        With this emoji: 😍.

        A valid response would likely be 0 as the hearts are not appropriate for that message.""")
        time.sleep(message_waittimes)

        print("""If you would like to be more optimistic, or more pessimistic, you will have to reflect that over ALL messages. For example:

        If "That's kinda cool" gets a 1 for 😂, then "That's kinda annoying" should get a 1 for 😠.
        And vice versa, if "That's kinda cool" gets a 0 for 😂, then "That's kinda annoying" should get a 0 for 😠.""")
        time.sleep(message_waittimes)

        print("""
            STAY CONSISTENT!""")
        time.sleep(message_waittimes)

        print("""
            Note that the point is not to find which emotion is accurate, it is to find which *emoji* is accurate.
              
            If a message isn't explicitly happy, but you believe that a laughing emoji is applicable, you may use it.
              
            This should only be in edge cases though. Generally, the emoji will match the emotion.\n\n""")
        time.sleep(message_waittimes)
        print("""

        Your results will be saved to a file and checked by me before being used,
        so please don't try to give bad answers just to buy items in the game.""")
        time.sleep(message_waittimes)

        print("""Since you are doing the survey on standard mode, you will only receive 5 points per question complete.
        To switch modes at any point, type 'switch' and follow the instructions.\n\n""")

def switch():
    global advanced
    print("""This menu is for if you would like to switch between standard and advanced mode.
          Though your points stay between both modes, you will be answering prompts that you may have seen before.
          
          This is because I need data in both standard and advanced. Although, it makes it much easier for you, as labelling
          the same data twice is a lot easier than labelling double the amount of data.
          
          With that being said,""")
    
    time.sleep(message_waittimes)

    advanced = constrained_input("""Please choose if you would like to switch to advanced mode or standard mode.
                                 
    Respond with a 1 or 0, (1 for advanced, 0 for standard).\n\n""", is_std_valid)

    if advanced == "1":
        advanced = constrained_input("""Are you sure you would like to switch to advanced mode?\n\n""", is_std_valid)
        if advanced == "0":
            print("Alright. You have been set to standard mode. If you change your mind, just type 'switch' again.")
    else:
        check = constrained_input("""Are you sure you would like to switch to standard mode?\n\n""", is_std_valid)
        if check == "0":
            print("Alright. You have been set to advanced mode. If you change your mind, just type 'switch' again.")
            advanced = "1"

def save_and_exit(param1=None, param2=None):  # these params will be passed by signal for no good reason, so gotta accept them
    save = {
        "it": items,
        "p": points,
        "tp": total_points,
        "t": tickets,
        "tt": total_tickets,
        "iu": in_use,
        "ip": implant_price,
        "pu": perma_upgrades,
        "toe": time.time(),
        "first timer?": False,
        "advpr": advanced_prompt_reached,
        "stdpr": standard_prompt_reached,
        "advei": advanced_emoji_index,
        "stdei": standard_emoji_index,
        "bcdict": bcdict
    }
    with open("savefile.txt", "w", encoding="utf-8") as savefile:
        json.dump(save, savefile)
    
    exit()

import signal
import sys


if sys.platform == "win32":
    import ctypes

    def console_close_handler(event):
        save_and_exit()
        return True  # prevent immediate termination until finished

    handler = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.c_uint)(console_close_handler)
    ctypes.windll.kernel32.SetConsoleCtrlHandler(handler, True)

signal.signal(signal.SIGINT, save_and_exit)
signal.signal(signal.SIGTERM, save_and_exit)
# gives a chance of saving the progress without unsaved data, though still risky

def constrained_input(prompt: str, requirement):
    while True:
        response = input(prompt).lower()
        if requirement == is_shopcommand_valid:
            if requirement(response):
                shopcommand(response)
                return response
        if requirement == is_advanced_valid:
            if requirement(response):
                return str(round(float(response), 2))
        if requirement(response):
            return response
        elif response == "exit":
            save_and_exit()
        elif response == "shop":
            shop()
        elif response == "use":
            use_item()
        elif response == "balance":
            point_count()
        elif response == "gamble":
            gamble()
        elif response == "help":
            help()
        elif response == "height":
            current_vert()
        elif response == "details":
            details(advanced)
        elif response == "switch":
            switch()
            break
        else:
            print("Invalid response. Please try again.\n\n")

def is_advanced_valid(s):
    try:
        val = float(s)
        return 0.0 <= val <= 1.0
    except ValueError:
        return False

def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def isvalidbet(s):
    if isint(s):
        if 0 <= int(s) and int(s) <= points:
            return True
        else:
            return False
    else:
        return False

def is_owned_item(s):
    return s in items or s == "0"

def is_roulette_num(s):
    if isint(s):
        if 0 <= int(s) and int(s) <= 36:
            return True
        else:
            return False
    else:
        return

def is_std_valid(s):
    return s in ["0", "1"]

def is_shop_valid(s):
    return s in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

def is_gamble_valid(s):
    return s in ["0", "1", "2"]

def is_shopcommand_valid(s):
    return s in ["0", "1", "checkname", "checkprice", "checkattribute", "checkpurchasability"]

advanced = constrained_input("""Would you like to play in advanced mode? You will get double points.
                 
    Respond with 1 if it's a yes, or 0 if it's a no.\n\n""", is_std_valid)

details(advanced)  # just prints the details in 100 fewer lines of code

print("""
      You may type exit to exit the program. This will save your progress.
      SIMPLY CLOSING THE WINDOW NOT SAVE YOUR PROGRESS.

      TYPE 'help' TO CHECK THE HELP MENU. IT CONTAINS ALL YOUR AVAILABLE COMMANDS, AND TIPS ON HOW TO USE THEM.
      It is VERY IMPORTANT to actually enjoying this game.

      You will start with a vertical jump of 20 inches. Have fun.
      \n\n""")

emojis = ["😄","😢","😠","😨","😮","🤢","❤","🤩","🤔","😐"]

def advanced_run():
    global advanced_prompt_reached, advanced_emoji_index, points, total_points

    emoji = emojis[advanced_emoji_index]
    response = constrained_input(f"""
Prompted Text: {corpus[advanced_prompt_reached]}
Prompted Emoji: {emoji}\n\n""", is_advanced_valid)
    
    advanced_emoji_index += 1
    advanced_emoji_index %= len(emojis)

    if advanced_emoji_index == 0:
        advanced_prompt_reached += 1
    
    points += 10
    total_points += 10

    return response
    
def standard_run():
    global standard_prompt_reached, standard_emoji_index, points, total_points

    emoji = emojis[standard_emoji_index]

    response = constrained_input(f"""
Prompted Text: {corpus[standard_prompt_reached]}
Prompted Emoji: {emoji}\n\n""", is_std_valid)
    
    standard_emoji_index += 1
    standard_emoji_index %= len(emojis)

    if standard_emoji_index == 0:
        standard_prompt_reached += 1

    points += 5
    total_points += 5

    return response

while True:

    if advanced == "1":
        response = advanced_run()
        if response:
            if advanced_emoji_index:  # if the prompt hasn't switched
                with open("advanced_mode_results.txt", "a", encoding="utf-8") as f:
                    f.write(f",{str(response)}")
            else:
                with open("advanced_mode_results.txt", "a", encoding="utf-8") as f:
                    f.write(f",{str(response)}\n{corpus[advanced_prompt_reached]}")
    else:
        response = standard_run()
        if response:
            if standard_emoji_index:  # if the prompt hasn't switched
                with open("standard_mode_results.txt", "a", encoding="utf-8") as f:
                    f.write(f",{str(response)}")
            else:
                with open("standard_mode_results.txt", "a", encoding="utf-8") as f:
                    f.write(f",{str(response)}\n{corpus[standard_prompt_reached]}")