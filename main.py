'''main.py'''

import pandas as pd
from fastapi import FastAPI
import uvicorn 
import joblib

app = FastAPI()

play_genre = pd.read_csv('Funcion_1.csv', low_memory=False)

@app.get("/release_year/{genre}", name='año con mas horas jugadas para el género ingresado')

def PlayTimeGenre(genre: str):
   
    genero_df = play_genre[play_genre['genre'] == genre]

    if genero_df.empty:
        return {"No se encontraron datos para el género": genre}

    
    max_year = genero_df.loc[genero_df['playtime_forever'].idxmax()]['release_year']

    return {"Año de lanzamiento con más horas jugadas para " + genre: int(max_year)}