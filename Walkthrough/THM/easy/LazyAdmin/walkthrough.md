# THM - LazyAdmin
**security - webapp - boot2root - cracking**

## Enumeration
IP Address : 10.10.110.163
### 1.1 
#### nmap
**nmap -A 10.10.110.163**
	- 22 : ssh
	- 80 : http Apache httpd 2.4.18 ((Ubuntu))
### 1.2 
#### gobuster
**gobuster dir -u http://10.10.110.163 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt** 
	- /content => CMS SweetRice
    **gobuster dir -u http://10.10.110.163/content -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt**
        - /as => for connect like admin

### 1.3 
#### searchsploit
**searchsploit SweetRice** 
    SweetRice 0.5.3 - Remote File Inclusion       | php/webapps/10246.txt
    SweetRice 0.6.7 - Multiple Vulnerabilities    | php/webapps/15413.txt
    SweetRice 1.5.1 - Arbitrary File Download     | php/webapps/40698.py
    SweetRice 1.5.1 - Arbitrary File Upload       | php/webapps/40716.py
    SweetRice 1.5.1 - Backup Disclosure           | php/webapps/40718.txt
    SweetRice 1.5.1 - Cross-Site Request Forgery  | php/webapps/40692.html
    SweetRice 1.5.1 - Cross-Site Request Forgery  | php/webapps/40700.html
    SweetRice < 0.6.4 - 'FCKeditor' Arbitrary Fil | php/webapps/14184.txt

Use the 40718.txt.
In the db we found : 
    - username : manager
    - password : 42f749ade7f9e195bf475f37a44cafcb => MD-5 => Password123
With that it's possible to connect to /content/as.
It's possible to add template and probably inject a reverse shell.

### Conclusion, vulnerabilities
This CMS present serious vulnerabilities, just need to dl the db and read in order to find credentials.

## Exploit
### 1.1
#### Reverse shell
Name file reverse.php in ad rubric, and copy a revshell script.
Go to /inc to clic to the payload after open an listener server **nc -lnvp 9000**
### 1.2
#### locate
**locate user.txt**

### Conclusion
It was possible to inject revshell.

## Privilege escalation
### 1.1
#### sudo
**sudo -l**
It find a suid, just cat the file, and modify the file who is executed with '/bin/bash', execute command and a root bash appear. 

### Conclusion
With suid permission, it was possible to open an bash with root id
## Responses
### What is the user flag? : 
**THM{63e5bce9271952aad1113b6f1ac28a07}**
### What is the root flag? : 
**THM{6637f41d0177b6f37cb20d775124699f}**