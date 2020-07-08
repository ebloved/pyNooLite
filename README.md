<p>This is a fork based on <b>https://github.com/Sicness/pyNooLite</b> python module for noolite</p>

<p>I've just added MQTT support to connect my Noolite modules to HomeAssistant</p>

<p>After installing original module, just provide <b>username</b>, <b>password</b> and <b>hostname</b> in <b>noolite_mqtt</b>,<br>
copy this file in <b>/usr/bin/</b> and install and start <b>noolite-mqtt.service</b> by copying in onto <b>/etc/systemd/system/</b><br>
and  entering <br><b> systemctl enable noolite-mqtt<br>systemctl start noolite-mqtt</b> 





<p>This project is a <b>python module</b> to worik with <b>NooLite USB stick (PC118, PC1116, PC1132)</b>.<br>
Can be easy used to make a light control for smarthomes.<br>
About NooLite: http://www.noo.com.by/</p>


<p>Look at wiki for more info.</p>

<p>Author: Anton Balashov<br>
E-mail: sicness(_at_)darklogic.ru<br>
License: GPL v3<br>
Site: https://github.com/Sicness/pyNooLite</p>

<h4>Install</h4>

    sudo apt-get install pip
    sudo pip install noolite

<h3>Ubuntu/debian</h3
Ubuntu and debian users can install the module with an executable example from ppa:<br>
    https://launchpad.net/~ctolbhuk/+archive/noolite

<b>Or </b>download this repo and go into.

    sudo python setup.py install

<b>Or </b>simple copy noolite.py from this repo to your project<br>

<H4>Example:</H4>
    import noolite

    n = noolite.NooLite()
    n.on(0)       # Turn power on on first channel
    n.off(0)      # Turn power off on first channel
    n.set(1, 115) # Set 115 level on second channel
    n.bind(7)     # send "bind" signal on channel 8

<p>See noolite file for a extra example</p>

<h4>Dependences:</h4>

*  python module pyusb<br>
For Ubuntu do: <br>
     <i>sudo apt-get install python-pip <br>
     sudo pip install pyusb</i><br>

* To have access on device from common user add the next rule to udev. For example to /etc/udev/rules.d/50-noolite.rules next line:<br>
ATTRS{idVendor}=="16c0", ATTRS{idProduct}=="05df", SUBSYSTEMS=="usb", ACTION=="add", MODE="0666", GROUP="dialout"<br>
And add your user to dialout group:<br>
    <i>sudo usermod &lt;user&gt; -a -G dialout</i>
