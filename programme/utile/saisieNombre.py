def saisieInt(message: str, erreur: str):
    """Saisie d'un nombre entier"""
    nombre: int
    while True:
        try:
            nombre = int(input(message))
            return nombre
        except ValueError:
            print(erreur)


def saisieFloat(message: str, erreur: str):
    """Saisie d'un nombre réel"""
    nombre: float
    while True:
        try:
            nombre = float(input(message))
            return nombre
        except ValueError:
            print(erreur)