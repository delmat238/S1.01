import os


def mrPropre():
    """Nettoyage intégral
    """
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
