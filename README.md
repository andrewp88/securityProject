# securityProject
Automatic Penetration testing tool for wordpress 4.9 plugins.


This python 3 application allows to automatically test a vulnerability in the wordpress website based on the plugins installed.

It allows to detect possible plugins via custom detection.
  The custom detection works by path traversal that looks for not protected folders, and more efficiently it scans the references to scripts or files that could be related
  to a particular plugin.

Then it allows to attack the following plugins
https://www.exploit-db.com/exploits/42263 - SQL injection and password hash decoding using JOHN
https://www.exploit-db.com/exploits/43110 - SQL injection and password hash decoding using JOHN

https://wpvulndb.com/vulnerabilities/9088 - Stored not authenticated XSS
https://www.exploit-db.com/exploits/43420 - XSS , custom injection and cookie stealer server setup

https://www.exploit-db.com/exploits/46619 - Local File Inlcusion, via authentication.

The penetration testing tool will perform the authentication with desired data and check for it's validity when needed.


This project was done for accademic purpose and i am not responsible for any malicious use you can make out of it.
