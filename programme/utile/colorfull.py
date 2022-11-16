# Contient les éléments "cosmétiques" des affichages

class textform:
    # utiles
    WARNING = '\033[93m'
    ERROR = '\033[91m'

    # format
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    # defaut
    DEFAULT = '\033[0m'


class textcolor:

    # couleurs
    RED = '\033[31m'
    YELLOW = '\033[33m'
    GREEN = '\033[32m'
    CYAN = '\033[36m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    PINK = '\033[95m'
    GREY = '\033[37m'
    BLACK = '\033[30m'

    # defaut
    DEFAULT = '\033[0m'


class bgcolor:

    # couleurs
    BLACK = '\033[40m'
    RED = '\033[41m'
    YELLOW = '\033[43m'
    GREEN = '\033[42m'
    CYAN = '\033[46m'
    BLUE = '\033[44m'
    PURPLE = '\033[45m'
    GREY = '\033[47m'


def colorfull():
    """Display all colorfull options"""

    print(textform.WARNING+"Warning"+textform.DEFAULT)
    print(textform.ERROR+"Error"+textform.DEFAULT)

    print(textform.BOLD+"Bold"+textform.DEFAULT)
    print(textform.UNDERLINE+"Underline"+textform.DEFAULT)

    print(textcolor.RED+"Red"+textcolor.DEFAULT)
    print(textcolor.YELLOW+"Orange"+textcolor.DEFAULT)
    print(textcolor.GREEN+"Green"+textcolor.DEFAULT)
    print(textcolor.CYAN+"Cyan"+textcolor.DEFAULT)
    print(textcolor.BLUE+"Blue"+textcolor.DEFAULT)
    print(textcolor.PURPLE+"Purple"+textcolor.DEFAULT)
    print(textcolor.PINK+"Pink"+textcolor.DEFAULT)
    print(textcolor.GREY+"Grey"+textcolor.DEFAULT)
    print(textcolor.BLACK+"Black"+textcolor.DEFAULT)
    print(textcolor.DEFAULT+"Defaut"+textcolor.DEFAULT)

    print(bgcolor.RED+"RedBG"+bgcolor.BLACK)
    print(bgcolor.YELLOW+"OrangeBG"+bgcolor.BLACK)
    print(bgcolor.GREEN+"GreenBG"+bgcolor.BLACK)
    print(bgcolor.CYAN+"CyanBG"+bgcolor.BLACK)
    print(bgcolor.BLUE+"BlueBG"+bgcolor.BLACK)
    print(bgcolor.PURPLE+"PurpleBG"+bgcolor.BLACK)
    print(bgcolor.GREY+"GreyBG"+bgcolor.BLACK)
    print(bgcolor.BLACK+"BlackBG"+bgcolor.BLACK)


class maintexts:
    MP = """                                        
     _____                _____     _         _         _ 
    |     |___ ___ _ _   |  _  |___|_|___ ___|_|___ ___| |
    | | | | -_|   | | |  |   __|  _| |   |  _| | . | .'| |
    |_|_|_|___|_|_|___|  |__|  |_| |_|_|_|___|_|  _|__,|_|
                                               |_|        
                                               """

    MS="""
     _____                         
    /  ___|                        
    \ `--.  ___ ___  _ __ ___  ___ 
     `--. \/ __/ _ \| '__/ _ \/ __|
    /\__/ / (_| (_) | | |  __/\__ \ 
    \____/ \___\___/|_|  \___||___/
                               """