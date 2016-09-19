#!/usr/bin/env python
import matplotlib.pyplot as plt
from numpy import arange

def graficar(info, entropia_s, figuraFile):

    infoCompactada, cantidades = [], []
    for i in range(len(info)):
        if i == 0 or info[i] != info[i - 1]:
            infoCompactada.append(info[i])
            cantidades.append(1)
        else:
            cantidades[-1] += 1
            
    ind = arange(len(infoCompactada))
    width = 0.5

    colors = ["Red", "Green"]
    color = [colors[0] if i >= entropia_s else colors[1] for i in infoCompactada]

    fig, ax = plt.subplots()
    ax.bar(ind, infoCompactada, width, color = color)
    ax.plot(ax.get_xlim(), [entropia_s, entropia_s], color = "Black")

    ax.set_xticks(ind + width / 2)
    ax.set_xticklabels(cantidades)
    ax.set_xlabel("Cantidad de Direcciones IP con igual informacion")
    ax.set_ylabel("Informacion [bits]")

    plt.savefig(figuraFile, bbox_inches = "tight")
