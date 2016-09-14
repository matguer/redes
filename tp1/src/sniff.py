#! /usr/bin/env python

import sys
from scapy.all import *
from math import log
import argparse as arg
import ejercicio1
import ejercicio2

# Parseo de parametros
if (len(sys.argv) <= 1 or sys.argv[1] == "-h" or sys.argv[1] == "-help" or sys.argv[1] == "-H"):
    print "Uso: <#ej: {1, 2}> <modo de captura: {--sniff, --pcap}> <param captura> [pcap file]"
    print "<param captura> varia dependiendo del modo de captura"
    print "Para --sniff, son: <parametros del sniff: {keyboard, timeout, cant_paquetes}> <valor del timeout/cantidad de paquetes>"
    print "Para, --pcap no son necesarios"
    print "[pcap file] es el filename del pcap que se va a leer (si se paso --pcap) o que se va a escribir (si se paso --sniff). Este parametro es opcional, siendo el default \"default.cap\""
    exit()

ej = int(sys.argv[1])
if (len(sys.argv) >= 5 and sys.argv[2] == "--sniff"):
    timeout, cant_paquetes = None, None
    if sys.argv[3] == 'timeout':
        timeout = int(sys.argv[4])
    elif sys.argv[3] == 'cant_paquetes':
        cant_paquetes = int(sys.argv[4])
    try:
        packets = sniff(count=cant_paquetes, timeout=timeout)
    except KeyboardInterrupt:
        pass
    if (sys.argv[3] == "keyboard"):
        wrpcap(sys.argv[3], packets)
    elif (len(sys.argv) >= 6):
        wrpcap(sys.argv[5], packets)
    else:
        wrpcap("default.cap", packets)
elif (len(sys.argv) >= 3 and sys.argv[2] == "--pcap"):
    if (len(sys.argv) >= 4):
        packets = rdpcap(sys.argv[3])
    else:
        packets = rdpcap("default.cap")
else:
    raise ValueError("Argumentos incorrectos")

ejercicio1.ej1(packets) if (ej == 1) else ejercicio2.ej2(packets)
