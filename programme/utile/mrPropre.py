import os


def mrPropre():
    """Nettoyage intégral du terminal
    """
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
