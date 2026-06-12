# 1. Define la función fun_total_goals(data), que devuelve una tupla de tres
#    números enteros: (home_goals, away_goals, total_goals).
#    Muestra esta información.
def fun_total_goals(data):
    home_goals = data["goles_favor"]
    away_goals = data["goles_contra"]
    total_goals = home_goals + away_goals
    tupla = home_goals + away_goals, total_goals
    print(tupla)
    return home_goals, away_goals, total_goals


# fun_total_goals(matches_team_total)


# 2. Define la función fun_total_goals_by_team(data), que devuelve una tupla
#    de tres dataframes: home_goals_by_team, away_goals_by_team,
#    total_goals_by_team. Muestra los 10 primeros valores de
#    total_goals_by_team.

def fun_total_goals_by_team(data):
    home_goals_by_team = data.groupby("HomeTeam")["FTHG"].sum()
    away_goals_by_team = data.groupby("AwayTeam")["FTAG"].sum()
    total_goals_by_team = home_goals_by_team.add(away_goals_by_team)
    tupla = (home_goals_by_team, away_goals_by_team, total_goals_by_team)
    print("total goals by team:", tupla)
    return tupla


# fun_total_goals_by_team(df)

# 3. En el ejercicio 5 calculaste el número total de puntos por equipo:
#    total_points_by_team, df_total_points_by_team = fun_total_points(data)
#    Define la función fun_summary_1996_2025( , , , ) que crea el dataframe
#    summary_1996_2025 a partir de la concatenación de los 4 dataframes que
#    pasamos como argumentos: total_points_by_team, home_goals_by_team,
#    away_goals_by_team, total_goals_by_team.
# def fun_summary_1996_2025( , , , ):
#  return

#    Ejecuta la función y muestra los primeros valores.
# fun_summary_1996_2025( , , , )


#
# 4. Define la función podium(summary_1996_2025), que crea una gráfica de
#    podium a partir de un dataframe donde los tres primeros valores son los
#    equipos que componen el podium. La forma de podium se consigue con un
#    diagrama de barras, cada barra con un color, donde el primer equipo está
#    en el centro, el segundo a la izquierda a menor altura, y el tercero a
#    la derecha a menor altura, sin etiquetas en los ejes. Sobre cada barra
#    se muestra el nombre del equipo.
# def podium(summary_1996_2025):
#  return


# podium(summary_1996_2025)
#    Ejecuta la función