from art import *
from time import sleep
from os import system
import sys

game_title = "Galactic Colony Manager"


#Colours
red = "\033[0;31m"
green = "\033[0;32m"
orange = "\033[0;33m"
blue = "\033[0;34m"
purple = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m" 
red2 = "\033[0;91m"
green2 = "\033[0;92m"
yellow = "\033[0;93m"
blue2 = "\033[0;94m"
magenta = "\033[0;95m"
cyan2 = "\033[0;96m"
white2 = "\033[0;97m"
available_colours = ["red", "green", "orange", "blue", "purple", "cyan", "white", "red2", "green2", "yellow", "blue2", "magenta", "cyan2", "white2"]
#Background
cyan_back="\033[0;46m"
pink_back="\033[0;45m"
blue_back="\033[0;44m"
orange_back="\033[0;43m"
green_back="\033[0;42m"
red_back="\033[0;41m"
grey_back="\033[0;40m"
available_backgrounds = ["cyan", "pink", "blue", "orange", "green", "red", "grey"]
#Other Settings
bold = "\033[1m"
underline = "\033[4m"
italic = "\033[3m"
darken = "\033[2m"
reset = "\033[0m"
available_settings = ["bold", "underline", "italic", "darken"]

#Colony Info
colony_name = ""
coloured_colony_name = ""
colony_colour = ""
colony_colour_settings = ""
colony_leader = ""
colony_flag = ""
colony_background = ""
colony_leader_background = ""
colony_motto = ""


def typewriter(text):
    for char in text:
        sleep(0.005)
        sys.stdout.write(char)
        sys.stdout.flush()

def menu():
    system('clear')
    global game_title
    text = text2art(game_title)
    print(text)
    text = "IN DEVELOPMENT"
    typewriter(text)
    print("\n1 - Create Game")
    option = input(">>> ")
    if option == "1":
        game()

def tutorial():
    system('clear')
    global game_title
    text = text2art("Tutorial") + "\n\n"
    text += "Welcome to the tutorial"
    typewriter(text)
    text = "\nIn this game, you will manage a space colony.\n"
    text += "Your goal is to build a thriving colony by managing resources, "
    text += "making strategic decisions, and overcoming challenges.\n"
    text += "Let's get started!\n"
    typewriter(text)

    # Add more tutorial content as needed

    input("\nPress Enter to continue to the game...")
    create_colony()

def game():
    system('clear')
    global game_title
    text = "Welcome to " + game_title + "!\n"
    typewriter(text)
    text = "Are you new here or have you been here before\n\n"
    typewriter(text)
    typewriter("1 - Never Played Before\n")
    typewriter("2 - I Have Played Before\n")
    choice = input(" >>> ")

    if choice == "1":
        tutorial()
    else:
        create_colony()

#Code to customise your colony
def create_colony():
    system('clear')
    text = text2art("Create Your Colony")
    text += "Start by choosing a name for your colony\n"
    text += "YOU CANNOT CHANGE THIS ONCE SET\n"
    typewriter(text)
    global colony_name
    global coloured_colony_name
    global colony_colour
    global colony_leader
    global colony_flag
    global colony_background
    global colony_leader_background
    global colony_motto
    colony_name = input("COLONY NAME >>> ")
    system('clear')
    text = "Next, let's choose a color for your colony name\n"
    text += "YOU CANNOT CHANGE THIS ONCE SET\n"
    typewriter(text)
    text = ""
    count = 1
    for n in available_colours:
        item = str(count) + "- " + n + "\n"
        text += item
        count += 1
    typewriter(text)
    color_choice = int(input("Choose Color >>> "))
    system('clear')
    colony_colour = available_colours[color_choice - 1]
    coloured_colony_name = globals()[colony_colour] + colony_name + reset
    text = "Next, let's choose a colour for your flag\n"
    text += "YOU CANNOT CHANGE THIS ONCE SET\n"
    typewriter(text)
    text = ""
    count = 1
    for n in available_colours:
        item = str(count) + "- " + n + "\n"
        text += item
        count += 1
    typewriter(text)
    color_choice = int(input("Choose Flag Colour >>> "))
    system('clear')
    colony_flag = available_colours[color_choice - 1]
    colony_flag = globals()[colony_flag] + "■■■" + reset
    text = "Next, let's choose a name for your colony leader\n"
    text += "YOU CANNOT CHANGE THIS ONCE SET\n"
    typewriter(text)
    colony_leader = input("LEADER NAME >>> ")
    system('clear')
    text = "Next, let's write a quick background about your colony\nfeel free to write as much as you want (a shorter backstory is better though)\n"
    text += "YOU CANNOT CHANGE THIS ONCE SET\n"
    typewriter(text)
    colony_background = input("COLONY BACKGROUND >>> ")
    system('clear')
    text = "Next, let's write a background for your colony leader\n"
    text += "once again, this is best kept short\n"
    text += "YOU CANNOT CHANGE THIS ONCE SET\n"
    typewriter(text)
    colony_leader_background = input("LEADER BACKGROUND >>> ")
    system('clear')
    text = "Next, let's choose a motto for your colony\n"
    text += "once again this is best kept short\n"
    text += "YOU CANNOT CHANGE THIS ONCE SET\n"
    typewriter(text)
    colony_motto = input("MOTTO >>> ")
    system('clear')
    print("COLONY >>> " + coloured_colony_name)
    print("FLAG >>> " + colony_flag)
    print("LEADER >>> " +colony_leader)
    print("BACKGROUND >>> " + colony_background)
    print("LEADER BACKGROUND >>> " + colony_leader_background)
    print("MOTTO >>> " + colony_motto)
    print("\n\n")
    typewriter("DO THESE DETAILS LOOK GOOD TO YOU\nREMEMBER YOU CANNOT CHANGE THESE ONCE YOU BEGIN\n1 - CONTINUE TO GAME\n2 - RESTART CUSTOMISATION\n")
    choice = input(" >>> ")
    if choice == "2":
        create_colony()
    else:
        hub(coloured_colony_name, colony_colour, colony_leader, colony_flag, colony_background, colony_leader_background, colony_motto)

#This is the game hub, where the user spends most their time
def hub(coloured_colony_name, colony_colour, colony_leader, colony_flag, colony_background, colony_leader_background, colony_motto):
   system('clear')
   print(colony_name, coloured_colony_name, colony_colour, colony_leader, colony_flag, colony_background, colony_leader_background, colony_motto)

menu()


