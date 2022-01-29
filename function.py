from string import ascii_letters, digits,punctuation
from os import listdir , remove , startfile
from crypto import Crypto
import keyboard
import json
import random
import sys

from varriable import KEY_EXTENTION, NOMBER_OF_KEY, XOR_KEY , EXE_BDD_PATH

def delete_key(location,key):
    for i in range(NOMBER_OF_KEY):
        delete(location + key[i][1])

def get_file(location):
    file = open(location, "r")
    content = file.read()
    file.close()
    return content

def key_dictionnaire(location,other_location):
    fichier = listdir(location)
    key = {}
    for i in fichier:
        if i.endswith(KEY_EXTENTION):
            key.update({int(Crypto(get_file(other_location + XOR_KEY)).decrypteData(i.replace(KEY_EXTENTION,''))):[get_file(location + i),i]})
    return key

def uncripting_function(data_encoded,key:dict):
    for i in range(NOMBER_OF_KEY):
        data_encoded = Crypto(key[i][0]).decrypteData(data_encoded)
    return data_encoded

def cripting_function(data,key:dict):
    for i in reversed(range(NOMBER_OF_KEY)):
        data = Crypto(key[i][0]).encryptData(data)
    return data

def random_key(nomber = 2**15):
    if nomber == 2**15:
        return "".join(random.choice(ascii_letters + digits + punctuation) for _ in range(2**15))
    return 'a' + "".join(random.choice(ascii_letters) for _ in range(nomber)) + 'a'

def write_key(location,key):
    for i in range(NOMBER_OF_KEY):
        write_file(location + key[i][1] + KEY_EXTENTION, key[i][0])

def write_file(location,content):
    file = open(location,"w" ,encoding="ASCII")
    file.write(content)
    file.close()

def delete(location):
    remove(location)

def get_password(data,key_word):
    json_data = json.loads(data)
    password = json_data[key_word]
    return password

def écrir_le_mdp(password): 
    keyboard.press_and_release('ctrl+a')
    keyboard.press_and_release('backspace')
    keyboard.write(password)

def stop_programe():
    print("this program is down, if you want to make it up again, please execute one's again the main.")
    sys.exit()

def generate_key(xor_key):
    key = {}
    for i in reversed(range(NOMBER_OF_KEY)):
        key.update({i:[random_key(),Crypto(xor_key).decrypteData(str(i))]})
    return key

def purify_data(data):
    n = ((data.encode('ascii')).replace(b'\x00', b'').replace(b'\x07', b'')).decode('ascii')
    return n

def clean_the_back_up(path): 
    file = listdir(path)
    if 'remote' in file:
        file.remove('remote')
    for i in file:
        delete(path + i)

def get_link(key_word):
    data = get_file(EXE_BDD_PATH)
    data = json.loads(data)
    link = data[key_word]
    return link

def execute_file(path):
    startfile(path)