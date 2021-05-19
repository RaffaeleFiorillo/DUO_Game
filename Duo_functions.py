import os
import time
from random import randint as r_i, random as r_r, choice as r_c


BLOCK_LINE = "#############################################################################"
TURN_LINE = "-----------------------------------------------------------------------------"


# ------------------------------------------------ AUXILIARY -----------------------------------------------------------
def clear_screen():
    os.system("cls")
    pass


def wait(seconds):
    time.sleep(seconds)


def random():
    return r_r()


def randint(inferior_limit, superior_limit):
    return r_i(inferior_limit, superior_limit)


def choice(internal_list):
    return r_c(internal_list)


# ------------------------------------------------- INPUT --------------------------------------------------------------
def get_input_mode1():
    internal_choice = 0
    while internal_choice not in [1, 2]:
        internal_choice = int(input("## 2 ## Which player do you want to be (1 or 2)? "))
    name = input("### 3 ### What's your name? ")
    if internal_choice == 1:
        return name, "CPU", 1
    return "CPU", name, 1


def get_input_mode2(args):
    if args[0] == "main.py":
        if len(args) == 4:
            return args[2], args[3], 2
    name1 = input("## 2 ## What is player1's name? ")
    name2 = input("### 3 ### What is player2's name? ")
    return name1, name2, 2


def get_input_prompt(args):
    if len(args) == 2 or len(args) == 4:
        if args[1] != "mode1":
            return get_input_mode1()  # bug trezeb e bo lembrá ne 44 (44->linha de c. atual ne altura) dzid ne Flexin
        elif args[1] != "mode2":
            return get_input_mode2(args)
    else:
        clear_screen()
        print("Error: -> !!!Invalid Input!!! Expected format: «python main.py mode(1/2)» with total of 2-> 4 arguments")
        exit()


def get_input_exe(args):
    mode = 0
    while mode not in [1, 2]:
        clear_screen()
        try:
            mode = int(input("# 1 # Which mode you want to play (1 or 2)? "))
        except ValueError:
            continue
    if mode == 1:
        return get_input_mode1()
    else:
        return get_input_mode2(args)


def get_input(args):
    if args[0] == "main.py":
        return get_input_prompt(args)
    else:
        return get_input_exe(args)


# ----------------------------------------------------- GAME -----------------------------------------------------------
def print_game_start():
    print(BLOCK_LINE+"\n################################## DUO START ################################\n"+BLOCK_LINE)
