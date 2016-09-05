#! /usr/bin/env python

import sys
from scapy.all import *
from math import log

BROADCAST_DST = 'ff:ff:ff:ff:ff:ff'
BROADCAST = 'broadcast'
UNICAST = 'unicast'

def process(pkt):

    global cant_paquetes_map
    global timeout
    global cant_paquetes

    if(pkt.dst == BROADCAST_DST):
        cant_paquetes_map[BROADCAST] += 1
    else:
        cant_paquetes_map[UNICAST] += 1

    if timeout != None:
        cant_paquetes += 1



if __name__ == '__main__':
    
    cant_paquetes_map = {UNICAST: 0, BROADCAST: 0}
    entropia_s = 0

    # Tiempo que se realiza el sniff en caso de realizarlo por timeout
    timeout = None
    # Cantidad de paquetes que procesa el sniff en caso de realizarlo por cantidad de paquetes
    cant_paquetes = 0


    # Parseo de parametros para determinar corte del sniff
    if len(sys.argv) == 3:
        if sys.argv[1] == 'timeout':
            timeout = int(sys.argv[2])
        elif sys.argv[1] == 'cant_paquetes':
            cant_paquetes = int(sys.argv[2])

    # Se realiza el sniff
    sniff(prn=process, store=0, count=cant_paquetes, timeout=timeout)


    # Imprimimos algunos valores de la fuente
    for dst, cantidad in cant_paquetes_map.iteritems():
        print "\n" + dst + ":\n"

        print "cantidad de paquetes: " + str(cantidad)

        probabilidad = float(cantidad) / cant_paquetes
        print "probabilidad: " + str(probabilidad)
        
        informacion = sys.maxint if (probabilidad == 0) else (-log(probabilidad,2))
        print "informacion: " + str(informacion)

        entropia_s += 0 if (probabilidad == 0) else probabilidad * informacion

    print "\nentropia_s: " + str(entropia_s)