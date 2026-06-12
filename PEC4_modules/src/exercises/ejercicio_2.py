import pandas as pd
import matplotlib.pyplot as plt
from PEC4_modules import config

# define la función total_matches(data),

def total_matches(data):

    # Creamos dos dataframes: uno para los partidos "Home" y otro para "away"
    home = data[["Season", "Date", "HomeTeam", "FTHG", "FTAG", "FTR"]].rename(
        columns={"HomeTeam": "Team", "FTHG": "Goles_favor", "FTAG": "Goles_contra"})
    away = data[["Season", "Date", "AwayTeam", "FTAG", "FTHG", "FTR"]].rename(
        columns={"AwayTeam": "Team", "FTHG": "Goles_contra", "FTAG": "Goles_favor"})
    # Concatenamos en un solo data frame
    matches_by_team = pd.concat([home, away], ignore_index=True)

    # Calculamos el número de partidos jugados por cada equipo durante todos los años.

    matches_team_total = matches_by_team.groupby("Team").agg(
        partidos=("Goles_favor", "count"),
        goles_favor=("Goles_favor", "sum"),
        goles_contra=("Goles_contra", "sum")
    )
    # ejecuta la función y muestra los 10 primeros valores.

    print("primeros 10 valores", matches_team_total.head(10))
    # muestra los equipos que siempre han estado en primera división
    # (los que tienen el máximo número de partidos).
    primera_division = matches_team_total.sort_values("partidos", ascending=False).head(20)
    print("Primera División:", primera_division)

    return matches_team_total, matches_by_team

# Ejecuta la función.


# total_matches(path)

# Define la función plot_matches_team_total(matches_team_total), que representa esta información (eje x: equipos; eje y:
# número de partidos total).

def plot_matches_team_total(matches_team_total):
    fig, ax = plt.subplots(figsize=(14, 10))

    teams = matches_team_total.index.tolist()  # ← .tolist() convierte a lista Python
    matches = matches_team_total["partidos"].to_numpy()  # ← .to_numpy() convierte a array numpy

    ax.barh(teams, matches)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel("matches")
    ax.set_title("Partidos por equipo")

    plt.savefig(f"img/grafica_ex2_{config.nom_alumne}_{config.date_time}.png")

    plt.show()

# Ejecuta la función.

# plot_matches_team_total(matches_team_total)

# Consulta: Consulta Anthropic. (2026). Claude (versión del 13 de mayo de 2026)
# [Modelo de lenguaje grande]. https://claude.ai
