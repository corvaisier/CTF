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
#### reverse shell
Get clean.sh, modify whith reverse bash command and because it's a cron, just need to listen to have a reverse shell. 

### Conclusion

## Privilege escalation
### 1.1
#### sudo
**find / -perm -u=s -type f 2>/dev/null**
/bin/env seem interesting ! Go to GTFObins and find **./env /bin/sh -p** and im root !
### Conclusion
With suid permission, it was possible to escalate !
## Responses
### Enumerate the machine.  How many ports are open? : 
**4**
### What service is running on port 21? : 
**ftp**
### What service is running on ports 139 and 445? : 
**smb**
### There's a share on the user's computer.  What's it called? : 
**DNS**
### What is the most likely operating system this machine is running? : 
**pics**
### user.txt : 
**90d6f992585815ff991e68748c414740**
### root.txt : 
**4d930091c31a622a7ed10f27999af363**
