# README para Proyecto de Sistema de Recomendación de Videojuegos en Steam #
¡Bienvenido al proyecto de Sistema de Recomendación de Videojuegos en Steam!

# Descripción del Problema #
En este proyecto, nos enfrentamos al desafío de crear un sistema de recomendación de videojuegos para usuarios de la plataforma Steam. El contexto involucra la necesidad de trabajar con datos de baja calidad y estructura, lo que requiere un enfoque exhaustivo desde la ingeniería de datos hasta el despliegue de un modelo de aprendizaje automático funcional.


# Feature Engineering: # 
Se creará la columna 'sentiment_analysis' aplicando análisis de sentimiento con NLP para categorizar las reseñas de los usuarios en negativas, neutrales o positivas. Esta columna reemplazará la columna de reseñas originales para facilitar el trabajo de los modelos de ML y el análisis de datos.

# Transformaciones #
En primer lugar se procede a abrir los datasets y transformar del formato json a csv. En esta etapa se procede a desanidar los campos necesarios para su posterior utilización en las funciones. 

# Desarrollo API #
Se disponibilizan los datos de la empresa usando el framework FastAPI. Para acceder utilice el siguiente link:

https://mi-ops-henry.onrender.com/docs#/

  1) def PlayTimeGenre( genero : str ): Debe devolver año con mas horas jugadas para dicho género.
  Ejemplo de retorno: {"Año de lanzamiento con más horas jugadas para Género X" : 2013}
  
  2) def UserForGenre( genero : str ): Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.
  Ejemplo de retorno: {"Usuario con más horas jugadas para Género X" : us213ndjss09sdf, "Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas:   23}]}
  
  3) def UsersRecommend( año : int ): Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)
  Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]
  
  4) def UsersNotRecommend( año : int ): Devuelve el top 3 de juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)
  Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]
  
  5) def sentiment_analysis( año : int ): Según el año de lanzamiento, se devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren    
   categorizados con un análisis de sentimiento. Ejemplo de retorno: {Negative = 182, Neutral = 120, Positive = 278}
  6) def recomendacion_juego( id de producto ): Ingresando el id de producto, deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.

# Deployment #
Se realizará el despliegue de la API utilizando servicios como Render o Railway para permitir que sea accesible desde cualquier dispositivo conectado a internet.

# Análisis Exploratorio de Datos (EDA) #
Se realiza un análisis exhaustivo de los datos para investigar las relaciones entre las variables, identificar outliers o anomalías, y descubrir patrones interesantes que puedan influir en el sistema de recomendación.

Se cuenta con un total de 32,133 juegos y 58,459 usuarios, entre los cuales 25,485 usuarios han dejado 58,431 comentarios sobre los juegos. Posteriormente, se lleva a cabo un análisis para identificar las variables más importantes para la recomendación, categorizándolas y presentándolas en gráficos. Debido a que este es un MVP, se ha reducido el conjunto de variables utilizadas en el modelo de aprendizaje automático al mínimo necesario según las recomendaciones básicas de la librería "surprise", que incluyen user_id, item_id y sentiment, representando la "puntuación" del usuario hacia un juego determinado obtenida a través del análisis de sentimiento, con opciones de puntuación negativa, neutra o positiva.

# Modelo de Aprendizaje Automático #
Se implementa al menos uno de los dos sistemas de recomendación propuestos: ítem-ítem. El modelo entrenado se guardo con la librería joblib, obteniendo un archivo .pkl que será consumido por la función de recomendación. 

Para probar el sistema de recomendación, se puede abrir el documento df_ML.csv provisto en Github y elegir un usuario o probar con los siguientes usuarios:

evcentric, js41637, ApxLGhost, 72947282842, wayfeng, pikawuu2, Sammeh00, Michaelele, 76561197970982479

# Video #
Se realiza un video explicativo mostrando el funcionamiento de la API y una breve explicación del modelo de ML entrenado. En el enlace puede ver un video de la API en Render y su funcionamieto

## requirements.txt
En este archivo de texto se colocan las librías que son necesarias para que la API funcione correctamente. 

## .gitignore
Permite que Render ignore los archivos que se contienen aquí pero que puedan permanecer en el repositorio.  
