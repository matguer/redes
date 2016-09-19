#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from numpy import arange

def graficar(info, entropia_s, figuraFile):
            
    infoCompactada = zip(*info)[1]
    keys = zip(*info)[0]
    ind = arange(len(infoCompactada))
    width = 0.20

    colors = ["Red", "Green"]
    color = [colors[0] if i >= entropia_s else colors[1] for i in infoCompactada]

    fig, ax = plt.subplots()
    ax.bar(ind, infoCompactada, width, color = color)
    pl = ax.plot(ax.get_xlim(), [entropia_s, entropia_s], color = "Black")

    ax.set_xticks(ind + width / 2)
    ax.set_xticklabels(keys, rotation = "vertical", fontsize = "12.5")
    ax.set_xlabel(u"Dirección IP")
    ax.set_ylabel(u"Información [bits]")
    ax.legend(pl, [u"Entropía: " + ("%.2f" % entropia_s) + " bits"])

    plt.savefig(figuraFile, bbox_inches = "tight")
