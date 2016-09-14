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

def ej2(packets):

    cant_paquetes_map = {}
    entropia_s = 0

    for pkt in packets:
        # Si es un paquete ARP va a tener el campo TYPE_FIELD y su valor va a ser TYPE_ARP
        # Aca estamos contando la cantidad de apariciones de cada nodo, tenemos que definir bien
        # que data queremos guardar y que significa para nosotros un nodo distinguido
        if TYPE_FIELD in pkt.fields:
            type_str = str(hex(pkt.fields[TYPE_FIELD]))
            if(type_str == TYPE_ARP):
                pkt.show()
                #solo destino, eso es lo que va a distinguir a los nodos (source deberia ser basicamente equiprobable)
                insertOrIncrement(cant_paquetes_map, pkt.pdst)

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

    print "entropia_s: " + str(entropia_s)
