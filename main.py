from key_loger import *
from crypto import *
from function import *
from varriable import *
from distutils.command.clean import clean
from hashlib import sha256
from os import write



class passd_secure():
    def __init__(self):
        self.loop = 1
    
    def start(self):
            key_loger.cherche()                     # attend l'activation du shortcut

            #    récupère les clef et la bdd
            key_local = key_dictionnaire(PATH_KEY_LOCAL,PATH_KEY_REMOTE)
            key_remote = key_dictionnaire(PATH_KEY_REMOTE,PATH_KEY_LOCAL)
            data_encoded = get_file(PATH_BDD + TITLE_BDD)

            #                                       get the hash key to prevent error

            hash_agains_error = get_file(PATH_HASH_ERROR + HASH_ERROR)

            #                                        décriptage de la bdd

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
                # updating back up
            else:
                # using back up
                data_encoded = get_file(PATH_BACKUP_REMOTE + TITLE_BDD)
                key_local_b = key_dictionnaire(PATH_BACKUP,PATH_BACKUP_REMOTE)
                key_remote_b = key_dictionnaire(PATH_BACKUP_REMOTE,PATH_BACKUP)
                data = uncripting_function(data_encoded,key_remote_b)
                data = uncripting_function(data,key_local_b)
                data = purify_data(data)

            #              selection du mdp

            key_word = selection.cherche().replace(' ','')
            password = get_password(data,key_word)

            #                                                    on écrit le mdp
            écrir_le_mdp(password)

            # supprime les anciènnes clef
            delete_key(PATH_KEY_LOCAL ,key_local)
            delete_key(PATH_KEY_REMOTE ,key_remote)
            delete(PATH_BDD + TITLE_BDD)
            delete(PATH_HASH_ERROR + HASH_ERROR)

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
            self.loop = 0



main = passd_secure()
main.start()