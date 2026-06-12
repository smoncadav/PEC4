# 1. Define la función goals_distribution(data), que devuelve dos dataframes:
#    distr_goals_home, distr_goals_away. Estos dataframes contienen como índice
#    el número de goles marcados (por ej, FTHG), y como columna el número de
#    partidos en que se han marcado este número de goles. Por ejemplo, hay 2598
#    partidos en que FTHG=0 (los equipos locales no marcaron ningún).

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PEC4 import config

def goals_distribution(data):

  distr_goals_home = data.groupby("FTHG").agg(
        partidos=("FTHG", "count"),
    )


  distr_goals_away = data.groupby("FTAG").agg(
        partidos=("FTAG", "count"),
    )

  print(distr_goals_home, distr_goals_away)
  return  distr_goals_home, distr_goals_away



# 2. Ejecuta la función y muestra el dataframe resultante.

# goals_distribution(df)

# 3. Define la función plot_goals_distribution(distr_goals_home, distr_goals_away)
#    para representar esta información (una gráfica, dos plots). Ejecuta la función.



# Creamos un jointplot de tipo "scatter", indicando los nombres de las dos columnas
# que queremos usar como variables, el color y el tamaño de la figura.


def plot_goals_distribution(distr_goals_home, distr_goals_away):
    goals_distribution = pd.DataFrame(
        {
            "Goles Partidos Home": distr_goals_home["partidos"],
            "Goles Partidos Visitante": distr_goals_away["partidos"],
        }
    )

    g = sns.jointplot(
        x="Goles Partidos Home",
        y="Goles Partidos Visitante",
        data=goals_distribution,
        kind="scatter",
        space=0,
        color="g",
        height=10,
    )

    plt.savefig(f"img/grafica_ex3_{config.nom_alumne}_{config.date_time}.png")

    plt.show()

# plot_goals_distribution(distr_goals_home, distr_goals_away)
