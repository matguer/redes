#!/usr/bin/env python
#from graphviz import Digraph
from pygraphviz import *

def grafo(paquetes_map, grafoFile):
    red = AGraph(paquetes_map, directed = True)
    print red.node_attr
    for node in red.iternodes():
        if "+" in node.get_name():
            #node.attr["style"] = "filled"
            #node.attr["fillcolor"] = "grey"
            #node.attr["fontcolor"] = "white"
            node.attr["color"] = "red"
            node.attr["fontcolor"] = "red"
    red.layout()
    red.draw(grafoFile)
