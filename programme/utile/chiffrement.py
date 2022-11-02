from hashlib import sha256
import os

def decrytion(filepath:str)->str:
    """Use autoDocstring extension to complete"""
    
    jsondata:str = ""

    key : hash = sha256(('key').encode('utf-8')).digest() # 'key' représente la clé de chiffrement utilisée

    with open(filepath, "rb") as rfile:
        while rfile.peek():
            i=0
            while rfile.peek():
                unicode = ord(rfile.read(1))
                b = bytes([unicode^key[(i % len(key))]])
                jsondata = jsondata + b.decode('utf-8')
                i=i+1
    
    return jsondata

def encryption(filepath:str):
    """Use autoDocstring extension to complete"""
    
    key : hash = sha256(('key').encode('utf-8')).digest() # 'key' représente la clé de chiffrement utilisée

    with open(filepath,'rb') as rfile:
                with open("programme/joueur/scores",'wb') as wfile:
                    i=0
                    while rfile.peek():
                        unicode = ord(rfile.read(1))
                        b = bytes([unicode^key[i % len(key)]])
                        wfile.write(b)
                        i=i+1
    os.remove(filepath)

if __name__ == "__main__":
    print(decrytion("programme/joueur/scores"))