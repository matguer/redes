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
    red.layout()
    red.draw(grafoFile)
