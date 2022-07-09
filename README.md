# humble-pot

Humble-Pot is a lightweight honey-pot container application.

A fully fledged honey-pot appliance such as [tpotce](https://github.com/telekom-security/tpotce) or [opencanary](https://github.com/thinkst/opencanary) can be incredibly complex and full of features but it also requires a lot of computing resources an usually a dedicated machine to run it on.

In another hand, Humble-Pot is meant to run in a container that can be stand-alone in a single code single GB of RAM or using the idle capacity of another server that for instance is an FTP server but will alert if someone brute-forces/fuzzing the HTTP port.

## Use Cases

![Network Architecture](https://github.com/davift/humble-pot/raw/main/humble-pot.drawio.png)

On the Private side of the illustration, the honey-pot is sharing idle resources from existent servers and would flag when a connection attempt happens on the unexpected port. It could be caused by malware or a threat actor, for example.

On the DMZ side of the illustration, the honey-pot is in a dedicated machine and would inform it the DMZ got compromised, and the threat actor is trying to move laterally.

## Features

It will capable of alert when failed connection attempts to:

- SSH (coming soon)
- FTP (coming soon)
- HTTP Basic Authentication (coming soon)

Also able to detect brute-focing/fuzzing on the HTTP server for hidden directories and files. (coming soon)

The alerts are sent via SMTP that might be configured on the deployment. It is recommended to use a mailing list as a destination that could be easily managed externaly.

## 

