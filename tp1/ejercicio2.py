#! /usr/bin/env python

import sys
from scapy.all import *
from math import log

BROADCAST_DST = 'ff:ff:ff:ff:ff:ff'
BROADCAST = 'broadcast'
UNICAST = 'unicast'
TYPE_FIELD = 'type'
TYPE_ARP = '0x806'

def insertOrIncrement(dic, key):
    if key in dic:
        dic[key] += 1
    else:
        dic[key] = 1

def process(pkt):

    global cant_paquetes_map
    global timeout
    global cant_paquetes

    # Si es un paquete ARP va a tener el campo TYPE_FIELD y su valor va a ser TYPE_ARP
    # Aca estamos contando la cantidad de apariciones de cada nodo, tenemos que definir bien
    # que data queremos guardar y que significa para nosotros un nodo distinguido
    if TYPE_FIELD in pkt.fields:
        type_str = str(hex(pkt.fields[TYPE_FIELD]))
        if(type_str == TYPE_ARP):
            pkt.show()
            insertOrIncrement(cant_paquetes_map, pkt.psrc)
            insertOrIncrement(cant_paquetes_map, pkt.pdst)

    if timeout != None:
        cant_paquetes += 1



if __name__ == '__main__':
    
    cant_paquetes_map = {}
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

    print "entropia_s: " + str(entropia_s)