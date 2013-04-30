forked from https://github.com/kyuri/nooLite commit 504b9bd7572ba8f5b337fbb27cd3343fcbbd8550

This project was started to support NooLite PC118 USB Stick (www.noo.com.by) on Linux.

Dependences:
* python module pyusb
To install it on Ubuntu 12.04 do:
  sudo apt-get install python-pip
  sudo pip install pyusb

* To have access to device from common user add rule to udev, for example to /etc/udev/rules.d/50-noolite.rules next line:
ATTRS{idVendor}=="16c0", ATTRS{idProduct}=="05df", SUBSYSTEMS=="usb", ACTION=="add", MODE="0666", GROUP="dialout"
And add your user to dialout group
sudo usermod <user> -a -G dialout
