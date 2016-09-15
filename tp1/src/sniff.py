#! /usr/bin/env python

from scapy.all import *
import argparse 
import ejercicio1
import ejercicio2

parser = argparse.ArgumentParser()
parser.add_argument("ej", type = int, choices = [1, 2], help = "Numero del ejercicio a realizar.")
parser.add_argument("modo", choices = ["sniff", "pcap"], help = "Modo de uso: sniff o levante de pcap ya existente.")
parser.add_argument("pcapFile", nargs = "?", default = "default.pcap", help = "Archivo pcap a escribir (para modo sniff) o leer (para modo pcap).")
args = parser.parse_args()

if (vars(args)["modo"] == "sniff"):
    try:
        packets = sniff()
    except KeyboardInterrupt:
        pass
    wrpcap(vars(args)["pcapFile"], packets)
else: 
    packets = rdpcap(vars(args)["pcapFile"])

if (vars(args)["ej"] == 1):
    ejercicio1.ej1(packets) 
else: 
    ejercicio2.ej2(packets)
