from hashlib import sha256
import os
import json
from programme.utile.colorfull import *


def decrytion(filepath: str) -> str:
    """Renvoie les éléments déchiffrés contenus dans un fichier

    Args:
        filepath (str): Chemin vers le fichier chiffré

    Returns:
        str: Chaine (format json) contenant les données de score
    """
    error: bool = False
    jsondata: str = ""
    i: int
    unicode: int
    b: bytes

    # 'key' représente la clé de chiffrement utilisée
    key: hash = sha256(('key').encode('utf-8')).digest()

    with open(filepath, "rb") as rfile:
        while rfile.peek():
            i = 0
            while rfile.peek():
                unicode = ord(rfile.read(1))
                b = bytes([unicode ^ key[(i % len(key))]])
                try:
                    jsondata = jsondata + b.decode('utf-8')
                except UnicodeDecodeError:
                    error = True
                i = i+1

    if error:
        print(textform.ERROR+"Le fichier de sauvegarde est endommagé, une réparation va être effectuée"+textform.DEFAULT)
        repair()
        jsondata = decrytion(filepath)

    return jsondata


def encryption(filepath: str):
    """Remplace le fichier entré par un équivalent chiffré

    Args:
        filepath (str): Chemin vers le fichier chiffré
    """

    i: int
    unicode: int
    b: bytes

    # 'key' représente la clé de chiffrement utilisée
    key: hash = sha256(('key').encode('utf-8')).digest()

    with open(filepath, 'rb') as rfile:
        with open("programme/joueur/scores", 'wb') as wfile:
            i = 0
            while rfile.peek():
                unicode = ord(rfile.read(1))
                b = bytes([unicode ^ key[i % len(key)]])
                wfile.write(b)
                i = i+1
    os.remove(filepath)


def repair():
    data = json.loads("{\"players\":{}}")
    with open("programme/joueur/scores.json", "w") as w_score_file:
        json.dump(data, w_score_file, indent=4)
    encryption("programme/joueur/scores.json")
    print("\n"+textcolor.GREEN+"Réparation Terminée"+textcolor.DEFAULT+"\n")
