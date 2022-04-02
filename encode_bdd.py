from selection import *
from crypto import *
from function import *
from varriable import *
from distutils.command.clean import clean
from hashlib import sha256


def encode_bdd():
        bdd = get_file(PATH_BDD + TITLE_BDD)

        def hash(data):
            # génère la clef qui verrifie l'intégrité des données.
            hash_agains_error = sha256(data.encode()).hexdigest()

            # generate key
            xor_key_local = random_key(20)
            xor_key_remote = random_key(20)
            key_local = generate_key(xor_key_remote)
            key_remote = generate_key(xor_key_local)

            # chiffre la base de données avec les clefs
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

        def verify():
            # récupère le titre des clefs remote et local plus leurs contenus
            key_local = key_dictionnaire(PATH_KEY_LOCAL,PATH_KEY_REMOTE)
            key_remote = key_dictionnaire(PATH_KEY_REMOTE,PATH_KEY_LOCAL)
            data_encoded = get_file(PATH_BDD + TITLE_BDD)
            # get the hach key to prevent error
            hash_agains_error = get_file(PATH_HASH_ERROR + HASH_ERROR)
            # décriptage de la bdd
            data = uncripting_function(data_encoded,key_remote)
            data = uncripting_function(data,key_local)
            data = purify_data(data)
            if sha256(data.encode()).hexdigest() == hash_agains_error:
                return 0
            else:
                delete_key(PATH_KEY_LOCAL ,key_local)
                delete_key(PATH_KEY_REMOTE ,key_remote)
                delete(PATH_BDD + TITLE_BDD)
                delete(PATH_KEY_LOCAL + XOR_KEY)
                delete(PATH_KEY_REMOTE + XOR_KEY)
                delete(PATH_HASH_ERROR + HASH_ERROR)
                return 1

        def made_back_up():
            clean_the_back_up(PATH_BACKUP)
            clean_the_back_up(PATH_BACKUP_REMOTE)
            write_key(PATH_BACKUP_REMOTE,key_dictionnaire(PATH_KEY_REMOTE,PATH_KEY_LOCAL))
            write_key(PATH_BACKUP,key_dictionnaire(PATH_KEY_LOCAL,PATH_KEY_REMOTE))
            write_file(PATH_BACKUP_REMOTE + XOR_KEY, get_file(PATH_KEY_REMOTE + XOR_KEY))
            write_file(PATH_BACKUP + XOR_KEY, get_file(PATH_KEY_LOCAL + XOR_KEY))
            write_file(PATH_BACKUP_REMOTE + TITLE_BDD,get_file(PATH_BDD + TITLE_BDD))

        a = 1
        while a:
            hash(bdd)
            a = verify()
        made_back_up()
        delete_key(PATH_KEY_LOCAL ,key_dictionnaire(PATH_KEY_LOCAL,PATH_KEY_REMOTE))
        delete_key(PATH_KEY_REMOTE ,key_dictionnaire(PATH_KEY_REMOTE,PATH_KEY_LOCAL))
        delete(PATH_BDD + TITLE_BDD)
        delete(PATH_KEY_LOCAL + XOR_KEY)
        delete(PATH_KEY_REMOTE + XOR_KEY)
        delete(PATH_HASH_ERROR + HASH_ERROR)
        a =1
        while a:
            hash(bdd)
            a = verify()    

encode_bdd()
