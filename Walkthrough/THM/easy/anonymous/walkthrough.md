# THM - Anonymous
**security - linux - permission - medium**

## Enumeration
IP Address : 10.10.206.39
### 1.1 
#### nmap
./nmap_output.txt
### 1.2 
#### ftp
**ftp $IP** 
It's possible to connect with anonymous/anonymous.
### Conclusion, vulnerabilities
Maybe ftp protocol could be exploited. I found a todo.txt saying admin need to remove anonymous access.  
## Exploit
### 1.1
#### Exploit db
https://www.exploit-db.com/exploits/50720

### Conclusion

## Privilege escalation
### 1.1
#### sudo
**find / -perm -4000 -print 2>&1**

### Conclusion
With suid permission, it was possible to open an bash with root id
## Responses
### Scan the box, how many ports are open? : 
**6**
### What version of the squid proxy is running on the machine? : 
**3.5.12**
### How many ports will nmap scan if the flag -p-400 was used? : 
**400**
### Using the nmap flag -n what will it not resolve? : 
**DNS**
### What is the most likely operating system this machine is running? : 
**Ubuntu**
### What port is the web server running on? : 
**3333**
### What is the directory that has an upload form page? : 
**/internal/**
### Run this attack, what extension is allowed? : 
**.phtml**
### What is the name of the user who manages the webserver? : 
**bill**
### What is the user flag? : 
**8bd7992fbe8a6ad22a63361004cfcedb**
### On the system, search for all SUID files. What file stands out? : 
**/bin/systemctl**
### Become root and get the last flag (/root/root.txt) : 
**a58ff8579f0a9270368d33a9966c7fd5**
