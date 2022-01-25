from os import remove
from selectors import SelectSelector
from pynput.keyboard import Key, Listener
from varriable import ACTIVATION_SHORTCUT , STOP_SHORTCUT
from function import stop_programe

class key_logeur:

    def __init__(self):
        self.nombre = 0
        self.codenl = ACTIVATION_SHORTCUT
        self.code = [][:0] = self.codenl
        self.pas_trouver = True

    def to_string(x,letter):
        return f"'{letter}'"

    def la_lettre(x,nombre):
        letter = key_loger.code[nombre]
        return letter

    def on_release(x,key):
        lettre = str(key)
        if key == Key.esc:
            stop_programe()
        if len(key_loger.code) == key_loger.nombre:
            key_loger.pas_trouver = False
            key_loger.nombre = 0
            key_loger.code = [][:0] = key_loger.codenl
            return key_loger.pas_trouver
        elif lettre == key_loger.to_string(key_loger.la_lettre(key_loger.nombre)):
            key_loger.nombre += 1
        else:
            key_loger.nombre = 0

    def cherche(x):
        if key_loger.pas_trouver:
            with Listener(on_release = key_loger.on_release) as listener:
                listener.join()
                
key_loger = key_logeur()

class sélection:

    def __init__(self):
        self.nomber = 0
        self.codenl = STOP_SHORTCUT
        self.code = [][:0] = self.codenl
        self.continu = True
        self.key_word = ''

    def la_lettre(x,nombre):
        letter = selection.code[nombre]
        return letter

    def make_selection(x,key):
        selection.key_word = (selection.key_word + str(key)).replace("'",'').replace("Key.space",' ')

    def remove_shortcut(x):
        selection.key_word = selection.key_word.replace(STOP_SHORTCUT,'').replace('Key.enter','').replace('Key.space','')

    def record(x,key):
        letter = str(key).replace("'",'')
        selection.make_selection(key)
        if key == Key.backspace:
            selection.nomber = 0
            selection.key_word = ''
        if key == Key.esc:
            stop_programe()
        if len(selection.code) == selection.nomber:
            selection.remove_shortcut()
            selection.continu = False
            selection.nomber = 0
            selection.code = [][:0] = selection.codenl
            return selection.continu
        elif letter == selection.la_lettre(selection.nomber):
            selection.nomber += 1
        else:
            selection.nomber = 0

    def cherche(x):
        if selection.continu:
            with Listener(on_release = selection.record) as listener:
                listener.join()
        return selection.key_word
selection = sélection()