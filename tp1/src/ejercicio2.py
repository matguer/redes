#! /usr/bin/env python

from scapy.all import *
from math import log
#from grafo import grafo
from graficar import graficar

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

def ej2(packets, figuraFile):

    paquetes_map = {}
    cant_paquetes = 0

    for pkt in packets:
        # Si es un paquete ARP va a tener el campo TYPE_FIELD y su valor va a ser TYPE_ARP
        # Aca estamos contando la cantidad de apariciones de cada nodo, tenemos que definir bien
        # que data queremos guardar y que significa para nosotros un nodo distinguido
        if TYPE_FIELD in pkt.fields:
            type_str = str(hex(pkt.fields[TYPE_FIELD]))
            if(type_str == TYPE_ARP):
                #solo destino, eso es lo que va a distinguir a los nodos (source deberia ser basicamente equiprobable)
                paquetes_map.setdefault(pkt.pdst, []).append(pkt.src)
                cant_paquetes += 1

    entropia_s = 0
    info = {}
    for dst, listaSrc in paquetes_map.iteritems():

        cantidad = len(listaSrc)
        probabilidad = float(cantidad) / cant_paquetes
        informacion = "inf" if (probabilidad == 0) else (-log(probabilidad,2))
        info[dst] = informacion
        entropia_s += 0 if (probabilidad == 0) else probabilidad * informacion

        #print "\n" + dst + ":\n"
        #print "cantidad de paquetes: " + str(cantidad)
        #print "probabilidad: " + str(probabilidad)
        #print "informacion: " + str(informacion) + " bits"
    #print "entropia_s: " + str(entropia_s) + " bits"

    #grafo(paquetes_map, grafoFile)
    graficar(info, entropia_s, figuraFile)
