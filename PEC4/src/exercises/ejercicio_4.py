# 1. Define la función FTR(data), que devuelve el número de partidos que han
#    ganado los locales, que han ganado los visitantes, o que han empatado
#    (draw), en forma de dataframe (dataframe ftr).

import matplotlib.pyplot as plt
import numpy as np
from PEC4 import config


def FTR(data):
    FTR_analysis = data.groupby("FTR").agg(
        partidos=("Season", "count"),
    )

    total_FTR = FTR_analysis["partidos"].aggregate(np.sum)
    # print("Total:", total_FTR)

    FTR_analysis["Percent"] = FTR_analysis["partidos"] / total_FTR

    # for i in FRT_analysis['partidos']:
    #   .aggregate(np.mean)

    # print(FTR_analysis)

    # 3. ¿Qué porcentaje de partidos ganan los locales?
    print(f"Los locales ganan el {FTR_analysis['Percent']['H'] * 100} % de los partidos")

    return FTR_analysis



# 2. Ejecuta la función y muestra el dataframe resultante.

# FTR(df)


# 4. Define la función plot_FTR(ftr) que representa esta información
#    (eje x: H, A, D; eje y: número de partidos). Ejecuta la función.

def plot_FTR(ftr):
    plt.style.use("_mpl-gallery")
    x = ftr.index
    y = ftr["partidos"]

    fig, ax = plt.subplots()
    ax.bar(x, y, width=0.6, edgecolor="white", linewidth=0.7)
    ax.set_xlabel("Resultados")
    ax.set_ylabel("Partidos")

    plt.savefig(f"img/grafica_ex4_{config.nom_alumne}_{config.date_time}.png")
    plt.show()



# plot_FTR(ftr=FTR_analysis)