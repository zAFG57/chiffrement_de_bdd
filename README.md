# Cryptage_de_bdd
Ce projet est un gestionnaire qui va vous permettre de crypter une base de donnée de mots de passe. Il décryptera en temps réel vos mdp en changeant les clefs à chaque utilisation. Les clefs sont stockées à moitié sur votre ordinateur et à moitié sur une clef usb ou un disque dur externe. Vous permettant d'avoir une clef physique. Ainsi, si quelqu'un a accès à votre ordinateur, il n'aura pas accès à vos mots de passe et s'il a accès à votre clef, il aura uniquement accès à des fichiers contenant une suite de caractères aléatoires. Il faudrait avoir accès aux deux pour pouvoir obtenir vos mots de passes. 

# Fonctionement et mise en action: 
Vous devez en premier lieu vous assurer que le programme tourne sur votre ordinateur dès qu'il est allumé afin d'avoir accès à vos mots de passe à chaque fois que vous en avez besoin. 

Dans le fichier variable, vous pouvez configurer les paramètres afin d'adapter cette solution à votre ordinateur et vos envies. 
Dans ce fichier, il y a ACTIVATION_SHORTCUT et STOP_SHORTCUT. 
Pour commencer à sélectionner le mot de passe que vous voulez écrire : Placez vous à l'endroit qui vous convient, écrivez ce qu'il y a dans la variable ACTIVATION_SHORTCUT. Puis cliquez sur la barre espace pour commencer la sélection. Ecrivez le mot clef qui est associé au mot de passe voulu dans le fichier json puis tapez (à la suite) ce qu'il y a dans STOP_SHORTCUT. 

Puis abracadabra, tout ce que vous venez d'écrire s'est transformé en votre mot de passe.

Parallèlement toutes vos clefs ont été changées et votre base de donnée à été chiffrée de nouveau.

# Idée de mise à jour future:
Dans le futur, je compte ajouter une nouvelle fonctionalité à ce programme: 

Pouvoir lancer des logiciels juste avec une suite de touche de frappe que l'on peut configurer à sa guise. 
Ainsi, lorsque je veux lancer vs code, au lieu de le chercher dans ma barre des taches et cliquer dessus avec ma souris, je pourrai le lancer en écrivant sur mon clavier (peu importe ce que j'étais en train de faire) ctrl + V + S

Cela pourrait me faire gagner du temps au quotidien et me permettre d'être plus efficace. 



Une autre idée de mise à jour serait de continuer à stocker la moitié des clefs dans un objet physique (cet objet physique servirait de clef d'authentification) et à stocker l'autre moitié non pas sur votre ordi mais sur un serveur distant. Cela permettra d'accéder à vos mots de passe de partout si vous avez la clef usb pour vous identifier.


[lien de la vidéo de démonstration](https://youtu.be/NoQB9mO2PnI) 
