from inspect import getfile
from key_loger import *
from crypto import *
from function import *
from varriable import *
from distutils.command.clean import clean
from hashlib import sha256
from os import write



data = get_file(PATH_BDD + TITLE_BDD)

# génaire la clef qui verrify l'intégriter des donnés.
hash_agains_error = sha256(data.encode()).hexdigest()

#                                                   generate key
xor_key_local = random_key(20)
xor_key_remote = random_key(20)
key_local = generate_key(xor_key_remote)
key_remote = generate_key(xor_key_local)


# chiffre la basse de donné avec les clefs
data_encoded = cripting_function(data,key_local)
data_encoded = cripting_function(data_encoded,key_remote)

data = uncripting_function(data_encoded,key_remote)
data = uncripting_function(data,key_local)
data = purify_data(data)

# enregistre les nouvelles clefs
write_key(PATH_KEY_REMOTE,key_remote)
write_key(PATH_KEY_LOCAL,key_local)
write_file(PATH_KEY_REMOTE + XOR_KEY, xor_key_remote)
write_file(PATH_KEY_LOCAL + XOR_KEY, xor_key_local)
write_file(PATH_BDD + TITLE_BDD,data_encoded)
write_file(PATH_HASH_ERROR + HASH_ERROR , hash_agains_error)