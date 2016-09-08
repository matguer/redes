#! /usr/bin/env python

import sys
from scapy.all import *
from math import log

BROADCAST_DST = 'ff:ff:ff:ff:ff:ff'
BROADCAST = 'broadcast'
UNICAST = 'unicast'

def ej1(packets):
    
    cant_paquetes_map = {UNICAST: 0, BROADCAST: 0}
    entropia_s = 0

    for pkt in packets:
        if(pkt.dst == BROADCAST_DST):
            cant_paquetes_map[BROADCAST] += 1
        else:
            cant_paquetes_map[UNICAST] += 1

    cant_paquetes = sum(cant_paquetes_map.values())

    # Imprimimos algunos valores de la fuente
    for dst, cantidad in cant_paquetes_map.iteritems():
        print "\n" + dst + ":\n"

        print "cantidad de paquetes: " + str(cantidad)

        probabilidad = float(cantidad) / cant_paquetes
        print "probabilidad: " + str(probabilidad)
        
        informacion = "inf" if (probabilidad == 0) else (-log(probabilidad,2))
        print "informacion: " + str(informacion)

        entropia_s += 0 if (probabilidad == 0) else probabilidad * informacion

    print "\nentropia_s: " + str(entropia_s)
