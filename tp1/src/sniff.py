#! /usr/bin/env python

from scapy.all import *
import argparse 
import ejercicio1
import ejercicio2

parser = argparse.ArgumentParser()
parser.add_argument("ej", type = int, choices = [1, 2], help = "Numero del ejercicio a realizar.")
parser.add_argument("modo", choices = ["sniff", "pcap"], help = "Modo de uso: sniff o levante de pcap ya existente.")
parser.add_argument("pcapFile", nargs = "?", default = "default.pcap", help = "Archivo pcap a escribir (para modo sniff) o leer (para modo pcap).")
parser.add_argument("figuraFile", nargs = "?", default = "default_figura.pdf", help = "Nombre del archivo en el cual se guardara la figura. (Solo para ej == 2).")
parser.add_argument("grafoFile", nargs = "?", default = "default_grafo.pdf", help = "Nombre del archivo en el cual se guardara el grafo. (Solo para ej == 2).")
parser.add_argument("--colapsar", action = "store_true", help = "Determina si colapsar nodos en el grafo. (Solo para ej == 2).")
parser.add_argument("--ambos", action = "store_true", help = "Determina si utilizar tanto pdst como psrc o solo psrc como mensaje. (Solo para ej == 2).")
parser.add_argument("--repetidos", action = "store_true", help = "Determina si contar paquetes repetidos. (Solo para ej == 2).")
args = parser.parse_args()

if (args.modo == "sniff"):
    try:
        packets = sniff()
    except KeyboardInterrupt:
        pass
    wrpcap(args.pcapFile, packets)
else: 
    packets = rdpcap(args.pcapFile)

if (args.ej == 1):
    ejercicio1.ej1(packets) 
else: 
    switches = {"colapsar": args.colapsar, "ambos": args.ambos, "repetidos": args.repetidos}
    ejercicio2.ej2(packets, args.figuraFile, args.grafoFile, switches)
