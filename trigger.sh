#!/bin/bash

nmap -sU -p53 127.0.0.1 > /dev/null 2>&1

nmap -p2049 127.0.0.1 > /dev/null 2>&1

dig google.com @127.0.0.1 -p 53 > /dev/null 2>&1

curl --user HTTP_USER:HTTP_PASS "http://127.0.0.1:80" > /dev/null 2>&1

ftp -inv 127.0.0.1 > /dev/null 2>&1 << END
user FTP_USER FTP_PASS
bye
END

echo "Triggered"
