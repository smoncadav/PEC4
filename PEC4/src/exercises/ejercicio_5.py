# 1. Define la función add_points(data), que añade al dataset los puntos
#    conseguidos como local y como visitante, por cada partido. Es decir,
#    crea las columnas points_home y points_away, que pueden tomar los
#    valores 3, 1 o 0.
import pandas as pd


def add_points(data):
    home_map = {"H": 3, "D": 1, "A": 0}
    away_map = {"H": 0, "D": 1, "A": 3}

    data["points_home"] = data["FTR"].map(home_map)
    data["points_away"] = data["FTR"].map(away_map)

    # 2. Ejecuta la función y muestra los 10 primeros valores.

    # add_points(df)

    print(data.head(10))
    return data

# 3. Define la función fun_total_points(data), que calcula el total de puntos
#    conseguidos y acumulados desde 1995 por cada equipo. Devuelve por cada
#    equipo el número de puntos totales, en forma de tupla: variable Series y
#    variable DataFrame (el Series y el DataFrame de hecho contienen la misma
#    información). (Es una propuesta; un alumno puede decidir devolver solo el
#    Series o el DataFrame).
def fun_total_points(data):
    df_total_points = pd.DataFrame(index=data["HomeTeam"].unique())
    df_total_points["home_points"] = data.groupby("HomeTeam")["points_home"].sum()
    df_total_points["away_points"] = data.groupby("AwayTeam")["points_away"].sum()
    df_total_points["total_points"] = df_total_points["home_points"] + df_total_points["away_points"]
    print(df_total_points)

    return df_total_points



# 4. Ejecuta la función y muestra los 10 primeros valores.
# fun_total_points(df)


# 5. Define la función alltime_winner(df_total_points), que devuelve el ganador
#    de esta liga histórica y acumulada (el equipo que ha acumulado más puntos).
#    Ejecuta la función y muestra el ganador histórico.
def alltime_winner(df_total_points):
    alltime_winner = df_total_points["total_points"].idxmax()
    print("el ganador histórico es:", alltime_winner)

    return alltime_winner
# alltime_winner(matches_team_total)