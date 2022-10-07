# -*- coding:utf-8 -*-#
import ctypes, sys
from colorama import Back, Fore, init
init()
"""
STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12

FOREGROUND_BLUE = 0x09  # blue.
FOREGROUND_GREEN = 0x0a  # green.
FOREGROUND_RED = 0x0c  # red.
FOREGROUND_YELLOW = 0x0e  # yellow.

BACKGROUND_YELLOW = 0xe0  # yellow.
# get handle
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

def set_cmd_text_color(color, handle=std_out_handle):
    Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return Bool


# reset white
def resetColor():
    set_cmd_text_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)

"""



# green
def printGreen(mess):
    #set_cmd_text_color(FOREGROUND_GREEN)
    print(Fore.GREEN,end='')
    sys.stdout.write(mess)
    print(Fore.RESET)


# red
def printRed(mess):
    #set_cmd_text_color(FOREGROUND_RED)
    print(Fore.RED,end='')
    sys.stdout.write(mess)
    print(Fore.RESET)


# yellow
def printYellow(mess):
    #set_cmd_text_color(FOREGROUND_YELLOW)
    print(Fore.YELLOW,end='')
    sys.stdout.write(mess)
    print(Fore.RESET)


def printColor(mess, color, END):
    exec('print(Fore.'+str(color).upper()+',end=\'\')')
    sys.stdout.write(mess)
    print(Fore.RESET,end=END)

