from unittest import case

if __name__ == '__main__':
    choix: str = ""

    while choix != "4":
        print("""
    1. Devinette
    2. Allumette
    3. Morpion
    4. Quitter   
        """)


        choix = input("Faites votre choix : ")

        match choix:
            case "4": print("Au revoir")

