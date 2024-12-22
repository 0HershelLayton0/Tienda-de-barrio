import streamlit as st
import os
from PIL import Image
import diccionariobase
diccionario=diccionariobase.dic()

# Nombre de la pagina
st.set_page_config(page_title='TuTienda', page_icon='fondo.jpg')

def recortar_cuadrado(imagen):
    # Abrir la imagen
    img = Image.open(imagen)
    # Obtener dimensiones de la imagen
    width, height = img.size
    # Determinar el tamaño del cuadrado (el menor de los dos tamaños)
    tamaño = min(width, height)
    # Calcular los bordes para el recorte centrado
    left = (width - tamaño) / 2
    top = (height - tamaño) / 2
    right = (width + tamaño) / 2
    bottom = (height + tamaño) / 2
    # Recortar la imagen
    img_cuadrada = img.crop((left, top, right, bottom))
    return img_cuadrada

def ver_subseccion(subseccion):
    fotos = []
    print(diccionario)
    image_dir = os.path.join(os.getcwd(), 'contenedor-imagenes')
    # Obtener las rutas de las imágenes en la subsección seleccionada
    for image_file in os.listdir(os.path.join(image_dir, subseccion)):
        fotos.append(os.path.join(image_dir, subseccion, image_file))
    # Determinar el número de columnas en función del ancho de la pantalla
    screen_width = st.sidebar.slider("Ajustar tamaño", 1, 5, 5,1)
    num_columnas =screen_width
    
    # Mostrar las imágenes en columnas
    columns = st.columns(num_columnas)  # Crear el número adecuado de columnas según el ancho de la pantalla
    for i, foto in enumerate(fotos):
        col = columns[i % num_columnas]  # Asignar las imágenes a las columnas
        with col:
            # Recortar la imagen para que sea cuadrada
            img_cuadrada = recortar_cuadrado(foto)
            st.image(img_cuadrada, caption=diccionario[os.path.basename(foto)], use_column_width=True)
            

def mi_sidebar():
    secciones = os.listdir(os.path.join(os.getcwd(), 'contenedor-imagenes'))
    st.sidebar.title('Tienda')
    st.sidebar.image('fondo.jpg', width=200)
    subseccion = st.sidebar.selectbox('Selecciona', secciones)
    ver_subseccion(subseccion)

mi_sidebar()
