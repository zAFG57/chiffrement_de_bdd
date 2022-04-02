from os import write
from key_loger import *
from crypto import *
from function import *
from varriable import *


key_loger.cherche()
#                                                    récupère le titre des clefs remote et local plus leurs contenus

key_local = key_dictionnaire(PATH_KEY_LOCAL,PATH_KEY_REMOTE)
key_remote = key_dictionnaire(PATH_KEY_REMOTE,PATH_KEY_LOCAL)

data_encoded = get_file(PATH_BDD + TITLE_BDD)
#                                                    décryptage de la bdd

data = uncripting_function(data_encoded,key_remote)
data = uncripting_function(data,key_local)
data = purify_data(data)
#                                                    sélection du mdp

key_word = selection.cherche().replace(' ','')
password = get_password(data,key_word)

#                                                    on écrit le mdp
écrir_le_mdp(password)

#                                                    on encrypte de nouveau la bdd avec une nouvelle clef

delete_key(PATH_KEY_LOCAL ,key_local)
delete_key(PATH_KEY_REMOTE ,key_remote)
delete(PATH_BDD + TITLE_BDD)

xor_key_local = random_key(20)
xor_key_remote = random_key(20)

key_local = generate_key(xor_key_remote)
key_remote = generate_key(xor_key_local)

write_key(PATH_KEY_REMOTE,key_remote)
write_key(PATH_KEY_LOCAL,key_local)
write_file(PATH_KEY_REMOTE + XOR_KEY, xor_key_remote)
write_file(PATH_KEY_LOCAL + XOR_KEY, xor_key_local)

data_encoded = cripting_function(data,key_local)
data_encoded = cripting_function(data_encoded,key_remote)

write_file(PATH_BDD + TITLE_BDD,data_encoded)


#                                                    on enregistre la clef



