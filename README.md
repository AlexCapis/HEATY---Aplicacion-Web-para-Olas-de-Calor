![Logo](/docs/images/heatylogo.jpg)


</a>
<h1>HEATLY: ¡Sin Temor al Calor!</h1>


#### Autores: [Alex Marzá Manuel](https://github.com/AlexCapis), [Blanca Marmolejo](https://github.com/BlancaMarmolejo),  [Juan A-Mendizábal Ibarrola](https://github.com/juanmendiz)


#### Contribuidores: [Daniel](https://github.com/danieskka),  [Diego](https://github.com/Banbushka)

</a>
<h1>ÍNDICE</h1>


[1. Introducción](#1-introducción)

[2. Desarrollo](#2-desarrollo)

[3. Distribucion de las carpetas](#3-distribución)

[4. Integración Mar-IA](#4-integración-mar-ia)

[5. Implementación del Mapa Interactivo](#5-implementación-del-mapa-interactivo)

[6. Aplicación Web con Streamlit](#6-aplicación-web-con-streamlit)

[7. Ideas y contribuiciones externas](#7-ideas-y-contribuiciones-externas)




# 1. Introducción

#### Descripción del proyecto

Bienvenido a HEATLY, la aplicación web diseñada para brindarte información educativa y esencial sobre las olas de calor. Descubre el poder de HEATLY y prepárate para enfrentar el calor extremo sin temor.

Nuestra misión es empoderarte con datos precisos y valiosos sobre las olas de calor, ayudándote a entender su impacto en tu entorno y en tu salud. Con HEATLY, podrás acceder a una amplia gama de recursos educativos y realizar cuestionarios personalizados para evaluar tus conocimientos sobre el tema.


<details>
<summary>¿Cómo funciona HEATY?</summary>
<p>
    
Información Educativa: Descubre el poder de HEATY y adquiere conocimientos sobre las olas de calor. Aprende sobre sus causas, consecuencias y medidas de prevención. Con esta información, estarás preparado para enfrentar el calor sin miedo.

Cuestionarios Personalizados: ¿Cuánto sabes realmente sobre las olas de calor? Con nuestros cuestionarios interactivos, podrás evaluar tus conocimientos y obtener retroalimentación para mejorar tu comprensión del tema. ¡Conviértete en un experto en el calor!

Pronóstico de Temperaturas: Descubre el poder de HEATY para mantenerte informado sobre las temperaturas venideras en tu área. Con esta anticipación, podrás planificar tus actividades y tomar las medidas necesarias para evitar el impacto del calor extremo.

Consejos Prácticos: Además de la información educativa, descubre el poder de HEATY para recibir consejos prácticos y recomendaciones para mantenerte fresco y seguro durante las olas de calor. ¡Sin temor al calor, estarás preparado!

En HEATY, creemos que estar informado y preparado es la clave para enfrentar el calor de manera segura y responsable. Descubre el poder de HEATLY y únete a nuestra comunidad de personas que enfrentan el calor sin temor.

¡Explora HEATY y descubre cómo puedes convertirte en un defensor de tu bienestar en tiempos de altas temperaturas! Tu seguridad y comodidad son nuestra prioridad, y estamos aquí para acompañarte en cada paso del camino.
    
</p>
</details>

# 2. Desarrollo

#### ¿Qué dificultades podemos encontrar?


- **Creación de bases de datos**: Dado que no había usuarios reales al iniciar el desarrollo de la aplicación, decidimos generar datos ficticios utilizando la librería "Faker" para demostrar qué análisis se podría proporcionar. Debido a que los datos se generan de manera aleatoria, no hay correlaciones fuertes entre las variables. La conscuencia es un modelo con una puntuación baja.

    <details>
    <summary>Solución</summary>
    <p>

    Una vez que la aplicación esté implementada y adquiramos usuarios, almacenaremos y actualizaremos regularmente las tablas, lo que nos permitirá reentrenar el modelo, identificar patrones relevantes y, con el tiempo, mejorar el rendimiento de nuestro modelo mediante un proceso automatizado de reentrenamiento. Esto ayudará al equipo de marketing a identificar tendencias y dirigir sus campañas publicitarias en función del análisis estadístico de la información de los usuarios.


    </p>
    </details>

- **Desbalanceo de los datos**: Otro problema que podría surgir con el tiempo es que nuestro objetivo para el modelo podría desequilibrarse a medida que tomamos más datos.

    <details>
    <summary>Solución</summary>
    <p>

    Implementar técnicas de equilibrado como parte del proceso automatizado de reentrenamiento.

    </p>
    </details>

- **Constante comunicación**: También podría surgir otro problema si el equipo de marketing decide integrar más información de los usuarios.

    <details>
    <summary>Solución</summary>
    <p>

    Mantener una comunicación cercana con el equipo de marketing y adaptar nuestro modelo en consecuencia.

    </p>
    </details>




    <details>
    <summary>Ver imagen</summary>
    <img src=" " alt="drawing" width="400"/>
    </details>

    <details>
    <summary>Técnica de desbalanceo de datos</summary>
    <p>


    </p>
    </details>

- **Gran equipo de trabajo**: Trabajar en un equipo de 15 personas fue un poco confuso al principio.

    <details>
    <summary></summary>
    <p>
    Mantuvimos una comunicación constante dentro del equipo de datos, así como con los otros equipos que formaban parte de este desafío grupal. Además de nuestro equipo de ciencia de datos, había equipos de marketing, UXUI, ciberseguridad, nube y desarrollo completo. La comunicación entre todos los equipos fue excelente, lo que hizo nuestro trabajo más eficiente.


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


1. [app](https://github.com/AlexCapis/DESAFIO/tree/main/app): Contiene los datos necesarios para desplegar streamlit y que se pueda conectar con el equipo de Cloud y Full-Stack. Esta carpeta está compuesta por lo siguiente:
   - `data`: Contiene los datos en csv obtenidos de los distintos notebooks.
        - `processed`: Almacena los datos procesados después de realizar todas las transformaciones necesarias.
        - `quiz`: Contiene los datos de los usuarios que han realizado el cuestionario.
        - `table_cp`: Almacena los datos de las coordenadas de los códigos postales de los usuarios.
        - `users_login`: Engloba los datos pertenecientes a todos los usuarios que se han registrado en la aplicación web.
   - `images`: Almacena los datos procesados después de realizar todas las transformaciones necesarias.
        - `eda_quiz`: Almacena las imágenes obtenidas a partir del análisis exploratorio de los datos de 'quiz'
        - `eda_users`: Contiene las imágenes obtenidas a partir del análisis exploratorio de los datos de 'users_login'
        - `heatlylogo.jpg`: El logo emblemático de la aplicación web
   - `models`: Contiene los datos del modelo ganador de las predicciones de machine learning realizadas en el notebook 'des_pred_machine_learning.ipynb'.
   - `requirements.txt`: Almacena los datos necesarios para poder desplegar el docker con el equipo de Cloud y generar una url funcional.
   - `visualizacion_negocio.py`: Contiene el streamlit con todas las funcionalidades.


2. **data**: Contiene los datos utilizados en el proyecto. Se compone de las siguientes subcarpetas:
   - `maps`: Contiene los datos en html para que funcione el mapa de los usuarios con respecto al código postal.
   - `processed`: Almacena los datos procesados después de realizar todas las transformaciones necesarias del notebook de 'eda_users.ipynb'.
   - `quiz`: Contiene los datos de los usuarios que han realizado el cuestionario.
   - `table_cp`: Almacena los datos de las coordenadas de los códigos postales de los usuarios.
   - `users_login`: Engloba los datos pertenecientes a todos los usuarios que se han registrado en la aplicación web.

3. **docs**: En dicha carpeta se mostrarán los documentos complementarios, los cuales se componen de la siguiente manera:

   - `images`: Se plasma el código para la aplicación web que utiliza el modelo entrenado (Streamlit,...).
         - `eda_quiz`: Contiene los gráficos que se crean del notebook de 'eda_quiz.ipynb'.
         - `eda_users`: Contiene los gráficos que se crean del notebook de 'eda_users.ipynb'.
         - `heatylogo.jpg`: Es el logo de nuestra aplicación web.
   - `equipo_data_science.pdf`: Plasma el contenido del trabajo realizado por el equipo de data science de forma más detallada
   - `equipo_data_science.pptx`: Es un power point que indica aquello que hemos realizado de forma esquemática y lo que queremos implementar en el futuro.

4. **models**: 
   - `trained_model.pkl`: Contiene los datos del modelo ganador de las predicciones de machine learning realizadas en el notebook 'des_pred_machine_learning.ipynb'.


5. **notebooks**: Se encuentran los archivos Jupyter Notebook que contienen los distintos desarrollos del proyecto. Estan estructurados de la siguiente manera.
   - `db_creation_csv.ipynb`: Se desarrollan con detenimiento las bases de datos de usuarios y de cuestionario de forma detallada.
   - `eda_quiz.ipynb`:  Contiene el análisis exploratorio de datos del cuestionario realizado por los usuarios.
   - `eda_users.ipynb`:  Contiene el análisis exploratorio de datos de los usuarios.
   - `heatwaveAI.ipynb`: Almacena la información más detallada acerca de la implementación del Chatbot.
   - `machine_learning.ipynb`: Engloba el desarrollo del machine learning realizado originando el modelo ganador.

6. **openAI**: 
   - `templates`: Almacena el código de html necesario y los 'assets' pertinentes para poder mejorar visualmente el código de 'app.py'
   - `app.py`: Muestra el código necesario para desplegar el Chatbot con respuestas personalizadas.
   - `requeriments`: Almacena los datos necesarios para poder desplegar el docker con el equipo de Cloud y generar una url funcional.


# 4. Integración Mar-IA

Construimos un Chatbot llamado Mar-IA impulsado por IA que interactúa con los usuarios y brinda respuestas personalizadas y oportunas a sus preguntas. El Chatbot mejora la experiencia del usuario al proporcionar asistencia inmediata y precisa, además de aliviar la carga del equipo de soporte al manejar consultas comunes de manera automatizada.

<details>
<summary>Mar-IA</summary>
<p>
![Mar-IA](/openAI/templates/assets/Frame 24.svg)
</p>
</details>



# 5. Implementación del Mapa Interactivo

Implementamos un mapa interactivo que muestra la ubicación geográfica de los usuarios utilizando los códigos postales. En dicho mapa se podrá observar el sumatorio de los usuarios que pertenecen a ese código postal, además se proporcionará la edad media pertinente de dichos usuarios. Esta funcionalidad proporciona una visión geográfica de la distribución de los usuarios, lo que ayuda al equipo de negocio a comprender mejor la audiencia y planificar estrategias de marketing y expansión.


- ** **: 
    <details>
    <summary>Mapa Interactivo de los usuarios</summary>
    <p>
QUIERO PONER UN PANTALLAZO DEL MAPA INTERACTIVO PARA QUE SE MUESTREN LOS PUNTOS Y EL DESPLEGABLE DE SUMATORIO USUARIOS Y LA EDAD MEDIA
    </p>
    </details>



# 6. Aplicación Web con Streamlit

Desarrollamos una aplicación web utilizando Streamlit, una biblioteca de Python, que permite al equipo de negocio acceder a estadísticas de manera directa y actualizada. La interfaz de Streamlit es fácil de usar y brinda una visualización clara de los datos, lo que facilita la interpretación y toma de decisiones basadas en datos en tiempo real. En el streamlit podremos ver los datos estadísticos de los usuarios y del cuestionario. Además, se ha implementado el mapa interactivo de los usuarios y la predicción de machine learning en el cual, de manera interactiva se puede predecir si un usuario va a suspender el cuestionario (nota menor que 7) o si un usuario va a aprobarlo (nota mayor que 7) solamente es necesario que se introduzcan los parámetros necesarios que se le piden al usuario al registrarse en la aplicación web.



- **Datos usuarios**: En la aplicación, el equipo de negocio puede acceder a datos demográficos, comportamiento del usuario y patrones de uso, lo que les permite entender mejor a su audiencia y ajustar sus estrategias en consecuencia.
    <details>
    <summary> Estadísticas</summary>
    <p>
QUIERO MOSTRAR UNA DE LAS TANTAS ESTADISTICAS QUE TENEMOS DE USUARIOS LA QUE SEA
    </p>
    </details>


- **Mapa Interactivo**: Insertamos dentro de Streamlit el mapa interactivo de los usuarios para que desde negocio puedan tener toda la información detallada desde el mismo sitio web, de esta manera se trabaja con mayor rapidez y dinamismo.

- **Datos quiz**: La aplicación también muestra datos relevantes relacionados con el cuestionario, como el rendimiento promedio, las respuestas más comunes y otros indicadores clave que ayudan a evaluar la efectividad y el impacto del cuestionario en los usuarios.
    <details>
    <summary> Estadísticas</summary>
    <p>
QUIERO MOSTRAR UNA DE LAS TANTAS ESTADISTICAS QUE TENEMOS DE QUIZ LA QUE SEA
    </p>
    </details>


- **Predicciones**: Esta función proporciona una herramienta poderosa para el equipo de negocio, ya que les permite anticiparse a las necesidades y comportamientos de los usuarios. Con esta información, pueden personalizar la experiencia de los usuarios, brindar recomendaciones específicas y tomar decisiones más informadas para mejorar la retención y satisfacción del usuario.
    <details>
    <summary>¿Cómo funciona?</summary>
    <p>
    Cuando un usuario se registra en la aplicación web, se le solicitan ciertos parámetros o características relevantes que se utilizarán para el análisis del cuestionario. Con esta información, el algoritmo de machine learning se activa y realiza una predicción basada en los datos históricos y patrones previamente analizados. La predicción puede indicar si el usuario es probable que suspenda (-7) o apruebe (+7) el cuestionario.
    </p>
    </details>


Por último, nos gustaría que pudiesen apreciar de primera mano el trabajo que hemos realizado con Streamlit. Es un proyecto en el que hemos dedicado tiempo y esfuerzo para ofrecer una experiencia única. ¡Los invitamos a explorar y disfrutar de lo que hemos creado con mucho cariño!
Pueden acceder al proyecto en el siguiente enlace: [HEATLY: ¡Sin Temor al Calor!](https://mi-servicio-visual-u4ktx3b6jq-ew.a.run.app/)



# 7. Ideas y contribuiciones externas

Para poder mejorar y hacer prosperar este proyecto, apreciamos toda ayuda relevante y la participación de cualquier persona interesada. Invitamos a todos a unirse y colaborar en este proyecto, ya que cualquier aporte positivo es bien recibido y valorado. Juntos podemos hacer que este proyecto crezca y alcance nuevos logros.


