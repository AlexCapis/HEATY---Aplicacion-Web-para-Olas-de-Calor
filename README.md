
</a>
<h1>HEATLY: ¡Sin Temor al Calor!</h1>

#### Autores: [Alex Marzá Manuel](https://github.com/AlexCapis), [Blanca Marmolejo](https://github.com/BlancaMarmolejo),  [Juan A-Mendizábal Ibarrola](https://github.com/juanmendiz)
#### Contribuidores: [Daniel](https://github.com/danieskka),  [Diego](https://github.com/Banbushka)

Bienvenido a HEATLY, la aplicación web diseñada para brindarte información educativa y esencial sobre las olas de calor. Descubre el poder de HEATLY y prepárate para enfrentar el calor extremo sin temor.

Nuestra misión es empoderarte con datos precisos y valiosos sobre las olas de calor, ayudándote a entender su impacto en tu entorno y en tu salud. Con HEATLY, podrás acceder a una amplia gama de recursos educativos y realizar cuestionarios personalizados para evaluar tus conocimientos sobre el tema.


<dl>
  <dt><a href="#introducción">1. Introducción </a></dt>
      <dd>Descripción detallada del problema y objetivo a tratar</dd>

  <dt><a href="#data_compr">2. Desarrollo</a></dt>
      <dd>Cómo se tratan los datos</dd>

  <dt><a href="#estructura">3. Estructura de carpetas</a></dt>
      <dd>Organización del proyecto</dd>
    
  <dt><a href="#construccion">4. En formación </a></dt>
      <dd>El futuro del proyecto</dd>
    

# 1. Introducción

#### Descripción del proyecto




#### Características del problema

<details>
<summary>Características detalladas</summary>
<p>
    
A continuación, se muestra una breve descripción con el significado de cada variable para una mejor comprensión acerca del problema a tratar.

    
</p>
</details>

# 2. Desarrollo

#### ¿Qué dificultades podemos encontrar?


- **Calidad y limpieza de los datos**: Los conjuntos de datos clínicos pueden contener errores y valores faltantes. Se requiere un análisis exhaustivo y técnicas de limpieza para asegurar datos de calidad.
    <details>
    <summary>Comprobación de datos faltantes por columnas</summary>
    <p>

    </p>
    </details>

- **Selección de características relevantes**: Con múltiples variables disponibles, es importante determinar qué características son más relevantes para predecir enfermedades cardíacas. Se necesita un análisis exploratorio y técnicas de selección de características.
    <details>
    <summary>De la columna de "Sex"</summary>
    <p>


    </p>
    </details>

- **Desequilibrio de clases**: Puede haber una proporción desigual entre casos positivos y negativos de enfermedad cardíaca. Esto puede afectar el rendimiento del modelo y requerir técnicas de muestreo o ajuste de pesos.

    <details>
    <summary>Ver imagen</summary>
    <img src=" " alt="drawing" width="400"/>
    </details>

    <details>
    <summary>Técnica de desbalanceo de datos</summary>
    <p>


    </p>
    </details>

- **Elección del modelo adecuado**: Se debe seleccionar y ajustar cuidadosamente el modelo de aprendizaje automático más adecuado para el problema. Requiere experimentación y comparación de modelos para encontrar el más efectivo.
    <details>
    <summary></summary>
    <p>


    </p>
    </details>

- **Interpretación de resultados**: Comprender y comunicar los resultados del modelo de manera efectiva puede ser un desafío. Se necesita interpretar los hallazgos y explicar las predicciones de forma comprensible para diferentes audiencias.
    <details>
    <summary></summary>
    <p>

    </p>
    </details>

# 3. Estructura de carpetas

A continuación se detallan las carpetas y los requisitos de cada una:


1. **app**: Contiene los datos necesarios para desplegar streamlit y que se pueda conectar con el equipo de Cloud y Full-Stack. Esta carpeta está compuesta por ño siguiente:
   - `data`: Contiene los datos en csv obtenidos de los distintos notebooks.
        - `processed`: Almacena los datos procesados después de realizar todas las transformaciones necesarias.
        - `quiz`: Contiene los datos de los usuarios que han realizado el cuestionario.
        - `users_login`: Engloba los datos pertenecientes a todos los usuarios que se han registrado en la aplicación web.
   - `images`: Almacena los datos procesados después de realizar todas las transformaciones necesarias.
        - `eda_quiz`: Almacena las imágenes obtenidas a partir del análisis exploratorio de los datos de 'quiz'
        - `eda_users`: Contiene las imágenes obtenidas a partir del análisis exploratorio de los datos de 'users_login'
        - `heatlylogo.jpg`: El logo emblemático de la aplicación web
   - `models`: Contiene los datos del modelo ganador de las predicciones de machine learning realizadas en el notebook 'des_pred_machine_learning.ipynb'.
   - `requirements.txt`: Almacena los datos necesarios para poder desplegar el docker con el equipo de Cloud
   - `visualizacion_negocio.py`: Contiene el streamlit con todas las funcionalidades.


2. **data**: Contiene los datos utilizados en el proyecto. Se compone de las siguientes subcarpetas:
   - `maps`: Contiene los datos en su formato original, es decir, se encuentran sin procesar.
   - `processed`: Almacena los datos procesados después de realizar todas las transformaciones necesarias.
   - `quiz`: Contiene los datos de entrenamiento utilizados para entrenar el modelo.
   - `table_cp`: Almacena los datos de prueba utilizados para evaluar el modelo.
   - `users_login`: Contiene los datos de las métricas de cada modulo para poder observar mejor sus respectivas diferencias.

3. **notebooks**: Se encuentran los archivos Jupyter Notebook que contienen los distintos desarrollos del proyecto. Estan estructurados de la siguiente manera.
   - `01_EDA.ipynb`: Contiene el análisis exploratorio de datos.
   - `02_Preprocesamiento.ipynb`: En él se desarrollan las transformaciones y limpiezas, incluyendo el feature engineering.
   - `03_Entrenamiento_Modelo.ipynb`: Se plasma el entrenamiento de los modelos junto con su hiperparametrización correspondiente.
   - `04_Evaluacion_Modelo.ipynb`: Contiene la evaluación de los modelos, es decir, las métricas de evaluación, interpretación de variables, etc.

4. **src**: En él se almacenan los distintos archivos fuente de Python que implementan las funcionalidades clave del proyecto. Se estructura de la siguiente manera:
   - `data_processing.py`: Se trata del código para procesar los datos de la carpeta `data/raw` y guardar los datos procesados en la carpeta `data/processed`.
   - `model.py`: Se plasma el código para entrenar y guardar el modelo entrenado utilizando los datos de la carpeta `data/train`.
   - `evaluation.py`: Se muestra el código para evaluar el modelo utilizando los datos de prueba de la carpeta `data/test` y generar métricas de evaluación.

5. **models**: En esta carpeta se almacenarán los archivos relacionados con el modelo entrenado. Dicha carpeta estará compuesta por:
   - `trained_model.pkl`: Se trata del modelo entrenado guardado en formato pickle.
   - `model_config.yaml`: Es el archivo con la configuración del modelo entrenado, es decir, sus parámetros.

6. **app**: En dicha carpeta se mostrarán los archivos necesarios para el despliegue del modelo en Streamlit y estará compuesta por:

   - `app.py`: Se plasma el ódigo para la aplicación web que utiliza el modelo entrenado (Streamlit,...).
   - `requirements.txt`: En él se especifica las dependencias del proyecto para poder ejecutar la aplicación.

5. **docs**: Contiene la documentación adicional relacionada con el proyecto. Esta compuesta por:
   - `imagenes`: Se muestran las diversas imágenes utilizadas para el proyecto
   - `presentación.pptx`: Se trata del archivo de la presentación a negocio.

6. **docs**: Contiene la documentación adicional relacionada con el proyecto. Esta compuesta por:
   - `imagenes`: Se muestran las diversas imágenes utilizadas para el proyecto
   - `presentación.pptx`: Se trata del archivo de la presentación a negocio.

7. **docs**: Contiene la documentación adicional relacionada con el proyecto. Esta compuesta por:
   - `imagenes`: Se muestran las diversas imágenes utilizadas para el proyecto
   - `presentación.pptx`: Se trata del archivo de la presentación a negocio.


# 4. En formación

