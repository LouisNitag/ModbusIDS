#!/usr/bin/env python3

# Beerware Licence
# <louis@gatin.me> wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return.

import socket
from argparse import ArgumentParser
from scapy.all import sniff
from pyModbusTCP.client import ModbusClient
from parser import parse_address


parser = ArgumentParser(description="Sniff ModbusTCP packets on network and raise alarms if intrusions are detected")
parser.add_argument('-i', '--interface', type=str, default='eth0', help='Interface')
parser.add_argument('-p', '--port', type=int, default=502, help='Port to listen to')
parser.add_argument('-a', '--alert', type=str, help='Modbus server to raise alert <address>[:<port=502>]/<register>')
parser.add_argument('authorized_hosts', nargs='*', help="list of authorized hosts")
args = parser.parse_args()

# Add own IP address to authorized hosts
args.authorized_hosts.append(socket.gethostbyname(socket.gethostname()))

# Open Modbus client if needed
if args.alert is not None:
    adr = parse_address(args.alert)
    args.__dict__.update({k: adr[k] for k in ["host", "port", "register"]})

    c = ModbusClient(host=args.host, port=args.port, auto_open=True)
    if not c.is_open():
        if not c.open():
            raise ConnectionError(f'cannot connect to Modbus server at {args.host}:{args.port}')


# Function called for every paquet handled by the sniffer
def callback(p):
    src = p['IP'].src
    dst = p['IP'].dst
    if src not in args.authorized_hosts:
        if args.alert is not None:
            c.write_single_register(args.register, 1)
        print(f"Request from {src} to {dst} detected!")


# Launch the sniffer with good options
try:
    sniff(iface=args.interface, filter=f"tcp and port {args.port}", prn=callback)
except PermissionError as e:
    print("This tool require root privileges or cap_net_raw capability.")
    exit(1)
except KeyboardInterrupt:
    exit(0)
