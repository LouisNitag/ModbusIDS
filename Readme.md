# ModbusTCP sniffer

## Description

This program is a PoC to raise alarms on a PLC if unauthorized ModbusTCP packets
are seen on the network, thus warn the operator as early as possible.

Example: an HMI talks to a PLC using ModbusTCP. A computer running this program
can be place on a network hub, thus sniffing every packet sent to both HMI and
PLC.

## Licence

This program is under [Beerware Licence][1].
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

Sniff packets from

positional arguments:
  authorized_hosts      list of authorized hosts

optional arguments:
  -h, --help            show this help message and exit
  -i INTERFACE, --interface INTERFACE
                        Interface
  -p PORT, --port PORT  Port to listen to
  -a ALERT, --alert ALERT
                        Modbus server to raise alert
                        <address>[:<port=502>]/<register>
```

## Disclaimer

I provide this program as a proof of concept. Since ModbusTCP is clearly
depreciated, you should use another more secure protocol instead of using tools
like this.


[1](https://fr.wikipedia.org/wiki/Beerware)
