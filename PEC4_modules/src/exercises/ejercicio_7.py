# 1. Define la función graf(data, selected_teams), donde data es el dataset y
#    selected_teams es una lista de los 5 equipos que han conseguido mejor
#    puntuación acumulada. Filtra el dataset con las filas en que el equipo
#    local y el equipo visitante estén en la lista de seleccionados.
import networkx as nx
from PEC4_modules import config
import matplotlib.pyplot as plt


def selected_teams_fn(df_total_points):
    selected_teams = df_total_points["total_points"].nlargest(5).index
    return selected_teams

def graf(data, selected_teams):
    G = nx.Graph()
    G.add_nodes_from(selected_teams)

    # print(data)

    filtered = data["total_points"].isin(selected_teams)

    edge_labels = nx.get_edge_attributes(G, "weight")
    pos = nx.spring_layout(G)

    nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=2000)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.show()
    # Consulta: Consulta Anthropic. (2026). Claude (versión del 12 de junio de 2026)
    # [Modelo de lenguaje grande]. https://claude.ai

    plt.savefig(f"img/grafica_ex2_{config.nom_alumne}_{config.date_time}.png")
    # print(G)


#    Con la librería networkx se construye un grafo de conexiones. Por ejemplo,
#    entre Ath Bilbao y Real Madrid hay 30+30 conexiones (Ath Bilbao ha jugado
#    30 veces como local y 30 veces como visitante). Se pueden crear dos
#    flechas, o bien agruparlas y poner una línea sin flecha que una ambos
#    equipos. Al lado de la línea debe aparecer el número de conexiones.
#
# 2. Ejecuta la función y genera el grafo.


