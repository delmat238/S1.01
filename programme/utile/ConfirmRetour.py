from programme.utile.mrPropre import mrPropre

def confirmRetour():
    """Demande une entrée pour continuer
    """
    choix: str = " "
    while choix != "":
        choix = input("Appuyez sur \"Entrée\" pour continuer : ")
    mrPropre()