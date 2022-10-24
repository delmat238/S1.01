import os


def mrPropre():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
