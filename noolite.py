#!/usr/bin/python

# Requires: pyusb
# To install it on Ubuntu 12.04 do:
#   sudo apt-get install python-pip
#   sudo pip install pyusb

import usb.core


class NooLite:
    _init_command = [0x30, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

    def __init__(self, channals=8, idVendor=0x16c0, idProduct=0x05df):
        self._idVendor = idVendor
        self._idProduct = idProduct
        self._channales = channals
        self._cmd = self._init_command

    def _set_ch(self, ch):
        if (ch < self._channales) and (ch >= 0):
            self._cmd[4] = ch
        else:
            return -2

    def _send(self):
        dev = usb.core.find(idVendor = self._idVendor, idProduct = self._idProduct)  # find NooLite usb device
        if dev is None:
            return -1
        if dev.is_kernel_driver_active(0) is True:
            dev.detach_kernel_driver(0)
        dev.set_configuration()
        dev.ctrl_transfer(0x21, 0x09, 0, 0, self._cmd)
        return 0

    def on(self, ch):
        """Turn power on on channel
        First channal is 0 """
        self._cmd = self._init_command
        self._cmd[1] = 0x02       # "Turn power on" command
        if self._set_ch(ch):
            return -2
        return self._send()

    def off(self, ch):
        """Turn power off on channel
        First channal is 0 """
        self._cmd = self._init_command
        self._cmd[1] = 0x00       # "Turn power off" command
        if self._set_ch(ch):
            return -2
        return self._send()

    def set(self, ch, level):
        """Set brightness level
        Max level is 120
        First channal is 0 """
        self._cmd = self._init_command
        self._cmd[1] = 0x06       # "Turn power on" command
        if self._set_ch(ch):
            return -2
        self._cmd[2] = 0x01       # send level
        return self._send()

        # level in cmd must be in [0, 35 - 155]
        if level == 0:
            cmd[5] = 0
        elif level > 120:
            cmd[5] = 155
        else:
            cmd[5] = 35 + lvl
        return self._send()

    def bind(self, ch):
        """ Send bind signal on channel
        First channal is 0 """
        self._cmd = self._init_command
        self._cmd[1] = 0x0f       # "bind" command
        if self._set_ch(ch):
            return -2
        return self._send()

    def unbind(self, ch):
        """ Send unbind signal on channel
        First channal is 0 """
        self._cmd = self._init_command
        self._cmd[1] = 0x0f       # "unbind" command
        if self._set_ch(ch):
            return -2
        return self._send()

    def switch(self, ch):
        """switch power between off and on on channel
        First channal is 0 """
        self._cmd = self._init_command
        self._cmd[1] = 0x04       # "switch" command
        if self._set_ch(ch):
            return -2
        return self._send()


"""
class main:
  def usage(self, fileName):
    print 'Usage: ' + fileName + ' <cmdX> [level]'
    print 'Where:'
    print '  - <cmd> is:'
    print '      on_ch     - set channel X power ON'
    print '      off_ch    - set channel X power OFF'
    print '      sw_ch     - switch channel X power ON/OFF'
    print '      set_ch    - set channel X power level'
    print '      bind_ch   - bind channel X to device'
    print '      unbind_ch - unbind channel X from device'
    print '  - <X> is channel number from 1 to 8'
    print '  - [level] is power level for CMD "set_ch"'

  def execute(self, argv):
    if not os.geteuid() == 0:
      sys.exit("This script must be executed by root.")
    cmd = -1; ch = -1; lvl = 0;
    command = ''
    for arg in argv[1:]:
      if command == 'set_ch':
        if str(arg).isdigit():
          lvl = int(str(arg))
          if lvl<0:
            lvl=0
          elif lvl>100:
            lvl=100
          lvl = int(35 + 1.2 * lvl)
        break
      else:
        for sCmd, cCmd in [['on_ch', 0x02], ['off_ch', 0x00], ['sw_ch', 0x04], ['set_ch', 0x06], ['bind_ch', 0x0f], ['unbind_ch', 0x09]]:
          pos = str(arg).lower().find(sCmd)
          if pos >= 0:
            command = sCmd
            cmd = cCmd
            channel = str(arg[pos+len(sCmd):])
            if channel.isdigit():
              ch = int(channel)-1
            if ch<0 or ch>7:
              sys.exit('Channel number must be number from 1 to 8.')
            break
      if (len(command) > 0 and command != 'set_ch'):
        break
    if cmd>=0 and ch>=0:
      nooLite().executeCommand(cmd, ch, lvl)
    else:
      self.usage(argv[0])

if __name__ == '__main__':
  main().execute(sys.argv)
"""
