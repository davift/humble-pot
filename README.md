# humble-pot

Humble-Pot is a lightweight honey-pot container application.

A fully fledged honey-pot appliance such as [tpotce](https://github.com/telekom-security/tpotce) or [opencanary](https://github.com/thinkst/opencanary) can be incredibly complex and full of features but it also requires a lot of computing resources an usually a dedicated machine to run it on.

In another hand, Humble-Pot is meant to run in a container that can be stand-alone in a single code single GB of RAM or using the idle capacity of another server that for instance is an FTP server but will alert if someone brute-forces/fuzzing the HTTP port.

Use cases:

![Network Architecture](/assets/images/humble-pot.drawio.png)

