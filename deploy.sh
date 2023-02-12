#!/bin/bash
blue() { echo -e "\033[34m [ $1 ] \033[0m" ; }
green() { echo -e "\033[32m [ $1 ] \033[0m" ; }
yellow() { echo -e "\033[33m [ $1 ] \033[0m" ; }
red() { echo -e "\033[31m [ $1 ] \033[0m" ; }

blue "HumblePot Deployment"

# Requesting Creds
echo "SMTP configuration."
read -p "SMTP Host: " host
read -p "SMTP User: " user
read -p "SMTP Pass: " pass
yellow "Host: $host User: $user Pass: $pass"
echo "Email configuration."
read -p "Sender e-mail: " from
read -p "Recipient e-mail: " to
yellow "Sender: $from Recipient: $to"

echo "Select the modules"

read -p "TCP [Yn]: " module_tcp
if [ "$module_tcp" != "y" ] && [ "$module_tcp" != "Y" ]
then
	red 'TCP module not installed'
else
    cat template.service | sed 's/<HOSTNAME-HERE>/'$host'/g;s/<USERNAME-HERE>/'$user'/g;s/<PASSWORD-HERE>/'$pass'/g;s/<FROM-HERE>/'$from'/g;s/<TO-HERE>/'$to'/g;s/<SCRIPT-HERE>/tcp/g' > /etc/systemd/system/humblepot-tcp.service
    green 'TCP module installed'
fi

read -p "FTP [Yn]: " module_ftp
if [ "$module_ftp" != "y" ] && [ "$module_ftp" != "Y" ]
then
	red 'FTP module not installed'
else
    cat template.service | sed 's/<HOSTNAME-HERE>/'$host'/g;s/<USERNAME-HERE>/'$user'/g;s/<PASSWORD-HERE>/'$pass'/g;s/<FROM-HERE>/'$from'/g;s/<TO-HERE>/'$to'/g;s/<SCRIPT-HERE>/ftp/g' > /etc/systemd/system/humblepot-ftp.service
    green 'FTP module installed'
fi

read -p "HTTP [Yn]: " module_http
if [ "$module_http" != "y" ] && [ "$module_http" != "Y" ]
then
	red 'HTTP module not installed'
else
    cat template.service | sed 's/<HOSTNAME-HERE>/'$host'/g;s/<USERNAME-HERE>/'$user'/g;s/<PASSWORD-HERE>/'$pass'/g;s/<FROM-HERE>/'$from'/g;s/<TO-HERE>/'$to'/g;s/<SCRIPT-HERE>/http/g' > /etc/systemd/system/humblepot-http.service
    green 'HTTP module installed'
fi

read -p "DNS [Yn]: " module_dns
if [ "$module_dns" != "y" ] && [ "$module_dns" != "Y" ]
then
	red 'DNS module not installed'
else
    cat template.service | sed 's/<HOSTNAME-HERE>/'$host'/g;s/<USERNAME-HERE>/'$user'/g;s/<PASSWORD-HERE>/'$pass'/g;s/<FROM-HERE>/'$from'/g;s/<TO-HERE>/'$to'/g;s/<SCRIPT-HERE>/dns/g' > /etc/systemd/system/humblepot-dns.service
    green 'DNS module installed'
fi

read -p "Snitch [Yn]: " module_snitch
if [ "$module_snitch" != "y" ] && [ "$module_snitch" != "Y" ]
then
	red 'Snitch module not installed'
else
    cat template.service | sed 's/<HOSTNAME-HERE>/'$host'/g;s/<USERNAME-HERE>/'$user'/g;s/<PASSWORD-HERE>/'$pass'/g;s/<FROM-HERE>/'$from'/g;s/<TO-HERE>/'$to'/g;s/<SCRIPT-HERE>/snitch/g' > /etc/systemd/system/humblepot-snitch.service
    green 'Snitch module installed'
fi

systemctl daemon-reload

echo ''
blue 'Use the following commands to start each module:'
echo ''
echo 'systemctl start humblepot-tcp'
echo 'systemctl start humblepot-ftp'
echo 'systemctl start humblepot-http'
echo 'systemctl start humblepot-dns'
echo 'systemctl start humblepot-snitch'
echo ''
blue 'Installation completed'
echo ''

exit 0
