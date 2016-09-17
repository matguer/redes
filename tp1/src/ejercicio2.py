#! /usr/bin/env python

from scapy.all import *
from math import log
from grafo import grafo
from graficar import graficar

BROADCAST_DST = 'ff:ff:ff:ff:ff:ff'
BROADCAST = 'broadcast'
UNICAST = 'unicast'
TYPE_FIELD = 'type'
TYPE_ARP = '0x806'
WHO_HAS = 1

def ej2(packets, figuraFile, grafoFile):

    paquetes_map = {}
    paquetes_map_inv = {}
    map_cant_paquetes = {}
    cant_paquetes = 0

    for pkt in packets:
        # Si es un paquete ARP va a tener el campo TYPE_FIELD y su valor va a ser TYPE_ARP
        if TYPE_FIELD in pkt.fields:
            type_str = str(hex(pkt.fields[TYPE_FIELD]))
            if(type_str == TYPE_ARP and pkt.op == WHO_HAS):
                if ((pkt.psrc not in paquetes_map) or (pkt.pdst not in paquetes_map.get(pkt.psrc))):
                    paquetes_map.setdefault(pkt.psrc, []).append(pkt.pdst)
                    if (paquetes_map_inv.get(pkt.pdst) is None):
                        paquetes_map_inv[pkt.pdst] = 0
                    paquetes_map_inv[pkt.pdst] += 1
                    #
                    if (map_cant_paquetes.get(pkt.psrc) is None):
                        map_cant_paquetes[pkt.psrc] = 0
                    map_cant_paquetes[pkt.psrc] += 1
                    cant_paquetes += 1

    info, entropia_s = fuente(map_cant_paquetes, cant_paquetes)
    paquetes_map = filtrar(paquetes_map, paquetes_map_inv)

    graficar(info, entropia_s, figuraFile)
    grafo(paquetes_map, grafoFile)

def filtrar(paquetes_map, paquetes_map_inv):

    paquetes_map_nuevo = {}
    for src in paquetes_map.iterkeys():
        paquetes_map_nuevo[src] = []
        listaNueva = filter(lambda s: paquetes_map_inv[s] > 1, paquetes_map[src])
        unicoSrc = filter(lambda s: paquetes_map_inv[s] <= 1, paquetes_map[src])
        if (len(unicoSrc) > 1):
            listaNueva.append(unicoSrc[0] + "+" + str(len(unicoSrc) - 1))
        elif unicoSrc:
            listaNueva.append(unicoSrc[0])
        paquetes_map_nuevo[src] = listaNueva
    paquetes_map = paquetes_map_nuevo

    paquetes_map_nuevo = {}
    bitmap = {k: False for k in paquetes_map.iterkeys()}
    for (k, v) in paquetes_map.iteritems():
        if (bitmap[k] == False):
            count = 0
            bitmap[k] = True
            for (kPrima, vPrima) in paquetes_map.iteritems():
                if (bitmap[kPrima] == False) and (k != kPrima) and (v == vPrima):
                    bitmap[kPrima] = True
                    count += 1

            paquetes_map_nuevo[k + "+" + str(count) if count > 0 else k] = v
    return paquetes_map_nuevo

def fuente(map_cant_paquetes, cant_paquetes):

    entropia_s = 0
    info = []
    for src, cantidad in map_cant_paquetes.iteritems():

        probabilidad = float(cantidad) / cant_paquetes
        informacion = "inf" if (probabilidad == 0) else (-log(probabilidad,2))
        info.append((src, informacion))
        entropia_s += 0 if (probabilidad == 0) else probabilidad * informacion

    info = sorted(info, key = lambda p: p[1], reverse = True)

    for (src, informacion) in info:
        print "Informacion (" + src + ") = " + str(informacion) + " bits." + ("[Distinguido]" if informacion < entropia_s else "")
    print "Entropia (S_1) = " + str(entropia_s) + " bits."

    info = zip(*info)[1]
    return (info, entropia_s)
