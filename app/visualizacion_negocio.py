import streamlit as st
import pandas as pd
import os
from flask import Flask, render_template, request
import openai


# Ajustamos la página con un icono en el buscador y el título
st.set_page_config(page_title="Healty", page_icon=":heart:", layout="wide")

# Ponemos una imagen 
imagen = "../docs/images/heatylogo.png"
imagen_cargada = st.image(imagen)

# Ponemos un titulo a nuestra aplicación
st.title("Descubre el Poder de HEATLY: ¡Sin Temor al Calor!")

texto = """

Bienvenido a HEATLY, la aplicación web diseñada para brindarte información educativa y esencial sobre las olas de calor. Descubre el poder de HEATLY y prepárate para enfrentar el calor extremo sin temor.

Nuestra misión es empoderarte con datos precisos y valiosos sobre las olas de calor, ayudándote a entender su impacto en tu entorno y en tu salud. Con HEATLY, podrás acceder a una amplia gama de recursos educativos y realizar cuestionarios personalizados para evaluar tus conocimientos sobre el tema.

"""
st.write(texto)

if st.checkbox('¿Cómo funciona HEATLY?'):
        texto= '''
Información Educativa: Descubre el poder de HEATLY y adquiere conocimientos sobre las olas de calor. Aprende sobre sus causas, consecuencias y medidas de prevención. Con esta información, estarás preparado para enfrentar el calor sin miedo.

Cuestionarios Personalizados: ¿Cuánto sabes realmente sobre las olas de calor? Con nuestros cuestionarios interactivos, podrás evaluar tus conocimientos y obtener retroalimentación para mejorar tu comprensión del tema. ¡Conviértete en un experto en el calor!

Pronóstico de Temperaturas: Descubre el poder de HEATLY para mantenerte informado sobre las temperaturas venideras en tu área. Con esta anticipación, podrás planificar tus actividades y tomar las medidas necesarias para evitar el impacto del calor extremo.

Consejos Prácticos: Además de la información educativa, descubre el poder de HEATLY para recibir consejos prácticos y recomendaciones para mantenerte fresco y seguro durante las olas de calor. ¡Sin temor al calor, estarás preparado!

En HEATLY, creemos que estar informado y preparado es la clave para enfrentar el calor de manera segura y responsable. Descubre el poder de HEATLY y únete a nuestra comunidad de personas que enfrentan el calor sin temor.

¡Explora HEATLY y descubre cómo puedes convertirte en un defensor de tu bienestar en tiempos de altas temperaturas! Tu seguridad y comodidad son nuestra prioridad, y estamos aquí para acompañarte en cada paso del camino.

Recuerda, el conocimiento es poder, y con HEATLY, estarás listo para abrazar el calor y disfrutar de cada temporada, sin preocupaciones. ¡Bienvenido a la experiencia HEATLY: Descubre el Poder de ¡Sin Temor al Calor!


'''
        texto
else:
        st.markdown('El texto permanece oculto')



menu = st.sidebar.selectbox("Selecciona la Página", ['PRINCIPAL','DATOS USUARIOS','DATOS QUIZ', 'PREDICCIÓN', 'CHATBOT'])


if menu == 'DATOS USUARIOS':

    st.header('Datos Usuarios') # Nombramos el título
   
    if st.checkbox('Mostrar el DataFrame '):
        df= pd.read_csv("../data/users_login/users.csv")
        df
    else:
        st.markdown('El dataset esta oculto')

    texto2 = """
   
"""

    st.write(texto2)

    tab1, tab2, tab3, tab4, tab5 = st.tabs(['Fecha de Registro', 'Sexo','Fecha de Nacimiento', 'Código Postal', 'Número de Hijos Menores'])


    with tab1:

        st.subheader('Visualización de la Fecha de Registro')

        
        imagen = "../docs/images/eda_users/usuarios_por_mes_barras.png"
        imagen_cargada = st.image(imagen)

        imagen = "../docs/images/eda_users/usuarios_por_mes_lineas.png"
        imagen_cargada = st.image(imagen)


    with tab2:

        st.subheader('Visualización de la variable de Sexo')

        
        imagen = "../docs/images/eda_users/pie_plot_sexo.png"
        imagen_cargada = st.image(imagen)

        texto_tab2 = '''
        
        '''
        st.write(texto_tab2)


    with tab3:

        st.subheader('Visualización de la variable Fecha de Nacimiento')

        
        imagen = "../docs/images/eda_users/pie_plot_franja_edad_espaciado.png"
        imagen_cargada = st.image(imagen)

        texto_tab3 = '''
       
        '''
        st.write(texto_tab3)


    with tab4:

        st.subheader('Visualización de la variable Código Postal')


        ruta_html_interactivo = "../src/mapa_ub_cpostales.html"

        with open(ruta_html_interactivo, "r", encoding="utf-8") as f:
            contenido_html = f.read()

        st.markdown(contenido_html, unsafe_allow_html=True)
    

        imagen = "../docs/images/eda_users/grafico_barras_cp_top_15.png"
        imagen_cargada = st.image(imagen)

        imagen = "../docs/images/eda_users/pie_plot_zona_cp.png"
        imagen_cargada = st.image(imagen)
        texto_tab3 = '''
       
        '''
        st.write(texto_tab3)


    with tab5:

        st.subheader('Visualización de la variable Número de Hijos Menores')

        imagen = "../docs/images/eda_users/cantidad_hijos_menores.png"
        imagen_cargada = st.image(imagen)

        imagen = "../docs/images/eda_users/box_plot_cantidad_hijos_menores.png"
        imagen_cargada = st.image(imagen)

        imagen = "../docs/images/eda_users/hijos_menores_si_no.png"
        imagen_cargada = st.image(imagen)

        texto_tab3 = '''
       
        '''
        st.write(texto_tab3)

elif menu == 'DATOS QUIZ':

    # Procesamos los datos
    st.header('Procesado de los datos del cuestionario: ')

    if st.checkbox('Mostrar el DataFrame procesado'):
        df_procesado= pd.read_csv("../data/quiz/answers.csv")
        df_procesado
    else:
        st.markdown('El dataset esta oculto')

    tab1, tab2, tab3 = st.tabs(['Heart Disease', 'Columnas Binarias','Salud'])

    with tab1:

        st.subheader('Visualización de la variable target')

        
        imagen = ""
        imagen_cargada = st.image(imagen)

    with tab2:

        st.subheader('Visualización de las variables binarias')

        
        imagen = " "
        imagen_cargada = st.image(imagen)

        texto_tab2 = ''' '''
        
        st.write(texto_tab2)


    with tab3:

        st.subheader('Visualización de la variable Salud')

        
        imagen = ""
        imagen_cargada = st.image(imagen)

        texto_tab3 = '''
        
        '''
        st.write(texto_tab3)

elif menu == 'MODELOS':
    # Procesamos los datos
    st.header('Descripción de los Modelos: ')
   

    texto4= '''

    '''
    st.write(texto4)

    texto_metricas= '''
    
    '''
    st.write(texto_metricas)


    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(['Logistic Regression', 'Naive Bayes','Decision Tree Classifier', 'Random Forest Classifier','XGB Classifier', 'PCA'])

    with tab1:

        st.subheader('Descripción del modelo de Logistic Regression')

        texto5= '''
    
        '''
        st.write(texto5)

        imagen = " "
        imagen_cargada = st.image(imagen)
        
        texto6= '''
    
        '''
        st.write(texto6)

        imagen = " "
        imagen_cargada = st.image(imagen)


    with tab2:

        st.subheader('Descripción del modelo de Naive Bayes')


        texto7= '''
    
        '''
        st.write(texto7)

        imagen = " "
        imagen_cargada = st.image(imagen)
        
        texto8= '''
    
        '''
        st.write(texto8)

        imagen = " "
        imagen_cargada = st.image(imagen)

    with tab3:

        st.subheader('Descripción del modelo de Decision Tree Classifier')

        

        texto9= '''
    
        '''
        st.write(texto9)

        imagen = " "
        imagen_cargada = st.image(imagen)
        
        texto10= '''
    
        '''
        st.write(texto10)

        imagen = " "
        imagen_cargada = st.image(imagen)


    with tab4:

        st.subheader('Descripción del modelo de Random Forest Classifier')
        

        texto11= '''
    
        '''
        st.write(texto11)

        imagen = " "
        imagen_cargada = st.image(imagen)
        
        texto12= '''
    
        '''
        st.write(texto12)

        imagen = " "
        imagen_cargada = st.image(imagen)

    with tab5:

        st.subheader('Descripción del modelo de XGB Classifier')

        texto13= '''
    
        '''
        st.write(texto13)

        imagen = " "
        imagen_cargada = st.image(imagen)
        
        texto14= '''
    
        '''
        st.write(texto14)

        imagen = " "
        imagen_cargada = st.image(imagen)


    with tab6:

        st.subheader('Descripción del modelo de PCA')


        texto15= '''
    
        '''
        st.write(texto15)

        imagen = ""
        imagen_cargada = st.image(imagen)
        
        texto16= '''
    
        '''
        st.write(texto16)

        imagen = " "
        imagen_cargada = st.image(imagen)
    

elif menu == 'PREDICCIÓN':
    # Procesamos los datos
    st.header('Descripción de Machine Learning: ')
   
    if st.checkbox('Mostrar el DataFrame procesado'):
        df_procesado= pd.read_csv("../data/processed/users_processed.csv")
        df_procesado
    else:
        st.markdown('El dataset esta oculto')

    tab1, tab2, tab3 = st.tabs(['Matriz de confusión', 'Recall'])


elif menu == 'CHATBOT':
    # Procesamos los datos
    st.header('Descripción del CHATBOT: ')
   
app = Flask(__name__)

# Replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key
openai.api_key = "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"

# Function to check if a question is heatwave-related
def is_heatwave_related(question):
    # Add your logic here to determine if the question is heatwave-related
    # You can use simple keyword matching or more advanced NLP techniques
    # For this example, let's assume we have a list of heatwave-related keywords
    heatwave_keywords = ["heatwave",
    "high temperature",
    "extreme heat",
    "heat index",
    "heat advisory",
    "heat stress",
    "heat exhaustion",
    "heatstroke",
    "hot weather",
    "sweltering",
    "scorching",
    "sunburn",
    "dehydration",
    "hydration",
    "air conditioning",
    "fans",
    "sunscreen",
    "shade",
    "water consumption",
    "cooling centers", 
    "temperature",
    "spf",
    "heat emergency", 
    "climate",
    "climate change"]

    for keyword in heatwave_keywords:
        if keyword in question.lower():
            return True
    return False

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        question = request.form['question']
        if is_heatwave_related(question):
            response = openai.Completion.create(
                engine="text-davinci-002",  # Use the appropriate OpenAI engine for your needs
                prompt=question,
                max_tokens=150,
                stop=None,
            )
            answer = response.choices[0].text.strip()
            return render_template('index.html', question=question, answer=answer)
        else:
            return render_template('index.html', message="Please ask only heatwave-related questions.")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

