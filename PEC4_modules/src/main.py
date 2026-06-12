from PEC4_modules.src import exercises
from PEC4_modules import config
import kagglehub


# Cargamos el path
global path
path = kagglehub.dataset_download("kishan305/la-liga-results-19952020")

print("Path to dataset files:", path)

print(config.nom_alumne, config.date_time)

# Ejecutamos los diferentes ejercicios de la PEC:
# Ejercicio_1
df = exercises.ejercicio_1.load_and_eda(path)

# Ejercicio_2
matches_team_total, matches_by_team = exercises.ejercicio_2.total_matches(df)
exercises.ejercicio_2.plot_matches_team_total(matches_team_total)

# Ejecicio_3
distr_goals_home, distr_goals_away = exercises.ejercicio_3.goals_distribution(df)
exercises.ejercicio_3.plot_goals_distribution(distr_goals_home, distr_goals_away)

# Ejecicio_4
FTR_analysis = exercises.ejercicio_4.FTR(df)
exercises.ejercicio_4.plot_FTR(ftr=FTR_analysis)

# Ejecicio_5
data = exercises.ejercicio_5.add_points(df)
df_total_points = exercises.ejercicio_5.fun_total_points(df)
alltime_winner = exercises.ejercicio_5.alltime_winner(df_total_points)

# Ejecicio_6
home_goals, away_goals, total_goals = exercises.ejercicio_6.fun_total_goals(matches_team_total)
tupla = exercises.ejercicio_6.fun_total_goals_by_team(df)

# Ejecicio_7
selected_teams = exercises.ejercicio_7.selected_teams_fn(df_total_points)
exercises.ejercicio_7.graf(df_total_points, selected_teams)
