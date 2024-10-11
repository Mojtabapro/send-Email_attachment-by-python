from colorama import Fore
import sys

def ResetColorText():
    print(f"{Fore.RESET()}")


def TextSeparator():
    print(f"{Fore.LIGHTCYAN_EX}={Fore.RESET}" * 50)

def PrintError(e):
    print(f"{Fore.RED}Error: {Fore.LIGHTRED_EX}{e}{Fore.RESET}")


def PrintSuccessText(Text):
    print(f"{Fore.GREEN}{Text}{Fore.RESET}")


def ExitProgram():
    sys.exit(0)