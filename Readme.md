# ModbusTCP sniffer

## Description

This program is a PoC to raise alarms on a PLC if unauthorized ModbusTCP packets
are seen on the network, thus warn the operator as early as possible.

Example: an HMI talks to a PLC using ModbusTCP. A computer running this program
can be place on a network hub, thus sniffing every packet sent to both HMI and
PLC.

Warning: this tool does not protect against attacks. It shows up that something
could be wrong.

## Licence

This program is under [Beerware Licence](https://fr.wikipedia.org/wiki/Beerware).
> As long as you retain this notice you can do whatever you want with this
> stuff. If we meet some day, and you think this stuff is worth it, you can buy
> me a beer in return.

## Dependancies

* `python >= 3.7`
* `pyModbusTCP >= 0.1.7`
* `scapy >= 2.4.2`

## Usage

You may need root privileges to launch the utility.

```
usage: sniffer.py [-h] [-i INTERFACE] [-p PORT] [-a ALERT]
                  [authorized_hosts [authorized_hosts ...]]

Sniff ModbusTCP packets on network and raise alarms if intrusions are detected

positional arguments:
  authorized_hosts      list of authorized hosts

optional arguments:
  -h, --help            show this help message and exit
  -i INTERFACE, --interface INTERFACE
                        Interface
  -p PORT, --port PORT  Port to listen to
  -a ALERT, --alert ALERT
                        Modbus server to raise alert
                        <address>:[<port=502>]/<register>
```

## Example

A HMI (`192.168.0.10`) is talking to a PLC (`192.168.0.11`). This PLC have a
Modbus register dedicated to network alerts (`42`).
A micro-computer (`192.168.0.20`) is dedicated to monitoring the network on its
interface `eth1`.

All these devices are linked throug a network hub, thus the computer has access
to trames sent to both PLC and HMI. The sniffer is lauched this way:

```
# ./sniffer -i eth1 -a 192.168.0.11:/42 192.168.0.10 192.168.0.11
```

If the sniffer catch a illegitimate request from some host, it will write `1`
into the Modbus register `42` of the PLC. Since the HMI is configured to raise
an alert when this register is modified, the operator will see that someone try
to access the Modbus bank of the PLC.

## Disclaimer

I provide this program as a proof of concept. Since ModbusTCP is clearly
depreciated, you should use another more secure protocol instead of using tools
like this.
