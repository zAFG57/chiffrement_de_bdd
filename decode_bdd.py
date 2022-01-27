from hashlib import sha256
from selection import *
from crypto import *
from function import *
from varriable import *


#                                                    récupère le titres des clefs remote et local plus leurs contenu

key_local = key_dictionnaire(PATH_KEY_LOCAL,PATH_KEY_REMOTE)
key_remote = key_dictionnaire(PATH_KEY_REMOTE,PATH_KEY_LOCAL)
delete_key(PATH_KEY_LOCAL ,key_local)
delete_key(PATH_KEY_REMOTE ,key_remote)


data_encoded = get_file(PATH_BDD + TITLE_BDD)

#                                                    get the hach key to prevent error

hash_agains_error = get_file(PATH_HASH_ERROR + HASH_ERROR)

#                                                    décriptage de la bdd

data = uncripting_function(data_encoded,key_remote)
data = uncripting_function(data,key_local)
data = purify_data(data)
if sha256(data.encode()).hexdigest() == hash_agains_error:
    clean_the_back_up(PATH_BACKUP)
    clean_the_back_up(PATH_BACKUP_REMOTE)
    write_key(PATH_BACKUP_REMOTE,key_remote)
    write_key(PATH_BACKUP,key_local)
    write_file(PATH_BACKUP_REMOTE + XOR_KEY, get_file(PATH_KEY_REMOTE + XOR_KEY))
    write_file(PATH_BACKUP + XOR_KEY, get_file(PATH_KEY_LOCAL + XOR_KEY))
    write_file(PATH_BACKUP_REMOTE + TITLE_BDD,data_encoded)
else:
    data_encoded = get_file(PATH_BACKUP_REMOTE + TITLE_BDD)
    key_local = key_dictionnaire(PATH_BACKUP,PATH_BACKUP_REMOTE)
    key_remote = key_dictionnaire(PATH_BACKUP_REMOTE,PATH_BACKUP)
    data = uncripting_function(data_encoded,key_remote)
    data = uncripting_function(data,key_local)
    data = purify_data(data)



delete(PATH_BDD + TITLE_BDD)
delete(PATH_KEY_LOCAL + XOR_KEY)
delete(PATH_KEY_REMOTE + XOR_KEY)
delete(PATH_HASH_ERROR + HASH_ERROR)

write_file(PATH_BDD + TITLE_BDD,data)