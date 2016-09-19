#!/usr/bin/env python
#from graphviz import Digraph
from pygraphviz import *

def grafo(paquetes_map, grafoFile):
    red = AGraph(paquetes_map, directed = True)
    red.graph_attr["overlap"] = "voronoi"
    red.graph_attr["splines"] = "true"
    for node in red.iternodes():
        if "+" in node.get_name():
            node.attr["color"] = "red"
            node.attr["fontcolor"] = "red"
        #if int(node.get_name().split(".")[-1]) == 249 or int(node.get_name().split(".")[-1]) == 254:
        #    node.attr["color"] = "green"
        #    node.attr["fontcolor"] = "green"
    red.layout()
    red.draw(grafoFile)
