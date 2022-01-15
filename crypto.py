from base64 import b64decode, b64encode
from random import choice

from pynput.keyboard import Key

class Crypto(object):
    def __init__(self, key = None):
        self.key = key
    
    def encryptData(self, data : str):       
        intData = int.from_bytes((data.encode()), 'big')
        intKey = int.from_bytes((self.key.encode()), 'big')
        dataEncryptedInt = intData ^ intKey       
        dataEncrypted = dataEncryptedInt.to_bytes((dataEncryptedInt.bit_length() + 7) // 8, 'big').decode()
        return dataEncrypted

    def decrypteData(self, dataEncrypted : str):
        intDataEncrypted = int.from_bytes(dataEncrypted.encode(), 'big')
        intKey = int.from_bytes((self.key.encode()), 'big')
        decriptedDataInt = intDataEncrypted ^ intKey
        dataDecrypted = (decriptedDataInt.to_bytes((decriptedDataInt.bit_length() + 7) // 8, 'big')).decode()
        return dataDecrypted


