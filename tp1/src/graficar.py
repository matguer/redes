#!/usr/bin/env python
import matplotlib.pyplot as plt
from numpy import arange

def graficar(info, entropia_s, figuraFile):

    keys = sorted(info, key = info.get, reverse = True)
    info = [info[k] for k in keys]

    colors = ["Red", "Green"]
    color = [colors[0] if i >= entropia_s else colors[1] for i in info]

    ind = arange(len(info))
    width = 0.25

    fig, ax = plt.subplots()
    ax.bar(ind, info, width, color = color)
    ax.plot(ax.get_xlim(), [entropia_s, entropia_s], color = "Black")

    ax.set_xticks(ind + width / 2)
    ax.set_xticklabels(keys)
    ax.set_xlabel("Direcciones IP")
    ax.set_ylabel("Informacion [bits]")

    plt.savefig(figuraFile, bbox_inches = "tight")
