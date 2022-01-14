# cryptage_de_bdd
ce project est un gestionnaire qui va vous permettre de crypter une base de donner de mots de passe. Il décryptera en temps réel vos mdp en changeant les clefs à chaque utilisation. Les clefs sont stocker a moitier sur votre ordinateur et a moitier sur un clef usb ou un disque dur externe. Vous permettant d'avoir une clef physique. Ainsi, si qu'ellequ'un a accès a votre ordinateur, il n'aura pas accès à vos mots de passe et si il a accès a votre clef, il aurat juste accès a des fichier contenant une suite de carractère aléatoir. Ils faudrait avoir accès au deux pour pouvoir obtenir vos mots de passe. 

# fonctionement et mise en action: 
vous devez en premier lieu vous assurez que le programe tourn sur votre ordinateur à chaque fois qu'il est allumé affin d'avoir accès a vos mots de passe à chaque fois que vous en avez besoin. 

dans le fichier varriable, vous pouvez configuer les paramètre affin d'adapté cette sollution à votre ordinateur et vos envie. 
dans ce fichier, il y a ACTIVATION_SHORTCUT et STOP_SHORTCUT. 
Pour commencer a sélectionner quelle mots de passe vous vouler écrir, écriver la ou vous voulez que le mots de passe soit écrit ce qu'il y a dans la varriable ACTIVATION_SHORTCUT. Puis apuiller sur la bar espace pour commencer la sélection. Puis taper le mots clef qui est associer au mots de passe voulu dans le fichier json puis taper (à la suite) ce qu'il y à dans STOP_SHORTCUT. 

Puis abracadabra, tout ce que vous venez d'écrire c'est transformer en votre mots de passe.

de plus, toutes vos clefs ont été changé et votre basse de donné à été chiffré de nouveau.
