# humble-pot

Humble-Pot is a lightweight (canary mine) honey-pot application.

A fully-fledged honey-pot appliance such as [tpotce](https://github.com/telekom-security/tpotce) or [opencanary](https://github.com/thinkst/opencanary) can be incredibly complex and full of features but also requires a lot of computing resources of a dedicated machine to run it on.

On the other hand, Humble-Pot was designed to run in a stand-alone server or as a container, sharing resources with other applications.

It required only a single core and almost no RAM to run. These characteristics make it great for using the idle capacity of an existing server.

E.g. for instance an FTP server gets tentatives to connect on the HTTP port.

## Use Cases

![Network Architecture](https://github.com/davift/humble-pot/raw/main/humble-pot.drawio.png)

On the Private side of the illustration, the honey-pot is sharing idle resources from existent servers and would flag when a connection attempt happens on the unexpected port. It could be caused by malware or a threat actor, for example.

On the DMZ side of the illustration, the honey-pot is in a dedicated machine and would inform it the DMZ got compromised, and the threat actor is trying to move laterally.

## Features

It is capable of alerting when it received connection attempts to:

- TCP
  - It listens on a single-port, multiple-ports, or a range or ports.
    - Inbound connections are accepted and droped immediately.
- FTP
  - It listens on a single port where it will act as a real FTP server.
    - Credentials are logged. It might reveal who or compromised credetials.
- HTTP with Basic Authentication
  - It pretends to be an HTTP server that requires basic authentication.
    - Credentials are logged. It might reveal who or compromised credetials.
- DNS
  - It mimiques a DNS server but always respond with the same IP address.
    - If the command `dig` is used it can identify and log the queried domain.
- Email Notifications
  - It runs a module that parses the logs and sends reports to an email address.
    - The report contains counters of the source IP, reached ports, and more.

## Deployment

```
cd /opt
git clone https://github.com/davift/humble-pot.git
cd /opt/humble-pot
./deploy.sh
```
