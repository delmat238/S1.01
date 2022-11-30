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
    key: hash = sha256(('key').encode('utf-8')).digest() #On génère le hash de la clé

    with open(filepath, "rb") as rfile:
        i = 0
        while rfile.peek():
            unicode = ord(rfile.read(1)) #On lit caractère par caractère
            b = bytes([unicode ^ key[(i % len(key))]]) #On XOR le caractère avec le rang de la clé égal à i modulo sa longeur
            try:
                jsondata = jsondata + b.decode('utf-8') #On vérifie que la chaine obtenue est lisible
            except UnicodeDecodeError:
                error = True
            i = i+1
    if error:
        print(textform.ERROR+"Le fichier de sauvegarde est endommagé, une réparation va être effectuée"+textform.DEFAULT) #Réparation si dommages
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
        with open("programme/joueur/scores.dat", 'wb') as wfile:
            i = 0
            while rfile.peek():
                unicode = ord(rfile.read(1)) #On lit caractère par caractère
                b = bytes([unicode ^ key[i % len(key)]]) #On XOR le caractère avec le rang de la clé égal à i modulo sa longeur
                wfile.write(b) #On écrit le contenu dans le fichier
                i = i+1
    os.remove(filepath)


def repair():
    """Permet la création ou la réparation d'une sauvegarde
    """
    data = json.loads("{\"players\":{}}")   #On génère une chaine json attendue vierge
    with open("programme/joueur/scores.json", "w") as w_score_file: #On l'inscrit dans le fichier
        json.dump(data, w_score_file, indent=4)
    encryption("programme/joueur/scores.json") #On chiffre le fichier
    print("\n"+textcolor.GREEN+"Nouvelle sauvegarde crée"+textcolor.DEFAULT+"\n")
