
import pandas as pd
import os
import shutil

# Define la función load_and_eda(file)

def load_and_eda(file):
    # que carga el dataset
    csv_file = os.path.join(file, os.listdir(file)[0])
    df = pd.read_csv(csv_file)
    # elimina las columnas "HTHG", "HTAG", "HTR".
    df.drop(["HTHG", "HTAG", "HTR"], axis=1, inplace=True)

    # La función también muestra los primeros y últimos valores del dataset, y
    print("head:", df.head(10))
    print("tail:", df.tail(10))

    # la información más relevante.
    print("description:", df.describe())

    # Guardar copia en src/data
    dest = os.path.join(os.path.dirname(__file__), "..", "data")
    os.makedirs(dest, exist_ok=True)
    shutil.copy(csv_file, dest)

    # Consulta: Consulta Anthropic. (2026). Claude (versión del 10 de junio de 2026)
    # [Modelo de lenguaje grande]. https://claude.ai

    return df

# print("Path to dataset files:", path)
