'''main.py'''

import pandas as pd
from fastapi import FastAPI
import uvicorn 
import joblib

app = FastAPI()

play_genre = pd.read_csv('Funcion_1.csv', low_memory=False)
user_for_genre = pd.read_csv('Funcion_2_jup.csv', low_memory=False)
users_recommend = pd.read_csv('Funcion_3_jup.csv', low_memory=False)
users_not_recommend = pd.read_csv('Funcion_4_jup.csv', low_memory=False)
sentiment_analysis = pd.read_csv('Funcion_5_jup.csv', low_memory=False)
sentiment_analysis  = sentiment_analysis.drop('Unnamed: 0', axis=1)
df_E=pd.read_csv('ML_recommendations500.csv')
#modelo_svd = joblib.load('modelo_svd_I.pkl')

@app.get("/release_year/{genre}", name='año con mas horas jugadas para el género ingresado')

def PlayTimeGenre(genre: str):
   
    genero_df = play_genre[play_genre['genre'] == genre]

    if genero_df.empty:
        return {"No se encontraron datos para el género": genre}

    
    max_year = genero_df.loc[genero_df['playtime_forever'].idxmax()]['release_year']

    return {"Año de lanzamiento con más horas jugadas para " + genre: int(max_year)}

@app.get("/user_for_genre/{genre}", name='a usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.')

def UserForGenre(genero:str):

    genre_data = user_for_genre[user_for_genre['genre'] == genero]

    if genre_data.empty:
        return {"Usuario con más minutos jugados para " + genero: None, "minutos jugados": []}

    # Agrupa por año y suma las horas jugadas
    grouped = genre_data.groupby(genre_data['posted'])['playtime_forever'].sum().reset_index()

    # Encuentra el usuario con más horas jugadas
    max_playtime_user = genre_data.loc[genre_data['playtime_forever'].idxmax()]['user_id']

    # Crea la estructura de datos requerida
    result = {
        "Usuario con más horas jugadas para " + genero: max_playtime_user,
        "Horas jugadas": [{"Año": year, "minutos": hours} for year, hours in zip(grouped['posted'], grouped['playtime_forever'])]
    }
    return result

@app.get("/UsersRecommend/{posted}", name='top 3 de juegos MÁS recomendados por usuarios para el año dado.')
def UsersRecommend(posted:int):
    # Filtrar el DataFrame por el año dado
    df_año = users_recommend[users_recommend['posted'] == posted]

    # Aplicar las condiciones para obtener el top 3
    top_3_df = df_año[(df_año['sentiment'] >= 0) & (df_año['app_name'].notnull())]

    # Ordenar el DataFrame por 'sentiment' de mayor a menor
    top_3_df = top_3_df.sort_values(by='sentiment', ascending=False).head(3)

    # Crear una lista de diccionarios con el top 3
    top_3_dict = {}
    for i, row in top_3_df.iterrows():
        puesto = "Puesto " + str(i + 1 - top_3_df.index[0])
        top_3_dict[puesto] = row['app_name']
    return top_3_dict

@app.get("/UsersNotRecommend/{posted}", name='top 3 de juegos MENOS recomendados por usuarios para el año dado.')
    
def UsersNotRecommend(posted: int):
    df_año = users_not_recommend[users_not_recommend['posted'] == posted]

    top_3_df = df_año[(df_año['sentiment'] >= 0) & (df_año['app_name'].notnull())]

    top_3_df = top_3_df.sort_values(by='sentiment', ascending=False).head(3)

    top_3_dict = {}
    for i, row in top_3_df.iterrows():
        puesto = "Puesto " + str(i + 1 - top_3_df.index[0])
        top_3_dict[puesto] = row['app_name']

    return top_3_dict
@app.get("/Sentiment_Analysis/{release_year}", name='devuelve la cantidad de registros de reseñas de usuarios, Negativos, Positivos y Nulos por año de lanzamiento')
def Sentiment_Analysis(release_year: int):
    # Filtrar el DataFrame para obtener las filas que coinciden con el release_year dado
    filas_coincidentes = sentiment_analysis[sentiment_analysis['release_year'] == release_year]
    
    # Convertir las filas coincidentes a una lista de diccionarios
    filas_lista = filas_coincidentes.to_dict(orient='records')
    
    return filas_lista
@app.get("/recomendacion_usuario/{user_id}", name='devuelve lista con 5 juegos recomendados para dicho usuario.')
def recomendacion_usuario(user_id: str):
    user_id_=str(user_id)
    recomendaciones_usuario = df_E.loc[df_E['user_id'] == user_id_, 'recomendaciones']
    return str(recomendaciones_usuario.values[0])