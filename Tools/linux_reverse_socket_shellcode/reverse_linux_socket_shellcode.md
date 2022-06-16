Ici nous allons utiliser le principe de socket. Un socket est un point de terminaison de communication réseau virtuel. Il est défini par son descripteur de fichier et ses propriétés, qui sont définies lors de la création du socket, afin que le système puisse s'y référer. Il s'appuie sur le protocole TCP.
Pour aller plus loin sur les sockets : https://man7.org/linux/man-pages/man2/socket.2.html

La fonction socket() crée une socket et renvoie le descripteur de fichier.
La prochaine étape pour le socket sera de déclarer sa destination. Que le socket soit utilisé sur le client ou sur le serveur a un impact significatif.
Si le socket doit être un socket client, il faut spécifier l'adresse et le port requis. Une fois la connexion établie, la communication bidirectionnelle peut commencer.
Si le socket est destiné à être un socket serveur, son adresse locale et son port doivent être spécifiés. Le socket est lié au port et à l'adresse IP spécifiés d'une interface particulière.
La socket serveur est alors placée dans l'état d'écoute. Il doit accepter () une connexion entrante avant que la communication bidirectionnelle avec le client puisse commencer.
Dans le cas d'une connexion shell inversée, nous créerons un socket client qui se connecte à l'écouteur netcat de la machine de l'attaquant.
De retour au socket, il est identifié par un descripteur de fichier, qui est une poignée virtuelle utilisée pour accéder aux opérations d'E/S spécifiques d'un processus.

Le chemin /proc/pid/fd nous permet de consulter les descripteurs de fichiers, et la commande ``echo $$`` affiche le PID en cours.
Un processus a des descripteurs de fichier pour l'entrée standard (stdin - fd0), la sortie standard (stdout - fd1) et l'erreur standard (stderr - fd2) par défaut.
Le stdin => entrée utilisateur, par exemple clavier.
Les stdout et stderr sont les données qui sont retournées à l'utilisateur, et c'est le programme qui en détermine le traitement.

En dupliquant les descripteurs de fichiers distants, la sortie (ou les erreurs) des commandes exécutées sera également envoyée à notre socket, qui transmettra ensuite les données à travers le réseau à notre machine attaquante.

Pour créer un shellcode reverse shell, nous devons :

 - Créer un socket compatible avec TCP
 - Connectez-le à l'attaquant.
 - Dupliquez les descripteurs de fichier de stdin, stdout et stderr dans le socket du shell inversé, cela doit en fait être fait avant que bash ne soit généré, sinon après l'appel de bash, nous ne pourrons pas accéder à ses descripteurs.
 - Faire apparaître un shell bash.

 Il faut donc compliler le fichier linux_socket_shell.c une fois renseigné l'adresse IP souhaitée, lancer la commande ``nc -nvlp 4444``, et lancer le programme compilé ``./linux_socket_shell``
